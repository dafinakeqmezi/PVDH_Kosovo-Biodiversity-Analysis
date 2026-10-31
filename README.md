<table border="0">
 <tr>
    <td><img src="https://github.com/user-attachments/assets/9002855f-3f97-4b41-a180-85d1e24ad34a" alt="University Logo" width="110" align="left"/></td>
    <td>
      <p><strong>University of Prishtina</strong></p>
      <p>Faculty of Electrical and Computer Engineering</p>
      <p>Computer and Software Engineering — Master's Program</p>
      <p>Professor: Prof. Mergim Hoti</p>
      <p>Assistant: Blend Berisha</p>
      <p>Course: Data Preparation and Visualization</p>
    </td>
 </tr>
</table>

---

## Contributors
Dafina Keqmezi, Delize Kadriu, Jeta Syla

Academic Year: 2026 / 2027

---

## Part I group report

The consolidated [Part I report](reports/raporti_pjesa_1.md) covers all preprocessing stages by topic, without individual task attribution. Detailed task reports and CSV tables remain supporting evidence.

The GBIF download DOI/date remain unconfirmed; no citation was invented.

The [processed-output audit](reports/verifikimi_i_te_dhenave_te_perpunuara.md) reports 22 passing checks. Run `python scripts/verify_processed.py` for read-only verification. The samples use the original data, not the cleaned checkpoint; they contain 85 and 89 IDs subsequently removed as duplicates. Notebook 03 now executes and exports its outputs end to end. The full pipeline passed in a fresh environment; see the [reproducibility report](reports/riprodhueshmeria.md) and [submission checklist](reports/lista_e_dorezimit.md).

## Repository structure

```
PVDH/
├── dataset/
│   └── kosovo_overall_biodiversity.csv      
├── notebooks/
│   ├── 01b_analiza_burimeve.ipynb           
│   ├── 01_mbledhja_kualiteti.ipynb          
│   ├── 02_pastrimi.ipynb                   
│   └── 03_vetite.ipynb                      
├── processed/
│   ├── biodiversity_clean.csv               
│   ├── cleaning_log.csv                     
│   ├── municipalities.csv                  
│   ├── agg_*.csv / agg_*_v2.csv             
│   ├── sample_random.csv, sample_stratified.csv
│   ├── biodiversity_features.csv            
│   └── pca_municipalities.csv               
├── reports/
│   ├── 01_*.csv                             
│   ├── *.md                                 
│   └── raporti_pjesa_1.md         
├── requirements.txt
└── README.md
```

## Setup and how to run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_pipeline.py
```

Tested with Python 3.13.5 and pandas 3.0.6 in a newly installed virtual environment on macOS arm64. On Windows use `.venv\Scripts\activate` instead. Direct dependencies are pinned in `requirements.txt`; `requirements-lock.txt` records the complete tested macOS environment.

`run_pipeline.py` executes in a temporary local clone and prints the paths to the execution record and executed notebooks. It uses the invoking Python environment for every kernel and leaves this checkout's data unchanged. Keep the Git history containing duplicate-reference commit `d2708c6`. The bootstrap pass regenerates the municipality reference table before cleaning; this avoids the dependency between notebook 02 and notebook 01's final aggregate section.

For manual execution, use the repo root or `notebooks/` as working directory. With the committed municipality reference table available, use the following order. For regeneration without existing derived files, use the script's bootstrap pass first:

| Order | Notebook | Input | Output |
|---|---|---|---|
| 1 | `01b_analiza_burimeve.ipynb` | original dataset, GBIF API (results cached in `processed/gbif_datasets_cache.csv`; internet only for datasets not yet cached) | `processed/sources_summary.csv` |
| 2 | `02_pastrimi.ipynb` | original dataset, `municipalities.csv`; duplicate candidates read from Git commit `d2708c6` | `processed/biodiversity_clean.csv` (frozen: the notebook refuses to overwrite it with different content), `processed/cleaning_log.csv` |
| 3 | `01_mbledhja_kualiteti.ipynb` | original dataset; `add_taxon_features()` read from `03_vetite.ipynb`; `biodiversity_clean.csv` for section 8 | `reports/01_*.csv`, `processed/municipalities.csv`, aggregates (`agg_*.csv`, `agg_*_v2.csv`), samples |
| 4 | `03_vetite.ipynb` | cleaned CSV/schema/manifest, publisher cache, municipality taxon matrices v1/v2 | `biodiversity_features.csv`, standardized matrices and PCA scores for both v1 and v2; the final execution cell exports all five files |

To run a notebook from start to end without opening it (the same as Restart & Run All):

```bash
python -m jupyter nbconvert --to notebook --execute --inplace notebooks/01_mbledhja_kualiteti.ipynb
```

Notebook 01 takes a few minutes, mostly for the 200 repeated samples in section 7. Every section ends with a "Dokumentimi i hapit" cell (input, what was done, rows/columns before and after, why, output, commit).

---

## Dataset

**File:** `dataset/kosovo_overall_biodiversity.csv`

### Source: GBIF

[GBIF – Global Biodiversity Information Facility](https://www.gbif.org) is an international open-data network, funded by governments, that aggregates biodiversity records from museums, herbaria, research institutions and citizen-science platforms worldwide. Records follow the Darwin Core standard. Each record is an *occurrence*: one organism observed or collected at a given place and time.

Our dataset combines records from **125 GBIF datasets** published by **80 publishing organizations** (108 distinct `institutionCode` values). The CSV has no publisher columns, so the publisher of each dataset was retrieved from the GBIF API (`/v1/dataset/{datasetKey}` → `/v1/organization/{key}`) in [`01b_analiza_burimeve.ipynb`](notebooks/01b_analiza_burimeve.ipynb). The main sources are:

| Publisher | Main dataset | Records | % | Cumulative % | Basis of record | License |
|---|---|---|---|---|---|---|
| Cornell Lab of Ornithology (US) | EOD – eBird Observation Dataset | 26,009 | 55.54 | 55.54 | Human observation | CC BY 4.0 |
| HabiProt (RS) | Arthropod observations from the HabiProt Alciphron database | 8,122 | 17.34 | 72.88 | Human observation | CC BY-NC 4.0 |
| iNaturalist.org (US) | iNaturalist Research-grade Observations | 4,286 | 9.15 | 82.03 | Human observation | CC BY-NC / CC BY / CC0 |
| Observation.org | Observation.org, Nature data from around the World | 1,436 | 3.07 | 85.10 | Human observation | CC BY-NC 4.0 |
| naturgucker.de | NABU\|naturgucker | 721 | 1.54 | 86.64 | Human observation | CC BY 4.0 |
| Pl@ntNet | Pl@ntNet automatically identified occurrences | 660 | 1.41 | 88.05 | Human observation | CC BY 4.0 |
| University of Graz | Herbarium GZU | 659 | 1.41 | 89.46 | Preserved specimen | CC BY 4.0 |
| VectorNet | VectorNet observations | 587 | 1.25 | 90.71 | Human observation | CC BY 4.0 |
| Macedonian Ecological Society | High-altitude endemic beetles of the western Balkans | 483 | 1.03 | 91.74 | Occurrence | CC BY-NC 4.0 |
| CIAT | Global database of crop wild relatives | 386 | 0.82 | 92.56 | Occurrence | CC BY 4.0 |
| *70 other publishers* | | 3,482 | 7.44 | 100.00 | | |

Three publishers supply 82% of all records, and 90.7% of records are human observations (mostly citizen science). The full breakdown by publisher × dataset × basis of record × license is in [`processed/sources_summary.csv`](processed/sources_summary.csv).

### Download details

| Property | Value |
|---|---|
| Country filter | Kosovo (GBIF country code `XK`) |
| Download date | **TODO** – exact date of the GBIF download (the latest record is from 2026-08-22, and the file is dated 2026-10-05) |
| Download DOI | **TODO** – `https://doi.org/10.15468/dl.xxxxxx` |
| Format | CSV, comma-separated, UTF-8, with a header row |
| Size | 22 MB (23,101,890 bytes) |
| Rows × columns | 46,831 records × 42 columns |

All coordinates fall inside Kosovo's borders. GBIF flags 7,505 records (16%) with `COUNTRY_DERIVED_FROM_COORDINATES`, meaning their country was assigned from the coordinates rather than given by the publisher.

Of the 42 columns, 34 are standard GBIF / Darwin Core fields. The other 8 are added attributes specific to Kosovo: `iucnRedListStatus`, `municipality`, `district`, `protectedArea`, `protectedAreaDesignation`, `strictlyProtected`, `iasUnionConcern` and `iasAppliesFrom`.

### Licenses

Each record keeps the license chosen by its publisher:

| License | Records | Datasets | Terms |
|---|---|---|---|
| CC BY 4.0 | 31,757 (67.8%) | 80 | Free use with attribution |
| CC BY-NC 4.0 | 14,267 (30.5%) | 25 | Attribution, non-commercial use only |
| CC0 1.0 | 807 (1.7%) | 22 | Public domain, no restrictions |

Because part of the data is CC BY-NC, the dataset as a whole may be used only for non-commercial purposes, such as this academic project. Attribution is satisfied by citing the GBIF download DOI.

### Overview

- **Records:** 46,831 rows, 42 columns, no duplicate rows
- **Time span:** 1826 – 2026 (median year 2020)
- **Kingdoms:** Animalia (42,003), Plantae (3,740), Fungi (1,006), plus a few Chromista, Protozoa and Bacteria records
- **Taxa:** 4,647 distinct scientific names, 4,095 species
- **Geography:** 7 districts, 38 municipalities, 20 protected areas

### Attribute groups and data types

| Group | Columns | Type |
|---|---|---|
| Identifiers | `gbifID`, `taxonKey`, `speciesKey`, `datasetKey`, `catalogNumber` | integer / nominal |
| Taxonomy | `kingdom`, `phylum`, `class`, `order`, `family`, `genus`, `species`, `scientificName`, `vernacularName`, `taxonRank` | categorical (nominal, hierarchical) |
| Conservation status | `iucnRedListCategory`, `iucnRedListStatus` | categorical (ordinal: LC < NT < VU < EN < CR < EX) |
| Time | `eventDate`, `year`, `month`, `day` | date / discrete numeric |
| Location | `decimalLatitude`, `decimalLongitude`, `coordinateUncertaintyInMeters`, `elevation` | continuous numeric |
| Administrative / protection | `locality`, `municipality`, `district`, `protectedArea`, `protectedAreaDesignation`, `strictlyProtected` | categorical / boolean |
| Observation | `basisOfRecord`, `individualCount`, `establishmentMeans`, `recordedBy`, `identifiedBy` | categorical / discrete numeric |
| Source / metadata | `institutionCode`, `collectionCode`, `license`, `issue`, `iasUnionConcern`, `iasAppliesFrom` | categorical / boolean |

### Data quality overview

Share of missing values for the most affected columns:

| Column | Missing |
|---|---|
| `iasAppliesFrom` | 99.9% |
| `establishmentMeans` | 99.5% |
| `identifiedBy` | 83.5% |
| `elevation` | 79.0% |
| `coordinateUncertaintyInMeters` | 68.3% |
| `protectedArea`, `protectedAreaDesignation` | 55.0% |
| `individualCount` | 37.8% |
| `locality` | 32.6% |
| `eventDate` / `year` | 4.7% / 4.8% |
| `species`, `iucnRedListCategory` | 2.6% |

Other observations:
- Coordinates, `district`, `municipality` and `basisOfRecord` are complete.
- `iucnRedListCategory` contains 15,705 `NE` (Not Evaluated) records, which act as a hidden "unknown" value.
- 1,296 records (2.8%) are identified only above species level (genus, family, order, unranked, etc.).
- The `issue` column holds GBIF quality flags that can be used to filter unreliable records.

---

## Phase I results

| Step | Result |
|---|---|
| Data | 46,831 records × 42 columns from GBIF; after cleaning 46,456 records × 83 columns (`processed/biodiversity_clean.csv`) |
| Sources | 125 datasets from 80 publishers; eBird, HabiProt and iNaturalist supply 82.03% of records; 90.71% are human observations |
| Types | 42 columns typed (18 nominal, 5 ID, 5 ordinal, 4 interval, 4 text, 2 ratio, 2 binary, 2 date); memory 31.9 → 13.6 MB |
| Quality | 35 checks in 5 dimensions. Format/range checks do not prove spatial or biological accuracy; 93.16% of rows have species, date, coordinates and municipality. IUCN evaluation availability is 63.84%; `NE`/`DD` are retained reported codes, not blank cells. 8,225 records have uncertainty 7071 m, consistent with grid-generalized coordinates; 1,645 rows (3.51%) have a serious GBIF flag |
| Bias | One location (Henc wetland) holds 27.86% of records and one observer 35.18%; birds are 61.47% of records but 6.23% of species |
| Cleaning | 375 duplicates removed (235 groups); `elevation = 0` set to missing; blank protected areas named "Jashtë zonës së mbrojtur"; `individualCount` not imputed (17,587 missing); 102 logged steps |
| Integration | Area and population of the 38 municipalities from official sources (ASK census 2024, 2017 territory measurement); join 38/38 with no row lost |
| Aggregation | By municipality, time, class × district and species; on the cleaned data only record counts change (−0.80%), no species, class, year or municipality is lost |
| Sampling | Random and class-stratified samples of 10,000; the stratified sample keeps the class distribution best (TVD 0.104 vs 0.703 pp); both keep only 46.6% of species, so species analyses use the full dataset |
| Features | 45 feature columns (time, taxonomy, IUCN, protection, source, elevation zone, period, count class, one-hot, flags, `log1p`); municipality PCA keeps PC1–PC3 (77.04% of variance) |

Report sections: [`reports/raporti_pjesa_1.md`](reports/raporti_pjesa_1.md) (collection to sampling).

## Phase I – Data Preprocessing (15%)

Goal: prepare the dataset for analysis and visualization.

### Phase I checklist

| Requirement | Status | Notebook | Main documents |
|---|---|---|---|
| Data collection | done | 01, 01b | README "Dataset", `reports/fjalori_i_te_dhenave.md` |
| Data types | done | 01 §2 | `reports/tipet_e_te_dhenave.md` |
| Data quality | done | 01 §3 | `reports/korniza_e_kualitetit.md`, `plotesia.md`, `vlefshmeria.md`, `flamujt_gbif.md`, `unikaliteti.md`, `konsistenca_dhe_anshmeria.md` |
| Integration | done | 01 §5, 02 | `reports/burimet_e_te_dhenave_te_komunave.md`, `bashkimi_i_komunave.md`; cross-source duplicates and category harmonization in `largimi_i_duplikateve.md`, `pastrimi_i_kategorive.md` |
| Aggregation | done | 01 §6, §8 | `reports/agregimi_sipas_komunes.md`, `agregimi_sipas_kohes.md`, `agregimi_sipas_specieve_dhe_rajonit.md`, `rikalkulimi.md`. IUCN: threatened species per municipality and the IUCN category of each species |
| Sampling | done | 01 §7 | `reports/mostrimi.md` |
| Cleaning | done | 02 | `reports/finalizimi_i_datasetit.md`, `validimi.md`, `processed/cleaning_log.csv` |
| Missing values | done | 02 | `reports/strategjia_e_mungesave.md`, `vendimet_per_mungesat_strukturore.md`, `vendimi_per_numrin_e_individeve.md` |
| Dimensionality reduction | done | 03 | redundant columns dropped (`reports/redundanca.md`, `zgjedhja_e_vetive.md`); municipality PCA (`reports/pca_komunat.md`) |
| Feature subset selection | done | 03 | `reports/rendesia_e_kolonave.md` (analytical importance of each column), `zgjedhja_e_vetive.md` |
| Feature creation | done | 03 | `reports/vetite_kohore.md`, `vetite_taksonomike.md`, `vetite_e_burimit.md` |
| Discretization | done | 03 | `reports/zona_e_lartesise.md`, `periudhat_kohore.md`, `klasa_e_numrit.md` |
| Binarization | done | 03 | `reports/kolonat_dummy.md`, `kodimi_iucn_dhe_flamujve.md` |
| Transformation | done | 03 | `reports/transformimi_log1p.md`, `shkallezimi_pca.md` |

Key findings (full tables in [`reports/`](reports/)):
- `eventDate` uses 11 different ISO 8601 formats, including year-only, year-month and date ranges (447 records); the start date and its precision were extracted
- 3,336 records share the same taxon, coordinates and date (possible duplicates across sources)
- 3,634 records have `elevation = 0` (37% of filled elevations), which acts as a placeholder for "unknown"
- `individualCount` is highly skewed (median 2, max 10,200); `coordinateUncertaintyInMeters` reaches 4,226 km
- All coordinates fall inside Kosovo; no future dates; `eventDate` and `year` are consistent

Tables written by notebook 01 (`reports/`):

---
