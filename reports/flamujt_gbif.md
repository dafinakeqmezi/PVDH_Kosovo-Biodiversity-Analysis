# Flamujt e GBIF

**Versioni:** 1.0  
**Data:** 22.10.2026  
**Statusi:** 35 flamujt e kolonës `issue`, të numëruar dhe të klasifikuar.

## Varësia

Ky task zbaton kontrollin V9 të **Kornizës së kualitetit** (`reports/korniza_e_kualitetit.md`). Llogaritja është te seksioni 3.5 i `notebooks/01_mbledhja_kualiteti.ipynb`, dhe tabela ruhet në `reports/01_flamujt_gbif.csv`. Përshkrimet e flamujve merren nga dokumentacioni zyrtar i GBIF: [OccurrenceIssue](https://gbif.github.io/gbif-api/apidocs/org/gbif/api/vocabulary/OccurrenceIssue.html).

## Si matet

- Kolona `issue` ndahet sipas `;`. Një rresht mund të ketë disa flamuj.
- **n** = numri i rreshtave me flamurin. **%** = n / 46,831 × 100.
- **Rëndësia:**
  - **serioz:** vlera e një kolone që përdoret në analizë mungon, u zëvendësua ose është e pasigurt;
  - **informativ:** GBIF plotësoi ose standardizoi një vlerë, ose flamuri prek një fushë që nuk është në dataset ose nuk përdoret.
- **Bosh te kolona** (vetëm te seriozët) = sa nga rreshtat me flamurin e kanë kolonën përkatëse NaN. Kjo tregon efektin e flamurit në dataset.

## Tabela e flamujve

Seriozët së pari, pastaj sipas n.

| Flamuri | n | % | Rëndësia | Kolona | Bosh te kolona | Arsyeja |
|---|---:|---:|---|---|---:|---|
| `TAXON_MATCH_HIGHERRANK` | 756 | 1.61 | **serioz** | species | 702 | Taksoni u përputh vetëm në rang më të lartë; identiteti i species humbet. |
| `RECORDED_DATE_INVALID` | 508 | 1.08 | **serioz** | eventDate | 497 | Datë e pavlefshme te burimi; GBIF nuk e interpreton dot. |
| `INDIVIDUAL_COUNT_INVALID` | 351 | 0.75 | **serioz** | individualCount | 351 | Numri nuk është numër i plotë pozitiv dhe hiqet. |
| `TAXON_MATCH_FUZZY` | 190 | 0.41 | **serioz** | scientificName | 0 | Emri u përputh në mënyrë të përafërt; taksoni mund të jetë i gabuar. |
| `BASIS_OF_RECORD_INVALID` | 120 | 0.26 | **serioz** | basisOfRecord | 0 | Vlera nuk lexohet dhe zëvendësohet me OCCURRENCE. |
| `RECORDED_DATE_MISMATCH` | 87 | 0.19 | **serioz** | eventDate | 2 | eventDate kundërshton year/month/day te burimi; data është e pasigurt. |
| `TAXON_MATCH_NONE` | 28 | 0.06 | **serioz** | kingdom | 28 | Asnjë përputhje me backbone-in; e gjithë taksonomia mungon. |
| `COORDINATE_UNCERTAINTY_METERS_INVALID` | 7 | 0.01 | **serioz** | coordinateUncertaintyInMeters | 7 | Pasiguria është e pavlefshme dhe hiqet. |
| `TAXON_MATCH_NAME_AND_ID_AMBIGUOUS` | 1 | 0.00 | **serioz** | scientificName | 0 | ID-ja dhe emri çojnë te taksone të ndryshme. |
| `SCIENTIFIC_NAME_AND_ID_INCONSISTENT` | 1 | 0.00 | **serioz** | scientificName | 0 | Emri nuk përputhet me emrin e ID-së së regjistruar. |
| `CONTINENT_DERIVED_FROM_COORDINATES` | 44,725 | 95.50 | informativ | continent (jo në dataset) | – | Kontinenti u nxor nga koordinatat, që janë të vlefshme. |
| `TAXON_CONCEPT_ID_NOT_FOUND` | 26,628 | 56.86 | informativ | taxonKey | – | ID-ja e burimit nuk u gjet, por taksoni u përputh me emrin. |
| `COORDINATE_ROUNDED` | 14,944 | 31.91 | informativ | decimalLatitude, decimalLongitude | – | Koordinata u rrumbullakua në 5 shifra dhjetore (~1 m). |
| `COUNTRY_DERIVED_FROM_COORDINATES` | 7,505 | 16.03 | informativ | countryCode (jo në dataset) | – | Vendi u nxor nga koordinatat; të gjitha pikat janë brenda Kosovës. |
| `TAXON_ID_NOT_FOUND` | 6,083 | 12.99 | informativ | taxonKey | – | ID-ja e burimit nuk u gjet, por taksoni u përputh me emrin. |
| `GEODETIC_DATUM_ASSUMED_WGS84` | 3,850 | 8.22 | informativ | decimalLatitude, decimalLongitude | – | Datumi mungonte dhe u supozua WGS84; zhvendosja e mundshme është më e vogël se pasiguria e zakonshme. |
| `OCCURRENCE_STATUS_INFERRED_FROM_INDIVIDUAL_COUNT` | 1,927 | 4.11 | informativ | occurrenceStatus (jo në dataset) | – | Statusi u nxor nga individualCount. |
| `INSTITUTION_MATCH_NONE` | 1,351 | 2.88 | informativ | institutionCode | – | Përputhja me regjistrin GRSciColl; prek vetëm metadatat e institucionit, jo vëzhgimin. |
| `INSTITUTION_MATCH_FUZZY` | 452 | 0.97 | informativ | institutionCode | – | Përputhja me regjistrin GRSciColl; prek vetëm metadatat e institucionit, jo vëzhgimin. |
| `COUNTRY_INVALID` | 379 | 0.81 | informativ | countryCode (jo në dataset) | – | Vlera e vendit nuk u lexua; vendi u nxor nga koordinatat brenda Kosovës. |
| `COLLECTION_MATCH_NONE` | 176 | 0.38 | informativ | collectionCode | – | Përputhja me regjistrin GRSciColl; prek vetëm metadatat e institucionit, jo vëzhgimin. |
| `COLLECTION_MATCH_FUZZY` | 154 | 0.33 | informativ | collectionCode | – | Përputhja me regjistrin GRSciColl; prek vetëm metadatat e institucionit, jo vëzhgimin. |
| `INSTITUTION_COLLECTION_MISMATCH` | 109 | 0.23 | informativ | institutionCode | – | Përputhja me regjistrin GRSciColl; prek vetëm metadatat e institucionit, jo vëzhgimin. |
| `SCIENTIFIC_NAME_ID_NOT_FOUND` | 79 | 0.17 | informativ | taxonKey | – | ID-ja e emrit nuk u gjet, por taksoni u përputh me emrin. |
| `REFERENCES_URI_INVALID` | 65 | 0.14 | informativ | references (jo në dataset) | – | Link i pavlefshëm; fusha nuk përdoret. |
| `COORDINATE_PRECISION_INVALID` | 63 | 0.13 | informativ | coordinatePrecision (jo në dataset) | – | Fusha nuk është në dataset; koordinatat janë të vlefshme. |
| `NUCLEOTIDE_SEQUENCE_GAPS_REMOVED` | 44 | 0.09 | informativ | sekuenca e ADN-së (jo në dataset) | – | Përpunim i sekuencës së ADN-së; nuk përdoret. |
| `TYPE_STATUS_INVALID` | 29 | 0.06 | informativ | typeStatus (jo në dataset) | – | Statusi i ekzemplarit tip; nuk përdoret. |
| `MULTIMEDIA_URI_INVALID` | 15 | 0.03 | informativ | media (jo në dataset) | – | Link i pavlefshëm; fusha nuk përdoret. |
| `AMBIGUOUS_INSTITUTION` | 12 | 0.03 | informativ | institutionCode | – | Përputhja me regjistrin GRSciColl; prek vetëm metadatat e institucionit, jo vëzhgimin. |
| `NUCLEOTIDE_SEQUENCE_ENDS_TRIMMED` | 6 | 0.01 | informativ | sekuenca e ADN-së (jo në dataset) | – | Përpunim i sekuencës së ADN-së; nuk përdoret. |
| `SUSPECTED_TYPE` | 3 | 0.01 | informativ | typeStatus (jo në dataset) | – | Statusi i ekzemplarit tip me pasiguri; nuk përdoret. |
| `AGE_OR_STAGE_RANK_MISMATCH` | 2 | 0.00 | informativ | konteksti gjeologjik (jo në dataset) | – | Mosha gjeologjike e fosileve; nuk përdoret. |
| `IDENTIFIED_DATE_INVALID` | 1 | 0.00 | informativ | dateIdentified (jo në dataset) | – | Data e identifikimit; data e vëzhgimit nuk preket. |
| `AMBIGUOUS_COLLECTION` | 1 | 0.00 | informativ | collectionCode | – | Përputhja me regjistrin GRSciColl; prek vetëm metadatat e institucionit, jo vëzhgimin. |

## Rreshtat sipas flamujve

| Rreshti ka | Rreshta | % |
|---|---:|---:|
| pa asnjë flamur | 1,426 | 3.04 |
| vetëm flamuj informativë | 43,760 | 93.44 |
| të paktën një flamur serioz | 1,645 | 3.51 |

| Rëndësia | Flamuj | Paraqitje gjithsej |
|---|---:|---:|
| serioz | 10 | 2,049 |
| informativ | 25 | 108,603 |

## Gjetjet kryesore

- **96.96% e rreshtave kanë të paktën një flamur, por vetëm 1,645 rreshta (3.51%) kanë flamur serioz.** Flamujt më të shpeshtë (`CONTINENT_DERIVED_FROM_COORDINATES` 95.50%, `TAXON_CONCEPT_ID_NOT_FOUND` 56.86%, `COORDINATE_ROUNDED` 31.91%) janë informativë: GBIF vetëm ka plotësuar ose standardizuar vlerën.
- **Taksonomia është problemi më i madh:** `TAXON_MATCH_HIGHERRANK` te 756 rreshta, dhe te 702 prej tyre `species` mungon. Kjo shpjegon pjesën më të madhe të 1,213 rreshtave pa species. `TAXON_MATCH_FUZZY` (190) e mban species-in, por taksoni mund të jetë i gabuar.
- **Datat:** `RECORDED_DATE_INVALID` (508) shpjegon 497 nga 2,190 datat që mungojnë. `RECORDED_DATE_MISMATCH` (87) ka datë, por burimi jep data që kundërshtojnë njëra-tjetrën.
- **Vlerat e hequra ose të zëvendësuara:** 351 `individualCount` dhe 7 `coordinateUncertaintyInMeters` u bënë NaN. 120 `basisOfRecord` të palexueshme u bënë `OCCURRENCE`, kështu që nuk dihet nëse janë vëzhgime apo ekzemplarë.
- **Flamujt e koordinatave janë informativë.** Asnjë rresht nuk ka `COUNTRY_COORDINATE_MISMATCH`, `ZERO_COORDINATE` ose `PRESUMED_SWAPPED_COORDINATE`, dhe kontrollet VL1–VL3 (`reports/vlefshmeria.md`) i konfirmojnë koordinatat.

## Vendimi dhe arsyetimi

- **Kriteri i rëndësisë është efekti në kolonat e analizës, jo shpeshtësia e flamurit.** Një flamur i shpeshtë, si `COORDINATE_ROUNDED` (rrumbullakim në ~1 m), nuk prish asgjë. Një flamur i rrallë, si `TAXON_MATCH_NONE` (28), e bën rreshtin të papërdorshëm për analizën taksonomike.
- **10 flamuj janë seriozë**, sepse prekin taksonominë, datën, numrin e individëve, `basisOfRecord` ose pasigurinë, që përdoren në pyetjet e projektit. Efekti u verifikua në dataset (kolona "Bosh te kolona").
- **25 flamuj janë informativë.** Ata prekin fusha që nuk janë në dataset (`continent`, `countryCode`, `typeStatus`, sekuencat e ADN-së, linket), metadatat e institucionit (GRSciColl), ose ID-të e burimit kur taksoni u përputh me emrin.
- **`COORDINATE_PRECISION_INVALID` u kalua nga serioz në informativ**, krahasuar me versionin e parë të V9 te korniza, sepse `coordinatePrecision` nuk është në dataset. U shtuan `RECORDED_DATE_MISMATCH`, `TAXON_MATCH_NAME_AND_ID_AMBIGUOUS` dhe `SCIENTIFIC_NAME_AND_ID_INCONSISTENT`. Prandaj V9 ndryshoi nga 1,617 në 1,645 rreshta. Lista e seriozëve tani merret automatikisht nga seksioni 3.5.
- **Rreshtat me flamuj seriozë nuk fshihen këtu.** Ato shënohen me flamur binar. Vendimi për secilin grup merret te pastrimi: p.sh. `TAXON_MATCH_HIGHERRANK` përjashtohet vetëm nga analizat sipas species.
- **`n_issues`** (numri i flamujve për rresht), që e krijon Jeta, duhet të mbështetet te kjo tabelë. Përndryshe flamujt informativë, që i ka 93% e rreshtave, do ta mbulonin sinjalin e seriozëve.

## Dokumentimi i detyrës

- **Input:** kolona `issue` e `dataset/kosovo_overall_biodiversity.csv`, dokumentacioni [OccurrenceIssue](https://gbif.github.io/gbif-api/apidocs/org/gbif/api/vocabulary/OccurrenceIssue.html) i GBIF.
- **Çka u bë:** `issue` u nda sipas `;`. U numëruan 35 flamujt me n dhe %, dhe secili u klasifikua si serioz ose informativ, me kolonën që prek dhe arsyen. Lista e seriozëve u lidh me kontrollin V9 të kornizës.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 / 42.
- **Pse u bë:** 96.96% e rreshtave kanë flamuj. Pa klasifikim, ose do të fshiheshin rreshta të mirë, ose do të mbeteshin pa shënim rreshtat me taksonomi, datë ose numër të gabuar.
- **Output:** `reports/flamujt_gbif.md`, `reports/01_flamujt_gbif.csv` (Flamuri | n | % | Rëndësia | Kolona | Bosh te kolona | Arsyeja), seksioni 3.5 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Add GBIF flag counts and severity classification`.
