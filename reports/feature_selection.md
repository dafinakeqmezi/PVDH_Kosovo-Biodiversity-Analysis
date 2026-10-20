# Zgjedhja e nënbashkësisë së vetive

**Versioni:** 1.0  
**Data:** 20.10.2026  
**Statusi:** Vendimi mbahet ose largohet për 42 kolonat.

## Varësia

Ky task përdor rëndësinë e 12.10.2026 (`reports/column_importance.md`), redundancën e 11.10.2026 (`reports/redundancy.md`), mungesat e 11.10.2026 (`processed/missing_report.csv`) dhe tipet e 12.10.2026 (`reports/data_types.md`). Qëllimi i analizës mbetet: shpërndarja sipas komunës, grupi biologjik, koha, statusi IUCN, zonat e mbrojtura dhe kualiteti i të dhënave.

## Si është vendosur

- **Largohet** nëse është e tepërt, nëse rëndësia është e ulët dhe nuk i përgjigjet një pyetjeje, ose nëse mungon mbi 80% dhe nuk është kolonë e pyetjes.
- **Mbahet** nëse rëndësia është e lartë për një pyetje, edhe kur ka mungesa.
- **Mbahet** nëse rëndësia është e mesme, nuk është e tepërt dhe mungesa nuk e zbraz kolonën.
- Tipi i synuar merret nga `reports/data_types.md`. Ai tregon si ruhet kolona që mbetet.

Numri nuk është caktuar paraprakisht. Pas 42 vendimeve mbeten **29** kolona dhe largohen **13**.

## Tabela e vendimit

| Kolona | Vendimi | Arsyeja |
|---|---|---|
| `gbifID` | largohet | Rëndësi e ulët. Është ID, jo përgjigje e një pyetjeje. Mungesa 0%. |
| `taxonKey` | mbahet | Rëndësi e mesme për grupin biologjik. Redundanca e ruan, sepse nuk është i njëjtë me `speciesKey`. Mungesa 0.08%. Tipi i synuar `Int64`. |
| `speciesKey` | mbahet | Rëndësi e mesme për grupin biologjik. Redundanca e ruan. Mungesa 2.59%. Tipi i synuar `Int64`. |
| `datasetKey` | mbahet | Rëndësi e mesme për kualitetin, sepse tregon burimin. Mungesa 0%. Tipi i synuar `category`. |
| `catalogNumber` | largohet | Rëndësi e ulët. Është ID brenda koleksionit. Mungesa 26.82%. |
| `scientificName` | mbahet | Rëndësi e lartë për grupin biologjik. Redundanca e ruan bashkë me `species`. Mungesa 0.08%. Tipi i synuar `category`. |
| `species` | mbahet | Rëndësi e lartë për grupin biologjik. Mungesa 2.59%. Tipi i synuar `category`. |
| `vernacularName` | largohet | Rëndësi e ulët. Emri i zakonshëm nuk është grupi biologjik. Mungesa 8.27%. |
| `kingdom` | mbahet | Rëndësi e lartë për grupin biologjik. Mungesa 0.08%. Tipi i synuar `category`. |
| `phylum` | mbahet | Rëndësi e lartë për grupin biologjik. Mungesa 0.15%. Tipi i synuar `category`. |
| `class` | mbahet | Rëndësi e lartë për grupin biologjik. Mungesa 0.83%. Tipi i synuar `category`. |
| `order` | mbahet | Rëndësi e lartë për grupin biologjik. Mungesa 0.71%. Tipi i synuar `category`. |
| `family` | mbahet | Rëndësi e lartë për grupin biologjik. Mungesa 0.34%. Tipi i synuar `category`. |
| `genus` | mbahet | Rëndësi e lartë për grupin biologjik. Mungesa 0.42%. Tipi i synuar `category`. |
| `taxonRank` | mbahet | Rëndësi e mesme për grupin biologjik, sepse tregon sa i saktë është emri. Mungesa 0.08%. Tipi i synuar `category (ordered)`. |
| `iucnRedListCategory` | mbahet | Rëndësi e lartë për statusin IUCN. Mungesa 2.59%. Tipi i synuar `category (ordered)`. |
| `iucnRedListStatus` | largohet | Redundante me `iucnRedListCategory`: 8/8 kode, përputhje 1:1 100%. Rëndësia është e ulët. |
| `eventDate` | mbahet | Rëndësi e lartë për kohën. Mungesa 4.68%. Tipi i synuar `datetime64`. |
| `year` | mbahet | Rëndësi e lartë për kohën. Mungesa 4.84%. Tipi i synuar `Int64`. |
| `month` | mbahet | Rëndësi e lartë për kohën. Mungesa 6.12%. Tipi i synuar `Int64`. |
| `day` | mbahet | Rëndësi e mesme për kohën. Mungesa 6.87%. Tipi i synuar `Int64`. |
| `decimalLatitude` | mbahet | Rëndësi e mesme për shpërndarjen sipas komunës. Mungesa 0%. Tipi i synuar `float64`. |
| `decimalLongitude` | mbahet | Rëndësi e mesme për shpërndarjen sipas komunës. Mungesa 0%. Tipi i synuar `float64`. |
| `coordinateUncertaintyInMeters` | mbahet | Rëndësi e lartë për kualitetin e vendndodhjes. Mungesa 68.34% nuk e heq, sepse pyetja e kualitetit mbështetet te kjo kolonë. Tipi i synuar `float64`. |
| `elevation` | largohet | Rëndësi e ulët: nuk i përgjigjet asnjërës pyetje. Mungesa 79.03%. |
| `locality` | mbahet | Rëndësi e mesme për vendin. Mungesa 32.57%. Tipi i synuar `str`. |
| `municipality` | mbahet | Rëndësi e lartë për shpërndarjen sipas komunës. Mungesa 0%. Tipi i synuar `category`. |
| `district` | mbahet | Rëndësi e mesme: grupon komunat, por nuk i zëvendëson. Mungesa 0%. Tipi i synuar `category`. |
| `protectedArea` | mbahet | Rëndësi e lartë për zonat e mbrojtura. Mungesa 55.01% do të thotë pikë jashtë zonës, sipas tipeve. Tipi i synuar `category`. |
| `protectedAreaDesignation` | mbahet | Rëndësi e lartë për llojin e zonës. Redundanca e ruan bashkë me emrin. Mungesa 55.01%. Tipi i synuar `category`. |
| `strictlyProtected` | mbahet | Rëndësi e mesme për zonat e mbrojtura. Mungesa 0%. Tipi i synuar `bool`. |
| `basisOfRecord` | mbahet | Rëndësi e lartë për kualitetin. Mungesa 0%. Tipi i synuar `category`. |
| `individualCount` | largohet | Rëndësi e ulët: numri i individëve nuk është pyetje e projektit. Mungesa 37.79%. |
| `establishmentMeans` | largohet | Rëndësi e ulët dhe mungesa 99.49%. |
| `recordedBy` | largohet | Rëndësi e ulët. Është tekst me emra, jo masë kualiteti. Mungesa 8.23%. |
| `identifiedBy` | largohet | Rëndësi e ulët dhe mungesa 83.48%. |
| `institutionCode` | mbahet | Rëndësi e mesme për kualitetin, sepse tregon institucionin. Mungesa 7.92%. Tipi i synuar `category`. |
| `collectionCode` | largohet | Rëndësi e ulët. Mungesa 28.76%. |
| `license` | largohet | Rëndësi e ulët. Licenca nuk i përgjigjet pyetjeve të analizës. Mungesa 0%. |
| `issue` | mbahet | Rëndësi e lartë për kualitetin. Mungesa 3.04%. Tipi i synuar `str`. |
| `iasUnionConcern` | largohet | Rëndësi e ulët. Speciet e huaja nuk janë një nga pyetjet. Mungesa 0%. |
| `iasAppliesFrom` | largohet | Rëndësi e ulët dhe mungesa 99.95%. |

## Kolonat që mbeten

`taxonKey`, `speciesKey`, `datasetKey`, `scientificName`, `species`, `kingdom`, `phylum`, `class`, `order`, `family`, `genus`, `taxonRank`, `iucnRedListCategory`, `eventDate`, `year`, `month`, `day`, `decimalLatitude`, `decimalLongitude`, `coordinateUncertaintyInMeters`, `locality`, `municipality`, `district`, `protectedArea`, `protectedAreaDesignation`, `strictlyProtected`, `basisOfRecord`, `institutionCode`, `issue`.

## Kolonat që largohen

`gbifID`, `catalogNumber`, `vernacularName`, `iucnRedListStatus`, `elevation`, `individualCount`, `establishmentMeans`, `recordedBy`, `identifiedBy`, `collectionCode`, `license`, `iasUnionConcern`, `iasAppliesFrom`.

## Vendimi dhe arsyetimi

Nënbashkësia analitike ka 29 kolona. 13 kolonat e tjera nuk hyjnë në të, sepse janë të tepërta, nuk i përgjigjen pyetjeve, ose janë pothuajse bosh. CSV-ja fillestare mbetet me 42 kolona. Ky vendim zëvendëson listën e 9 tetorit, e cila hiqte `taxonKey` dhe `speciesKey` si të tepërta dhe e linte `elevation` në analizë.

## Dokumentimi i detyrës

- **Varësia:** `reports/column_importance.md` (12.10.2026), `reports/redundancy.md` (11.10.2026), `processed/missing_report.csv` (11.10.2026), `reports/data_types.md` (12.10.2026).
- **Input:** `reports/column_importance.md`, `reports/redundancy.md`, `processed/missing_report.csv`, `reports/data_types.md`.
- **Çka u bë:** Për 42 kolonat u vendos mbahet ose largohet. Plani i 9 tetorit u përditësua.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 në CSV / 29 në nënbashkësinë analitike.
- **Pse u bë:** Numri i kolonave duhet të dalë nga kriteret, jo të caktohet paraprakisht.
- **Output:** `reports/feature_selection.md`, `notebooks/03_vetite.ipynb`.
- **Commit:** `Add the feature selection list with a reason for each column`.
