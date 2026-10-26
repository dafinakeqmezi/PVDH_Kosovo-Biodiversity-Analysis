"""Test notebook helpers without executing its data export cells."""
import ast
import json
from pathlib import Path
import unittest

import numpy as np
import pandas as pd


NOTEBOOK = Path(__file__).resolve().parents[1] / "notebooks/02_pastrimi.ipynb"


def notebook_helpers(cell_id):
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    cell = next(c for c in notebook["cells"] if c.get("id") == cell_id)
    tree = ast.parse("".join(cell["source"]))
    tree.body = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    namespace = {"pd": pd, "np": np}
    exec(compile(tree, str(NOTEBOOK), "exec"), namespace)
    return namespace


class InvalidValuesTests(unittest.TestCase):
    def setUp(self):
        self.helpers = notebook_helpers("invalid-values")

    def test_threshold_uses_distribution_and_area(self):
        policy = self.helpers["uncertainty_policy"]
        threshold, radius = policy(pd.Series([10, 20, 30, np.nan, 0, -1, np.inf]), pd.Series([np.pi]))
        self.assertEqual(threshold, 20)
        self.assertAlmostEqual(radius, 1000)
        threshold, _ = policy(pd.Series([2000, 4000, 6000]), pd.Series([np.pi, np.nan]))
        self.assertAlmostEqual(threshold, 1000)
        with self.assertRaises(ValueError):
            policy(pd.Series([np.nan, 0]), pd.Series([1]))

    def test_uncertainty_boundaries_and_missing(self):
        values = pd.Series([np.nan, 0, -1, np.inf, -np.inf, 50, 100, 101])
        result = self.helpers["uncertainty_status"](values, 100)
        self.assertEqual(result.tolist(), ["unknown", "invalid", "invalid", "invalid", "invalid",
                                           "within_screening_threshold", "within_screening_threshold", "above_screening_threshold"])

    def test_species_and_finer_are_not_higher_ranks(self):
        ranks = pd.Series(["SPECIES", "SUBSPECIES", "VARIETY", "FORM", "GENUS", "FAMILY", "UNRANKED", None, "SPECIES", "UNKNOWN"])
        names = pd.Series(["a"] * 8 + [None, "a"])
        result = self.helpers["species_level_flag"](ranks, names)
        expected = pd.Series([True, True, True, True, False, False, pd.NA, pd.NA, pd.NA, pd.NA], dtype="boolean")
        pd.testing.assert_series_equal(result, expected)


class IndividualCountTests(unittest.TestCase):
    def setUp(self):
        self.summarize = notebook_helpers("count-decision")["count_statistics"]

    def test_missing_is_not_zero_and_reported_zero_is_kept(self):
        values = pd.Series([0, 1, 5, pd.NA], dtype="Int64")
        original = values.copy()
        stats = self.summarize(values)
        self.assertEqual(stats["mungesa_pct"], 25)
        self.assertEqual(stats["mediana"], 1)
        self.assertEqual(stats["zero"], 1)
        self.assertEqual(stats["te_plotesuara"], 3)
        pd.testing.assert_series_equal(values, original)

    def test_no_observations_does_not_invent_a_median(self):
        stats = self.summarize(pd.Series([pd.NA, pd.NA], dtype="Int64"))
        self.assertEqual(stats["mungesa_pct"], 100)
        self.assertEqual(stats["te_plotesuara"], 0)
        self.assertTrue(np.isnan(stats["mediana"]))
        self.assertTrue(np.isnan(stats["skewness"]))

    def test_empty_and_small_groups(self):
        self.assertTrue(np.isnan(self.summarize(pd.Series([], dtype="Int64"))["mungesa_pct"]))
        stats = self.summarize(pd.Series([2], dtype="Int64"))
        self.assertEqual(stats["mediana"], 2)
        self.assertTrue(np.isnan(stats["skewness"]))


class FinalCheckpointTests(unittest.TestCase):
    def setUp(self):
        self.helpers = notebook_helpers("final-checkpoint")
        self.counts = [dict(hapi="first", rreshta_para=10, kolona_para=2, rreshta_pas=9, kolona_pas=2),
                       dict(hapi="freeze", rreshta_para=9, kolona_para=2, rreshta_pas=9, kolona_pas=2)]
        self.log = pd.DataFrame([{**row, "hapi": "02_clean:" + row["hapi"], "input": "raw.csv",
                                  "arsyeja": "reason", "output": "clean.csv", "commit": "message"}
                                 for row in self.counts])

    def test_complete_log_and_unrelated_steps(self):
        other = self.log.iloc[[0]].assign(hapi="01:quality")
        log = pd.concat([other, self.log], ignore_index=True)
        result = self.helpers["validate_cleaning_log"](log, self.counts, (10, 2), (9, 2))
        self.assertEqual(len(result), 2)

    def test_reject_missing_duplicate_or_reordered_steps(self):
        for log in [self.log.iloc[:1], pd.concat([self.log, self.log.iloc[:1]]), self.log.iloc[::-1]]:
            with self.assertRaises(AssertionError):
                self.helpers["validate_cleaning_log"](log, self.counts, (10, 2), (9, 2))

    def test_reject_incorrect_dimensions_and_blank_reason(self):
        for field, value in [("rreshta_para", 8), ("arsyeja", " ")]:
            log = self.log.copy()
            log.loc[1, field] = value
            with self.assertRaises(AssertionError):
                self.helpers["validate_cleaning_log"](log, self.counts, (10, 2), (9, 2))

    def test_freeze_allows_identical_content_only(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "checkpoint.csv"
            self.helpers["ensure_frozen_content"](path, b"first")
            path.write_bytes(b"first")
            self.helpers["ensure_frozen_content"](path, b"first")
            with self.assertRaises(ValueError):
                self.helpers["ensure_frozen_content"](path, b"different")
            self.assertEqual(path.read_bytes(), b"first")

    def test_saved_checkpoint_matches_manifest_and_log(self):
        import hashlib
        root = NOTEBOOK.parent.parent
        manifest = json.loads((root / "processed/biodiversity_clean_manifest.json").read_text())
        for key in ["source", "dataset", "schema"]:
            actual = hashlib.sha256((root / manifest[key]).read_bytes()).hexdigest()
            self.assertEqual(actual, manifest[key + "_sha256"])
        log = pd.read_csv(root / manifest["log"])
        own = log.loc[log["hapi"].str.startswith("02_clean:")]
        self.assertEqual(len(own), manifest["cleaning_steps"])
        self.assertEqual(hashlib.sha256(own.to_csv(index=False).encode("utf-8")).hexdigest(), manifest["cleaning_log_sha256"])
        counts = pd.read_csv(root / "reports/numerimet_e_pastrimit.csv").to_dict("records")
        self.helpers["validate_cleaning_log"](log, counts, (46831, 42), (manifest["rows"], manifest["column_count"]))
        data = pd.read_csv(root / manifest["dataset"], low_memory=False)
        self.assertEqual(data.shape, (manifest["rows"], manifest["column_count"]))
        self.assertTrue(data["gbifID"].is_unique)
        self.assertFalse(data["elevation"].eq(0).any())


if __name__ == "__main__":
    unittest.main()
