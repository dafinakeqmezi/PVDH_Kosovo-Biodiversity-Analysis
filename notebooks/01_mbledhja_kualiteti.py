import pandas as pd
import numpy as np
from pathlib import Path

pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 200)

try:
    ROOT = Path(__file__).resolve().parent.parent
except NameError:  
    ROOT = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()

DATA_PATH = ROOT / "dataset" / "kosovo_overall_biodiversity.csv"
REPORTS_DIR = ROOT / "reports"


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")

section("1. MBLEDHJA E TË DHËNAVE")
df_raw = pd.read_csv(DATA_PATH, low_memory=False)
print(f"Rreshta: {df_raw.shape[0]:,}  |  Kolona: {df_raw.shape[1]}")
print(df_raw.head(3).T)

df_raw.info(memory_usage="deep")

section("Madhësia e skedarëve")
GITHUB_LIMIT_MB = 100


def file_size_mb(path):
    return path.stat().st_size / 1024**2


print(f"Dataseti origjinal: {file_size_mb(DATA_PATH):.1f} MB")
print(f"Në memorie (pandas): {df_raw.memory_usage(deep=True).sum() / 1024**2:.1f} MB")

drop_planned = ["iasAppliesFrom", "establishmentMeans", "identifiedBy", "iucnRedListStatus",
                "taxonKey", "catalogNumber", "collectionCode", "issue"]
cleaned_mb = len(df_raw.drop(columns=drop_planned).to_csv(index=False).encode("utf-8")) / 1024**2
sample_mb = len(df_raw.sample(frac=0.1, random_state=42).to_csv(index=False).encode("utf-8")) / 1024**2
print(f"Versioni i pastruar (vlerësim): {cleaned_mb:.1f} MB")
print(f"Mostra 10% (vlerësim): {sample_mb:.1f} MB")
print(f"Kufiri i GitHub: {GITHUB_LIMIT_MB} MB")

section("2. DEFINIMI I TIPEVE TË TË DHËNAVE")
df = df_raw.copy()

int_cols = ["year", "month", "day", "individualCount", "taxonKey", "speciesKey"]
for c in int_cols:
    df[c] = df[c].astype("Int64")

cat_cols = [
    "kingdom", "phylum", "class", "order", "family", "taxonRank",
    "iucnRedListStatus", "municipality", "district", "protectedArea",
    "protectedAreaDesignation", "basisOfRecord", "establishmentMeans",
    "institutionCode", "collectionCode", "datasetKey", "license", "iasAppliesFrom",
]
for c in cat_cols:
    df[c] = df[c].astype("category")

iucn_order = ["LC", "NT", "VU", "EN", "CR", "EW", "EX"]
df["iucnRedListCategory"] = pd.Categorical(
    df["iucnRedListCategory"].replace({"NE": np.nan, "DD": np.nan}),
    categories=iucn_order, ordered=True,
)

mem_before = df_raw.memory_usage(deep=True).sum() / 1024**2
mem_after = df.memory_usage(deep=True).sum() / 1024**2
print(f"Memoria: {mem_before:.1f} MB -> {mem_after:.1f} MB")

type_summary = pd.DataFrame({
    "tipi_origjinal": df_raw.dtypes.astype(str),
    "tipi_i_ri": df.dtypes.astype(str),
    "vlera_unike": df_raw.nunique(),
})
print(type_summary[type_summary.tipi_origjinal != type_summary.tipi_i_ri])

section("3.1 VLERAT E ZBRAZËTA")
missing = pd.DataFrame({
    "mungojne": df_raw.isna().sum(),
    "perqindja": (df_raw.isna().mean() * 100).round(2),
}).sort_values("perqindja", ascending=False)
print(missing[missing.mungojne > 0])

print("\nRreshta pa asnjë vlerë që mungon:", df_raw.dropna().shape[0])
print("Kolona komplet:", missing.index[missing.mungojne == 0].tolist())

print(df_raw["iucnRedListCategory"].value_counts(dropna=False))

section("3.2 DUPLIKATET")
print("Rreshta identikë:", df_raw.duplicated().sum())
print("gbifID të përsëritura:", df_raw["gbifID"].duplicated().sum())

key = ["scientificName", "decimalLatitude", "decimalLongitude", "eventDate"]
print("Vëzhgime të mundshme të dyfishta (takson + koordinata + data):", df_raw.duplicated(subset=key).sum())

section("3.3 FORMATET E eventDate")
dates = df_raw["eventDate"].dropna()
fmt = (dates.str.replace(r"\d", "9", regex=True)
            .value_counts()
            .rename_axis("formati")
            .to_frame("regjistrime"))
print(fmt)

start = df_raw["eventDate"].str.split("/").str[0].str[:10]
df["eventDate"] = pd.to_datetime(start, format="ISO8601", errors="coerce")
df["eventDatePrecision"] = pd.Categorical(
    start.str.len().map({4: "year", 7: "month", 10: "day"})
)
df["isDateRange"] = df_raw["eventDate"].str.contains("/", na=False)

print("\nData të palexueshme:", (df["eventDate"].isna() & df_raw["eventDate"].notna()).sum())
print("Intervale datash:", df["isDateRange"].sum())
print(df["eventDatePrecision"].value_counts(dropna=False))


both = df["eventDate"].notna() & df["year"].notna()
mismatch = both & (df["eventDate"].dt.year != df["year"])
print("\nMospërputhje eventDate vs year:", mismatch.sum())
print("Data në të ardhmen:", (df["eventDate"] > pd.Timestamp.today()).sum())

section("3.4 VLERAT E DYSHIMTA")
print(df[["year", "decimalLatitude", "decimalLongitude", "coordinateUncertaintyInMeters",
          "elevation", "individualCount"]].describe().T)

LAT, LON = (41.85, 43.27), (20.01, 21.80)
ELEV = (297, 2656)

checks = {
    "Koordinata jashtë Kosovës": ~df.decimalLatitude.between(*LAT) | ~df.decimalLongitude.between(*LON),
    "Lartësia = 0 m": df.elevation == 0,
    "Lartësia jashtë 297–2656 m (pa 0)": df.elevation.notna() & (df.elevation != 0) & ~df.elevation.between(*ELEV),
    "Pasiguria e koordinatave > 10 km": df.coordinateUncertaintyInMeters > 10_000,
    "Viti para 1900": df.year < 1900,
    "Identifikim mbi nivelin e species": df.species.isna(),
}
quality = pd.DataFrame({
    "regjistrime": {k: int(v.sum()) for k, v in checks.items()},
})
quality["perqindja"] = (quality.regjistrime / len(df) * 100).round(2)
print()
print(quality)


ic = df["individualCount"].dropna()
q1, q3 = ic.quantile([0.25, 0.75])
upper = q3 + 1.5 * (q3 - q1)
print(f"\nQ1={q1}, Q3={q3}, kufiri i sipërm IQR={upper}")
print("Outliers:", (ic > upper).sum(), "| Maksimumi:", ic.max())
print(ic.value_counts().head(10))

section("3.5 FLAMUJT E GBIF (issue)")
issues = (df_raw["issue"].dropna()
          .str.split(";")
          .explode()
          .value_counts()
          .rename_axis("flamuri")
          .to_frame("regjistrime"))
issues["perqindja"] = (issues.regjistrime / len(df_raw) * 100).round(2)
print(issues.head(15))

section("3.6 KONSISTENCA E VLERAVE KATEGORIKE")
for c in ["kingdom", "taxonRank", "basisOfRecord", "district", "license", "strictlyProtected", "iasUnionConcern"]:
    print(f"--- {c} ---")
    print(df[c].value_counts(dropna=False).to_string(), "\n")

section("4. RUAJTJA E RAPORTEVE")
REPORTS_DIR.mkdir(exist_ok=True)
missing.to_csv(REPORTS_DIR / "01_vlerat_e_zbrazeta.csv")
quality.to_csv(REPORTS_DIR / "01_kontrollet_e_kualitetit.csv")
issues.to_csv(REPORTS_DIR / "01_gbif_issues.csv")
print("Raportet u ruajtën në", REPORTS_DIR.resolve())
