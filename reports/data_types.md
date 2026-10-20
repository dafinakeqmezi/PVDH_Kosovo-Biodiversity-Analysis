# Definimi i tipeve të të dhënave

**Versioni:** 1.0  
**Data:** 19.10.2026  
**Statusi:** Tipet për 42 kolonat.

## Varësia

Ky task varet nga **Fjalori i të dhënave** (`reports/data_dictionary.md`) për kuptimin e kolonave dhe nga **Kandidatët për redundancë** (`reports/redundancy.md`) për kolonat që do të hiqen. Konvertimi bëhet te seksioni 2 i `notebooks/01_mbledhja_kualiteti.ipynb`, dhe rezultati ruhet në `reports/01_tipet_e_kolonave.csv`.

## Qëllimi

Për secilën kolonë përcaktohen tri gjëra:

- **Tipi në pandas:** si e lexon `pd.read_csv` kolonën (pandas 3.0.1; teksti lexohet si `str`, ndërsa në pandas 2 si `object`).
- **Tipi konceptual:** çfarë përfaqëson vlera dhe cilat veprime kanë kuptim mbi të.
- **Tipi i synuar:** tipi në pandas pas konvertimit.

## Tipet konceptuale

| Tipi | Kuptimi | Veprime me kuptim |
|---|---|---|
| **ID** | Identifikues; vlera nuk ka kuptim numerik | barazi, bashkim (merge) |
| **nominal** | Kategori pa renditje | barazi, numërim, modë |
| **ordinal** | Kategori me renditje, por pa distancë të barabartë | + krahasim (<, >), mediana |
| **interval** | Numerik; diferencat kanë kuptim, zero është arbitrare | + mbledhje/zbritje, mesatare |
| **ratio** | Numerik me zero absolute (0 = mungesë) | + raporte ("dyfish") |
| **binar** | Dy vlera: TRUE/FALSE | numërim, përqindje |
| **datë** | Pikë në kohë | renditje, diferenca kohore |
| **tekst** | Tekst i lirë ose listë vlerash | kërkim, ndarje (split) |

## Tabela e tipeve

| Kolona | Tipi në pandas | Tipi konceptual | Tipi i synuar | Arsyeja |
|---|---|---|---|---|
| `gbifID` | `int64` | ID | `int64` | Unik për çdo rresht dhe pa mungesa; mbetet numër i plotë. |
| `scientificName` | `str` | nominal | `category` | 4,647 vlera që përsëriten; `category` kursen memorie. |
| `species` | `str` | nominal | `category` | 4,095 vlera; grupimi kryesor biologjik. |
| `vernacularName` | `str` | nominal | `category` | Emër i zakonshëm i taksonit; 3,314 vlera që përsëriten. |
| `kingdom` | `str` | nominal | `category` | 7 kategori. |
| `phylum` | `str` | nominal | `category` | 25 kategori. |
| `class` | `str` | nominal | `category` | 68 kategori. |
| `order` | `str` | nominal | `category` | 226 kategori. |
| `family` | `str` | nominal | `category` | 683 kategori. |
| `genus` | `str` | nominal | `category` | 2,421 kategori. |
| `taxonRank` | `str` | ordinal | `category (ordered)` | Rangjet kanë renditje: KINGDOM < PHYLUM < CLASS < ORDER < FAMILY < GENUS < SPECIES < SUBSPECIES < VARIETY < FORM. `UNRANKED` (214) nuk ka vend në renditje dhe bëhet NaN. |
| `taxonKey` | `float64` | ID | `Int64` | Çelës numerik; lexohet `float64` vetëm për shkak të 37 mungesave. `Int64` e ruan si numër të plotë me NaN. |
| `speciesKey` | `float64` | ID | `Int64` | Njësoj si `taxonKey` (1,213 mungesa). |
| `iucnRedListCategory` | `str` | ordinal | `category (ordered)` | LC < NT < VU < EN < CR < EW < EX. `NE` (15,705) dhe `DD` (17) nuk janë shkallë rreziku dhe bëhen NaN. |
| `iucnRedListStatus` | `str` | ordinal | `category (ordered)` | E njëjta shkallë me fjalë. Sipas `redundancy.md` hiqet në fazën e pastrimit. |
| `eventDate` | `str` | datë | `datetime64` | 11 formate ISO 8601. Te 447 intervalet merret data e fillimit; precizioni ruhet te `eventDatePrecision` (seksioni 3.3). |
| `year` | `float64` | interval | `Int64` | Viti nuk ka zero absolute; numër i plotë me mungesa. |
| `month` | `float64` | ordinal | `Int64` | 12 muaj të renditur (ciklik). Mbetet numër për krijimin e `season`. |
| `day` | `float64` | ordinal | `Int64` | Dita e muajit; numër i plotë me mungesa. |
| `decimalLatitude` | `float64` | interval | `float64` | Gradë; 0° (ekuatori) është referencë arbitrare. |
| `decimalLongitude` | `float64` | interval | `float64` | Gradë; 0° (Greenwich) është referencë arbitrare. |
| `coordinateUncertaintyInMeters` | `float64` | ratio | `float64` | Distancë në metra; 0 do të thotë pa pasiguri. Mbetet `float64` për `log1p` dhe shkallëzim më vonë. |
| `elevation` | `float64` | interval | `float64` | 0 m është niveli i detit, jo mungesë lartësie. Vlerat 0 (3,634) trajtohen si mungesë te pastrimi, jo këtu. |
| `locality` | `str` | tekst | `str` | Përshkrim i lirë në shumë gjuhë; 1,448 vlera pa strukturë. |
| `municipality` | `str` | nominal | `category` | 38 komuna (emra dygjuhësh). |
| `district` | `str` | nominal | `category` | 7 rajone. |
| `protectedArea` | `str` | nominal | `category` | 20 zona; NaN = jashtë zonës së mbrojtur. |
| `protectedAreaDesignation` | `str` | nominal | `category` | 5 lloje zonash. |
| `strictlyProtected` | `bool` | binar | `bool` | TRUE/FALSE pa mungesa; lexohet drejt si `bool`. |
| `basisOfRecord` | `str` | nominal | `category` | 7 kategori. |
| `individualCount` | `float64` | ratio | `Int64` | Numër individësh: zero absolute dhe vetëm numra të plotë. |
| `establishmentMeans` | `str` | nominal | `category` | 2 vlera (native/introduced). Mungon 99.5%, prandaj hiqet sipas planit. |
| `recordedBy` | `str` | tekst | `str` | Emra njerëzish, ndonjëherë disa të ndarë me `;`. |
| `identifiedBy` | `str` | tekst | `str` | Njësoj si `recordedBy`; mungon 83.5% dhe hiqet sipas planit. |
| `institutionCode` | `str` | nominal | `category` | 108 kode institucionesh. |
| `collectionCode` | `str` | nominal | `category` | 88 kode koleksionesh. |
| `catalogNumber` | `str` | ID | `str` | Vetëm 14.8% e vlerave janë numra; 34,021 vlera unike, prandaj `category` nuk kursen memorie. |
| `datasetKey` | `str` | ID | `category` | UUID, por vetëm 125 vlera që përsëriten; `category` kursen memorie dhe përdoret për grupim. |
| `license` | `str` | nominal | `category` | 3 licenca. |
| `issue` | `str` | tekst | `str` | Listë flamujsh të ndarë me `;`. Do të ndahet në flamuj binarë, jo si një kategori. |
| `iasUnionConcern` | `bool` | binar | `bool` | TRUE/FALSE pa mungesa. |
| `iasAppliesFrom` | `str` | datë | `datetime64` | 3 data. Mungon 99.9%, prandaj hiqet sipas planit. |

## Përmbledhje

| Tipi konceptual | Kolona |
|---|---:|
| nominal | 18 |
| ID | 5 |
| ordinal | 5 |
| interval | 4 |
| tekst | 4 |
| ratio | 2 |
| binar | 2 |
| datë | 2 |
| **Totali** | **42** |

Pas konvertimit, memoria bie nga **31.9 MB** në **13.6 MB**.

## Vendimi dhe arsyetimi

- **Kategoritë nominale → `category`.** Edhe kolonat me shumë vlera (`scientificName`, `species`, `genus`) përsëriten shumë herë në 46,831 rreshta, kështu që `category` zë më pak memorie dhe e shpejton grupimin.
- **Kolonat ordinale → `category (ordered)`.** Kështu funksionojnë krahasimet, p.sh. `iucnRedListCategory >= "VU"` për `isThreatened`, dhe renditja në grafikë është e saktë.
- **Vlerat "e panjohur" → NaN.** `NE`, `DD`, `Not Evaluated`, `Data Deficient` dhe `UNRANKED` nuk janë nivele të shkallës. Nëse do të mbeteshin, do ta prishnin renditjen. Konvertimi shton 15,722 NaN te secila kolonë IUCN dhe 214 te `taxonRank`.
- **Numrat e plotë me mungesa → `Int64`.** `float64` e bën `2026` në `2026.0`. `Int64` e ruan numrin e plotë dhe NaN njëkohësisht.
- **Matjet e vazhdueshme mbeten `float64`.** Koordinatat, `elevation` dhe `coordinateUncertaintyInMeters` do të transformohen (`log1p`, `RobustScaler`), dhe këto japin vlera me presje.
- **Teksti i lirë dhe ID-të jo numerike mbeten `str`.** Ato nuk janë kategori analitike, dhe `category` me pothuajse aq kategori sa rreshta nuk kursen asgjë.
- **Konvertimi nuk heq kolona.** Kolonat që do të hiqen (`iucnRedListStatus`, `establishmentMeans`, `identifiedBy`, `iasAppliesFrom`) marrin gjithashtu tipin e duhur, që dataseti i konvertuar të mbetet i plotë deri te hapi i pastrimit.

## Dokumentimi i detyrës

- **Input:** `dataset/kosovo_overall_biodiversity.csv`, `reports/data_dictionary.md`, `reports/redundancy.md`.
- **Çka u bë:** Për secilën nga 42 kolonat u përcaktua tipi konceptual dhe tipi i synuar. Konvertimi u zbatua te seksioni 2 i `01_mbledhja_kualiteti.ipynb`, dhe një `assert` kontrollon që çdo kolonë ka marrë tipin e synuar.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 / 42.
- **Pse u bë:** Tipet e sakta mundësojnë krahasime të sakta (renditja IUCN), veprime me data, numra të plotë pa `.0` dhe ulin memorien nga 31.9 MB në 13.6 MB.
- **Output:** `reports/data_types.md`, `reports/01_tipet_e_kolonave.csv`, seksioni 2 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Add data types for the 42 columns`.
