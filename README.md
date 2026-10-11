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
│   ├── 01_mbledhja_kualiteti.py
│   └── 02_pastrimi.py
│   └── 03_vetite.py
├── reports/             
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        
pip install -r requirements.txt
python notebooks/01_mbledhja_kualiteti.py
python notebooks/02_pastrimi.py
```

---

## Dataset

**File:** `dataset/kosovo_overall_biodiversity.csv`

### Source: GBIF

[GBIF – Global Biodiversity Information Facility](https://www.gbif.org) is an international open-data network, funded by governments, that aggregates biodiversity records from museums, herbaria, research institutions and citizen-science platforms worldwide. Records follow the Darwin Core standard. Each record is an *occurrence*: one organism observed or collected at a given place and time.

Our dataset combines records from **125 GBIF datasets** published by **108 institutions**. The largest contributors are:

| Institution | Records | Source |
|---|---|---|
| CLO | 26,009 | eBird (Cornell Lab of Ornithology) |
| HabiProt | 8,122 | – |
| iNaturalist | 4,286 | iNaturalist research-grade observations |
| NABU \| naturgucker | 721 | – |
| GZU | 659 | – |

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

### 1. Data collection, data types and data quality — [`01_mbledhja_kualiteti.py`](notebooks/01_mbledhja_kualiteti.py)
- [x] Describe the data source (GBIF) and the meaning of each attribute
- [x] Assign correct data types (`eventDate` → datetime, `year`/`month`/`day` → integer, categorical columns → `category`)
- [x] Assess data quality: missing values, invalid coordinates, outliers, inconsistent values, GBIF `issue` flags

Key findings (full tables in [`reports/`](reports/)):
- `eventDate` uses 11 different ISO 8601 formats, including year-only, year-month and date ranges (447 records); the start date and its precision were extracted
- 3,336 records share the same taxon, coordinates and date (possible duplicates across sources)
- 3,634 records have `elevation = 0` (37% of filled elevations), which acts as a placeholder for "unknown"
- `individualCount` is highly skewed (median 2, max 10,200); `coordinateUncertaintyInMeters` reaches 4,226 km
- All coordinates fall inside Kosovo; no future dates; `eventDate` and `year` are consistent

### 2. Integration, aggregation, sampling, cleaning and missing values — [`02_pastrimi.py`](notebooks/02_pastrimi.py)
- [x] Create the documentation template and `log_step()` helper for cleaning steps
- [x] Initialize [`processed/cleaning_log.csv`](processed/cleaning_log.csv)
- [x] Inspect the initial structure: `shape`, `df.info()`, `dtypes` and 5 sample values per column
- [x] Create an issue list for mixed date formats, boolean values, bilingual names and `;`-separated lists
- [x] Create [`processed/missing_report.csv`](processed/missing_report.csv), sorted by missing-value percentage
- [ ] **Integration** – merge records coming from different `datasetKey` sources and harmonize column values
- [ ] **Aggregation** – summarize occurrences per species, district, municipality, year and IUCN category
- [ ] **Sampling** – draw a stratified sample (e.g. by `kingdom` or `district`) for faster exploration
- [ ] **Cleaning** – drop columns that are almost empty (`iasAppliesFrom`, `establishmentMeans`), remove records not identified to species level where needed, fix inconsistent text values
- [ ] **Missing value strategy** – drop rows where key fields are missing (`species`, `year`), impute `month`/`day` from `eventDate`, fill `protectedArea` with "Not protected", mark unknowns explicitly

Current outputs:
- [`processed/cleaning_log.csv`](processed/cleaning_log.csv) – empty cleaning log with the standard documentation columns
- [`processed/missing_report.csv`](processed/missing_report.csv) – number and percentage of missing values for every column
- [`reports/02_issue_list.csv`](reports/02_issue_list.csv) – initial list of structural/data-quality issues observed during exploration

### 3. Dimensionality reduction, feature selection, feature creation, discretization, binarization and transformation — [`03_vetite.py`](notebooks/03_vetite.py)
- [x] Document preprocessing plan v1 with decision and rationale
- [ ] **Dimensionality reduction** – remove redundant attributes (`iucnRedListStatus` vs. `iucnRedListCategory`, `taxonKey` vs. `scientificName`)
- [ ] **Feature subset selection** – keep the attributes relevant for the analysis (taxonomy, time, location, conservation status)
- [ ] **Feature creation** – e.g. `season` from `month`, `decade` from `year`, `isThreatened` from IUCN category, record count per species
- [ ] **Discretization** – bin `elevation` and `year` into ranges (e.g. lowland / hill / mountain, decades)
- [ ] **Binarization** – one-hot encode `kingdom`, `basisOfRecord`; convert `strictlyProtected` and `iasUnionConcern` to 0/1
- [ ] **Transformation** – normalize/scale numeric attributes (`elevation`, `individualCount`), apply log transform to skewed counts

---
