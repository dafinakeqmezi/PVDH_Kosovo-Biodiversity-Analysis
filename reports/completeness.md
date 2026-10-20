# Plotësia e të dhënave

**Versioni:** 1.0  
**Data:** 20.10.2026  
**Statusi:** Plotësia për kolonë dhe për rresht.

## Varësia

Ky task zbaton dimensionin **Plotësia** nga **Korniza e kualitetit** (`reports/quality_framework.md`, kontrollet P1–P8). Llogaritja është te seksioni 3.8 i `notebooks/01_mbledhja_kualiteti.ipynb`, dhe rezultatet ruhen në `reports/01_plotesia_kolona.csv` dhe `reports/01_plotesia_rreshta.csv`.

## Si matet

- **Plotësia e dukshme** = % e qelizave jo-NaN, ashtu siç e tregon `df.isna()`.
- **Mungesat e fshehura** janë vlera që duken të plota, por nënkuptojnë "e panjohur":

| Kolona | Vlera e fshehur | Pse është mungesë |
|---|---|---|
| `elevation` | `0` | Lartësia më e ulët në Kosovë është 297 m; 0 përdoret si "e panjohur". |
| `iucnRedListCategory` | `NE`, `DD` | Not Evaluated / Data Deficient: specia nuk ka status rreziku. |
| `iucnRedListStatus` | `Not Evaluated`, `Data Deficient` | E njëjta gjë me fjalë. |
| `taxonRank` | `UNRANKED` | Rangu nuk dihet. |
| `locality` | `unknown` | Tekst në vend të mungesës. |
| `recordedBy` | `unknown` | Tekst në vend të mungesës. |
| `identifiedBy` | `0`, `Anon.`, `unknown` | Tekst ose numër në vend të emrit. |

- **NaN që nuk është mungesë:** te `protectedArea` dhe `protectedAreaDesignation`, NaN do të thotë "jashtë zonës së mbrojtur". `iasAppliesFrom` vlen vetëm për 24 rreshtat me `iasUnionConcern = TRUE`, dhe aty është e plotë.
- **Plotësia reale** = (rreshta ku kolona aplikohet − NaN − mungesa të fshehura) / rreshta ku aplikohet × 100.
- **Të rikuperueshme:** mungesa te `year`/`month`/`day` që mund të plotësohen nga `eventDate`, sipas precizionit të datës.

## Tabela e plotësisë për kolonë

Renditur nga plotësia reale më e ulët.

| Kolona | Plotësia e dukshme % | NaN | Mungesa të fshehura | Mungesa reale | Plotësia reale % | Shënim |
|---|---:|---:|---|---:|---:|---|
| `establishmentMeans` | 0.51 | 46,591 | – | 46,591 | **0.51** |  |
| `elevation` | 20.97 | 37,011 | 3,634 (`0 m`) | 40,645 | **13.21** |  |
| `identifiedBy` | 16.52 | 39,096 | 15 (`0, Anon., unknown`) | 39,111 | **16.48** |  |
| `coordinateUncertaintyInMeters` | 31.66 | 32,004 | – | 32,004 | **31.66** |  |
| `individualCount` | 62.21 | 17,697 | – | 17,697 | **62.21** |  |
| `iucnRedListCategory` | 97.41 | 1,213 | 15,722 (`NE, DD`) | 16,935 | **63.84** |  |
| `iucnRedListStatus` | 97.41 | 1,213 | 15,722 (`Not Evaluated, Data Deficient`) | 16,935 | **63.84** |  |
| `locality` | 67.43 | 15,251 | 38 (`unknown`) | 15,289 | **67.35** |  |
| `collectionCode` | 71.24 | 13,469 | – | 13,469 | **71.24** |  |
| `catalogNumber` | 73.18 | 12,559 | – | 12,559 | **73.18** |  |
| `vernacularName` | 91.73 | 3,873 | – | 3,873 | **91.73** |  |
| `recordedBy` | 91.77 | 3,853 | 1 (`unknown`) | 3,854 | **91.77** |  |
| `institutionCode` | 92.08 | 3,711 | – | 3,711 | **92.08** |  |
| `day` | 93.13 | 3,219 | – | 3,219 | **93.13** | 401 plotësohen nga `eventDate` |
| `month` | 93.88 | 2,867 | – | 2,867 | **93.88** | 222 plotësohen nga `eventDate` |
| `year` | 95.16 | 2,268 | – | 2,268 | **95.16** | 78 plotësohen nga `eventDate` |
| `eventDate` | 95.32 | 2,190 | – | 2,190 | **95.32** |  |
| `issue` | 96.96 | 1,426 | – | 1,426 | **96.96** |  |
| `species` | 97.41 | 1,213 | – | 1,213 | **97.41** |  |
| `speciesKey` | 97.41 | 1,213 | – | 1,213 | **97.41** |  |
| `class` | 99.17 | 388 | – | 388 | **99.17** |  |
| `order` | 99.29 | 334 | – | 334 | **99.29** |  |
| `taxonRank` | 99.92 | 37 | 214 (`UNRANKED`) | 251 | **99.46** |  |
| `genus` | 99.58 | 195 | – | 195 | **99.58** |  |
| `family` | 99.66 | 158 | – | 158 | **99.66** |  |
| `phylum` | 99.85 | 69 | – | 69 | **99.85** |  |
| `scientificName` | 99.92 | 37 | – | 37 | **99.92** |  |
| `kingdom` | 99.92 | 37 | – | 37 | **99.92** |  |
| `taxonKey` | 99.92 | 37 | – | 37 | **99.92** |  |
| `iasAppliesFrom` | 0.05 | 46,807 | – | 0 | **100.00** | vlen vetëm kur iasUnionConcern = TRUE (24 rreshta) |
| `protectedArea` | 44.99 | 25,762 | – | 0 | **100.00** | NaN = jashtë zonës së mbrojtur |
| `protectedAreaDesignation` | 44.99 | 25,762 | – | 0 | **100.00** | NaN = jashtë zonës së mbrojtur |
| `gbifID` | 100.00 | 0 | – | 0 | **100.00** |  |
| `decimalLatitude` | 100.00 | 0 | – | 0 | **100.00** |  |
| `decimalLongitude` | 100.00 | 0 | – | 0 | **100.00** |  |
| `municipality` | 100.00 | 0 | – | 0 | **100.00** |  |
| `district` | 100.00 | 0 | – | 0 | **100.00** |  |
| `strictlyProtected` | 100.00 | 0 | – | 0 | **100.00** |  |
| `basisOfRecord` | 100.00 | 0 | – | 0 | **100.00** |  |
| `datasetKey` | 100.00 | 0 | – | 0 | **100.00** |  |
| `license` | 100.00 | 0 | – | 0 | **100.00** |  |
| `iasUnionConcern` | 100.00 | 0 | – | 0 | **100.00** |  |

## Tabela e plotësisë për rresht

Fushat kyçe janë **species**, **data** (`eventDate`), **koordinata** (`decimalLatitude` + `decimalLongitude`) dhe **komuna** (`municipality`).

| Grupi | Kategoria | Rreshta | % |
|---|---|---:|---:|
| **rreshta të plotë** | të 4 fushat kyçe të plota | 43,626 | 93.16 |
|  | të paktën një fushë kyçe mungon | 3,205 | 6.84 |
| **fusha kyçe e plotë** | species | 45,618 | 97.41 |
|  | data (eventDate) | 44,641 | 95.32 |
|  | koordinata (lat + lon) | 46,831 | 100.00 |
|  | komuna (municipality) | 46,831 | 100.00 |
| **numri i fushave që mungojnë** | 0 fusha kyçe mungojnë | 43,626 | 93.16 |
|  | 1 fushë kyçe mungon | 3,007 | 6.42 |
|  | 2 fusha kyçe mungojnë | 198 | 0.42 |
| **çfarë mungon** | mungon: data | 1,992 | 4.25 |
|  | mungon: species | 1,015 | 2.17 |
|  | mungon: species + data | 198 | 0.42 |
| **plotësia e të 42 kolonave** | < 50% | 22 | 0.05 |
|  | 50–75% | 3,356 | 7.17 |
|  | 75–90% | 18,998 | 40.57 |
|  | 90–100% | 24,455 | 52.22 |
|  | 100% | 0 | 0.00 |

Plotësia e të 42 kolonave për rresht llogaritet me mungesat e fshehura dhe pa kolonat ku NaN nuk është mungesë. Plotësia mesatare e një rreshti është **85.49%**, mediana **90.24%**.

## Gjetjet kryesore

- **43,626 rreshta (93.16%) i kanë të plota të 4 fushat kyçe.** Koordinatat dhe komuna janë 100% të plota. Mungesat vijnë vetëm nga data dhe species: mungon vetëm data te 1,992 rreshta, vetëm species te 1,015, dhe të dyja te 198.
- **Mungesat e fshehura e ulin shumë plotësinë te dy kolona.** IUCN duket 97.41% e plotë, por realisht është 63.84%, sepse 15,722 rreshta janë `NE`/`DD`. Te `elevation` plotësia bie nga 20.97% në 13.21% për shkak të 3,634 vlerave 0.
- **Te 9 kolona plotësia reale ndryshon nga ajo e dukshme.** Te 6 prej tyre bie (mungesa të fshehura). Te 3 rritet në 100%, sepse NaN-i i `protectedArea`, `protectedAreaDesignation` dhe `iasAppliesFrom` nuk është mungesë.
- **13 nga 42 kolonat janë 100% të plota.** Tri kolona janë nën 20%: `establishmentMeans` 0.51%, `elevation` 13.21%, `identifiedBy` 16.48%.
- **701 mungesa te data mund të plotësohen nga `eventDate`:** 78 te `year`, 222 te `month`, 401 te `day`.
- **Asnjë rresht nuk është 100% i plotë** në të 42 kolonat. Më shumë se gjysma e rreshtave (52.22%) janë 90–100% të plotë.

## Vendimi dhe arsyetimi

- **Mungesat e fshehura numërohen si mungesa.** Përndryshe plotësia e IUCN dhe e lartësisë do të dukej shumë më e mirë se ç'është, dhe analiza e rrezikshmërisë do të numëronte `NE` si status.
- **NaN-i strukturor nuk numërohet si mungesë.** Te `protectedArea`, NaN është informacion ("jashtë zonës"). Do të plotësohet me "Jashtë zonës së mbrojtur" te pastrimi, jo të fshihet.
- **Fushat kyçe janë species, data, koordinata dhe komuna**, sepse pa to nuk përgjigjen pyetjet kryesore: çka, kur dhe ku. Analiza kryesore do të bëhet me 43,626 rreshtat e plotë, ndërsa rreshtat pa datë mbeten për analizat hapësinore dhe taksonomike.
- **Llogaritja nuk e ndryshon datasetin.** Zëvendësimi i vlerave të fshehura me NaN dhe plotësimi nga `eventDate` bëhen te `02_pastrimi.ipynb`.

## Dokumentimi i detyrës

- **Input:** `dataset/kosovo_overall_biodiversity.csv`, `reports/quality_framework.md`.
- **Çka u bë:** U llogarit plotësia e dukshme dhe reale për secilën nga 42 kolonat, me mungesat e fshehura, dhe plotësia për rresht për fushat kyçe species, data, koordinata dhe komuna.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 / 42.
- **Pse u bë:** Për të ditur sa të dhëna janë realisht të përdorshme për secilën pyetje dhe për të vendosur strategjinë e trajtimit të mungesave.
- **Output:** `reports/completeness.md`, `reports/01_plotesia_kolona.csv`, `reports/01_plotesia_rreshta.csv`, seksioni 3.8 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Add completeness per column and per row`.
