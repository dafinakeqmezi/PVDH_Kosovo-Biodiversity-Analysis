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
- [ ] **Integration** – merge records coming from different `datasetKey` sources and harmonize column values
- [x] Aggregation by municipality: records, unique species, threatened species, species/km², records per 1,000 residents, plus the municipality × taxon_group matrix for PCA → [`processed/agg_municipality.csv`](processed/agg_municipality.csv), [`processed/agg_municipality_taxon.csv`](processed/agg_municipality_taxon.csv), [`reports/agregimi_sipas_komunes.md`](reports/agregimi_sipas_komunes.md)
- [x] Aggregation by time: records and unique species per year and a year × month table; 3,598 HabiProt records dated 30 November flagged for investigation as possible placeholders, not confirmed invalid dates → [`processed/agg_time.csv`](processed/agg_time.csv), [`reports/agregimi_sipas_kohes.md`](reports/agregimi_sipas_kohes.md)
- [x] Aggregation by species and district: class × district table and a species-level table (first and last year, municipalities, records) → [`processed/agg_class_district.csv`](processed/agg_class_district.csv), [`processed/agg_species.csv`](processed/agg_species.csv), [`reports/agregimi_sipas_specieve_dhe_rajonit.md`](reports/agregimi_sipas_specieve_dhe_rajonit.md)
- [ ] **Aggregation** – summarize occurrences per species, district, municipality, year and IUCN category
- [ ] **Sampling** – draw a stratified sample (e.g. by `kingdom` or `district`) for faster exploration
- [ ] **Cleaning** – apply the documented column-specific decisions, use species-level exclusions only where needed, and fix inconsistent text values
- [ ] **Apply missing-value strategy** – implement [`reports/strategjia_e_mungesave.md`](reports/strategjia_e_mungesave.md) in a derived dataset and log transformations; recover only explicit date components, use analysis-specific exclusions, and verify protection coverage before assigning "Not protected"
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

- [x] Apply the zero-elevation decision and add coordinate-uncertainty status and nullable `is_species_level`, without deleting rows or other extreme values. The uncertainty threshold combines the observed positive median with the smallest known municipality's equivalent radius; it is a screening policy, not GIS verification. See [`reports/vendimi_per_vlerat_e_pavlefshme.md`](reports/vendimi_per_vlerat_e_pavlefshme.md) and [`reports/rregullat_e_vlerave_te_pavlefshme.csv`](reports/rregullat_e_vlerave_te_pavlefshme.csv).

- [x] Analyze `individualCount` missingness and distribution overall and by source, record basis, class and district. Keep missing counts without imputation; preserve the existing missingness flag. See [`reports/vendimi_per_numrin_e_individeve.md`](reports/vendimi_per_numrin_e_individeve.md), [`reports/shperndarja_e_numrit_te_individeve.csv`](reports/shperndarja_e_numrit_te_individeve.csv), [`reports/numri_i_individeve_sipas_grupeve.csv`](reports/numri_i_individeve_sipas_grupeve.csv) and [`reports/numri_i_individeve_para_pas.csv`](reports/numri_i_individeve_para_pas.csv).

- [x] Finalize and freeze [`processed/biodiversity_clean.csv`](processed/biodiversity_clean.csv) by executing the entire cleaning pipeline from the original dataset. The checkpoint has 46,456 rows and 83 columns. Its [schema](processed/biodiversity_clean_schema.json) preserves datatype information and its [manifest](processed/biodiversity_clean_manifest.json) records checksums. See [finalization checks](reports/kontrolli_i_finalizimit.csv) and the [handoff report](reports/finalizimi_i_datasetit.md).
- [ ] Confirm delivery of the handoff message to Dafina and Jeta. The message is prepared in the finalization report; notification is not sent automatically.

Current scope for notebook 02: cleaning finalized through the 25 October checkpoint; team notification still requires confirmation. Dafina's candidate analysis is read from Git commit `d2708c640de830014edf4c4f35a528849c98455f`; run `git fetch origin` first if that commit is unavailable locally. No teammate files are overwritten by this import. Protected-area replacement uses the user's clarification of dataset semantics, with that source and its limits documented. Zero elevations are missing in the final CSV, while `elevation_was_zero` preserves their provenance. Individual counts are not imputed: 17,587 missing values remain among 46,456 records. The notebook verifies all its cleaning-log steps and refuses to overwrite a frozen checkpoint with different content. Subsequent corrections require an agreed new version. Teammates must regenerate aggregates, samples, features and PCA from this final input as applicable; notebook 02 does not regenerate their results.

### 3. Dimensionality reduction, feature selection, feature creation, discretization, binarization and transformation — [`03_vetite.ipynb`](notebooks/03_vetite.ipynb)
- [x] Document preprocessing plan v1 with decision and rationale
- [ ] **Dimensionality reduction** – remove redundant attributes (`iucnRedListStatus` vs. `iucnRedListCategory`, `taxonKey` vs. `scientificName`)
- [x] Feature subset decision: 29 columns kept and 13 dropped, with a reason for each column. The original CSV stays at 42 columns. Only `iucnRedListStatus` is a 1:1 duplicate; `taxonKey` and `scientificName` are both kept → [`reports/zgjedhja_e_vetive.md`](reports/zgjedhja_e_vetive.md)
- [ ] **Feature subset selection** – keep the attributes relevant for the analysis (taxonomy, time, location, conservation status)
- [x] Time features: `season` from `month`, `decade` from `year`, and `is_recent` for `year >= 2017`. A missing `year` or `month` stays missing. Function `add_time_features()` in notebook 03 → [`reports/vetite_kohore.md`](reports/vetite_kohore.md)
- [x] Taxonomic and conservation features: `taxon_group` from `class` (Zogj, Insekte, Bimë, Kërpudha, Tjera; missing class = "E panjohur") and `is_threatened` from the IUCN category (`VU`/`EN`/`CR` = 1, `LC`/`NT` = 0, `NE`/`DD`/NaN = NaN). The single `EX` row stays NaN and is documented separately. Function `add_taxon_features()` → [`reports/vetite_taksonomike.md`](reports/vetite_taksonomike.md)
- [x] Source and spatial features: `in_protected_area` is 1 when `protectedArea` names an area and 0 when it is blank or "Jashtë zonës së mbrojtur". `is_citizen_science` is 1 only for a citizen-science publisher and `HUMAN_OBSERVATION`. `n_issues` counts serious GBIF flags. Function `add_source_spatial_features()` in notebook 03 → [`reports/vetite_e_burimit.md`](reports/vetite_e_burimit.md)
- [ ] **Feature creation** – e.g. `season` from `month`, `decade` from `year`, `isThreatened` from IUCN category, record count per species
- [x] Elevation zones: `elevation_zone` is Fushë (297–800 m), Kodrinore (801–1,500 m) or Malore (1,501–2,656 m). Missing elevation (79.03%), `elevation = 0` and nine values outside 297–2,656 m are `E panjohur`. Function `add_elevation_zone()` in notebook 03 → [`reports/zona_e_lartesise.md`](reports/zona_e_lartesise.md)
- [x] Time periods: `period` from the original `year`, with cuts at 1900, 1950, 2000, 2010 and 2020. A missing `year` stays missing. Function `add_period()` in notebook 03 → [`reports/periudhat_kohore.md`](reports/periudhat_kohore.md)
- [x] Count classes: `count_class` from the original `individualCount` with `pd.qcut` (`q=4`, duplicate edge at 1 dropped). Equal-width `pd.cut` places 99.82% of known counts in one bin. A missing count stays missing. Function `add_count_class()` in notebook 03 → [`reports/klasa_e_numrit.md`](reports/klasa_e_numrit.md)
- [ ] **Discretization** – bin `elevation` and `year` into ranges (e.g. lowland / hill / mountain, decades)
- [x] One-hot encoding: 20 dummy columns for `taxon_group`, `district` and `basisOfRecord`. A category with fewer than 47 rows is merged into `Tjera`; only `OBSERVATION` (1 row) is merged. `drop_first` is false. Function `add_one_hot()` in notebook 03 → [`reports/kolonat_dummy.md`](reports/kolonat_dummy.md)
- [x] IUCN and flag encoding: `iucn_rank` is LC=1, NT=2, VU=3, EN=4, CR=5, EX=6, read once from `iucnRedListCategory`. `NE`, `DD` and missing stay missing, and `iucn_evaluated` is 0 for those rows. The 10 serious GBIF flags are 0/1 columns. Function `add_iucn_and_flags()` in notebook 03 → [`reports/kodimi_iucn_dhe_flamujve.md`](reports/kodimi_iucn_dhe_flamujve.md)
- [ ] **Binarization** – one-hot encode `kingdom`, `basisOfRecord`; convert `strictlyProtected` and `iasUnionConcern` to 0/1
- [x] Log transform: `individualCount_log1p` and `coordinateUncertaintyInMeters_log1p`. On the cleaned dataset, skewness falls from 26.63 to 2.07 and from 101.73 to −1.00. Missing values stay missing. Function `add_log1p()` in notebook 03 → [`reports/transformimi_log1p.md`](reports/transformimi_log1p.md)
- [x] PCA scaling: Z-scores of the municipality × `taxon_group` record proportions. `year`, latitude and longitude are not scaled. Function `standardize_pca_matrix()` in notebook 03 → [`reports/shkallezimi_pca.md`](reports/shkallezimi_pca.md)
- [x] PCA: PC1–PC3 on the standardized municipality × `taxon_group` matrix. Components with `explained_variance_` above 1 are kept; cumulative `explained_variance_ratio_` is 0.770411. PC6 is 0 because the six proportions sum to 1. Function `run_municipality_pca()` in notebook 03 → [`reports/pca_komunat.md`](reports/pca_komunat.md)
- [ ] **Transformation** – normalize/scale numeric attributes (`elevation`, `individualCount`), apply log transform to skewed counts

Current outputs:
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

---
