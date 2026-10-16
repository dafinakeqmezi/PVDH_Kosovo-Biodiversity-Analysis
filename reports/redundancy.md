# Kandidatët për redundancë

**Autor:** Jeta Syla  
**Versioni:** 1.0  
**Data:** 16.10.2026  
**Statusi:** Vendimi për gjashtë çiftet e kolonave.

## Varësia

Ky task varet nga **Fjalori i të dhënave** i përfunduar më 16.10.2026: `reports/data_dictionary.md`, versioni 1.0. Kuptimi semantik i secilës kolonë merret prej atij fjalori. Numri i vlerave unike dhe përputhja 1:1 llogariten te `dataset/kosovo_overall_biodiversity.csv`.

## Qëllimi

Qëllimi i këtij krahasimi është të vendosë, për secilin çift, cila kolonë ruhet dhe cila hiqet. Krahasimi mbështetet te numri i vlerave unike, përqindja e përputhjes 1:1 dhe kuptimi semantik i shkruar sot te fjalori.

Përputhja 1:1 llogaritet vetëm te rreshtat ku të dyja kolonat janë të plota. Një vlerë është 1:1 kur i përgjigjet saktësisht një vlere të kolonës tjetër. Rreshti është 1:1 kur kjo vlen në të dyja anët.

**Input:** `dataset/kosovo_overall_biodiversity.csv`, 46,831 rreshta dhe 42 kolona.

## Tabela e redundancës

| Çifti | Vlera unike | Kolona A → një vlerë B | Kolona B → një vlerë A | Rreshta 1:1 | Vendimi |
|---|---:|---:|---:|---:|---|
| `iucnRedListCategory` / `iucnRedListStatus` | 8 / 8 | 8/8 (100%) | 8/8 (100%) | 45,618/45,618 (100%) | **Ruaj** `iucnRedListCategory`. **Hiq** `iucnRedListStatus`. |
| `taxonKey` / `speciesKey` | 4,647 / 4,097 | 4,337/4,337 (100%) | 3,885/4,097 (94.8%) | 37,255/45,618 (81.7%) | **Ruaj të dyja.** |
| `scientificName` / `species` | 4,647 / 4,095 | 4,337/4,337 (100%) | 3,882/4,095 (94.8%) | 37,252/45,618 (81.7%) | **Ruaj të dyja.** |
| `protectedArea` / `protectedAreaDesignation` | 20 / 5 | 20/20 (100%) | 2/5 (40%) | 13,644/21,069 (64.8%) | **Ruaj të dyja.** |
| `municipality` / `district` | 38 / 7 | 38/38 (100%) | 0/7 (0%) | 0/46,831 (0%) | **Ruaj të dyja.** |
| `datasetKey` / `institutionCode` | 125 / 108 | 87/93 (93.5%) | 98/108 (90.7%) | 33,726/43,120 (78.2%) | **Ruaj të dyja.** |

Te `datasetKey` / `institutionCode`, 93 është numri i dataset-eve që kanë `institutionCode`. 32 dataset-e nuk e kanë këtë kod.

## Vendimi dhe arsyetimi

### `iucnRedListCategory` / `iucnRedListStatus`

**Ruhet** `iucnRedListCategory`. **Hiqet** `iucnRedListStatus`.

Të dyja mungojnë në të njëjtat 1,213 rreshta (2.6%). Te 45,618 rreshtat e plotë, secili kod ka saktësisht një emër dhe secili emër ka saktësisht një kod:

| `iucnRedListCategory` | `iucnRedListStatus` |
|---|---|
| `LC` | Least Concern |
| `NT` | Near Threatened |
| `VU` | Vulnerable |
| `EN` | Endangered |
| `CR` | Critically Endangered |
| `EX` | Extinct |
| `DD` | Data Deficient |
| `NE` | Not Evaluated |

Fjalori i të dhënave e përshkruan `iucnRedListCategory` si kategorinë e Listës së Kuqe të IUCN dhe `iucnRedListStatus` si të njëjtin status të shkruar me fjalë. Teksti i njëjtë është 0%, sepse njëra kolonë është kod dhe tjetra është emër, por informacioni është i njëjtë. Kodi është vlera standarde dhe emri rindërtohet prej tij.

### `taxonKey` / `speciesKey`

**Ruhen të dyja.** Asnjëra nuk hiqet.

`taxonKey` është çelësi i taksonit më të saktë në GBIF Backbone dhe mund të jetë sinonim. `speciesKey` është çelësi i species për atë vëzhgim. Nga 45,618 rreshta ku të dyja janë të plota, çelësat janë të barabartë në 43,214 rreshta (94.7%) dhe ndryshojnë në 2,404. Ndryshimi ndodh te nënllojet, format, varietetet dhe te species ku `taxonKey` nuk është i njëjtë me species e pranuar. `speciesKey` mungon në 1,176 rreshta ku `taxonKey` ekziston, sepse identifikimi është mbi species. Heqja e `taxonKey` e humb rangun më të saktë. Heqja e `speciesKey` e humb lidhjen e përbashkët të vëzhgimeve që i përkasin të njëjtës species.

### `scientificName` / `species`

**Ruhen të dyja.** Asnjëra nuk hiqet.

`scientificName` është emri shkencor me autorësi, i rangut më të ulët që mund të përcaktohet. Shembull: `Mantis religiosa (Linne, 1758)`. `species` nuk është term i Darwin Core. Në këtë dataset është emri i species pa autorësi, `Mantis religiosa`. Teksti është i njëjtë vetëm në 1 rresht. Emri i species gjendet brenda `scientificName` në 43,934 nga 45,618 rreshta (96.3%), por kjo nuk i bën kolonat të njëjta: autorësia mungon te `species`, dhe 1,176 rreshta kanë `scientificName` pa `species` sepse rangu është gjini, familje ose më lart. `scientificName` ka 4,647 vlera, `species` ka 4,095. Heqja e njërës e humb ose autorësinë, ose emrin e pastër që përdoret për grupim.

### `protectedArea` / `protectedAreaDesignation`

**Ruhen të dyja.** Asnjëra nuk hiqet.

`protectedArea` është emri i zonës së mbrojtur, për shembull `Parku Kombëtar "Sharri"`. `protectedAreaDesignation` është lloji i asaj zone, për shembull `National Park`. Të dyja mungojnë në të njëjtat 25,762 rreshta (55.0%), sepse pika nuk bie në zonë të mbrojtur. Te 21,069 rreshtat e plotë ka 20 emra zonesh dhe 5 lloje. Çdo zonë ka një lloj, por një lloj përmban shumë zona:

| `protectedAreaDesignation` | Zona të ndryshme |
|---|---:|
| Natural Monument | 11 |
| Protected Landscape | 5 |
| National Park | 2 |
| Nature Park | 1 |
| Wetlands | 1 |

Vetëm 2 nga 5 llojet i përgjigjen një zone të vetme. Emri i zonës nuk zëvendëson llojin, as lloji nuk zëvendëson emrin.

### `municipality` / `district`

**Ruhen të dyja.** Asnjëra nuk hiqet.

`municipality` është komuna, njësia administrative më e vogël. Në këtë dataset ka 38 komuna dhe asnjë vlerë boshe. `district` nuk është term i Darwin Core. Në këtë dataset është njëri nga 7 rajonet e Kosovës dhe asnjë vlerë boshe. Çdo komunë bie në saktësisht një rajon, por asnjë rajon nuk ka vetëm një komunë, prandaj përputhja 1:1 e rreshtave është 0%. Emri është i njëjtë në 13,492 rreshta (28.8%), vetëm aty ku komuna e ka të njëjtin emër me rajonin.

| `district` | Komuna |
|---|---:|
| Prishtinë / Priština | 8 |
| Mitrovicë / Kosovska Mitrovica | 7 |
| Gjilan / Gnjilane | 6 |
| Ferizaj / Uroševac | 5 |
| Prizren | 5 |
| Gjakovë / Đakovica | 4 |
| Pejë / Peć | 3 |

Komuna tregon vendin më të saktë. Rajoni lejon përmbledhjen e disa komunave. Heqja e njërës e humb ose detajin, ose grupin.

### `datasetKey` / `institutionCode`

**Ruhen të dyja.** Asnjëra nuk hiqet.

`datasetKey` është UUID e datasetit të GBIF që e përmban vëzhgimin. Ka 125 vlera dhe asnjë boshllëk. `institutionCode` është emri ose shkurtesa e institucionit kujdestar, për shembull `iNaturalist`. Ka 108 vlera dhe mungon në 3,711 rreshta. Te 43,120 rreshtat ku të dyja janë të plota, 87 nga 93 dataset-e kanë një institucion të vetëm, kurse 6 dataset-e kanë më shumë se një kod. 98 nga 108 institucionet kanë një dataset të vetëm. 10 institucione kanë më shumë se një dataset. `MES` dhe `ZFMK` kanë nga 4. Dataseti dhe institucioni nuk janë i njëjti identifikues.

## Përfundimi

Nga gjashtë çiftet, vetëm `iucnRedListStatus` është redundant dhe hiqet. Pesë çiftet e tjera nuk janë 1:1. Secila kolonë ruan një kuptim që tjetra nuk e zëvendëson, prandaj ruhen të dyja.

## Dokumentimi i detyrës

- **Varësia:** `reports/data_dictionary.md`, 16.10.2026.
- **Input:** `dataset/kosovo_overall_biodiversity.csv` dhe fjalori i varësisë.
- **Çka u bë:** Për gjashtë çiftet u krahasuan vlerat unike, përputhja 1:1 dhe kuptimi semantik, pastaj u vendos cila kolonë ruhet dhe cila hiqet.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 / 42. Asnjë kolonë nuk u fshi nga CSV-ja. Vendimi është për përdorimin në analizë.
- **Pse u bë:** Për të mos hequr kolona që duken të ngjashme, por nuk përmbajnë të njëjtin informacion.
- **Output:** `reports/redundancy.md`.
- **Commit:** `Add redundancy decisions for six column pairs`.
