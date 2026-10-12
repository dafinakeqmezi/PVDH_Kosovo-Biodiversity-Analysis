import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pandas as pd

pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 220)
pd.set_option("display.max_colwidth", 60)

try:
    ROOT = Path(__file__).resolve().parent.parent
except NameError:
    ROOT = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()

DATA_PATH = ROOT / "dataset" / "kosovo_overall_biodiversity.csv"
PROCESSED_DIR = ROOT / "processed"
SOURCES_SUMMARY_PATH = PROCESSED_DIR / "sources_summary.csv"
GBIF_CACHE_PATH = PROCESSED_DIR / "gbif_datasets_cache.csv"
GBIF_API = "https://api.gbif.org/v1"
TOP_N = 15

PROCESSED_DIR.mkdir(exist_ok=True)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# %%
# 01b - Analiza e burimeve
#
# CSV-ja nuk ka kolonat publishingOrgKey / publishingOrg. Publikuesin e marrim nga GBIF API:
#   /dataset/{datasetKey}            -> titulli, DOI, publishingOrganizationKey
#   /organization/{organizationKey}  -> emri dhe vendi i publikuesit
# Rezultatet ruhen në cache (processed/gbif_datasets_cache.csv), që API të mos thirret në çdo ekzekutim.
# Nëse API nuk përgjigjet për ndonjë dataset, publikuesi merret nga institutionCode.

# %%
section("1. LEXIMI I TË DHËNAVE")
df = pd.read_csv(DATA_PATH, usecols=["datasetKey", "institutionCode", "basisOfRecord", "license"],
                 low_memory=False)
total = len(df)
print(f"Regjistrime: {total:,}  |  Dataset-e: {df.datasetKey.nunique()}  |  "
      f"institutionCode: {df.institutionCode.nunique()}")


# %%
section("2. METADATA NGA GBIF API")


def get_json(url):
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.load(r)
    except Exception as e:
        print(f"  ! {url}: {e}")
        return None


def fetch_dataset(key):
    d = get_json(f"{GBIF_API}/dataset/{key}")
    if d is None:
        return {"datasetKey": key}
    org_key = d.get("publishingOrganizationKey")
    org = get_json(f"{GBIF_API}/organization/{org_key}") if org_key else None
    return {
        "datasetKey": key,
        "datasetTitle": d.get("title"),
        "datasetDOI": d.get("doi"),
        "publishingOrgKey": org_key,
        "publishingOrg": org.get("title") if org else None,
        "publisherCountry": org.get("country") if org else None,
    }


keys = df.datasetKey.dropna().unique().tolist()
cache = pd.read_csv(GBIF_CACHE_PATH) if GBIF_CACHE_PATH.exists() else pd.DataFrame(columns=["datasetKey"])
cached_ok = cache.dropna(subset=["publishingOrg"]) if "publishingOrg" in cache else cache.iloc[0:0]
missing_keys = [k for k in keys if k not in set(cached_ok.datasetKey)]

print(f"Në cache: {len(keys) - len(missing_keys)}  |  Për t'u shkarkuar: {len(missing_keys)}")
if missing_keys:
    with ThreadPoolExecutor(max_workers=8) as pool:
        fetched = pd.DataFrame(list(pool.map(fetch_dataset, missing_keys)))
    cache = pd.concat([cached_ok, fetched], ignore_index=True)
    cache.to_csv(GBIF_CACHE_PATH, index=False)

meta = cache[cache.datasetKey.isin(keys)]
print(f"Publikues të gjetur nga API: {meta.publishingOrg.notna().sum()} / {len(keys)} dataset-e")


# %%
section("3. KOMBINIMI ME institutionCode")

# institutionCode-t për çdo dataset (një dataset mund të ketë disa)
inst = (df.dropna(subset=["institutionCode"])
          .groupby("datasetKey")["institutionCode"]
          .agg(lambda s: " | ".join(s.value_counts().index)))

df = df.merge(meta, on="datasetKey", how="left")
df["institutionCodes"] = df.datasetKey.map(inst)

# Fallback: nëse API nuk e ktheu publikuesin, përdoret institutionCode
df["publisher"] = df.publishingOrg
df["publisherSource"] = "GBIF API"
no_pub = df.publisher.isna()
df.loc[no_pub, "publisher"] = df.loc[no_pub, "institutionCode"].fillna("E panjohur")
df.loc[no_pub, "publisherSource"] = "institutionCode"
print(df.groupby("publisherSource").size().rename("regjistrime").to_string())


def share(counts):
    out = counts.rename("regjistrime").to_frame()
    out["perqindja"] = (out.regjistrime / total * 100).round(2)
    out["perqindja_kumulative"] = out.perqindja.cumsum().round(2)
    return out


# %%
section("4. BURIMET KRYESORE SIPAS PUBLIKUESIT")
by_pub = (df.groupby("publisher")
            .agg(regjistrime=("datasetKey", "size"),
                 dataset_e=("datasetKey", "nunique"),
                 basisOfRecord=("basisOfRecord", lambda s: s.mode().iat[0]),
                 license=("license", lambda s: ", ".join(s.value_counts().index)))
            .sort_values("regjistrime", ascending=False))
by_pub["perqindja"] = (by_pub.regjistrime / total * 100).round(2)
by_pub["perqindja_kumulative"] = by_pub.perqindja.cumsum().round(2)
print(f"Publikues gjithsej: {len(by_pub)}\n")
print(by_pub.head(TOP_N)[["regjistrime", "perqindja", "perqindja_kumulative", "dataset_e",
                          "basisOfRecord", "license"]])
print(f"\nTë tjerë ({len(by_pub) - TOP_N}): {by_pub.regjistrime.iloc[TOP_N:].sum():,} regjistrime "
      f"({by_pub.perqindja.iloc[TOP_N:].sum():.2f}%)")


# %%
section("5. BURIMET KRYESORE SIPAS DATASET-IT")
by_ds = (df.groupby(["datasetKey", "datasetTitle", "publisher"], dropna=False)
           .size().sort_values(ascending=False))
by_ds = share(by_ds).reset_index()
print(by_ds.head(TOP_N)[["datasetTitle", "publisher", "regjistrime", "perqindja", "perqindja_kumulative"]]
      .to_string(index=False))


# %%
section("6. SIPAS basisOfRecord")
print(share(df.basisOfRecord.value_counts()))


# %%
section("7. SIPAS LICENCËS")
print(share(df.license.value_counts()))


# %%
section("8. PUBLIKUESIT KRYESORË × basisOfRecord DHE × LICENCA")
top_pubs = by_pub.index[:10]
top = df[df.publisher.isin(top_pubs)]
print(pd.crosstab(top.publisher, top.basisOfRecord, margins=True, margins_name="Totali")
        .reindex(list(top_pubs) + ["Totali"]))
print()
print(pd.crosstab(top.publisher, top.license, margins=True, margins_name="Totali")
        .reindex(list(top_pubs) + ["Totali"]))


# %%
section("9. RUAJTJA: processed/sources_summary.csv")
group_cols = ["publisher", "publisherCountry", "publishingOrgKey", "datasetKey", "datasetTitle",
              "datasetDOI", "institutionCodes", "basisOfRecord", "license", "publisherSource"]
summary = (df.groupby(group_cols, dropna=False)
             .size().rename("regjistrime").reset_index()
             .sort_values("regjistrime", ascending=False))
summary["perqindja"] = (summary.regjistrime / total * 100).round(3)
summary.to_csv(SOURCES_SUMMARY_PATH, index=False)

assert summary.regjistrime.sum() == total
print(f"{len(summary)} rreshta (publikues × dataset × basisOfRecord × licencë) -> {SOURCES_SUMMARY_PATH}")
