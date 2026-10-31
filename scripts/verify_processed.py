"""Read-only consistency audit of saved preprocessing outputs.

Run from any directory: .venv/bin/python scripts/verify_processed.py
Notebook definitions are reused without executing their export cells.
"""
import ast
import hashlib
import io
import json
from pathlib import Path
import subprocess
import unicodedata

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "processed"


def cells(name):
    notebook = json.loads((ROOT / "notebooks" / name).read_text())
    return ["".join(c["source"]) for c in notebook["cells"] if c["cell_type"] == "code"]


def definitions(source, namespace, functions, assignments=()):
    tree = ast.parse(source)
    tree.body = [node for node in tree.body if
                 (isinstance(node, ast.FunctionDef) and node.name in functions)
                 or (isinstance(node, ast.Assign) and any(
                     isinstance(target, ast.Name) and target.id in assignments
                     for target in node.targets))]
    exec(compile(tree, "<notebook definitions>", "exec"), namespace)


def read(name, **kwargs):
    return pd.read_csv(PROCESSED / name, low_memory=False, **kwargs)


def csv_frame(frame, index=False):
    return pd.read_csv(io.StringIO(frame.to_csv(index=index)), low_memory=False)


def same(left, right):
    pd.testing.assert_frame_equal(left.reset_index(drop=True), right.reset_index(drop=True),
                                  check_dtype=False, check_exact=False, rtol=1e-9, atol=1e-10)


def same_aggregate(expected, saved):
    key = expected.columns[0]
    assert expected[key].is_unique and saved[key].is_unique
    # Equal-count rows can change order across pandas versions; compare by key.
    same(expected.sort_values(key), saved.sort_values(key))


def main():
    before = {p: hashlib.sha256(p.read_bytes()).hexdigest()
              for folder in ("dataset", "processed") for p in (ROOT / folder).glob("*") if p.is_file()}
    results = []

    def check(label, operation):
        try:
            detail = operation()
            results.append((label, "PASS", str(detail or "Matches saved data")))
        except Exception as error:
            results.append((label, "FAIL", str(error)))

    raw = pd.read_csv(ROOT / "dataset/kosovo_overall_biodiversity.csv", low_memory=False)
    clean = read("biodiversity_clean.csv")
    features = read("biodiversity_features.csv")
    removed = read("rreshtat_per_fshirje_duplikate.csv")
    ns = {"pd": pd, "np": np, "json": json, "Path": Path,
          "CLEAN_PATH": PROCESSED / "biodiversity_clean.csv",
          "SCHEMA_PATH": PROCESSED / "biodiversity_clean_schema.json"}
    for source in cells("02_pastrimi.ipynb"):
        definitions(source, ns, {"load_clean_dataset", "validation_value_rules", "assert_duplicate_survivors"})
    typed = ns["load_clean_dataset"]()
    for source in cells("03_vetite.ipynb"):
        # All code cells currently contain imports, constants and pure definitions only.
        tree = ast.parse(source)
        assert all(isinstance(n, (ast.Import, ast.ImportFrom, ast.Assign, ast.For, ast.FunctionDef))
                   for n in tree.body), "Review new notebook execution cells before auditing"
        exec(compile(tree, "<feature definitions>", "exec"), ns)

    def integrity():
        manifest = json.loads((PROCESSED / "biodiversity_clean_manifest.json").read_text())
        for key in ("source", "dataset", "schema"):
            assert hashlib.sha256((ROOT / manifest[key]).read_bytes()).hexdigest() == manifest[key + "_sha256"]
        path = "dataset/kosovo_overall_biodiversity.csv"
        assert subprocess.check_output(["git", "show", "HEAD:" + path], cwd=ROOT) == (ROOT / path).read_bytes()
        assert clean.shape == (46456, 83) and raw.shape == (46831, 42)
        assert clean.gbifID.is_unique and clean.gbifID.notna().all()
        assert set(raw.gbifID) - set(clean.gbifID) == set(removed.gbifID)
        assert len(removed) == 375 and set(clean.gbifID) <= set(raw.gbifID)
        assert all(ns["validation_value_rules"](typed).values())
        return "Hashes, original Git bytes, schema, value rules and 375 removed IDs agree"

    check("Checkpoint integrity", integrity)

    def duplicate_check():
        candidates = pd.read_csv(io.BytesIO(subprocess.check_output([
            "git", "show", "d2708c640de830014edf4c4f35a528849c98455f:processed/duplicate_candidates.csv"], cwd=ROOT)))
        decisions = pd.read_csv(ROOT / "reports/vendimet_e_grupeve_duplikate.csv")
        ns["assert_duplicate_survivors"](clean, candidates, decisions, removed)

    check("Approved duplicate survivors", duplicate_check)
    check("83 base columns preserved in features", lambda: same(features[clean.columns], clean))
    check("All 128 feature columns rebuilt", lambda: same(
        csv_frame(ns["build_features"](typed, read("gbif_datasets_cache.csv"))), features))

    ns.update({"unicodedata": unicodedata,
               "alb": lambda s: s.str.split(" / ").str[0],
               "pub_map": read("gbif_datasets_cache.csv").set_index("datasetKey").publishingOrg,
               "DISTRICTS": sorted(clean.district.str.split(" / ").str[0].unique())})
    names = {"municipality_key", "prepare", "agg_by_municipality", "agg_municipality_by_taxon",
             "agg_by_time", "agg_class_by_district", "agg_by_species", "run_all"}
    for source in cells("01_mbledhja_kualiteti.ipynb"):
        definitions(source, ns, names, {"JOIN_COLS", "GROUPS", "MONTHS", "MONTH_NAMES"})
    municipalities = read("municipalities.csv")
    municipalities["komuna_key"] = municipalities.komuna.map(ns["municipality_key"])
    ns["municipalities"] = municipalities
    for suffix, data in (("", raw), ("_v2", clean)):
        _, aggregates = ns["run_all"](data)
        for name, expected in aggregates.items():
            filename = name + suffix + ".csv"
            check(filename, lambda e=expected, f=filename: same_aggregate(csv_frame(e, index=True), read(f)))
        matrix = read("agg_municipality_taxon" + suffix + ".csv")
        scaled = ns["standardize_pca_matrix"](matrix)
        check("PCA standardization" + suffix, lambda s=scaled, x=suffix: same(
            csv_frame(s), read("matrica_pca_komuna_taxon" + x + ".csv")))

        def pca_check(matrix=matrix, suffix=suffix):
            expected = ns["run_pca_on_clean_matrix"](matrix)
            saved = read("pca_municipalities" + suffix + ".csv")
            same(expected[["komuna", "rajoni"]], saved[["komuna", "rajoni"]])
            assert list(expected.columns) == list(saved.columns)
            # Component signs may flip across LAPACK versions without changing PCA.
            for col in expected.columns[2:]:
                a, b = expected[col].to_numpy(), saved[col].to_numpy()
                assert np.allclose(a, b, rtol=1e-8, atol=1e-9) or np.allclose(a, -b, rtol=1e-8, atol=1e-9)
        check("PCA scores" + suffix, pca_check)

    raw_text = pd.read_csv(ROOT / "dataset/kosovo_overall_biodiversity.csv", dtype=str, keep_default_na=False)
    for filename in ("sample_random.csv", "sample_stratified.csv"):
        def sample_check(filename=filename):
            sample = read(filename, dtype=str, keep_default_na=False)
            assert sample.shape == (10000, 42) and sample.gbifID.is_unique
            original = raw_text.set_index("gbifID", drop=False).loc[sample.gbifID]
            same(sample, original)
            overlap = sample.gbifID.isin(removed.gbifID.astype(str)).sum()
            return f"10000 original-data rows; {overlap} IDs subsequently removed as duplicates"
        check(filename, sample_check)

    def independent_rules():
        for prefix in ("taxon_group_", "district_", "basisOfRecord_"):
            block = features.filter(regex="^" + prefix)
            assert block.isin([0, 1]).all().all() and block.sum(axis=1).eq(1).all()
        rank = clean.iucnRedListCategory.map({"LC": 1, "NT": 2, "VU": 3, "EN": 4, "CR": 5, "EX": 6})
        np.testing.assert_allclose(features.iucn_rank, rank, equal_nan=True)
        for column in ("individualCount", "coordinateUncertaintyInMeters"):
            np.testing.assert_allclose(features[column + "_log1p"], np.log1p(clean[column]), equal_nan=True)
        assert features.gbifID.equals(clean.gbifID)
    check("Independent one-hot, IUCN and log1p rules", independent_rules)

    def auxiliary_outputs():
        missing = read("missing_report.csv").set_index("kolona").loc[raw.columns]
        np.testing.assert_array_equal(missing.mungojne, raw.isna().sum())
        np.testing.assert_allclose(missing.perqindja, raw.isna().mean() * 100, atol=0.005)
        source = read("sources_summary.csv").groupby("datasetKey").regjistrime.sum()
        pd.testing.assert_series_equal(source.sort_index(), raw.groupby("datasetKey").size().sort_index(),
                                       check_names=False)
        joined = read("biodiversity_municipalities.csv")
        same(joined[raw.columns], raw)
        lookup = municipalities.set_index("komuna_key")
        for col in ns["JOIN_COLS"][1:]:
            expected = raw.municipality.map(ns["municipality_key"]).map(lookup[col])
            pd.testing.assert_series_equal(joined[col], expected, check_names=False, check_dtype=False)
        assert (PROCESSED / "kosovo_biodiversity_clean.csv").read_bytes() == (PROCESSED / "biodiversity_clean.csv").read_bytes()
        assert set(read("rreshtat_e_larguar_duplikate.csv").gbifID) == set(removed.gbifID)
        return "Missing inventory, publisher totals, municipality join, intermediate copy and removed-row IDs agree"
    check("Supporting processed outputs", auxiliary_outputs)
    assert all(hashlib.sha256(p.read_bytes()).hexdigest() == h for p, h in before.items())
    for label, status, detail in results:
        print(f"{status}: {label}: {detail}")
    failed = sum(status == "FAIL" for _, status, _ in results)
    print(f"\n{len(results) - failed} PASS / {failed} FAIL. No dataset or processed file changed.")
    return bool(failed)


if __name__ == "__main__":
    raise SystemExit(main())
