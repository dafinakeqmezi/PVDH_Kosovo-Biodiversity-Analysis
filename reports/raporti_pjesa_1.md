# Raporti i Pjesës I: përgatitja e të dhënave për analizë

**Projekt grupor: biodiversiteti në Kosovë**  
**Versioni i raportit:** 31.10.2026

Ky raport bashkon mbledhjen, kualitetin, pastrimin, integrimin, mostrimin dhe përgatitjen e vetive. Seksionet organizohen sipas fazës së analizës, pa ndarje të punës sipas personave. Raportet e hollësishme dhe tabelat mbeten evidencë mbështetëse.

| Versioni | Rreshta | Kolona | Përdorimi |
| --- | ---: | ---: | --- |
| Origjinali | 46,831 | 42 | Burimi i pandryshueshëm, diagnostikimi dhe mostrat v1 |
| Dataset-i i pastruar | 46,456 | 83 | Input-i i përbashkët për analizat pas pastrimit |
| Dataset-i me veti | 46,456 | 128 | 83 kolona të ruajtura + 45 të derivuara |
| PCA v2 | 38 | 5 | Komuna, rajoni dhe tre komponentët |

Agregimet pa prapashtesë janë mbi origjinalin; `*_v2.csv` janë mbi të dhënat e pastruara. Të dy versionet ruhen për gjurmueshmëri. Kontrolli numerik nuk është verifikim i çdo pretendimi biologjik ose gjeografik.

## 1. Mbledhja, burimet, tipet dhe kualiteti

### Mbledhja e të dhënave

Të dhënat janë shkarkuar nga [GBIF](https://www.gbif.org) (Global Biodiversity Information Facility) me filtrin e vendit Kosovë (`XK`). Çdo rresht është një *occurrence*: një organizëm i vëzhguar ose i mbledhur në një vend dhe kohë të caktuar, sipas standardit Darwin Core.

| Veti | Vlera |
|---|---|
| Skedari | `dataset/kosovo_overall_biodiversity.csv` (CSV, UTF-8, 22 MB) |
| Rreshta × kolona | 46,831 × 42 |
| Kolona Darwin Core / GBIF | 34 |
| Kolona të shtuara për Kosovën | 8 (`iucnRedListStatus`, `municipality`, `district`, `protectedArea`, `protectedAreaDesignation`, `strictlyProtected`, `iasUnionConcern`, `iasAppliesFrom`) |
| Periudha | 1826–2026 (viti median 2020) |
| Taksonomia | 4,647 emra shkencorë, 4,095 specie, 68 klasa |
| Gjeografia | 7 rajone, 38 komuna, 20 zona të mbrojtura |
| Licencat | CC BY 4.0 (67.81%), CC BY-NC 4.0 (30.46%), CC0 1.0 (1.72%) |

Për shkak të pjesës CC BY-NC, dataset-i si tërësi përdoret vetëm për qëllime jokomerciale. Citimi bëhet përmes DOI-t të shkarkimit nga GBIF, i cili i krediton të 125 dataset-et kontribuuese. Kuptimi i 42 kolonave është te `reports/fjalori_i_te_dhenave.md`.

### Burimet e të dhënave

CSV-ja nuk ka kolonat e publikuesit. Prandaj publikuesi u mor nga GBIF API (`/v1/dataset/{datasetKey}` → `/v1/organization/{key}`) dhe u gjet për **125 nga 125** dataset-et. `institutionCode` mbeti vetëm si rezervë, sepse ka 108 vlera për 80 publikues dhe mungon te disa dataset-e.

| Publikuesi | Regjistrime | % | % kumulative | Lloji kryesor |
|---|---:|---:|---:|---|
| Cornell Lab of Ornithology (eBird) | 26,009 | 55.54 | 55.54 | vëzhgim njerëzor, zogj |
| HabiProt | 8,122 | 17.34 | 72.88 | vëzhgim njerëzor, insekte |
| iNaturalist.org | 4,286 | 9.15 | 82.03 | vëzhgim njerëzor |
| Observation.org | 1,436 | 3.07 | 85.10 | vëzhgim njerëzor |
| 76 publikues të tjerë | 6,978 | 14.90 | 100.00 | |

- **Burimet janë shumë të përqendruara:** 3 publikues japin 82.03% të regjistrimeve, dhe 10 publikues 92.56%.
- **Dataset-i është kryesisht shkencë qytetare:** 90.71% e regjistrimeve janë `HUMAN_OBSERVATION`. Ekzemplarët e muzeve (`PRESERVED_SPECIMEN`) janë vetëm 3.73%.

Burimi: `notebooks/01b_analiza_burimeve.ipynb`, `processed/sources_summary.csv`.

### Tipet e të dhënave

Për secilën nga 42 kolonat u përcaktuan tipi në pandas, tipi konceptual dhe tipi i synuar pas konvertimit:

| Tipi konceptual | Kolona | Tipi i synuar në pandas |
|---|---:|---|
| nominal | 18 | `category` |
| ID | 5 | `int64` / `Int64` / `str` / `category` |
| ordinal | 5 | `category (ordered)` (IUCN, `taxonRank`) ose `Int64` (`month`, `day`) |
| interval | 4 | `Int64` (`year`) / `float64` (koordinatat, `elevation`) |
| tekst | 4 | `str` |
| ratio | 2 | `float64` / `Int64` |
| binar | 2 | `bool` |
| datë | 2 | `datetime64` |

- Tabela paraqet tipet konceptuale dhe eksperimentin diagnostik të notebook-ut 01. Checkpoint-i i pastrimit ruan `NE`, `DD` dhe `UNRANKED` si kategori të parenditura; vetëm rangu i derivuar IUCN në fazën e vetive ka mungesë për NE/DD. Konvertimi diagnostik nuk duhet ngatërruar me schema-n e dataset-it të pastruar.
- Numrat e plotë me mungesa u bënë `Int64`, që `2026` të mos bëhet `2026.0`.
- Konvertimi e ul memorien nga **31.9 MB në 13.6 MB**. Një `assert` kontrollon që çdo kolonë merr tipin e synuar.

Burimi: seksioni 2 i notebook-ut, `reports/tipet_e_te_dhenave.md`.

### Kualiteti i të dhënave

#### 4.1 Korniza

Kualiteti matet në **5 dimensione me 35 kontrolle**. Për çdo kontroll janë përcaktuar metrika, rregulli dhe kolonat:

| Dimensioni | Pyetja | Kontrolle |
|---|---|---:|
| Plotësia | A janë vlerat të pranishme? | 8 |
| Vlefshmëria | A janë brenda formatit, intervalit ose fjalorit? | 10 |
| Konsistenca | A përputhen kolonat e lidhura? | 9 |
| Unikaliteti | A paraqitet çdo vëzhgim një herë? | 5 |
| Aktualiteti | Sa të reja janë të dhënat? | 3 |

Metrika: % e rreshtave ku kontrolli aplikohet dhe që e plotësojnë. Vlefshmëria dhe konsistenca maten vetëm mbi vlerat që ekzistojnë, që një mungesë të mos numërohet dy herë. Burimi: seksioni 3.7, `reports/korniza_e_kualitetit.md`.

#### 4.2 Plotësia

- **Për rresht:** **43,626 rreshta (93.16%)** i kanë të plota katër fushat kyçe (species, data, koordinata, komuna). Koordinatat dhe komuna janë 100% të plota. Mungon vetëm data te 1,992 rreshta, vetëm species te 1,015, dhe të dyja te 198.
- **Plotësia fizike dhe disponueshmëria analitike dallojnë:** NE/DD dhe UNRANKED janë kode të raportuara, jo qeliza bosh. Tabela tregon disponueshmërinë për rangim/vlerësim; vetëm zeroja e lartësisë trajtohet si placeholder në pastrim.

| Kolona | Vlera e fshehur | Plotësia e dukshme | Plotësia reale |
|---|---|---:|---:|
| `iucnRedListCategory` | `NE`, `DD` (15,722) | 97.41% | **63.84%** |
| `elevation` | `0` (3,634) | 20.97% | **13.21%** |
| `taxonRank` | `UNRANKED` (214) | 99.92% | 99.46% |

- **Mungesat strukturore:** interpretimi i `protectedArea` si "jashtë zonës së mbrojtur" mbështetet në sqarim semantik, jo në verifikim GIS. `iasAppliesFrom` është raportuar në 24 regjistrime, jo domosdoshmërisht në 24 specie të ndryshme. 13 nga 42 kolonat janë 100% të plota.

Burimi: seksioni 3.8, `reports/plotesia.md`.

#### 4.3 Vlefshmëria

| Rregulla | Rreshta që dështojnë | % |
|---|---:|---:|
| Koordinatat brenda kufijve numerikë të kontrolluar (jo provë me poligone) | 0 | 0.00 |
| Viti brenda 1758–2026; `month` 1–12; `day` 1–31; data reale | 0 | 0.00 |
| `eventDate` e lexueshme si ISO 8601 (11 formate) | 0 | 0.00 |
| Intervalet e datave ≤ 1 vit | 53 nga 447 | 11.86 |
| Pa flamurin GBIF `RECORDED_DATE_INVALID` | 508 | 1.08 |
| `coordinateUncertaintyInMeters` ≠ 7071 | 8,225 | 55.47 |
| `elevation` ≠ 0 | 3,634 | 37.01 |
| `elevation` brenda 297–2,656 m (pa 0) | 9 | 0.15 |

- **Vlera 7071 te pasiguria (8,225 regjistrime)** është ≈ 5000·√2, gjysma e diagonales së një qelize 10 × 10 km. Kjo është në përputhje me koordinata të përgjithësuara në qendër qelize; vendi i saktë i vëzhgimit nuk verifikohet (kryesisht HabiProt, 122 pika të ndryshme). Komuna e këtyre rreshtave mund të jetë e pasaktë.
- **Pesë ekzemplarë herbariumi në Kaçanik me 2,750–3,050 m** janë jashtë diapazonit të përdorur në kontroll dhe kërkojnë verifikim burimor; vlerat jo-zero nuk fshihen automatikisht.

Burimi: seksioni 3.9, `reports/vlefshmeria.md`.

#### 4.4 Flamujt e GBIF

Kolona `issue` ka **35 flamuj**. Ata u klasifikuan sipas efektit në kolonat e analizës, jo sipas shpeshtësisë:
- **10 flamuj seriozë:** vlera mungon, u zëvendësua ose është e pasigurt. P.sh. `TAXON_MATCH_HIGHERRANK` (756 rreshta; te 702 prej tyre species mungon), `RECORDED_DATE_INVALID` (508), `INDIVIDUAL_COUNT_INVALID` (351), `BASIS_OF_RECORD_INVALID` (120 → `OCCURRENCE`).
- **25 flamuj informativë:** GBIF plotësoi ose standardizoi një vlerë, ose flamuri prek një fushë që nuk përdoret. P.sh. `CONTINENT_DERIVED_FROM_COORDINATES` (95.50%), `COORDINATE_ROUNDED` (31.91%).

96.96% e rreshtave kanë të paktën një flamur, por vetëm **1,645 rreshta (3.51%) kanë flamur serioz**. Burimi: seksioni 3.5, `reports/flamujt_gbif.md`.

#### 4.5 Unikaliteti

- `gbifID` është unik, dhe nuk ka rreshta identikë.
- Me kriterin species + data + koordinata + vëzhgues ka **1,288 grupe dhe 1,844 rreshta të tepërta**. Shqyrtimi manual i 18 grupeve tregoi se shumica nuk janë i njëjti vëzhgim: janë ekzemplarë me `catalogNumber` të ndryshëm, pika të rrjetës 10 km, ose numërime të ndara të së njëjtës ditë.
- **Definicioni i propozuar:** duplikat janë rreshtat nga dataset-e të ndryshme, ose nga i njëjti dataset me `individualCount` të njëjtë, pa ekzemplarë të ndryshëm dhe pa koordinata 7071 m. Ai jep **238 grupe dhe 378 rreshta të tepërta**.
- Vendimi i pastrimit pranoi 235 nga këto grupe dhe largoi **375 rreshta**.

Burimi: seksioni 3.10, `reports/unikaliteti.md`, `processed/duplicate_candidates.csv`.

#### 4.6 Konsistenca dhe anshmëria

**Konsistenca është e lartë:**
- municipality → district përputhet 100%, edhe me ndarjen zyrtare në 7 rajone dhe 38 komuna;
- genus → family është 99.99% brenda `kingdom`, me një përjashtim (`Aspicilia`, 4 rreshta);
- te 78 rreshta (9 specie) emri i species nuk fillon me gjininë, sepse emri dhe klasifikimi vijnë nga trajtime taksonomike të ndryshme (p.sh. *Lasiommata maera* nën *Pararge*).

**Anshmëria është e fortë.** Dataseti mat se ku dhe çka vëzhgojnë disa vëzhgues:

| Treguesi | Vlera |
|---|---|
| Zogj (Aves): % e regjistrimeve / % e specieve | 61.47% / 6.23% |
| Një pikë e vetme (Ligatinat e Henc, Graçanicë) | 27.86% e regjistrimeve |
| Rajoni i Prishtinës (pa pikën e Henc-it) | 54.95% (37.55%) |
| eBird | 55.54% |
| Një vëzhgues (obsr1505715) | 35.18% |

Rajoni me më shumë specie është Prizreni (1,582), me vetëm 11.25% të regjistrimeve. Burimi: seksioni 3.11, `reports/konsistenca_dhe_anshmeria.md`.


## 2. Mungesat, pastrimi dhe validimi

### Qëllimi dhe versionet e të dhënave

Pastrimi u zbatua mbi një kopje pune. [Dataset-i origjinal](../dataset/kosovo_overall_biodiversity.csv) mbetet i pandryshuar. Rezultati për analizat pasuese është [biodiversity_clean.csv](../processed/biodiversity_clean.csv), jo skedari i ndërmjetëm `kosovo_biodiversity_clean.csv`.

| Treguesi | Origjinali | Dataset-i i pastruar |
| --- | ---: | ---: |
| Rreshta | 46,831 | 46,456 |
| Kolona | 42 | 83 |
| Rreshta të larguar | - | 375 duplikate të miratuara |

U hoqën dy kolona dhe u shtuan 43: kryesisht flamuj, statuse, prejardhje dhe përfaqësime të datave. Kështu, 83 kolonat nuk janë 83 veti të pavarura për modelim. Vetëm largimi i duplikateve ndryshoi numrin e rreshtave; mungesat dhe ekstremet nuk u përdorën për fshirje rreshtash.

Përqindjet fillestare përdorin 46,831 rreshta, ndërsa statistikat pas duplikateve përdorin 46,456. Këta emërues nuk duhen përzier në raportin e përbashkët.

### Identifikimi dhe mekanizmat e mungesës

Eksplorimi përfshiu dimensionet, `info()`, tipet dhe shembuj nga kolonat. Inventari NaN u plotësua me lexim literal të tekstit për `unknown`, `NA`, `N/A`, `null`, `-`, tekstet bosh dhe hapësirat, që këta tokenë të mos fshiheshin nga parsimi automatik. U konfirmuan 40 qeliza shtesë për normalizim: 38 në `locality`, një në `recordedBy` dhe një në `identifiedBy`. `NE`/`DD` të IUCN dhe `UNRANKED` nuk u trajtuan si tokenë të zakonshëm mungese.

Për `elevation`, 3,634 zero u analizuan sipas burimit dhe vendndodhjes: 3,624 lidhen me HabiProt; zerot shfaqen në shtatë rajone dhe 32 komuna. Sipas [vendimit për lartësinë](vendimi_per_lartesine_zero.md), ato u trajtuan si placeholder, u kthyen në NaN dhe u ruajt flamuri `elevation_was_zero`. Nuk u imputua lartësi dhe nuk u krye verifikim i pavarur me model digjital të terrenit.

| Kolona | Mungesa efektive fillestare | Përqindja |
| --- | ---: | ---: |
| elevation, përfshirë zerot | 40,645 | 86.79% |
| coordinateUncertaintyInMeters | 32,004 | 68.34% |
| individualCount | 17,697 | 37.79% |
| eventDate | 2,190 | 4.68% |
| species | 1,213 | 2.59% |

Për këto pesë kolona u llogaritën mungesat sipas `datasetKey`, `basisOfRecord`, `class` dhe `district`. Për shembull, mungesa e `individualCount` varion nga 10.63% te Aves në 100% te Bivalvia; mungesa e `elevation` nga 45.24% në rajonin e Gjilanit në 98.16% në Prishtinë.

**Decision + Rationale:** Modeli i mungesës duket në përputhje me MAR të kushtëzuar nga karakteristikat e vëzhguara, por krahasimet përshkruese nuk provojnë MAR dhe nuk përjashtojnë MNAR. MCAR nuk merret si supozim pune. Grupimet janë margjinale; burimi, klasa dhe rajoni nuk janë efekte të pavarura shkakësore. Raportimi jo i rastësishëm dhe vlerat e pavëzhguara kufizojnë interpretimin dhe nuk justifikojnë imputim të përgjithshëm me mesatare ose modë.

Evidenca: [inventari NaN](../processed/missing_report.csv), [mungesat e fshehura](mungesat_e_fshehura.csv), [mungesat efektive](raporti_i_mungesave_efektive.csv), [tabelat sipas grupeve](mungesat_sipas_grupeve.csv), [interpretimi](mekanizmat_e_mungeses.md).

### Strategjia e zbatuar

Vendimet varen nga rëndësia, kuptimi dhe rikuperueshmëria, jo nga një prag universal. Tabela e mëposhtme grupon të 42 kolonat origjinale. Përqindjet e veçanta, rëndësia dhe rikuperimi për çdo kolonë janë në [tabelën e plotë të strategjisë](strategjia_e_mungesave.md); ajo ruan vendimin fillestar, ndërsa këtu përfshihet edhe sqarimi i mëvonshëm për zonat e mbrojtura.

| Kolonat | Vendimi i zbatuar | Rikuperimi dhe arsyetimi |
| --- | --- | --- |
| gbifID, datasetKey, license | keep | Identifikimi, burimi dhe licenca ruhen; nuk nevojitet imputim. |
| scientificName, species, kingdom, phylum, class, order, family, genus | keep + flag | Nuk shpiket identiteti ose klasifikimi; mungesat ruhen. |
| taxonRank, taxonKey, speciesKey | keep + flag | Nuk imputohen identifikues; ruhet rangu i raportuar. |
| vernacularName | keep | Emri i zakonshëm nuk është kusht për ruajtjen e regjistrimit. |
| iucnRedListCategory | keep + flag | NE/DD ruhen; kodimi ordinal i takon notebook-ut 03. |
| iucnRedListStatus | delete | Redundant me kategorinë IUCN, jo fshirje për shkak të mungesës. |
| eventDate | keep + flag; parsimi | Ruhet teksti, kufijtë dhe precizioni. |
| year, month | Rikuperim determinist i kushtëzuar + flag | Zero raste të përshtatshme; nuk bëhet imputim statistikor. |
| day | keep + flag | Nuk shpiket dita nga një datë e pjesshme. |
| decimalLatitude, decimalLongitude | keep + flag | Ruhen koordinatat dhe kontrollohen kufijtë numerikë. |
| coordinateUncertaintyInMeters | keep + flag/status | Mungesa nuk barazohet me saktësi; nuk imputohet. |
| elevation | zero në NaN + flag | Pa burim të verifikuar për rikuperim; ekstremet jo-zero ruhen. |
| locality | keep + flag | Normalizohen tokenët e konfirmuar, jo vendndodhje të hamendësuara. |
| municipality, district | keep | Ruhet origjinali; shtohet emri shqip i komunës. |
| protectedArea, protectedAreaDesignation | Plotësim strukturor + status | Bazuar në sqarim semantik të përdorueses, jo GIS të pavarur. |
| strictlyProtected, iasUnionConcern | keep; bool | Konvertim i tipit pa hamendësuar vlera. |
| basisOfRecord | keep; category | Konteksti i regjistrimit ruhet. |
| individualCount | keep + flag | NaN mbetet NaN; heterogjeniteti nuk justifikon imputim. |
| establishmentMeans | delete | Pothuajse bosh dhe jashtë pyetjeve kryesore; jo vetëm për shkak të %. |
| recordedBy, identifiedBy | keep + flag | Gjurmueshmëria ruhet; tokenët e konfirmuar bëhen NaN. |
| institutionCode, collectionCode, catalogNumber | keep | Nuk imputohen identifikues ose institucione. |
| issue | keep + flag | Bosh nuk nënkupton domosdoshmërisht problem. |
| iasAppliesFrom | keep + status | Dallohet mungesa strukturore; nuk shpiket datë. |

#### Mungesat strukturore

Para duplikateve, 25,762 vlera bosh të `protectedArea` u zëvendësuan me `Jashtë zonës së mbrojtur`; designation në të njëjtët rreshta u bë `Nuk aplikohet`. Pas duplikateve mbeten 25,580 regjistrime me këtë status dhe 20,876 me zonë të emërtuar.

**Decision + Rationale:** Interpretimi mbështetet në sqarimin semantik të përdorueses, jo dokumentacion të verifikuar të prodhuesit ose bashkim të pavarur hapësinor. Nuk pretendohet mungesë e mbrojtjes në çdo sistem zonash. Statusi ruan gjurmën e vendimit; emrat ekzistues nuk ndryshohen.

Për IAS, `iasAppliesFrom` mbetet bosh kur nuk aplikohet. Në origjinal, 46,807 raste klasifikohen `not_applicable` dhe 24 `reported`. Shih [vendimet dhe kufizimet](vendimet_per_mungesat_strukturore.md).

### Datat dhe tipet

`eventDate` ruhet si tekst origjinal. Nga 44,641 vlera të pranishme u krijuan `event_start`, `event_end`, `date_precision` dhe metadata të parsimit. Inventari ka 11 formate jo-bosh: përfshin 447 intervale, 409 data vetëm me vit dhe 173 me vit-muaj; 2,190 mungojnë.

**Decision + Rationale:** Kufijtë e një viti ose muaji përfaqësojnë intervalin e mundshëm, jo ditë reale vëzhgimi. Precizioni `day`, `month`, `year` ose `interval` ruhet veçmas. Teksti me orë mbetet në kolonën burimore; kufijtë e derivuar janë në nivel dite. Kontrollohen dështimet e parsimit dhe intervalet e përmbysura.

Plotësimi i `year`/`month` provohet vetëm nga data të plota ose intervale me skaje të plota brenda të njëjtit muaj dhe vit, pa konflikt me vlerat ekzistuese. Datat e pjesshme dhe intervalet ndërmjet muajve/viteve përjashtohen. **Rezultati është zero plotësime**, jo mungesë implementimi: mbeten 2,268 mungesa të vitit dhe 2,867 të muajit. `day` nuk plotësohet.

`year`, `month`, `day`, `taxonKey`, `speciesKey` dhe `individualCount` përdorin `Int64` nullable; `strictlyProtected` dhe `iasUnionConcern` bëhen bool. Kategoritë janë të parenditura; IUCN nuk kodohet ordinalisht në pastrim. Ky kodim kryhet në fazën e vetive, në notebook-un 03.

Evidenca: [formatet](formatet_e_datave.csv), [tipet para/pas](tipet_para_pas_pastrimit.csv), [vendimi year/month](vendimi_per_plotesimin_year_month.md), [gjurma për çdo qelizë](gjurma_e_plotesimit_year_month.csv).

### Duplikatet

Vendimi përdor analizën historike të unikalitetit nga commit-i `d2708c640de830014edf4c4f35a528849c98455f`. Kandidatët grupohen sipas species, datës, koordinatave dhe vëzhguesit të normalizuar.

**Decision + Rationale:** Ngjashmëria e çelësit nuk mjafton. Pranimi kërkon vëzhgues të njohur, precizion dite, përjashtim të rasteve me pasiguri 7,071 m, numërime identike përfshirë statusin e mungesës dhe mungesë konflikti në emrin shkencor ose `basisOfRecord`. Rastet ndërmjet burimeve kërkojnë shqyrtim pozitiv; numrat e ndryshëm të katalogut nuk bashkohen pa evidencën e përcaktuar.

Nga propozimi për 378 largime në 238 grupe u miratuan **375 largime në 235 grupe**; tri grupe u përjashtuan për konflikte. Fituesi ka më shumë fusha të plota nga 28 fusha të përcaktuara; barazimi zgjidhet me `gbifID` numerik më të vogël. Kur `individualCount` ndryshon, numërimet nuk zgjidhen arbitrarisht dhe nuk mblidhen.

Rreshtat kalojnë nga 46,831 në 46,456. Kontrolli verifikon një fitues për grup të miratuar dhe ruajtjen e grupeve të përjashtuara. Nuk pretendohet identifikimi i çdo përsëritjeje biologjike.

Evidenca: [rregulla](vendimi_per_duplikatet.md), [vendime grupesh](vendimet_e_grupeve_duplikate.csv), [lista e largimit](../processed/rreshtat_per_fshirje_duplikate.csv), [rreshtat e larguar](../processed/rreshtat_e_larguar_duplikate.csv), [kontrollet](kontrolli_i_largimit_te_duplikateve.csv).

### Kategoritë dhe vlerat e pavlefshme

Në 17 kolona kategorike u kontrolluan Unicode NFC, hapësirat dhe variantet e shkronjave. Rregullat prodhuan **zero ndryshime në qelizat ekzistuese**. U ruajt `municipality_original` dhe u krijua `municipality_sq` për 38 komuna nga pjesa shqip e emrit dygjuhësh; nuk u përdor përputhje e përafërt ose korrigjim i hamendësuar. Shih [pastrimin e kategorive](pastrimi_i_kategorive.md).

Për pasigurinë hapësinore, mediana pozitive është 7,071 m. Pragu operacional është minimumi i saj dhe rrezes ekuivalente të komunës më të vogël me sipërfaqe të njohur: `sqrt(sipërfaqja/pi) * 1000`, rreth **1,866.09 m**. Komunat pa sipërfaqe individuale nuk kontribuojnë në minimum. [Analiza e ndjeshmërisë](ndjeshmeria_e_pragut_te_pasigurise.csv) dokumenton alternativa.

**Decision + Rationale:** Ky është filtër orientues për analizë komunale, jo distancë reale nga kufiri ose provë që komuna është e saktë. Statuset janë 31,813 të panjohura, 9,091 mbi prag dhe 5,552 brenda pragut. Nuk fshihen këta rreshta.

`is_species_level` është True për 45,140 regjistrime në nivel specie ose më të imët me specie të njohur, False për 1,082 të rangjeve më të larta dhe NA për 234 raste të panjohura/pa rang të përdorshëm. NA nuk barazohet me False.

Të 3,634 zerot e lartësisë bëhen NaN; pas duplikateve mbeten 40,288 mungesa lartësie. Ekstremet jo-zero ruhen për shqyrtim, jo fshihen që validimi të kalojë. Evidenca: [rregullat](rregullat_e_vlerave_te_pavlefshme.csv), [arsyetimi](vendimi_per_vlerat_e_pavlefshme.md), [niveli taksonomik](niveli_taksonomik.csv).

### Vendimi për individualCount

Në dataset-in e pastruar ka 28,869 numërime të njohura dhe **17,587 mungesa (37.86%)**. Vlerat e njohura kanë minimum 1, medianë 2, kuartil të tretë 6, percentil 99 prej 150 dhe maksimum 10,200; mesatarja është 23.14 dhe skewness 26.63.

**Decision + Rationale:** Shpërndarja e anuar, heterogjeniteti i burimeve dhe mungesa e informacionit mbi përpjekjen e vëzhgimit nuk justifikojnë medianë të përgjithshme ose sipas grupit. Një occurrence nuk nënkupton domosdoshmërisht një individ. NaN ruhet me flamurin ekzistues; `was_imputed` nuk shtohet sepse nuk u imputua asnjë vlerë. Rënia nga 17,697 në 17,587 mungesa vjen nga largimi i 110 duplikateve me numërim bosh, jo nga plotësimi.

Evidenca: [vendimi](vendimi_per_numrin_e_individeve.md), [shpërndarja](shperndarja_e_numrit_te_individeve.csv), [krahasimi para/pas](numri_i_individeve_para_pas.csv).

### Përmbledhja e log-ut dhe ruajtja

Manifesti regjistron **102 hapa** të notebook-ut 02 në [cleaning_log.csv](../processed/cleaning_log.csv). Ky nuk është numër ndryshimesh: regjistrohen edhe hapa me zero vlera të ndryshuara. Numërimet e qelizave nuk mblidhen si rreshta unikë, sepse një rresht mund të preket disa herë.

| Faza | Rreshta pas | Kolona pas | Rezultati kryesor |
| --- | ---: | ---: | --- |
| Leximi dhe tokenët | 46,831 | 42 | 40 qeliza në NA |
| Flamuri i lartësisë dhe heqja e kolonave | 46,831 | 41 | +1 flamur, -2 kolona |
| Flamujt e mungesës | 46,831 | 69 | +28 flamuj |
| Statuset strukturore | 46,831 | 71 | Statusi i zonës dhe IAS |
| Parsimi i datave | 46,831 | 77 | +6 kolona |
| Tipet dhe rikuperimi year/month | 46,831 | 79 | +2 flamuj; 0 plotësime |
| Largimi i duplikateve | 46,456 | 79 | -375 rreshta |
| Pastrimi i kategorive | 46,456 | 81 | Origjinali dhe emri shqip i komunës |
| Vlerat e pavlefshme | 46,456 | 83 | Zero në NA, status pasigurie, nivel specie |
| Vendimi për numërimet dhe ruajtja | 46,456 | 83 | Pa imputim; ruajtje e kontrolluar |

CSV-ja nuk ruan vetë tipet pandas. [Schema](../processed/biodiversity_clean_schema.json) përdoret për rikthimin e tyre; [manifesti](../processed/biodiversity_clean_manifest.json) ruan dimensionet dhe SHA-256 të burimit, rezultatit, schema-s dhe log-ut. Riekzekutimi refuzon mbishkrimin e checkpoint-it me përmbajtje tjetër; korrigjimet kërkojnë version të ri të dakorduar.

### Validimi dhe kufijtë

[Validimi i ruajtur](validimi.md) raporton **23 PASS / 0 FAIL**. Assert-et mbulojnë integritetin e skedarëve, origjinalin kundrejt Git, dimensionet, ID-të, duplikatet sipas vendimit, tipet pas rileximit me schema, datat dhe diapazonet numerike të përcaktuara, mungesën e `elevation=0`, si dhe rendin e plotësinë e log-ut.

PASS do të thotë përputhje me këto rregulla, jo certifikim i saktësisë biologjike ose hapësinore të çdo regjistrimi. Mungesat e lejuara dhe ekstremet e ruajtura nuk janë dështime. Validimi nuk ndryshon dataset-in ose log-un.

Për raportin e përbashkët: diagnostikimi mbi origjinalin nuk është transformimi i checkpoint-it; IUCN këtu mbetet kategori e parenditur; zero plotësime year/month është rezultat i kontrollit. Datat e dyshuara si placeholder nuk duhen quajtur të konfirmuara pa evidencë burimore.


## 3. Integrimi, agregimi dhe mostrimi

### Integrimi

Për të normalizuar agregimet u integruan **sipërfaqja dhe popullsia e 38 komunave** nga burime zyrtare:

| Të dhëna | Burimi | Viti |
|---|---|---|
| Popullsia | ASK, Regjistrimi i Popullsisë 2024, Tab. 1.2 (me vlerësimin e ASK për 4 komunat veriore) | 2024 |
| Sipërfaqja | Matja zyrtare e territorit (Komisioni shtetëror / Agjencia Kadastrale), f. 52 | 2017 |

- **Kontrolli i totaleve:** popullsia mblidhet në **1,602,515**, dhe sipërfaqja në **10,905.25 km²**, saktësisht totalet zyrtare.
- **Mitrovicë e Jugut dhe e Veriut** kanë sipërfaqe të përbashkët (336.18 km²), sepse matja i jep bashkë.
- **Komunat veriore:** Leposaviq, Mitrovicë e Veriut, Zubin Potok dhe Zveçan e bojkotuan regjistrimin, kështu që popullsia e tyre është vlerësim i ASK. Numri i regjistruar ruhet veçmas.
- **Bashkimi:** çelësi i komunës është emri shqip pa diakritikë (`Graçanicë / Gračanica` → `gracanice`). Me left join dhe `validate="many_to_one"`: **38/38 komuna përputhen**, 46,831 rreshta para dhe pas, 0 rreshta pa përputhje. Mbi të dhënat e pastra: 38/38 dhe 46,456 rreshta.

Burimi: seksionet 5 dhe 5.2, `reports/burimet_e_te_dhenave_te_komunave.md`, `reports/bashkimi_i_komunave.md`.

### Agregimi

Agregimet finale janë mbi të dhënat e pastra (`processed/agg_*_v2.csv`). `taxon_group` dhe `is_threatened` vijnë nga funksioni `add_taxon_features()`.

**Sipas komunës** (`agg_municipality_v2.csv`):

| Treguesi | Rezultati |
|---|---|
| Më shumë regjistrime | Graçanicë: 14,563 (31.35%), 787.79 për 1,000 banorë, por vetëm 334 specie |
| Më shumë specie | Prizren 1,243, Prishtinë 1,149, Pejë 1,049 |
| Më shumë specie për km² | Junik 3.37, Ranillug 3.18 (komuna të vogla) |
| Specie të kërcënuara (VU, EN, CR) | 37 gjithsej; 28 nga 38 komuna kanë 0–3 |

`specie/km²` del më e lartë te komunat e vogla, sepse numri i specieve nuk rritet në proporcion me sipërfaqen. Matrica komunë × taxon_group (`agg_municipality_taxon_v2.csv`) është input-i i PCA-së.

**Sipas kohës** (`agg_time_v2.csv`):
- 2010–2026 kanë 86.80% të regjistrimeve me vit, me kulmin në 2020 (8,370).
- Regjistrimet dhe speciet nuk lëvizin bashkë: 2020 ka 8,370 regjistrime dhe 466 specie, kurse 2024 ka 3,730 regjistrime dhe 773 specie.
- **3,598 regjistrime të HabiProt kanë datën 30 nëntor, të dyshuar si placeholder, por jo të konfirmuar nga burimi**. Këto data nuk u ndryshuan. Në analizën e ndjeshmërisë pa to, nëntori ka 2.97% dhe kulmi sezonal është në maj (15.65%).

**Sipas specieve dhe rajonit** (`agg_class_district_v2.csv`, `agg_species_v2.csv`):
- Rajoni i Prishtinës ka 78.8% të regjistrimeve të zogjve. Likenet vijnë pothuajse vetëm nga Gjakova dhe Prizreni, nga një herbarium.
- Nga 4,095 speciet, 1,731 kanë vetëm 1 regjistrim, 2,155 janë vetëm në 1 komunë, dhe 754 nuk janë regjistruar pas vitit 2000.
- 264 regjistrime peshqish nuk kanë `class` në GBIF, kështu që dalin si "E panjohur" te `taxon_group`.

**Rikalkulimi mbi të dhënat e pastra:**
- Logjika u verifikua: mbi dataset-in origjinal jep saktësisht CSV-të v1.
- Largimi i 375 duplikatëve ul vetëm numrat e regjistrimeve (−0.80%). Nuk humbet asnjë specie, klasë, vit ose komunë.
- Ndryshimet më të mëdha janë te Graçanica (−109) dhe Kamenica (−108).

Burimi: seksionet 6, 6.2, 6.3 dhe 8; `reports/agregimi_sipas_komunes.md`, `reports/agregimi_sipas_kohes.md`, `reports/agregimi_sipas_specieve_dhe_rajonit.md`, `reports/rikalkulimi.md`.

### Mostrimi

Nga dataset-i origjinal me 46,831 rreshta u nxorrën dy mostra me **10,000 rreshta** dhe `random_state = 42`:
- **e rastësishme**;
- **e shtresëzuar sipas klasës**: shpërndarje proporcionale, dhe rreshtat pa klasë si shtresë më vete.

| Mostra | Klasa të përfaqësuara (nga 69) | Diferenca maks. sipas klasës | TVD |
|---|---:|---:|---:|
| e rastësishme | 46 | 0.222 pp | 0.703 pp |
| **e shtresëzuar** | 42 | **0.006 pp** | **0.104 pp** |

- **Mostra e shtresëzuar e ruan më mirë përbërjen sipas klasës.** Me 200 farë të ndryshme, mostra e rastësishme ka mesatarisht 0.89 pp TVD.
- Mostra e shtresëzuar lë jashtë vetëm klasat me 1–2 regjistrime. Të 35 klasat me ≥5 regjistrime janë të përfaqësuara.
- **Të dyja mostrat e përsërisin anshmërinë:** Graçanica ~31%, pika e Henc-it ~28%, eBird ~56%.
- **Të dyja ruajnë vetëm 1,909 nga 4,095 specie (46.6%)** dhe 14 nga 37 speciet e kërcënuara.

**Vendimi:**
- mostra e shtresëzuar përdoret për eksplorim dhe grafikë sipas grupit taksonomik;
- mostra e rastësishme përdoret si referencë;
- **dataset-i i plotë** përdoret për numrin e specieve, speciet e kërcënuara dhe çdo numër final.

Mostrimi nuk e korrigjon anshmërinë. Ajo trajtohet me normalizim (specie/km², regjistrime/1,000 banorë) dhe me kontrolle pa burimet dominuese. Burimi: seksionet 7–7.3, `reports/mostrimi.md`.

## 4. Vetitë, kodimi dhe transformimi

### Zgjedhja

Për nënbashkësinë analitike u dokumentua zgjedhja e 29 nga 42 kolonat origjinale dhe përjashtimi i 13. Kjo është zgjedhje analitike, jo pohim se CSV-ja e vetive ka vetëm 29 kolona: `biodiversity_features.csv` ruan të 83 kolonat e pastrimit dhe shton 45 të derivuara. Numri doli nga rëndësia, redundanca, mungesat, tipi dhe pyetjet e projektit. Nuk u caktua paraprakisht.

I vetmi çift vërtet i dyfishtë është statusi i IUCN. `iucnRedListStatus` largohet. `iucnRedListCategory` mbahet. `taxonKey` dhe `scientificName` nuk janë e njëjta gjë, prandaj të dyja mbeten. `elevation` dhe `individualCount` dalin nga nënbashkësia analitike, por detyrat e mëvonshme krijojnë veti prej tyre pa i kthyer në atë nënbashkësi dhe pa e shkruar CSV-në origjinale.

Burimi: `reports/fjalori_i_te_dhenave.md`, `reports/redundanca.md`, `reports/rendesia_e_kolonave.md`, `reports/zgjedhja_e_vetive.md`.

### Krijimi

`build_features(df, datasets)` i bashkon nëntë hapat dhe kthen tabelën; rezultati i ruajtur është te `processed/biodiversity_features.csv`: 46,456 rreshta dhe 128 kolona. 83 kolonat e pastruara qëndrojnë. Shtohen 45.

| Vetia | Burimi | Rregulli |
|---|---|---|
| `season` | `month` | dimër 12, 1, 2; pranverë 3–5; verë 6–8; vjeshtë 9–11 |
| `decade` | `year` | `(year // 10) * 10` |
| `is_recent` | `year` | `year >= 2017` |
| `taxon_group` | `class` | Zogj, Insekte, Bimë, Kërpudha, Tjera; klasa bosh = `E panjohur` |
| `is_threatened` | kodi IUCN | VU, EN, CR = 1; LC, NT = 0; NE, DD, bosh dhe EX mbeten bosh |
| `in_protected_area` | `protectedArea` | 1 kur ka emër zone; 0 kur është bosh ose «Jashtë zonës së mbrojtur» |
| `is_citizen_science` | publikuesi dhe `basisOfRecord` | 1 vetëm për publikues të shkencës qytetare dhe `HUMAN_OBSERVATION` |
| `n_issues` | `issue` | numëron 10 flamujt seriozë |

Ku mungon viti, `decade` dhe `is_recent` mbeten bosh. Ku mungon muaji, `season` mbetet bosh. Te të dhënat e pastra, grupet janë Zogj 28,532, Insekte 11,447, Bimë 3,723, Tjera 1,396, Kërpudha 970 dhe E panjohur 388. Rreshti i vetëm EX ka `is_threatened` bosh dhe `iucn_rank` 6. `is_citizen_science` është 1 për 40,984 rreshta dhe 0 për 5,472. Asnjë `datasetKey` nuk mbetet pa publikues.

Burimi: `reports/vetite_kohore.md`, `reports/vetite_taksonomike.md`, `reports/vetite_e_burimit.md`, `reports/lista_e_vetive.md`.

### Diskretizimi

Lartësia ndahet në Fushë [297, 800] m, Kodrinore (800, 1,500] m dhe Malore (1,500, 2,656] m. Këta janë kufijtë operacionalë të diskretizimit, jo një vendim i ri për fshirjen e vlerave; kufiri i poshtëm ndryshon nga referenca 270 m në raportin e pastrimit dhe mbetet kufizim për harmonizim burimor. 0 m nuk është lartësi reale e Kosovës. Te të dhënat e pastra, zeroja është bërë bosh nga pastrimi. E panjohur është 40,297, Fushë 3,711, Kodrinore 1,314 dhe Malore 1,134.

Viti origjinal ndahet në periudha: 1826–1899 (16), 1900–1949 (304), 1950–1999 (4,111), 2000–2009 (1,402), 2010–2019 (10,187) dhe 2020–2026 (28,168). 2,268 vite bosh mbeten bosh. `decade` mbetet kolonë më vete.

`individualCount` krahasoi `pd.cut` me `pd.qcut`. Gjerësia e barabartë fut pothuajse të gjitha vlerat e njohura në një grup, prandaj u përdor `pd.qcut(q=4, duplicates="drop")`; kufijtë e përsëritur japin tri kategori efektive. Te të dhënat e pastra: 1–2 = 15,815, 3–6 = 6,335, 7–10200 = 6,719, bosh = 17,587. Boshllëku nuk imputohet.

Burimi: `reports/zona_e_lartesise.md`, `reports/periudhat_kohore.md`, `reports/klasa_e_numrit.md`.

### Binarizimi

One-hot bëhet për `taxon_group`, `district` dhe `basisOfRecord`. Kategoria me më pak se 47 rreshta shkon te `Tjera`. Vetëm `OBSERVATION` u bashkua, si `basisOfRecord_Tjera`. `drop_first` është false, sepse heqja e parë alfabetike do të hiqte Bimë, Ferizajn dhe `HUMAN_OBSERVATION`. Dalin 20 kolona. Çdo rresht ka një 1 në secilin grup.

IUCN kodohet një herë nga `iucnRedListCategory`: LC=1, NT=2, VU=3, EN=4, CR=5, EX=6. NE, DD dhe boshllëku mbeten bosh, me `iucn_evaluated` 0. Te të dhënat e pastra, të vlerësuara janë 29,631 dhe të pavlerësuara 16,825. Dhjetë flamujt seriozë janë kolona 0/1. Shuma e tyre është 2,049. Flamujt informativë nuk bëhen kolona.

`kingdom` nuk merr one-hot, sepse grupi biologjik merret nga `class`. `iasUnionConcern` doli nga nënbashkësia. `strictlyProtected` mbetet bool, siç e la pastrimi.

Burimi: `reports/kolonat_dummy.md`, `reports/kodimi_iucn_dhe_flamujve.md`.

### Transformimi

`individualCount` dhe `coordinateUncertaintyInMeters` janë të anuara djathtas. Te të dhënat e pastra, `log1p` e ul skewness nga 26.63 në 2.07 dhe nga 101.73 në −1.00. Boshllëku mbetet bosh: 17,587 për numrin dhe 31,813 për pasigurinë. Shenja negative e pasigurisë pas `log1p` vjen sepse shumica e vlerave të njohura janë 7,071 m dhe bishti shkon deri në miliona metra. Vlera 7,071 mbahet.

`elevation` nuk shkallëzohet. Viti dhe koordinatat mbeten në njësinë e tyre.

Për krahasimin e komunave përdoren përpjesëtimet e `regjistrime_*`, pastaj Z-score me pjesëtues 38. Blloku `specie_*` nuk përzihet. Pas Z-score, secila nga gjashtë kolonat ka mesatare 0 dhe devijim standard 1.

Burimi: `reports/transformimi_log1p.md`, `reports/shkallezimi_pca.md`.


## 5. Reduktimi i dimensionit dhe PCA

### Reduktimi

Redundanca hoqi vetëm `iucnRedListStatus`. Varianca dhe korrelacioni u kontrolluan te 34 kolonat e one-hot, IUCN, flamujve dhe `log1p`. Pesë kolona kanë më pak se 47 njësha. I vetmi çift me korrelacion të paktën 0.80 është `flag_RECORDED_DATE_INVALID` dhe `flag_INDIVIDUAL_COUNT_INVALID`, +0.8227 te dataset-i origjinal dhe +0.8226 te i pastri. 348 rreshta i kanë të dyja, 160 vetëm datën dhe 3 vetëm numrin. Asnjë kolonë nuk u hoq. Tri grupet dummy mblidhen në 1, por asnjë çift i tyre nuk kalon 0.80.

#### PCA finale

Hyrja është matrica v2 e agregimit: 38 komuna dhe 46,456 regjistrime. `run_pca_on_clean_matrix()` përdor `standardize_pca_matrix()` dhe `run_municipality_pca()`. Komponentët me `explained_variance_` mbi 1 mbahen.

| Komponenti | explained_variance_ | explained_variance_ratio_ | Kumulative |
|---|---:|---:|---:|
| PC1 | 2.166778 | 0.351626 | 0.351626 |
| PC2 | 1.476464 | 0.239602 | 0.591228 |
| PC3 | 1.097941 | 0.178175 | 0.769403 |
| PC4 | 0.806205 | 0.130831 | 0.900234 |
| PC5 | 0.614774 | 0.099766 | 1.000000 |
| PC6 | 0.000000 | 0.000000 | 1.000000 |

Mbeten PC1, PC2 dhe PC3. Varianca kumulative është 0.769403. PC6 është 0, sepse gjashtë përpjesëtimet mblidhen në 1. Te matrica v1 kumulative ishte 0.770411 dhe po ashtu mbetën tri komponentë. Largimi i 375 duplikateve nuk e ndryshon vendimin.

| Grupi | PC1 | PC2 | PC3 |
|---|---:|---:|---:|
| Zogj | +0.657 | −0.183 | −0.125 |
| Insekte | −0.457 | +0.580 | −0.155 |
| Bimë | −0.316 | −0.540 | +0.078 |
| Kërpudha | −0.075 | +0.137 | +0.903 |
| Tjera | −0.308 | −0.548 | +0.118 |
| E panjohur | −0.398 | −0.140 | −0.352 |

PC1 peshon te zogjtë, PC2 te insektet kundrejt Tjera dhe bimëve, PC3 te kërpudhat. Graçanica është 3.201 te PC1: 14,351 nga 14,563 regjistrimet e saj janë zogj, 98.54%. Mamusha është 3.346 te PC2, sepse ka një regjistrim dhe ai është insekt. Dragashi është 3.712 te PC3.

`processed/pca_municipalities_v2.csv` ka 38 rreshta dhe kolonat `komuna`, `rajoni`, `PC1`, `PC2`, `PC3`. `processed/matrica_pca_komuna_taxon_v2.csv` ruan Z-score. Rezultati i v1 mbetet te `processed/pca_municipalities.csv` për krahasim.

Burimi: `reports/varianca_dhe_korrelacioni.md`, `reports/pca_komunat.md`, `reports/rikalkulimi.md`.

**Decision + Rationale:** Ruhet origjinali dhe checkpoint-i. Mospërputhjet e formulimit korrigjohen në raport; rezultatet historike nuk mbishkruhen për t'i paraqitur si rezultate të pastrimit.
