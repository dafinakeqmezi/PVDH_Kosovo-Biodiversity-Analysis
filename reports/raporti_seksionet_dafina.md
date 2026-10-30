# Raporti i Pjesës I – Para-procesimi: mbledhja, burimet, tipet, kualiteti, integrimi, agregimi dhe mostrimi

**Autorja:** Dafina Keqmezi  
**Data:** 29.10.2026  
**Burimi i numrave:** `notebooks/01_mbledhja_kualiteti.ipynb` dhe `notebooks/01b_analiza_burimeve.ipynb`. Kualiteti matet mbi dataset-in origjinal (46,831 rreshta). Agregimet finale janë mbi të dhënat e pastra të Delizës (46,456 rreshta, CSV-të `*_v2.csv`).

Dataset-i përmban 46,831 vëzhgime të biodiversitetit në Kosovë nga GBIF, me 42 kolona.
- **Kualiteti:** koordinatat dhe datat janë 100% të vlefshme. Problemet kryesore janë mungesat e fshehura (`NE`/`DD` te IUCN, `elevation = 0`), koordinatat e përgjithësuara në rrjetë 10 km dhe një anshmëri e fortë: një pikë e vetme dhe një vëzhgues japin përkatësisht 27.86% dhe 35.18% të regjistrimeve.
- **Integrimi:** dataset-i u bashkua me sipërfaqen dhe popullsinë zyrtare të 38 komunave pa humbur asnjë rresht.
- **Agregimi dhe mostrimi:** agregimet dhe mostrat tregojnë se numri i regjistrimeve mat përpjekjen e vëzhgimit, jo pasurinë e specieve.

---

## 1. Mbledhja e të dhënave

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

## 2. Burimet e të dhënave

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

## 3. Tipet e të dhënave

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

- Kolonat ordinale u bënë `category (ordered)`, dhe vlerat "e panjohur" (`NE`, `DD`, `UNRANKED`) u bënë NaN, sepse nuk kanë vend në shkallë.
- Numrat e plotë me mungesa u bënë `Int64`, që `2026` të mos bëhet `2026.0`.
- Konvertimi e ul memorien nga **31.9 MB në 13.6 MB**. Një `assert` kontrollon që çdo kolonë merr tipin e synuar.

Burimi: seksioni 2 i notebook-ut, `reports/tipet_e_te_dhenave.md`.

## 4. Kualiteti i të dhënave

### 4.1 Korniza

Kualiteti matet në **5 dimensione me 35 kontrolle**. Për çdo kontroll janë përcaktuar metrika, rregulli dhe kolonat:

| Dimensioni | Pyetja | Kontrolle |
|---|---|---:|
| Plotësia | A janë vlerat të pranishme? | 8 |
| Vlefshmëria | A janë brenda formatit, intervalit ose fjalorit? | 10 |
| Konsistenca | A përputhen kolonat e lidhura? | 9 |
| Unikaliteti | A paraqitet çdo vëzhgim një herë? | 5 |
| Aktualiteti | Sa të reja janë të dhënat? | 3 |

Metrika: % e rreshtave ku kontrolli aplikohet dhe që e plotësojnë. Vlefshmëria dhe konsistenca maten vetëm mbi vlerat që ekzistojnë, që një mungesë të mos numërohet dy herë. Burimi: seksioni 3.7, `reports/korniza_e_kualitetit.md`.

### 4.2 Plotësia

- **Për rresht:** **43,626 rreshta (93.16%)** i kanë të plota katër fushat kyçe (species, data, koordinata, komuna). Koordinatat dhe komuna janë 100% të plota. Mungon vetëm data te 1,992 rreshta, vetëm species te 1,015, dhe të dyja te 198.
- **Mungesat e fshehura e ulin shumë plotësinë reale:**

| Kolona | Vlera e fshehur | Plotësia e dukshme | Plotësia reale |
|---|---|---:|---:|
| `iucnRedListCategory` | `NE`, `DD` (15,722) | 97.41% | **63.84%** |
| `elevation` | `0` (3,634) | 20.97% | **13.21%** |
| `taxonRank` | `UNRANKED` (214) | 99.92% | 99.46% |

- **NaN që nuk është mungesë:** te `protectedArea`, NaN do të thotë "jashtë zonës së mbrojtur", dhe `iasAppliesFrom` vlen vetëm për 24 speciet pushtuese. 13 nga 42 kolonat janë 100% të plota.

Burimi: seksioni 3.8, `reports/plotesia.md`.

### 4.3 Vlefshmëria

| Rregulla | Rreshta që dështojnë | % |
|---|---:|---:|
| Koordinatat brenda Kosovës | 0 | 0.00 |
| Viti brenda 1758–2026; `month` 1–12; `day` 1–31; data reale | 0 | 0.00 |
| `eventDate` e lexueshme si ISO 8601 (11 formate) | 0 | 0.00 |
| Intervalet e datave ≤ 1 vit | 53 nga 447 | 11.86 |
| Pa flamurin GBIF `RECORDED_DATE_INVALID` | 508 | 1.08 |
| `coordinateUncertaintyInMeters` ≠ 7071 | 8,225 | 55.47 |
| `elevation` ≠ 0 | 3,634 | 37.01 |
| `elevation` brenda 297–2,656 m (pa 0) | 9 | 0.15 |

- **Vlera 7071 te pasiguria (8,225 regjistrime)** është ≈ 5000·√2, gjysma e diagonales së një qelize 10 × 10 km. Koordinata është qendra e qelizës, jo vendi i vëzhgimit (kryesisht HabiProt, 122 pika të ndryshme). Komuna e këtyre rreshtave mund të jetë e pasaktë.
- **Pesë ekzemplarë herbariumi në Kaçanik me 2,750–3,050 m** kanë lartësi që nuk ekziston në Kosovë.

Burimi: seksioni 3.9, `reports/vlefshmeria.md`.

### 4.4 Flamujt e GBIF

Kolona `issue` ka **35 flamuj**. Ata u klasifikuan sipas efektit në kolonat e analizës, jo sipas shpeshtësisë:
- **10 flamuj seriozë:** vlera mungon, u zëvendësua ose është e pasigurt. P.sh. `TAXON_MATCH_HIGHERRANK` (756 rreshta; te 702 prej tyre species mungon), `RECORDED_DATE_INVALID` (508), `INDIVIDUAL_COUNT_INVALID` (351), `BASIS_OF_RECORD_INVALID` (120 → `OCCURRENCE`).
- **25 flamuj informativë:** GBIF plotësoi ose standardizoi një vlerë, ose flamuri prek një fushë që nuk përdoret. P.sh. `CONTINENT_DERIVED_FROM_COORDINATES` (95.50%), `COORDINATE_ROUNDED` (31.91%).

96.96% e rreshtave kanë të paktën një flamur, por vetëm **1,645 rreshta (3.51%) kanë flamur serioz**. Burimi: seksioni 3.5, `reports/flamujt_gbif.md`.

### 4.5 Unikaliteti

- `gbifID` është unik, dhe nuk ka rreshta identikë.
- Me kriterin species + data + koordinata + vëzhgues ka **1,288 grupe dhe 1,844 rreshta të tepërta**. Shqyrtimi manual i 18 grupeve tregoi se shumica nuk janë i njëjti vëzhgim: janë ekzemplarë me `catalogNumber` të ndryshëm, pika të rrjetës 10 km, ose numërime të ndara të së njëjtës ditë.
- **Definicioni i propozuar:** duplikat janë rreshtat nga dataset-e të ndryshme, ose nga i njëjti dataset me `individualCount` të njëjtë, pa ekzemplarë të ndryshëm dhe pa koordinata 7071 m. Ai jep **238 grupe dhe 378 rreshta të tepërta**.
- Deliza pranoi 235 nga këto grupe dhe largoi **375 rreshta**.

Burimi: seksioni 3.10, `reports/unikaliteti.md`, `processed/duplicate_candidates.csv`.

### 4.6 Konsistenca dhe anshmëria

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

## 5. Integrimi

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

## 6. Agregimi

Agregimet finale janë mbi të dhënat e pastra (`processed/agg_*_v2.csv`). `taxon_group` dhe `is_threatened` vijnë nga funksioni i Jetës (`add_taxon_features()`).

**Sipas komunës** (`agg_municipality_v2.csv`):

| Treguesi | Rezultati |
|---|---|
| Më shumë regjistrime | Graçanicë: 14,563 (31.35%), 787.79 për 1,000 banorë, por vetëm 334 specie |
| Më shumë specie | Prizren 1,243, Prishtinë 1,149, Pejë 1,049 |
| Më shumë specie për km² | Junik 3.37, Ranillug 3.18 (komuna të vogla) |
| Specie të kërcënuara (VU, EN, CR) | 37 gjithsej; 28 nga 38 komuna kanë 0–3 |

`specie/km²` del më e lartë te komunat e vogla, sepse numri i specieve nuk rritet në proporcion me sipërfaqen. Matrica komunë × taxon_group (`agg_municipality_taxon_v2.csv`) është input-i i PCA-së së Jetës.

**Sipas kohës** (`agg_time_v2.csv`):
- 2010–2026 kanë 86.80% të regjistrimeve me vit, me kulmin në 2020 (8,370).
- Regjistrimet dhe speciet nuk lëvizin bashkë: 2020 ka 8,370 regjistrime dhe 466 specie, kurse 2024 ka 3,730 regjistrime dhe 773 specie.
- **3,598 regjistrime të HabiProt kanë datën zëvendësuese 30 nëntor** (insekte nga atlase të botuara). Pa to, nëntori ka 2.97% dhe kulmi sezonal është në maj (15.65%).

**Sipas specieve dhe rajonit** (`agg_class_district_v2.csv`, `agg_species_v2.csv`):
- Rajoni i Prishtinës ka 78.8% të regjistrimeve të zogjve. Likenet vijnë pothuajse vetëm nga Gjakova dhe Prizreni, nga një herbarium.
- Nga 4,095 speciet, 1,731 kanë vetëm 1 regjistrim, 2,155 janë vetëm në 1 komunë, dhe 754 nuk janë regjistruar pas vitit 2000.
- 264 regjistrime peshqish nuk kanë `class` në GBIF, kështu që dalin si "E panjohur" te `taxon_group`.

**Rikalkulimi mbi të dhënat e pastra:**
- Logjika u verifikua: mbi dataset-in origjinal jep saktësisht CSV-të v1.
- Largimi i 375 duplikatëve ul vetëm numrat e regjistrimeve (−0.80%). Nuk humbet asnjë specie, klasë, vit ose komunë.
- Ndryshimet më të mëdha janë te Graçanica (−109) dhe Kamenica (−108).

Burimi: seksionet 6, 6.2, 6.3 dhe 8; `reports/agregimi_sipas_komunes.md`, `reports/agregimi_sipas_kohes.md`, `reports/agregimi_sipas_specieve_dhe_rajonit.md`, `reports/rikalkulimi.md`.

## 7. Mostrimi

U nxorrën dy mostra me **10,000 rreshta** dhe `random_state = 42`:
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

---

## Pyetje të hapura

- **Data e saktë e shkarkimit nga GBIF dhe DOI-ja e shkarkimit** nuk janë ende në repo (README: TODO). Regjistrimi më i ri është i 22.08.2026, dhe skedari është i datës 05.10.2026. Pa DOI-n, citimi i GBIF-it nuk është i plotë.
- Mostrat e seksionit 7 janë nxjerrë nga dataset-i origjinal dhe mund të përmbajnë disa nga 375 duplikatët. Nëse përdoren te Pjesa II, duhen rinxjerrë mbi `biodiversity_clean.csv`.
