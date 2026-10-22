<table border="0">
 <tr>
    <td><img src="https://github.com/user-attachments/assets/9002855f-3f97-4b41-a180-85d1e24ad34a" alt="University Logo" width="110" align="left"/></td>
    <td>
      <p><strong>University of Prishtina</strong></p>
      <p>Faculty of Electrical and Computer Engineering</p>
      <p>Computer and Software Engineering — Master's Program</p>
      <p>Professor: Prof. Mergim Hoti</p>
      <p>Course: Data Preparation and Visualization</p>
    </td>
 </tr>
</table>

---

## Contributors
Dafina Keqmezi, Delize Kadriu, Jeta Syla

Academic Year: 2026 / 2027

---

## Repository structure

```
PVDH/
├── dataset/                
│   └── kosovo_overall_biodiversity.csv
├── processed/              
├── notebooks/            
│   ├── 01_mbledhja_kualiteti.ipynb
│   ├── 01b_analiza_burimeve.ipynb
│   ├── 02_pastrimi.ipynb
│   └── 03_vetite.ipynb
├── reports/             
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        
pip install -r requirements.txt
jupyter notebook notebooks/
```

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

### How to cite

GBIF requires citing the download through its DOI:

> GBIF.org (**TODO: DD Month YYYY**) GBIF Occurrence Download https://doi.org/10.15468/dl.xxxxxx

The DOI links to the full list of the 125 contributing datasets, so this single citation credits every publisher. See [GBIF citation guidelines](https://www.gbif.org/citation-guidelines).

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

## Phase I – Data Preprocessing (15%)

Goal: prepare the dataset for analysis and visualization.

### 1. Data collection, data types and data quality — [`01_mbledhja_kualiteti.ipynb`](notebooks/01_mbledhja_kualiteti.ipynb)
- [x] Describe the data source (GBIF) and the meaning of each attribute
- [x] Assign correct data types for all 42 columns: pandas type, conceptual type and target type → [`reports/data_types.md`](reports/data_types.md), [`reports/01_tipet_e_kolonave.csv`](reports/01_tipet_e_kolonave.csv)
- [x] Assess data quality: missing values, invalid coordinates, outliers, inconsistent values, GBIF `issue` flags
- [x] Quality framework: completeness, validity, consistency, uniqueness and timeliness, with 35 checks (metric, rule, columns, baseline value) → [`reports/quality_framework.md`](reports/quality_framework.md), [`reports/01_korniza_e_kualitetit.csv`](reports/01_korniza_e_kualitetit.csv)
- [x] Completeness per column (including hidden missing values) and per row (key fields: species, date, coordinates, municipality) → [`reports/completeness.md`](reports/completeness.md)
- [x] Validity: coordinates inside Kosovo, year range, month/day ranges, `eventDate` formats, frequency of 7071 in `coordinateUncertaintyInMeters`, `elevation` range → [`reports/validity.md`](reports/validity.md)
- [x] GBIF flags: count and % for each of the 35 `issue` flags, classified as serious or informative with a reason → [`reports/gbif_flags.md`](reports/gbif_flags.md)
- [x] Source analysis — [`01b_analiza_burimeve.ipynb`](notebooks/01b_analiza_burimeve.ipynb): publisher of each dataset from the GBIF API, grouped by publisher / dataset, `basisOfRecord` and `license` → [`processed/sources_summary.csv`](processed/sources_summary.csv)

Key findings (full tables in [`reports/`](reports/)):
- `eventDate` uses 11 different ISO 8601 formats, including year-only, year-month and date ranges (447 records); the start date and its precision were extracted
- 3,336 records share the same taxon, coordinates and date (possible duplicates across sources)
- 3,634 records have `elevation = 0` (37% of filled elevations), which acts as a placeholder for "unknown"
- `individualCount` is highly skewed (median 2, max 10,200); `coordinateUncertaintyInMeters` reaches 4,226 km
- All coordinates fall inside Kosovo; no future dates; `eventDate` and `year` are consistent

### 2. Integration, aggregation, sampling, cleaning and missing values — [`02_pastrimi.ipynb`](notebooks/02_pastrimi.ipynb)
- [x] Create the documentation template and `log_step()` helper for cleaning steps
- [x] Initialize [`processed/cleaning_log.csv`](processed/cleaning_log.csv)
- [x] Inspect the initial structure: `shape`, `df.info()`, `dtypes` and 5 sample values per column
- [x] Create an issue list for mixed date formats, boolean values, bilingual names and `;`-separated lists
- [x] Create [`processed/missing_report.csv`](processed/missing_report.csv), sorted by missing-value percentage
- [x] Audit hidden missing-value tokens and document the decision for `elevation = 0`
- [x] Compare missingness by source, `basisOfRecord`, class and district, with cautious interpretation of missingness mechanisms
- [x] Define a column-specific missing-value strategy using analytical importance and recoverability
- [ ] **Integration** – merge records coming from different `datasetKey` sources and harmonize column values
- [ ] **Aggregation** – summarize occurrences per species, district, municipality, year and IUCN category
- [ ] **Sampling** – draw a stratified sample (e.g. by `kingdom` or `district`) for faster exploration
- [ ] **Cleaning** – apply the documented column-specific decisions, use species-level exclusions only where needed, and fix inconsistent text values
- [ ] **Apply missing-value strategy** – implement [`reports/strategjia_e_mungesave.md`](reports/strategjia_e_mungesave.md) in a derived dataset and log transformations; recover only explicit date components, use analysis-specific exclusions, and verify protection coverage before assigning "Not protected"
- [x] Apply column removals, confirmed missing tokens and missingness flags to a separate working dataset; flag zero elevations without replacing them yet
- [x] Separate IAS structural missingness with status flags; retain unknown protected-area values
- [ ] Verify protected-area spatial coverage before replacing blanks with "outside protected area"
- [x] Parse dates into `event_start`, `event_end` and `date_precision`, preserving interval endpoints and original text
- [x] Convert nullable integers, booleans and unordered categories; leave IUCN ordinal encoding to notebook 03

Current outputs:
- [`processed/cleaning_log.csv`](processed/cleaning_log.csv) – per-step transformation log; reruns update this notebook's steps without duplicating them
- [`processed/missing_report.csv`](processed/missing_report.csv) – number and percentage of missing values for every column
- [`reports/02_lista_e_problemeve.csv`](reports/02_lista_e_problemeve.csv) – initial list of structural/data-quality issues observed during exploration
- [`reports/mungesat_e_fshehura.csv`](reports/mungesat_e_fshehura.csv) and [`reports/raporti_i_mungesave_efektive.csv`](reports/raporti_i_mungesave_efektive.csv) – literal-token audit and effective missingness without double counting
- [`reports/lartesia_zero_sipas_grupeve.csv`](reports/lartesia_zero_sipas_grupeve.csv), [`reports/regjistrimet_me_lartesi_zero.csv`](reports/regjistrimet_me_lartesi_zero.csv) and [`reports/vendimi_per_lartesine_zero.md`](reports/vendimi_per_lartesine_zero.md) – source/location evidence and the zero-elevation decision
- [`reports/mungesat_sipas_grupeve.csv`](reports/mungesat_sipas_grupeve.csv) and [`reports/mekanizmat_e_mungeses.md`](reports/mekanizmat_e_mungeses.md) – group denominators, missingness rates and interpretation limits
- [`reports/strategjia_e_mungesave.md`](reports/strategjia_e_mungesave.md) – strategy for all 42 columns; column cleaning and flags are implemented, while conditional recovery and protected-area verification remain pending
- [`processed/kosovo_biodiversity_clean.csv`](processed/kosovo_biodiversity_clean.csv) – intermediate working dataset through the type-conversion stage; not the final `biodiversity_clean.csv` checkpoint. The original CSV remains unchanged and all records are retained
- [`processed/kosovo_biodiversity_clean_schema.json`](processed/kosovo_biodiversity_clean_schema.json) – type/category metadata and source hash; use `load_clean_dataset()` in notebook 02 to restore CSV types
- [`reports/kolonat_para_pas_pastrimit.csv`](reports/kolonat_para_pas_pastrimit.csv), [`reports/numerimet_e_pastrimit.csv`](reports/numerimet_e_pastrimit.csv) and [`reports/tipet_para_pas_pastrimit.csv`](reports/tipet_para_pas_pastrimit.csv) – column changes, affected counts and types before/after
- [`reports/vendimet_per_mungesat_strukturore.md`](reports/vendimet_per_mungesat_strukturore.md) and [`reports/numerimet_e_mungesave_strukturore.csv`](reports/numerimet_e_mungesave_strukturore.csv) – evidence limits, flags and replacement counts
- [`reports/formatet_e_datave.csv`](reports/formatet_e_datave.csv) and [`reports/problemet_e_parsimit_te_datave.csv`](reports/problemet_e_parsimit_te_datave.csv) – observed date formats and parsing failures

Current scope for notebook 02: tasks through 18 October only. Protected-area replacement remains pending evidence. Later tasks (year/month recovery, duplicates, category harmonization, invalid-value replacement, individualCount treatment and the final checkpoint) are not implemented here. Zero elevations remain in the intermediate CSV with a flag; the earlier diagnostic missingness reports count them as unusable values for strategy planning.

### 3. Dimensionality reduction, feature selection, feature creation, discretization, binarization and transformation — [`03_vetite.ipynb`](notebooks/03_vetite.ipynb)
- [x] Document preprocessing plan v1 with decision and rationale
- [ ] **Dimensionality reduction** – remove redundant attributes (`iucnRedListStatus` vs. `iucnRedListCategory`, `taxonKey` vs. `scientificName`)
- [ ] **Feature subset selection** – keep the attributes relevant for the analysis (taxonomy, time, location, conservation status)
- [ ] **Feature creation** – e.g. `season` from `month`, `decade` from `year`, `isThreatened` from IUCN category, record count per species
- [ ] **Discretization** – bin `elevation` and `year` into ranges (e.g. lowland / hill / mountain, decades)
- [ ] **Binarization** – one-hot encode `kingdom`, `basisOfRecord`; convert `strictlyProtected` and `iasUnionConcern` to 0/1
- [ ] **Transformation** – normalize/scale numeric attributes (`elevation`, `individualCount`), apply log transform to skewed counts

---
