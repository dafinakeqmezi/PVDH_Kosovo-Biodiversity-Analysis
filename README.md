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

The [processed-output audit](reports/verifikimi_i_te_dhenave_te_perpunuara.md) reports 22 passing checks. Run `python scripts/verify_processed.py` for read-only verification. The samples use the original data, not the cleaned checkpoint; they contain 85 and 89 IDs subsequently removed as duplicates. Saved feature/PCA outputs match their inputs, but notebook 03 still needs an end-to-end execution/export cell for full reproducibility.

## Repository structure

```
PVDH/
├── dataset/
│   └── kosovo_overall_biodiversity.csv      original GBIF download (never modified)
├── notebooks/
│   ├── 01b_analiza_burimeve.ipynb           sources: publishers from the GBIF API (Dafina)
│   ├── 01_mbledhja_kualiteti.ipynb          collection, types, quality, integration, aggregation, sampling (Dafina)
│   ├── 02_pastrimi.ipynb                    missing values, duplicates, cleaning, validation (Deliza)
│   └── 03_vetite.ipynb                      feature selection and creation, encoding, transformation, PCA (Jeta)
├── processed/
│   ├── biodiversity_clean.csv               frozen cleaned dataset (46,456 rows) + schema and manifest
│   ├── cleaning_log.csv                     every cleaning step with rows/columns before and after
│   ├── municipalities.csv                   area and population of the 38 municipalities
│   ├── agg_*.csv / agg_*_v2.csv             aggregates on the original / cleaned data
│   ├── sample_random.csv, sample_stratified.csv
│   ├── biodiversity_features.csv            feature columns on the cleaned data
│   └── pca_municipalities.csv               municipality PCA scores
├── reports/
│   ├── 01_*.csv                             tables written by notebook 01
│   ├── *.md                                 one document per task, with decision and rationale
│   └── raporti_pjesa_1.md          group report: all Part I stages
├── requirements.txt
└── README.md
```

## Setup and how to run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

The notebooks were run with Python 3.14 and pandas 3.0.1. Run them from the repository root (or from `notebooks/`; the paths are resolved in both cases) in this order:

| Order | Notebook | Input | Output |
|---|---|---|---|
| 1 | `01b_analiza_burimeve.ipynb` | original dataset, GBIF API (results cached in `processed/gbif_datasets_cache.csv`; internet only for datasets not yet cached) | `processed/sources_summary.csv` |
| 2 | `02_pastrimi.ipynb` | original dataset; duplicate candidates read from Git commit `d2708c6` | `processed/biodiversity_clean.csv` (frozen: the notebook refuses to overwrite it with different content), `processed/cleaning_log.csv` |
| 3 | `01_mbledhja_kualiteti.ipynb` | original dataset; `add_taxon_features()` read from `03_vetite.ipynb`; `biodiversity_clean.csv` for section 8 | `reports/01_*.csv`, `processed/municipalities.csv`, aggregates (`agg_*.csv`, `agg_*_v2.csv`), samples |
| 4 | `03_vetite.ipynb` | `biodiversity_clean.csv` (features); `processed/agg_municipality_taxon.csv` (PCA matrix, original data; `agg_municipality_taxon_v2.csv` is the cleaned version) | feature functions (`build_features()`), `processed/biodiversity_features.csv`, `processed/matrica_pca_komuna_taxon.csv`, `processed/pca_municipalities.csv` |

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

The detailed task lists of each notebook follow.

### 1. Data collection, data types and data quality — [`01_mbledhja_kualiteti.ipynb`](notebooks/01_mbledhja_kualiteti.ipynb)
- [x] Describe the data source (GBIF) and the meaning of each attribute
- [x] Assign correct data types for all 42 columns: pandas type, conceptual type and target type → [`reports/tipet_e_te_dhenave.md`](reports/tipet_e_te_dhenave.md), [`reports/01_tipet_e_kolonave.csv`](reports/01_tipet_e_kolonave.csv)
- [x] Assess data quality: missing values, invalid coordinates, outliers, inconsistent values, GBIF `issue` flags
- [x] Quality framework: completeness, validity, consistency, uniqueness and timeliness, with 35 checks (metric, rule, columns, baseline value) → [`reports/korniza_e_kualitetit.md`](reports/korniza_e_kualitetit.md), [`reports/01_korniza_e_kualitetit.csv`](reports/01_korniza_e_kualitetit.csv)
- [x] Completeness per column (including hidden missing values) and per row (key fields: species, date, coordinates, municipality) → [`reports/plotesia.md`](reports/plotesia.md)
- [x] Validity: coordinates inside Kosovo, year range, month/day ranges, `eventDate` formats, frequency of 7071 in `coordinateUncertaintyInMeters`, `elevation` range → [`reports/vlefshmeria.md`](reports/vlefshmeria.md)
- [x] GBIF flags: count and % for each of the 35 `issue` flags, classified as serious or informative with a reason → [`reports/flamujt_gbif.md`](reports/flamujt_gbif.md)
- [x] Uniqueness: `gbifID` unique; logical duplicates by species + date + coordinates + observer, 18 groups reviewed manually, proposed definition → [`reports/unikaliteti.md`](reports/unikaliteti.md), [`processed/duplicate_candidates.csv`](processed/duplicate_candidates.csv)
- [x] Consistency (species → genus → family, municipality → district) and bias by class, region and source → [`reports/konsistenca_dhe_anshmeria.md`](reports/konsistenca_dhe_anshmeria.md)
- [x] Source analysis — [`01b_analiza_burimeve.ipynb`](notebooks/01b_analiza_burimeve.ipynb): publisher of each dataset from the GBIF API, grouped by publisher / dataset, `basisOfRecord` and `license` → [`processed/sources_summary.csv`](processed/sources_summary.csv)

Key findings (full tables in [`reports/`](reports/)):
- `eventDate` uses 11 different ISO 8601 formats, including year-only, year-month and date ranges (447 records); the start date and its precision were extracted
- 3,336 records share the same taxon, coordinates and date (possible duplicates across sources)
- 3,634 records have `elevation = 0` (37% of filled elevations), which acts as a placeholder for "unknown"
- `individualCount` is highly skewed (median 2, max 10,200); `coordinateUncertaintyInMeters` reaches 4,226 km
- All coordinates fall inside Kosovo; no future dates; `eventDate` and `year` are consistent

Tables written by notebook 01 (`reports/`):

| Notebook section | Tables |
|---|---|
| §3.1–3.4 First quality checks | [`01_vlerat_e_zbrazeta.csv`](reports/01_vlerat_e_zbrazeta.csv), [`01_kontrollet_e_kualitetit.csv`](reports/01_kontrollet_e_kualitetit.csv) |
| §2 Types | [`01_tipet_e_kolonave.csv`](reports/01_tipet_e_kolonave.csv) |
| §3.5 GBIF flags | [`01_flamujt_gbif.csv`](reports/01_flamujt_gbif.csv) |
| §3.7 Quality framework | [`01_korniza_e_kualitetit.csv`](reports/01_korniza_e_kualitetit.csv) |
| §3.8 Completeness | [`01_plotesia_kolona.csv`](reports/01_plotesia_kolona.csv), [`01_plotesia_rreshta.csv`](reports/01_plotesia_rreshta.csv) |
| §3.9 Validity | [`01_vlefshmeria_rregullat.csv`](reports/01_vlefshmeria_rregullat.csv), [`01_vlefshmeria.csv`](reports/01_vlefshmeria.csv), [`01_formatet_e_datave.csv`](reports/01_formatet_e_datave.csv), [`01_pasiguria_vlerat.csv`](reports/01_pasiguria_vlerat.csv), [`01_lartesia_jashte_diapazonit.csv`](reports/01_lartesia_jashte_diapazonit.csv) |
| §3.10 Uniqueness | [`01_unikaliteti.csv`](reports/01_unikaliteti.csv), [`01_duplikatet_sipas_llojit.csv`](reports/01_duplikatet_sipas_llojit.csv), [`01_duplikatet_shqyrtimi.csv`](reports/01_duplikatet_shqyrtimi.csv) |
| §3.11 Consistency and bias | [`01_konsistenca.csv`](reports/01_konsistenca.csv), [`01_anshmeria_klasa.csv`](reports/01_anshmeria_klasa.csv), [`01_anshmeria_rajoni.csv`](reports/01_anshmeria_rajoni.csv), [`01_anshmeria_burimi.csv`](reports/01_anshmeria_burimi.csv), [`01_anshmeria_perqendrimi.csv`](reports/01_anshmeria_perqendrimi.csv), [`01_anshmeria_paragrafi.md`](reports/01_anshmeria_paragrafi.md) |
| §5.2 Join | [`01_bashkimi_celesat.csv`](reports/01_bashkimi_celesat.csv), [`01_bashkimi_kontrolli.csv`](reports/01_bashkimi_kontrolli.csv) |
| §6 Aggregation by municipality | [`01_hartezimi_i_grupeve_taksonomike.csv`](reports/01_hartezimi_i_grupeve_taksonomike.csv) |
| §6.2 Aggregation by time | [`01_koha_sipas_dekades.csv`](reports/01_koha_sipas_dekades.csv), [`01_koha_sipas_muajit.csv`](reports/01_koha_sipas_muajit.csv) |
| §6.3 Species and district | [`01_specie_permbledhje.csv`](reports/01_specie_permbledhje.csv), [`01_specie_te_kercenuara.csv`](reports/01_specie_te_kercenuara.csv) |
| §7 Sampling | [`01_mostrimi_krahasimi_klasa.csv`](reports/01_mostrimi_krahasimi_klasa.csv), [`01_mostrimi_permbledhje.csv`](reports/01_mostrimi_permbledhje.csv), [`01_mostrimi_krahasimi_rajoni.csv`](reports/01_mostrimi_krahasimi_rajoni.csv), [`01_mostrimi_anshmeria.csv`](reports/01_mostrimi_anshmeria.csv), [`01_mostrimi_speciet.csv`](reports/01_mostrimi_speciet.csv) |
| §8 Recalculation | [`01_rikalkulimi_diferencat.csv`](reports/01_rikalkulimi_diferencat.csv), [`01_rikalkulimi_komunat.csv`](reports/01_rikalkulimi_komunat.csv), [`01_rikalkulimi_klasat.csv`](reports/01_rikalkulimi_klasat.csv), [`01_rikalkulimi_vitet.csv`](reports/01_rikalkulimi_vitet.csv), [`01_rikalkulimi_speciet.csv`](reports/01_rikalkulimi_speciet.csv) |

### 2. Integration, aggregation, sampling, cleaning and missing values — [`02_pastrimi.ipynb`](notebooks/02_pastrimi.ipynb)
- [x] Create the documentation template and `log_step()` helper for cleaning steps
- [x] Initialize [`processed/cleaning_log.csv`](processed/cleaning_log.csv)
- [x] Inspect the initial structure: `shape`, `df.info()`, `dtypes` and 5 sample values per column
- [x] Create an issue list for mixed date formats, boolean values, bilingual names and `;`-separated lists
- [x] Create [`processed/missing_report.csv`](processed/missing_report.csv), sorted by missing-value percentage
- [x] Audit hidden missing-value tokens and document the decision for `elevation = 0`
- [x] Compare missingness by source, `basisOfRecord`, class and district, with cautious interpretation of missingness mechanisms
- [x] Define a column-specific missing-value strategy using analytical importance and recoverability
- [x] External data for integration: area (km²) and population of the 38 municipalities with source, year and link → [`processed/municipalities.csv`](processed/municipalities.csv), [`reports/burimet_e_te_dhenave_te_komunave.md`](reports/burimet_e_te_dhenave_te_komunave.md)
- [x] Join: municipality key from the bilingual names, left join with area and population, 38/38 matched and 46,831 rows before and after → [`processed/biodiversity_municipalities.csv`](processed/biodiversity_municipalities.csv), [`reports/bashkimi_i_komunave.md`](reports/bashkimi_i_komunave.md)
- [x] Aggregation by municipality: records, unique species, threatened species, species/km², records per 1,000 residents, plus the municipality × taxon_group matrix for PCA → [`processed/agg_municipality.csv`](processed/agg_municipality.csv), [`processed/agg_municipality_taxon.csv`](processed/agg_municipality_taxon.csv), [`reports/agregimi_sipas_komunes.md`](reports/agregimi_sipas_komunes.md)
- [x] Aggregation by time: records and unique species per year and a year × month table; 3,598 HabiProt records dated 30 November flagged for investigation as possible placeholders, not confirmed invalid dates → [`processed/agg_time.csv`](processed/agg_time.csv), [`reports/agregimi_sipas_kohes.md`](reports/agregimi_sipas_kohes.md)
- [x] Aggregation by species and district: class × district table and a species-level table (first and last year, municipalities, records) → [`processed/agg_class_district.csv`](processed/agg_class_district.csv), [`processed/agg_species.csv`](processed/agg_species.csv), [`reports/agregimi_sipas_specieve_dhe_rajonit.md`](reports/agregimi_sipas_specieve_dhe_rajonit.md)
- [x] **Sampling** – random sample (10,000) and sample stratified by class (proportional), `random_state = 42`, with the % by class compared to the full dataset → [`processed/sample_random.csv`](processed/sample_random.csv), [`processed/sample_stratified.csv`](processed/sample_stratified.csv), [`reports/mostrimi.md`](reports/mostrimi.md)
- [x] Sampling conclusion: the stratified sample keeps the class distribution best; both samples keep the bias (Graçanica ~31%) and only 46.6% of species, so species analyses use the full dataset → section 7.3 of the notebook, [`reports/mostrimi.md`](reports/mostrimi.md)
- [x] Recalculation on the cleaned data (Deliza's checkpoint, 46,456 rows): integration and aggregates re-run with logic verified against v1; only record counts change (−375 duplicates, −0.80%), no species, class, year or municipality lost → `processed/agg_*_v2.csv`, [`reports/rikalkulimi.md`](reports/rikalkulimi.md)
- [x] Group report: collection, sources, types, quality, integration, aggregation and sampling, with numbers from the notebook → [`reports/raporti_pjesa_1.md`](reports/raporti_pjesa_1.md)
- [x] Apply column removals, confirmed missing tokens and missingness flags to a separate working dataset; initially flag zero elevations, then replace them in the invalid-value step
- [x] Separate IAS structural missingness with status flags
- [x] Replace blank protected-area names with "Jashtë zonës së mbrojtur" based on the user's clarification of dataset semantics; designation becomes "Nuk aplikohet" for those rows. This is not independent GIS verification
- [x] Parse dates into `event_start`, `event_end` and `date_precision`, preserving interval endpoints and original text
- [x] Convert nullable integers, booleans and unordered categories; leave IUCN ordinal encoding to notebook 03

Current outputs:
- [`processed/cleaning_log.csv`](processed/cleaning_log.csv) – per-step transformation log; reruns update this notebook's steps without duplicating them
- [`processed/missing_report.csv`](processed/missing_report.csv) – number and percentage of missing values for every column
- [`reports/02_lista_e_problemeve.csv`](reports/02_lista_e_problemeve.csv) – initial list of structural/data-quality issues observed during exploration
- [`reports/mungesat_e_fshehura.csv`](reports/mungesat_e_fshehura.csv) and [`reports/raporti_i_mungesave_efektive.csv`](reports/raporti_i_mungesave_efektive.csv) – literal-token audit and effective missingness without double counting
- [`reports/lartesia_zero_sipas_grupeve.csv`](reports/lartesia_zero_sipas_grupeve.csv), [`reports/regjistrimet_me_lartesi_zero.csv`](reports/regjistrimet_me_lartesi_zero.csv) and [`reports/vendimi_per_lartesine_zero.md`](reports/vendimi_per_lartesine_zero.md) – source/location evidence and the zero-elevation decision
- [`reports/mungesat_sipas_grupeve.csv`](reports/mungesat_sipas_grupeve.csv) and [`reports/mekanizmat_e_mungeses.md`](reports/mekanizmat_e_mungeses.md) – group denominators, missingness rates and interpretation limits
- [`reports/strategjia_e_mungesave.md`](reports/strategjia_e_mungesave.md) – initial strategy for all 42 columns; the subsequent protected-area clarification and its implementation are documented in [`reports/vendimet_per_mungesat_strukturore.md`](reports/vendimet_per_mungesat_strukturore.md)
- [`processed/kosovo_biodiversity_clean.csv`](processed/kosovo_biodiversity_clean.csv) – intermediate working dataset including approved duplicate removal, category cleaning and the subsequent documented cleaning decisions; not the final `biodiversity_clean.csv` checkpoint. The original CSV remains unchanged
- [`processed/kosovo_biodiversity_clean_schema.json`](processed/kosovo_biodiversity_clean_schema.json) – type/category metadata and source hash; use `load_clean_dataset()` in notebook 02 to restore CSV types
- [`reports/kolonat_para_pas_pastrimit.csv`](reports/kolonat_para_pas_pastrimit.csv), [`reports/numerimet_e_pastrimit.csv`](reports/numerimet_e_pastrimit.csv) and [`reports/tipet_para_pas_pastrimit.csv`](reports/tipet_para_pas_pastrimit.csv) – column changes, affected counts and types before/after
- [`reports/vendimet_per_mungesat_strukturore.md`](reports/vendimet_per_mungesat_strukturore.md) and [`reports/numerimet_e_mungesave_strukturore.csv`](reports/numerimet_e_mungesave_strukturore.csv) – evidence limits, flags and replacement counts
- [`reports/formatet_e_datave.csv`](reports/formatet_e_datave.csv) and [`reports/problemet_e_parsimit_te_datave.csv`](reports/problemet_e_parsimit_te_datave.csv) – observed date formats and parsing failures

- [x] Check missing year/month for unambiguous recovery from complete eventDate values or complete interval endpoints within one month; 0 eligible replacements in the current dataset
- [`reports/plotesimi_year_month_para_pas.csv`](reports/plotesimi_year_month_para_pas.csv), [`reports/gjurma_e_plotesimit_year_month.csv`](reports/gjurma_e_plotesimit_year_month.csv) and [`reports/vendimi_per_plotesimin_year_month.md`](reports/vendimi_per_plotesimin_year_month.md) – before/after missingness, per-cell decisions and rationale

- [x] Decide duplicate groups and select the most complete survivor, with a deterministic tie-break and explicit count-conflict exclusions
- [`reports/vendimi_per_duplikatet.md`](reports/vendimi_per_duplikatet.md), [`reports/vendimet_e_grupeve_duplikate.csv`](reports/vendimet_e_grupeve_duplikate.csv) and [`reports/renditja_e_kandidateve_duplikate.csv`](reports/renditja_e_kandidateve_duplikate.csv) – duplicate policy, group decisions and survivor ranking
- [`processed/rreshtat_per_fshirje_duplikate.csv`](processed/rreshtat_per_fshirje_duplikate.csv) – decision manifest for the 375 removed rows in 235 groups; each row links to its retained gbifID
- [x] Remove approved duplicates: 46,831 → 46,456 rows, with survivor and excluded-group checks recorded in [`reports/kontrolli_i_largimit_te_duplikateve.csv`](reports/kontrolli_i_largimit_te_duplikateve.csv)
- [`processed/rreshtat_e_larguar_duplikate.csv`](processed/rreshtat_e_larguar_duplikate.csv) and [`reports/largimi_i_duplikateve.md`](reports/largimi_i_duplikateve.md) – removed records and implementation audit
- [x] Normalize category whitespace and case variants; preserve `municipality_original` and derive `municipality_sq`
- [`reports/kategorite_para_pas.csv`](reports/kategorite_para_pas.csv), [`reports/permbledhja_e_pastrimit_te_kategorive.csv`](reports/permbledhja_e_pastrimit_te_kategorive.csv), [`reports/emrat_shqip_te_komunave.csv`](reports/emrat_shqip_te_komunave.csv) and [`reports/pastrimi_i_kategorive.md`](reports/pastrimi_i_kategorive.md) – category mappings, counts and rationale

- [x] Apply the zero-elevation decision and add coordinate-uncertainty status and nullable `is_species_level`, without deleting rows or other extreme values. The uncertainty threshold combines the observed positive median with the smallest known municipality's equivalent radius; it is a screening policy, not GIS verification. See [`reports/vendimi_per_vlerat_e_pavlefshme.md`](reports/vendimi_per_vlerat_e_pavlefshme.md) and [`reports/rregullat_e_vlerave_te_pavlefshme.csv`](reports/rregullat_e_vlerave_te_pavlefshme.csv). Supporting tables: [`reports/shperndarja_e_pasigurise.csv`](reports/shperndarja_e_pasigurise.csv), [`reports/frekuencat_e_pasigurise.csv`](reports/frekuencat_e_pasigurise.csv), [`reports/pasiguria_sipas_komunes.csv`](reports/pasiguria_sipas_komunes.csv), [`reports/shkalla_hapesinore_e_komunave.csv`](reports/shkalla_hapesinore_e_komunave.csv), [`reports/ndjeshmeria_e_pragut_te_pasigurise.csv`](reports/ndjeshmeria_e_pragut_te_pasigurise.csv), [`reports/niveli_taksonomik.csv`](reports/niveli_taksonomik.csv).

- [x] Analyze `individualCount` missingness and distribution overall and by source, record basis, class and district. Keep missing counts without imputation; preserve the existing missingness flag. See [`reports/vendimi_per_numrin_e_individeve.md`](reports/vendimi_per_numrin_e_individeve.md), [`reports/shperndarja_e_numrit_te_individeve.csv`](reports/shperndarja_e_numrit_te_individeve.csv), [`reports/numri_i_individeve_sipas_grupeve.csv`](reports/numri_i_individeve_sipas_grupeve.csv) and [`reports/numri_i_individeve_para_pas.csv`](reports/numri_i_individeve_para_pas.csv).

- [x] Finalize and freeze [`processed/biodiversity_clean.csv`](processed/biodiversity_clean.csv) by executing the entire cleaning pipeline from the original dataset. The checkpoint has 46,456 rows and 83 columns. Its [schema](processed/biodiversity_clean_schema.json) preserves datatype information and its [manifest](processed/biodiversity_clean_manifest.json) records checksums. See [finalization checks](reports/kontrolli_i_finalizimit.csv) and the [handoff report](reports/finalizimi_i_datasetit.md).
- [ ] Confirm delivery of the handoff message to Dafina and Jeta. The message is prepared in the finalization report; notification is not sent automatically.
- [x] Validate the saved checkpoint with assertions for approved duplicate survivors, schema/types, explicit value rules, row-count/log consistency and the untouched original dataset. The read-only checks produce [`reports/validimi.md`](reports/validimi.md) (the Albanian filename for the plan's `validation.md`) and [`reports/kontrollet_e_validimit.csv`](reports/kontrollet_e_validimit.csv). Retained questionable extremes and the limits of the checks are documented; validation does not alter the frozen data or log.

Current scope for notebook 02: cleaning finalized through the 25 October checkpoint; team notification still requires confirmation. Dafina's candidate analysis is read from Git commit `d2708c640de830014edf4c4f35a528849c98455f`; run `git fetch origin` first if that commit is unavailable locally. No teammate files are overwritten by this import. Protected-area replacement uses the user's clarification of dataset semantics, with that source and its limits documented. Zero elevations are missing in the final CSV, while `elevation_was_zero` preserves their provenance. Individual counts are not imputed: 17,587 missing values remain among 46,456 records. The notebook verifies all its cleaning-log steps and refuses to overwrite a frozen checkpoint with different content. Subsequent corrections require an agreed new version. Teammates must regenerate aggregates, samples, features and PCA from this final input as applicable; notebook 02 does not regenerate their results.

- [x] Group report, cleaning and validation: missing values, applied strategy, conversions, duplicates, cleaning, log summary and validation → [`reports/raporti_pjesa_1.md`](reports/raporti_pjesa_1.md). This documentation does not change the frozen checkpoint or mark presentation/full-pipeline checks complete.

### 3. Dimensionality reduction, feature selection, feature creation, discretization, binarization and transformation — [`03_vetite.ipynb`](notebooks/03_vetite.ipynb)
- [x] Document preprocessing plan v1 with decision and rationale
- [x] Feature subset decision: 29 columns kept and 13 dropped, with a reason for each column. The original CSV stays at 42 columns. Only `iucnRedListStatus` is a 1:1 duplicate; `taxonKey` and `scientificName` are both kept → [`reports/zgjedhja_e_vetive.md`](reports/zgjedhja_e_vetive.md)
- [x] Time features: `season` from `month`, `decade` from `year`, and `is_recent` for `year >= 2017`. A missing `year` or `month` stays missing. Function `add_time_features()` in notebook 03 → [`reports/vetite_kohore.md`](reports/vetite_kohore.md)
- [x] Taxonomic and conservation features: `taxon_group` from `class` (Zogj, Insekte, Bimë, Kërpudha, Tjera; missing class = "E panjohur") and `is_threatened` from the IUCN category (`VU`/`EN`/`CR` = 1, `LC`/`NT` = 0, `NE`/`DD`/NaN = NaN). The single `EX` row stays NaN and is documented separately. Function `add_taxon_features()` → [`reports/vetite_taksonomike.md`](reports/vetite_taksonomike.md)
- [x] Source and spatial features: `in_protected_area` is 1 when `protectedArea` names an area and 0 when it is blank or "Jashtë zonës së mbrojtur". `is_citizen_science` is 1 only for a citizen-science publisher and `HUMAN_OBSERVATION`. `n_issues` counts serious GBIF flags. Function `add_source_spatial_features()` in notebook 03 → [`reports/vetite_e_burimit.md`](reports/vetite_e_burimit.md)
- [x] Elevation zones: `elevation_zone` is Fushë (297–800 m), Kodrinore (801–1,500 m) or Malore (1,501–2,656 m). Missing elevation (79.03%), `elevation = 0` and nine values outside 297–2,656 m are `E panjohur`. Function `add_elevation_zone()` in notebook 03 → [`reports/zona_e_lartesise.md`](reports/zona_e_lartesise.md)
- [x] Time periods: `period` from the original `year`, with cuts at 1900, 1950, 2000, 2010 and 2020. A missing `year` stays missing. Function `add_period()` in notebook 03 → [`reports/periudhat_kohore.md`](reports/periudhat_kohore.md)
- [x] Count classes: `count_class` from the original `individualCount` with `pd.qcut` (`q=4`, duplicate edge at 1 dropped). Equal-width `pd.cut` places 99.82% of known counts in one bin. A missing count stays missing. Function `add_count_class()` in notebook 03 → [`reports/klasa_e_numrit.md`](reports/klasa_e_numrit.md)
- [x] One-hot encoding: 20 dummy columns for `taxon_group`, `district` and `basisOfRecord`. A category with fewer than 47 rows is merged into `Tjera`; only `OBSERVATION` (1 row) is merged. `drop_first` is false. Function `add_one_hot()` in notebook 03 → [`reports/kolonat_dummy.md`](reports/kolonat_dummy.md)
- [x] IUCN and flag encoding: `iucn_rank` is LC=1, NT=2, VU=3, EN=4, CR=5, EX=6, read once from `iucnRedListCategory`. `NE`, `DD` and missing stay missing, and `iucn_evaluated` is 0 for those rows. The 10 serious GBIF flags are 0/1 columns. Function `add_iucn_and_flags()` in notebook 03 → [`reports/kodimi_iucn_dhe_flamujve.md`](reports/kodimi_iucn_dhe_flamujve.md)
- [x] Log transform: `individualCount_log1p` and `coordinateUncertaintyInMeters_log1p`. On the cleaned dataset, skewness falls from 26.63 to 2.07 and from 101.73 to −1.00. Missing values stay missing. Function `add_log1p()` in notebook 03 → [`reports/transformimi_log1p.md`](reports/transformimi_log1p.md)
- [x] PCA scaling: Z-scores of the municipality × `taxon_group` record proportions. `year`, latitude and longitude are not scaled. Function `standardize_pca_matrix()` in notebook 03 → [`reports/shkallezimi_pca.md`](reports/shkallezimi_pca.md)
- [x] PCA: PC1–PC3 on the standardized municipality × `taxon_group` matrix. Components with `explained_variance_` above 1 are kept; cumulative `explained_variance_ratio_` is 0.770411. PC6 is 0 because the six proportions sum to 1. Function `run_municipality_pca()` in notebook 03 → [`reports/pca_komunat.md`](reports/pca_komunat.md)
- [x] Variance and correlation: among the one-hot, IUCN/flag and `log1p` columns, five columns have fewer than 47 ones and one flag pair has correlation 0.8227. None are removed. Function `review_variance_correlation()` in notebook 03 → [`reports/varianca_dhe_korrelacioni.md`](reports/varianca_dhe_korrelacioni.md)
- [x] Feature build: `build_features(df, datasets)` runs the nine occurrence-level feature steps on the 46,456-row checkpoint and adds 45 columns. Municipality PCA stays a separate matrix. Function in notebook 03 → [`reports/lista_e_vetive.md`](reports/lista_e_vetive.md)
- [x] PCA on the cleaned data: the same proportion and Z-score rules on `agg_municipality_taxon_v2.csv`. PC1–PC3 stay, cumulative `explained_variance_ratio_` is 0.769403. Report sections cover selection, creation, discretization, binarization, transformation and reduction. Function `run_pca_on_clean_matrix()` in notebook 03 → [`reports/raporti_pjesa_1.md`](reports/raporti_pjesa_1.md)

Current outputs:
- [`reports/rendesia_e_kolonave.md`](reports/rendesia_e_kolonave.md) – analytical importance (high / medium / low) of the 42 columns for the project questions
- [`reports/zgjedhja_e_vetive.md`](reports/zgjedhja_e_vetive.md) – final column decision; the original CSV is unchanged
- [`reports/vetite_kohore.md`](reports/vetite_kohore.md) – month-to-season mapping and the `is_recent` threshold
- [`reports/vetite_taksonomike.md`](reports/vetite_taksonomike.md) – class-to-group mapping and the IUCN decision, including the `EX` row
- [`reports/vetite_e_burimit.md`](reports/vetite_e_burimit.md) – protected-area, citizen-science and serious-flag criteria
- [`reports/zona_e_lartesise.md`](reports/zona_e_lartesise.md) – elevation zone boundaries and the unknown-elevation count
- [`reports/periudhat_kohore.md`](reports/periudhat_kohore.md) – year-period boundaries and the count in each period
- [`reports/klasa_e_numrit.md`](reports/klasa_e_numrit.md) – equal-width and equal-frequency comparison, and the chosen `count_class` counts
- [`reports/kolonat_dummy.md`](reports/kolonat_dummy.md) – one-hot columns for `taxon_group`, `district` and `basisOfRecord`, and the `drop_first` decision
- [`reports/kodimi_iucn_dhe_flamujve.md`](reports/kodimi_iucn_dhe_flamujve.md) – IUCN rank, `iucn_evaluated`, and the 10 serious-flag columns
- [`reports/transformimi_log1p.md`](reports/transformimi_log1p.md) – skewness before and after `log1p` for counts and coordinate uncertainty
- [`reports/shkallezimi_pca.md`](reports/shkallezimi_pca.md) – Z-scores of municipality by taxon-group record proportions for PCA
- [`reports/pca_komunat.md`](reports/pca_komunat.md) – variance, loadings and municipality scores in [`processed/pca_municipalities.csv`](processed/pca_municipalities.csv)
- [`reports/varianca_dhe_korrelacioni.md`](reports/varianca_dhe_korrelacioni.md) – low-variance columns and the high-correlation flag pair, all kept
- [`reports/lista_e_vetive.md`](reports/lista_e_vetive.md) – the 45 feature columns built on the cleaned dataset in [`processed/biodiversity_features.csv`](processed/biodiversity_features.csv)
- [`reports/raporti_pjesa_1.md`](reports/raporti_pjesa_1.md) – selection, creation, discretization, binarization, transformation, reduction, and the final PCA scores in [`processed/pca_municipalities_v2.csv`](processed/pca_municipalities_v2.csv)

---
