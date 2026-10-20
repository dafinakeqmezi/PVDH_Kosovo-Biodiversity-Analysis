# Korniza e kualitetit të të dhënave

**Versioni:** 1.0  
**Data:** 20.10.2026  
**Statusi:** Pesë dimensionet, 35 kontrolle dhe vlerat fillestare.

## Varësia

Kjo kornizë mbështetet te **Fjalori i të dhënave** (`reports/data_dictionary.md`), **Definimi i tipeve** (`reports/data_types.md`) dhe **Kandidatët për redundancë** (`reports/redundancy.md`). Kontrollet janë të implementuara te seksioni 3.7 i `notebooks/01_mbledhja_kualiteti.ipynb`, dhe rezultatet ruhen në `reports/01_korniza_e_kualitetit.csv`.

## Qëllimi

Kjo kornizë përcakton si matet kualiteti i datasetit. Për secilin dimension jep metrikën, kontrollin dhe kolonat. Ajo është baza për kontrollet e 14–18 tetorit: çdo kontroll i mëvonshëm i referohet një ID-je nga kjo kornizë (P1 … A3), dhe vlerat fillestare më poshtë shërbejnë për krahasim pas pastrimit.

## Si matet

Për çdo kontroll:

- **Aplikohet te:** rreshtat ku kontrolli ka kuptim. Vlefshmëria dhe konsistenca kontrollohen vetëm aty ku vlera ekziston, që një mungesë të mos numërohet dy herë (një herë te plotësia dhe një herë si vlerë e pavlefshme).
- **Nuk plotësojnë:** rreshtat që e shkelin rregullin.
- **Metrika:** `% e plotësimit = (aplikohen − nuk plotësojnë) / aplikohen × 100`.
- **Veprimi:** çfarë propozohet për rreshtat që nuk e plotësojnë. Vendimi përfundimtar merret te `02_pastrimi.ipynb`.

P8 matet me kolona (42), jo me rreshta.

## Tabela e kornizës

Për secilin dimension: metrika, kontrolli dhe kolonat. Vlerat fillestare dhe veprimet janë te tabelat e secilit dimension më poshtë.

| Dimensioni | Metrika | Kontrolli | Kolonat |
|---|---|---|---|
| **Plotësia** | % e rreshtave me të 8 kolonat kryesore të plota | **P1** – Të gjitha kolonat kryesore të plota | `species`, `eventDate`, `decimalLatitude`, `decimalLongitude`, `municipality`, `district`, `basisOfRecord`, `kingdom` |
|  | % e rreshtave me species të plotë | **P2** – Identifikim deri në species | `species` |
|  | % e rreshtave me eventDate të plotë | **P3** – Data e njohur | `eventDate` |
|  | % e rreshtave me kategori IUCN të vlerësuar (LC–EX) | **P4** – Statusi IUCN i vlerësuar (NE/DD = mungesë) | `iucnRedListCategory` |
|  | % e rreshtave me elevation të plotë dhe ≠ 0 | **P5** – Lartësia e njohur (0 m = mungesë) | `elevation` |
|  | % e rreshtave me coordinateUncertaintyInMeters të plotë | **P6** – Pasiguria e koordinatave e dhënë | `coordinateUncertaintyInMeters` |
|  | % e rreshtave me individualCount të plotë | **P7** – Numri i individëve i dhënë | `individualCount` |
|  | % e kolonave me ≤ 80% mungesa | **P8** – Kolona me jo më shumë se 80% mungesa | të 42 kolonat |
| **Vlefshmëria** | % e koordinatave brenda kutisë gjeografike të Kosovës | **V1** – Koordinatat brenda Kosovës (lat 41.85–43.27, lon 20.01–21.80) | `decimalLatitude`, `decimalLongitude` |
|  | % e lartësive (≠ 0) brenda 297–2656 m | **V2** – Lartësia brenda 297–2656 m | `elevation` |
|  | % e pasigurive të dhëna në intervalin (0, 10 000] m | **V3** – Pasiguria > 0 dhe ≤ 10 km | `coordinateUncertaintyInMeters` |
|  | % e eventDate të dhëna që lexohen si datë | **V4** – eventDate e lexueshme si ISO 8601 | `eventDate` |
|  | % e datave ≤ data e sotme | **V5** – Data jo në të ardhmen | `eventDate`, `year` |
|  | % e treshave year-month-day që formojnë datë reale | **V6** – month 1–12, day 1–31 dhe data year-month-day ekziston | `year`, `month`, `day` |
|  | % e individualCount të dhëna ≥ 1 | **V7** – individualCount ≥ 1 | `individualCount` |
|  | % e rreshtave me të gjitha vlerat kategorike brenda fjalorit | **V8** – Vlerat kategorike brenda fjalorit të lejuar (GBIF/DwC/IUCN) | `kingdom`, `taxonRank`, `basisOfRecord`, `iucnRedListCategory`, `license`, `establishmentMeans` |
|  | % e rreshtave pa asnjë flamur GBIF të pavlefshmërisë | **V9** – Pa flamuj GBIF të pavlefshmërisë | `issue` |
|  | % e individualCount të dhëna ≤ Q3 + 1.5·IQR | **V10** – individualCount jo outlier (IQR, > 13.5) | `individualCount` |
| **Konsistenca** | % e rreshtave ku viti/muaji/dita e eventDate = year/month/day | **K1** – eventDate përputhet me year/month/day (sipas precizionit) | `eventDate`, `year`, `month`, `day` |
|  | % e rreshtave ku çdo takson ka një prind brenda kingdom | **K2** – Hierarkia taksonomike: çdo takson ka një prind (brenda kingdom) | `genus`, `family`, `order`, `class`, `phylum`, `kingdom` |
|  | % e rreshtave ku fjala e parë e species = genus | **K3** – species fillon me genus | `species`, `genus` |
|  | % e rreshtave ku taxonRank dhe species përputhen | **K4** – taxonRank SPECIES ose më i ulët ⇔ species e plotë | `taxonRank`, `species` |
|  | % e rreshtave ku kodi dhe emri IUCN lidhen 1:1 | **K5** – iucnRedListCategory ↔ iucnRedListStatus 1:1 | `iucnRedListCategory`, `iucnRedListStatus` |
|  | % e rreshtave ku komuna lidhet me një rajon | **K6** – Çdo komunë i përket një rajoni | `municipality`, `district` |
|  | % e rreshtave ku zona e mbrojtur dhe lloji i saj përputhen | **K7** – protectedArea dhe protectedAreaDesignation bashkë; një zonë = një lloj | `protectedArea`, `protectedAreaDesignation` |
|  | % e rreshtave me iasAppliesFrom ku iasUnionConcern = TRUE | **K8** – iasAppliesFrom e plotë ⇒ iasUnionConcern = TRUE | `iasAppliesFrom`, `iasUnionConcern` |
|  | % e rreshtave pa hapësira të tepërta ose variante shkronjash | **K9** – Kategoritë pa hapësira të tepërta dhe pa variante të shkronjave | 18 kolonat nominale (shih `data_types.md`) |
| **Unikaliteti** | % e gbifID unike | **U1** – gbifID unik | `gbifID` |
|  | % e rreshtave që nuk janë kopje e një rreshti tjetër | **U2** – Pa rreshta identikë | të 42 kolonat |
|  | % e catalogNumber unike brenda datasetKey | **U3** – catalogNumber unik brenda dataset-it | `datasetKey`, `catalogNumber` |
|  | % e vëzhgimeve pa dyfish (takson + koordinata + data) | **U4** – Pa vëzhgime të dyfishta (takson + koordinata + data) | `scientificName`, `decimalLatitude`, `decimalLongitude`, `eventDate` |
|  | % e vëzhgimeve pa dyfish nga një dataset tjetër | **U5** – Pa dyfishime ndërmjet burimeve të ndryshme (datasetKey) | `scientificName`, `decimalLatitude`, `decimalLongitude`, `eventDate`, `datasetKey` |
| **Aktualiteti** | % e regjistrimeve me year ≥ 2017 | **A1** – Regjistrim nga 10 vitet e fundit (year ≥ 2017) | `year` |
|  | % e regjistrimeve me year ≥ 2000 | **A2** – Regjistrim nga viti 2000 e tutje | `year` |
|  | % e regjistrimeve nga dataset-e me të dhëna pas 2016 | **A3** – Dataset-i ka regjistrime pas vitit 2016 | `datasetKey`, `year` |

## Dimensionet

| Dimensioni | Pyetja | Kontrolle | 100% të plotësuara |
|---|---|---:|---:|
| **Plotësia** | A janë vlerat e pranishme? | 8 | 0 |
| **Vlefshmëria** | A janë vlerat brenda formatit, intervalit ose fjalorit të lejuar? | 10 | 6 |
| **Konsistenca** | A përputhen kolonat e lidhura me njëra-tjetrën? | 9 | 6 |
| **Unikaliteti** | A paraqitet çdo vëzhgim vetëm një herë? | 5 | 2 |
| **Aktualiteti** | Sa të reja janë të dhënat? | 3 | 0 |

Vlerat fillestare janë llogaritur mbi datasetin origjinal: 46,831 rreshta dhe 42 kolona.

### 1. Plotësia

| ID | Kontrolli | Kolonat | Aplikohet te | Nuk plotësojnë | % | Veprimi |
|---|---|---|---:|---:|---:|---|
| P1 | Të gjitha kolonat kryesore të plota | `species`, `eventDate`, `decimalLatitude`, `decimalLongitude`, `municipality`, `district`, `basisOfRecord`, `kingdom` | 46,831 | 3,205 | 93.16 | Analiza kryesore vetëm me rreshtat e plotë |
| P2 | Identifikim deri në species | `species` | 46,831 | 1,213 | 97.41 | Përjashto nga analiza sipas species |
| P3 | Data e njohur | `eventDate` | 46,831 | 2,190 | 95.32 | Përjashto nga analiza kohore |
| P4 | Statusi IUCN i vlerësuar (`NE`/`DD` = mungesë) | `iucnRedListCategory` | 46,831 | 16,935 | 63.84 | Shëno "i pavlerësuar" |
| P5 | Lartësia e njohur (0 m = mungesë) | `elevation` | 46,831 | 40,645 | 13.21 | 0 → NaN; vetëm veti ndihmëse |
| P6 | Pasiguria e koordinatave e dhënë | `coordinateUncertaintyInMeters` | 46,831 | 32,004 | 31.66 | Kategoria "e panjohur" te diskretizimi |
| P7 | Numri i individëve i dhënë | `individualCount` | 46,831 | 17,697 | 62.21 | Mos e imputo |
| P8 | Kolona me jo më shumë se 80% mungesa | të 42 kolonat | 42 kolona | 3 | 92.86 | Hiq `iasAppliesFrom`, `establishmentMeans`, `identifiedBy` |

Plotësia matet edhe për mungesat e fshehura: `NE`/`DD` te IUCN (15,722) dhe `elevation = 0` (3,634) duken si vlera, por në fakt janë "e panjohur".

### 2. Vlefshmëria

| ID | Kontrolli | Kolonat | Aplikohet te | Nuk plotësojnë | % | Veprimi |
|---|---|---|---:|---:|---:|---|
| V1 | Koordinatat brenda Kosovës (lat 41.85–43.27, lon 20.01–21.80) | `decimalLatitude`, `decimalLongitude` | 46,831 | 0 | 100.00 | Largo rreshtin |
| V2 | Lartësia brenda 297–2,656 m (pa 0) | `elevation` | 6,186 | 9 | 99.85 | Vendos NaN |
| V3 | Pasiguria > 0 dhe ≤ 10 km | `coordinateUncertaintyInMeters` | 14,827 | 90 | 99.39 | Shëno; jo për analizë hapësinore të detajuar |
| V4 | `eventDate` e lexueshme si ISO 8601 | `eventDate` | 44,641 | 0 | 100.00 | Vendos NaN |
| V5 | Data jo në të ardhmen | `eventDate`, `year` | 44,641 | 0 | 100.00 | Vendos NaN |
| V6 | `month` 1–12, `day` 1–31 dhe data ekziston | `year`, `month`, `day` | 43,612 | 0 | 100.00 | Vendos NaN |
| V7 | `individualCount` ≥ 1 | `individualCount` | 29,134 | 0 | 100.00 | Vendos NaN |
| V8 | Vlerat kategorike brenda fjalorit të lejuar | `kingdom`, `taxonRank`, `basisOfRecord`, `iucnRedListCategory`, `license`, `establishmentMeans` | 46,831 | 0 | 100.00 | Korrigjo ose vendos NaN |
| V9 | Pa flamuj GBIF të pavlefshmërisë¹ | `issue` | 46,831 | 1,617 | 96.55 | Shëno me flamur binar |
| V10 | `individualCount` jo outlier (IQR: > 13.5) | `individualCount` | 29,134 | 3,630 | 87.54 | Shëno; `log1p` te transformimi |

¹ `TAXON_MATCH_NONE`, `TAXON_MATCH_FUZZY`, `TAXON_MATCH_HIGHERRANK`, `RECORDED_DATE_INVALID`, `INDIVIDUAL_COUNT_INVALID`, `BASIS_OF_RECORD_INVALID`, `COORDINATE_PRECISION_INVALID`, `COORDINATE_UNCERTAINTY_METERS_INVALID`. Flamujt informues (p.sh. `COORDINATE_ROUNDED`, `COUNTRY_DERIVED_FROM_COORDINATES`) nuk numërohen, sepse tregojnë si e ka interpretuar GBIF vlerën, jo që vlera është e gabuar.

V10 është kontroll i besueshmërisë, jo i vlefshmërisë së rreptë: një tufë me 10,200 zogj është e mundshme, prandaj rreshtat vetëm shënohen.

### 3. Konsistenca

| ID | Kontrolli | Kolonat | Aplikohet te | Nuk plotësojnë | % | Veprimi |
|---|---|---|---:|---:|---:|---|
| K1 | `eventDate` përputhet me `year`/`month`/`day` (sipas precizionit) | `eventDate`, `year`, `month`, `day` | 44,563 | 0 | 100.00 | Plotëso `year`/`month`/`day` nga `eventDate` |
| K2 | Hierarkia taksonomike: çdo takson ka një prind brenda `kingdom` | `genus` → `family` → `order` → `class` → `phylum` → `kingdom` | 46,794 | 4 | 99.99 | Rishiko |
| K3 | `species` fillon me `genus` | `species`, `genus` | 45,618 | 78 | 99.83 | Rishiko |
| K4 | `taxonRank` SPECIES ose më i ulët ⇔ `species` e plotë | `taxonRank`, `species` | 46,580 | 0 | 100.00 | Rishiko |
| K5 | `iucnRedListCategory` ↔ `iucnRedListStatus` 1:1 | `iucnRedListCategory`, `iucnRedListStatus` | 45,618 | 0 | 100.00 | Mbaj `iucnRedListCategory` |
| K6 | Çdo komunë i përket një rajoni | `municipality`, `district` | 46,831 | 0 | 100.00 | Korrigjo rajonin |
| K7 | `protectedArea` dhe `protectedAreaDesignation` bashkë; një zonë = një lloj | `protectedArea`, `protectedAreaDesignation` | 46,831 | 0 | 100.00 | Korrigjo llojin |
| K8 | `iasAppliesFrom` e plotë ⇒ `iasUnionConcern` = TRUE | `iasAppliesFrom`, `iasUnionConcern` | 24 | 0 | 100.00 | Rishiko |
| K9 | Kategoritë pa hapësira të tepërta dhe pa variante të shkronjave | 18 kolonat nominale | 46,831 | 53 | 99.89 | `strip` + njësim i shkronjave |

### 4. Unikaliteti

| ID | Kontrolli | Kolonat | Aplikohet te | Nuk plotësojnë | % | Veprimi |
|---|---|---|---:|---:|---:|---|
| U1 | `gbifID` unik | `gbifID` | 46,831 | 0 | 100.00 | Largo dyfishin |
| U2 | Pa rreshta identikë | të gjitha | 46,831 | 0 | 100.00 | Largo dyfishin |
| U3 | `catalogNumber` unik brenda dataset-it | `datasetKey`, `catalogNumber` | 34,272 | 82 | 99.76 | Rishiko |
| U4 | Pa vëzhgime të dyfishta (takson + koordinata + data) | `scientificName`, `decimalLatitude`, `decimalLongitude`, `eventDate` | 44,617 | 2,830 | 93.66 | Shëno; vendos te integrimi |
| U5 | Pa dyfishime ndërmjet burimeve të ndryshme | si U4 + `datasetKey` | 44,617 | 34 | 99.92 | Mbaj një rresht për grup |

U4 numëron vetëm rreshtat me të katër kolonat e plota. Prandaj del 2,830, ndërsa seksioni 3.2 i notebook-ut jep 3,336, sepse aty numërohen edhe rreshtat pa datë.

### 5. Aktualiteti

| ID | Kontrolli | Kolonat | Aplikohet te | Nuk plotësojnë | % | Veprimi |
|---|---|---|---:|---:|---:|---|
| A1 | Regjistrim nga 10 vitet e fundit (`year` ≥ 2017) | `year` | 44,563 | 9,709 | 78.21 | Krahaso periudhat veç e veç |
| A2 | Regjistrim nga viti 2000 e tutje | `year` | 44,563 | 4,502 | 89.90 | Shëno si historik |
| A3 | Dataset-i ka regjistrime pas vitit 2016 | `datasetKey`, `year` | 44,563 | 1,621 | 96.36 | Shëno burimin si joaktiv |

Rreshtat që nuk plotësojnë kontrollet e aktualitetit nuk janë të gabuar. Ato janë të dhëna historike, dhe nuk duhet të përzihen pa shënim me vëzhgimet e reja. Viti median është 2020, regjistrimi më i ri është i 22.08.2026, dhe 55 nga 125 dataset-et nuk kanë asnjë regjistrim pas vitit 2016.

## Gjetjet kryesore

- **Plotësia është dimensioni më i dobët.** Kolonat kryesore janë të plota në 93.16% të rreshtave, por kolonat ndihmëse kanë shumë mungesa: lartësia e njohur vetëm 13.21%, pasiguria e koordinatave 31.66%. Statusi IUCN mungon në 36% të rreshtave pasi `NE`/`DD` trajtohen si mungesë.
- **Vlefshmëria është e lartë.** Koordinatat, datat dhe fjalorët janë 100% të vlefshëm. Problemet janë të vogla: 9 lartësi jashtë intervalit, 90 pasiguri mbi 10 km dhe 1,617 rreshta me flamuj GBIF të pavlefshmërisë.
- **Konsistenca ka tri probleme konkrete:**
  - K2: gjinia `Aspicilia` (likene) ka dy familje, 4 rreshta.
  - K3: te 78 rreshta, GBIF e ka zëvendësuar species me sinonimin e pranuar, por gjinia ka mbetur e vjetër, p.sh. `Pararge` / `Lasiommata maera`.
  - K9: `institutionCode` ka `BHAM_Maxted` dhe `BHAM_MAXTED`.
- **Unikaliteti:** 2,830 vëzhgime përsërisin taksonin, koordinatat dhe datën. Vetëm 34 prej tyre vijnë nga dataset-e të ndryshme, pra shumica janë brenda të njëjtit burim, p.sh. disa vëzhgues në të njëjtin vend. Te U3, një dataset vendos emrin e koleksionit ("UP-Spiders of Kosovo") te `catalogNumber`.
- **Aktualiteti:** 78% e regjistrimeve janë nga 10 vitet e fundit, por 10% janë para vitit 2000.

## Vendimi dhe arsyetimi

- **Pesë dimensione, 35 kontrolle të matshme.** Çdo kontroll ka ID, rregull të qartë dhe metrikë në përqindje, që të krahasohet para dhe pas pastrimit.
- **Vlefshmëria matet vetëm mbi vlerat ekzistuese.** Mungesat i takojnë plotësisë. Kështu një rresht pa lartësi nuk numërohet edhe si "lartësi e pavlefshme".
- **Pragjet:**
  - Kufijtë e Kosovës: kutia gjeografike lat 41.85–43.27, lon 20.01–21.80.
  - Lartësia: 297 m (Drini i Bardhë në kufi) deri në 2,656 m (Gjeravica).
  - 10 km: mbi këtë pasiguri, pika nuk lidhet me besueshmëri me një komunë.
  - 80% mungesa: kolona nuk mund të analizohet.
  - 10 vjet: periudha "e re" për krahasim.
- **Hierarkia taksonomike kontrollohet brenda `kingdom`.** Emrat e gjinive nuk janë unikë ndërmjet mbretërive: `Linaria` dhe `Prunella` janë gjini edhe te zogjtë edhe te bimët. Pa këtë kusht, 115 rreshta të saktë do të dilnin si gabime.
- **Kontrollet nuk ndryshojnë datasetin.** Ato vetëm masin dhe propozojnë veprime. Veprimet zbatohen te `02_pastrimi.ipynb` dhe regjistrohen te `processed/cleaning_log.csv`.

## Dokumentimi i detyrës

- **Input:** `dataset/kosovo_overall_biodiversity.csv`, `reports/data_dictionary.md`, `reports/data_types.md`, `reports/redundancy.md`.
- **Çka u bë:** U përcaktuan pesë dimensionet e kualitetit dhe 35 kontrolle me metrikë, rregull, kolona dhe veprim të propozuar. Kontrollet u implementuan te seksioni 3.7 i `01_mbledhja_kualiteti.ipynb` dhe u llogaritën vlerat fillestare.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 / 42.
- **Pse u bë:** Për të pasur një bazë të përbashkët dhe të matshme për kontrollet e 14–18 tetorit dhe për të krahasuar kualitetin para dhe pas pastrimit.
- **Output:** `reports/quality_framework.md`, `reports/01_korniza_e_kualitetit.csv`, seksioni 3.7 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Add data quality framework with five dimensions`.
