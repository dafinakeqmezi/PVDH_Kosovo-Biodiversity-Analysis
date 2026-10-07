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

## Dataset

**File:** `kosovo_overall_biodiversity.csv`

Species occurrence records for Kosovo, exported from GBIF (Global Biodiversity Information Facility).

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

### 1. Data collection, data types and data quality
- [ ] Describe the data source (GBIF) and the meaning of each attribute
- [ ] Assign correct data types (`eventDate` → datetime, `year`/`month`/`day` → integer, categorical columns → `category`)
- [ ] Assess data quality: missing values, invalid coordinates, outliers, inconsistent values, GBIF `issue` flags

### 2. Integration, aggregation, sampling, cleaning and missing values
- [ ] **Integration** – merge records coming from different `datasetKey` sources and harmonize column values
- [ ] **Aggregation** – summarize occurrences per species, district, municipality, year and IUCN category
- [ ] **Sampling** – draw a stratified sample (e.g. by `kingdom` or `district`) for faster exploration
- [ ] **Cleaning** – drop columns that are almost empty (`iasAppliesFrom`, `establishmentMeans`), remove records not identified to species level where needed, fix inconsistent text values
- [ ] **Missing value strategy** – drop rows where key fields are missing (`species`, `year`), impute `month`/`day` from `eventDate`, fill `protectedArea` with "Not protected", mark unknowns explicitly

### 3. Dimensionality reduction, feature selection, feature creation, discretization and binarization, transformation
- [ ] **Dimensionality reduction** – remove redundant attributes (`iucnRedListStatus` vs. `iucnRedListCategory`, `taxonKey` vs. `scientificName`)
- [ ] **Feature subset selection** – keep the attributes relevant for the analysis (taxonomy, time, location, conservation status)
- [ ] **Feature creation** – e.g. `season` from `month`, `decade` from `year`, `isThreatened` from IUCN category, record count per species
- [ ] **Discretization** – bin `elevation` and `year` into ranges (e.g. lowland / hill / mountain, decades)
- [ ] **Binarization** – one-hot encode `kingdom`, `basisOfRecord`; convert `strictlyProtected` and `iasUnionConcern` to 0/1
- [ ] **Transformation** – normalize/scale numeric attributes (`elevation`, `individualCount`), apply log transform to skewed counts

---