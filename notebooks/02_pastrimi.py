import pandas as pd
import numpy as np
from pathlib import Path

pd.set_option("display.max_columns", 80)
pd.set_option("display.width", 220)
pd.set_option("display.max_colwidth", 120)

try:
    ROOT = Path(__file__).resolve().parent.parent
except NameError:
    ROOT = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()

DATA_PATH = ROOT / "dataset" / "kosovo_overall_biodiversity.csv"
PROCESSED_DIR = ROOT / "processed"
REPORTS_DIR = ROOT / "reports"
CLEANING_LOG_PATH = PROCESSED_DIR / "cleaning_log.csv"
MISSING_REPORT_PATH = PROCESSED_DIR / "missing_report.csv"
ISSUE_LIST_PATH = REPORTS_DIR / "02_issue_list.csv"

PROCESSED_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# %%
# 02 - Integrimi, pastrimi dhe vlerat e zbrazëta


# %%
# Shablloni i dokumentimit dhe cleaning log

LOG_COLUMNS = [
    "hapi",
    "input",
    "rreshta_para",
    "kolona_para",
    "rreshta_pas",
    "kolona_pas",
    "arsyeja",
    "output",
    "commit",
]


def init_cleaning_log(path=CLEANING_LOG_PATH):
    """Krijon cleaning_log.csv bosh me kolonat standarde, nëse nuk ekziston."""
    if not path.exists():
        pd.DataFrame(columns=LOG_COLUMNS).to_csv(path, index=False)
    return path


def log_step(
    hapi,
    inputi,
    shape_para,
    shape_pas,
    arsyeja,
    outputi="",
    commit="pending",
    path=CLEANING_LOG_PATH,
):
    """Shton një rresht në cleaning_log.csv për një hap pastrimi."""
    init_cleaning_log(path)
    row = {
        "hapi": hapi,
        "input": inputi,
        "rreshta_para": shape_para[0],
        "kolona_para": shape_para[1],
        "rreshta_pas": shape_pas[0],
        "kolona_pas": shape_pas[1],
        "arsyeja": arsyeja,
        "output": outputi,
        "commit": commit,
    }
    log = pd.read_csv(path)
    log = pd.concat([log, pd.DataFrame([row])], ignore_index=True)
    log.to_csv(path, index=False)
    return log.tail(1)


section("Shablloni i dokumentimit dhe cleaning log")
init_cleaning_log()
print(pd.read_csv(CLEANING_LOG_PATH))

# Dokumentimi i hapit: Shablloni i dokumentimit dhe cleaning log
# 1. Input: Struktura e repo-s; folderët notebooks/, processed/, reports/;
#    skedari i planifikuar processed/cleaning_log.csv.
# 2. Çka u bë: U krijua shablloni i dokumentimit dhe funksionet
#    init_cleaning_log() / log_step() për regjistrimin e hapave të pastrimit.
# 3. Rreshta para / rreshta pas: Dataset-i nuk u ndryshua.
#    cleaning_log.csv: 0 rreshta, 9 kolona pas inicializimit.
# 4. Pse u bë: Për të pasur gjurmë të qartë të çdo vendimi dhe për ta bërë
#    punën të kontrollueshme nga profesori/grupi.
# 5. Output: processed/cleaning_log.csv bosh me kolonat standarde.
# 6. Commit: Add cleaning documentation template and log helper.


# %%
# Eksplorimi fillestar i strukturës

section("Eksplorimi fillestar i strukturës")
df_raw = pd.read_csv(DATA_PATH, low_memory=False)
rows_before, cols_before = df_raw.shape
print(f"Rreshta: {rows_before:,}")
print(f"Kolona: {cols_before:,}")
print(df_raw.head())

df_raw.info(memory_usage="deep")

dtypes_report = (
    df_raw.dtypes.astype(str)
    .rename("tipi_i_lexuar")
    .reset_index()
    .rename(columns={"index": "kolona"})
)
print("\nTipet e lexuara:")
print(dtypes_report.to_string(index=False))

five_values_per_column = pd.DataFrame({
    "kolona": df_raw.columns,
    "5_vlera_shembull": [
        df_raw[c].dropna().astype(str).drop_duplicates().head(5).tolist()
        for c in df_raw.columns
    ],
    "vlera_unike": [df_raw[c].nunique(dropna=True) for c in df_raw.columns],
})
print("\n5 vlera shembull nga çdo kolonë:")
print(five_values_per_column.to_string(index=False))

issue_rows = []

date_patterns = (
    df_raw["eventDate"]
    .dropna()
    .astype(str)
    .str.replace(r"\d", "9", regex=True)
    .value_counts()
)
if len(date_patterns) > 1:
    issue_rows.append({
        "kategoria": "Format datash",
        "kolona": "eventDate",
        "problemi": f"eventDate paraqitet në {len(date_patterns)} formate/pattern-e të ndryshme.",
        "shembuj": "; ".join(date_patterns.head(5).index.tolist()),
        "veprim_i_sugjeruar": (
            "Parsimi me pd.to_datetime pas ndarjes së intervaleve dhe ruajtja e "
            "precision/date-range flag."
        ),
    })

for c in df_raw.columns:
    values = set(df_raw[c].dropna().astype(str).str.upper().unique())
    if values and values.issubset({"TRUE", "FALSE"}):
        issue_rows.append({
            "kategoria": "Boolean TRUE/FALSE",
            "kolona": c,
            "problemi": "Kolona përmban vlera TRUE/FALSE që duhen standardizuar.",
            "shembuj": ", ".join(sorted(values)),
            "veprim_i_sugjeruar": "Konvertim në boolean ose 0/1 në fazën e pastrimit/binarizimit.",
        })

for c in ["municipality", "district", "protectedArea"]:
    count = df_raw[c].fillna("").astype(str).str.contains("/", regex=False).sum()
    if count > 0:
        examples = (
            df_raw.loc[df_raw[c].fillna("").astype(str).str.contains("/", regex=False), c]
            .dropna()
            .drop_duplicates()
            .head(5)
            .tolist()
        )
        issue_rows.append({
            "kategoria": "Emra dygjuhësh",
            "kolona": c,
            "problemi": f"{count} rreshta përmbajnë emra me ndarës /.",
            "shembuj": "; ".join(examples),
            "veprim_i_sugjeruar": (
                "Ruaj vlerën origjinale dhe, nëse nevojitet, krijo kolonë të "
                "standardizuar për analizë."
            ),
        })

for c in df_raw.columns:
    count = df_raw[c].fillna("").astype(str).str.contains(";", regex=False).sum()
    if count > 0:
        examples = (
            df_raw.loc[df_raw[c].fillna("").astype(str).str.contains(";", regex=False), c]
            .dropna()
            .drop_duplicates()
            .head(3)
            .tolist()
        )
        issue_rows.append({
            "kategoria": "Lista në një kolonë",
            "kolona": c,
            "problemi": f"{count} rreshta kanë disa vlera të ndara me ;.",
            "shembuj": "; ".join(examples),
            "veprim_i_sugjeruar": "Split + explode për raportim ose krijim flamujsh binarë.",
        })

issue_list = pd.DataFrame(issue_rows)
issue_list.to_csv(ISSUE_LIST_PATH, index=False)
print("\nLista e problemeve të vërejtura:")
print(issue_list.to_string(index=False))

# Dokumentimi i hapit: Eksplorimi fillestar i strukturës
# 1. Input: dataset/kosovo_overall_biodiversity.csv; të gjitha kolonat për
#    shape, info, dtypes dhe 5 vlera shembull.
# 2. Çka u bë: U kontrollua struktura fillestare e dataset-it dhe u krijua
#    lista e problemeve të vërejtura: data në formate të ndryshme, boolean
#    TRUE/FALSE, emra dygjuhësh dhe lista me ;.
# 3. Rreshta para / rreshta pas: Dataset-i nuk u ndryshua; df_raw.shape mbetet
#    i njëjtë para/pas eksplorimit.
# 4. Pse u bë: Për të kuptuar strukturën reale para çdo pastrimi dhe për të
#    shmangur vendime pa evidencë.
# 5. Output: reports/02_issue_list.csv, dtypes_report,
#    five_values_per_column, issue_list.
# 6. Commit: Add initial structure exploration and issue list.


# %%
# Inventari i vlerave të zbrazëta

section("Inventari i vlerave të zbrazëta")
missing_report = pd.DataFrame({
    "kolona": df_raw.columns,
    "mungojne": df_raw.isna().sum().values,
    "perqindja": (df_raw.isna().mean().values * 100).round(2),
    "vlera_te_plotesuara": df_raw.notna().sum().values,
}).sort_values(["perqindja", "kolona"], ascending=[False, True])

missing_report.to_csv(MISSING_REPORT_PATH, index=False)
print(missing_report.to_string(index=False))

print("\nKolonat më problematike për planin e pastrimit:")
print(missing_report[missing_report["mungojne"] > 0].head(15).to_string(index=False))

# Dokumentimi i hapit: Inventari i vlerave të zbrazëta
# 1. Input: dataset/kosovo_overall_biodiversity.csv; të gjitha kolonat.
# 2. Çka u bë: U llogarit numri dhe përqindja e NaN për çdo kolonë dhe raporti
#    u rendit nga kolona më e zbrazët.
# 3. Rreshta para / rreshta pas: Dataset-i nuk u ndryshua. Raporti ka një
#    rresht për çdo kolonë të dataset-it; kolonat e raportit janë kolona,
#    mungojne, perqindja, vlera_te_plotesuara.
# 4. Pse u bë: Për të vendosur strategjinë e trajtimit të vlerave të zbrazëta
#    në hapat e pastrimit.
# 5. Output: processed/missing_report.csv dhe tabela missing_report.
# 6. Commit: Add missing values inventory.
