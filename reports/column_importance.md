# Rëndësia analitike e kolonave

**Versioni:** 1.0  
**Data:** 18.10.2026  
**Statusi:** Tabela e rëndësisë për 42 kolonat.

## Varësia

Ky task varet nga **Fjalori i të dhënave** i 16.10.2026: `reports/data_dictionary.md`. Pyetjet e projektit janë: shpërndarja sipas komunës, grupi biologjik, koha, statusi IUCN, zonat e mbrojtura dhe kualiteti i të dhënave.

## Si është vlerësuar

- **E lartë:** pa këtë kolonë pyetja nuk përgjigjet.
- **E mesme:** e ndihmon pyetjen, por nuk është masa kryesore.
- **E ulët:** nuk përgjigjet në pyetje, është vetëm identifikues, ose përsërit një kolonë tjetër.

## Tabela e rëndësisë

| Column | Pyetja | Rëndësia |
|---|---|---|
| `gbifID` | asnjëra | e ulët |
| `taxonKey` | grupi biologjik | e mesme |
| `speciesKey` | grupi biologjik | e mesme |
| `datasetKey` | kualiteti i të dhënave | e mesme |
| `catalogNumber` | asnjëra | e ulët |
| `scientificName` | grupi biologjik | e lartë |
| `species` | grupi biologjik | e lartë |
| `vernacularName` | grupi biologjik | e ulët |
| `kingdom` | grupi biologjik | e lartë |
| `phylum` | grupi biologjik | e lartë |
| `class` | grupi biologjik | e lartë |
| `order` | grupi biologjik | e lartë |
| `family` | grupi biologjik | e lartë |
| `genus` | grupi biologjik | e lartë |
| `taxonRank` | grupi biologjik | e mesme |
| `iucnRedListCategory` | statusi IUCN | e lartë |
| `iucnRedListStatus` | statusi IUCN | e ulët |
| `eventDate` | koha | e lartë |
| `year` | koha | e lartë |
| `month` | koha | e lartë |
| `day` | koha | e mesme |
| `decimalLatitude` | shpërndarja sipas komunës | e mesme |
| `decimalLongitude` | shpërndarja sipas komunës | e mesme |
| `coordinateUncertaintyInMeters` | kualiteti i të dhënave | e lartë |
| `elevation` | asnjëra | e ulët |
| `locality` | shpërndarja sipas komunës | e mesme |
| `municipality` | shpërndarja sipas komunës | e lartë |
| `district` | shpërndarja sipas komunës | e mesme |
| `protectedArea` | zonat e mbrojtura | e lartë |
| `protectedAreaDesignation` | zonat e mbrojtura | e lartë |
| `strictlyProtected` | zonat e mbrojtura | e mesme |
| `basisOfRecord` | kualiteti i të dhënave | e lartë |
| `individualCount` | asnjëra | e ulët |
| `establishmentMeans` | asnjëra | e ulët |
| `recordedBy` | kualiteti i të dhënave | e ulët |
| `identifiedBy` | kualiteti i të dhënave | e ulët |
| `institutionCode` | kualiteti i të dhënave | e mesme |
| `collectionCode` | kualiteti i të dhënave | e ulët |
| `license` | asnjëra | e ulët |
| `issue` | kualiteti i të dhënave | e lartë |
| `iasUnionConcern` | asnjëra | e ulët |
| `iasAppliesFrom` | asnjëra | e ulët |

## Arsyetimi

Pyetja për komunën përgjigjet me `municipality`. `district` vetëm i grupon komunat, `locality` është përshkrim i lirë, kurse koordinatat e vendosin pikën, por nuk e emërtojnë komunën.

Grupi biologjik përgjigjet me `kingdom`, `phylum`, `class`, `order`, `family`, `genus`, `species` dhe `scientificName`. `taxonKey` dhe `speciesKey` janë çelësa, `taxonRank` tregon sa i saktë është emri, dhe `vernacularName` është emër i zakonshëm.

Koha përgjigjet me `eventDate`, `year` dhe `month`. `day` është më e imët se pyetja.

Statusi IUCN përgjigjet me `iucnRedListCategory`. `iucnRedListStatus` është i njëjti status i shkruar me fjalë, sipas fjalorit, prandaj është e ulët.

Zonat e mbrojtura përgjigjen me `protectedArea` dhe `protectedAreaDesignation`. `strictlyProtected` vetëm shton nëse mbrojtja është e rreptë.

Kualiteti i të dhënave përgjigjet me `issue`, `basisOfRecord` dhe `coordinateUncertaintyInMeters`. `datasetKey` dhe `institutionCode` tregojnë burimin, por nuk e masin cilësinë e pikës.

Kolonat e ulëta që nuk hyjnë në asnjë pyetje janë identifikues (`gbifID`, `catalogNumber`), lartësia, numri i individëve, mënyra e vendosjes, licenca dhe dy kolonat e specieve të huaja.

## Dokumentimi i detyrës

- **Varësia:** `reports/data_dictionary.md`, 16.10.2026.
- **Input:** fjalori i varësisë dhe pyetjet e projektit.
- **Çka u bë:** Secila nga 42 kolonat u lidh me një pyetje dhe u vlerësua e lartë, e mesme ose e ulët.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 / 42. CSV-ja nuk u ndryshua.
- **Pse u bë:** Për të ditur cilat kolona i përgjigjen pyetjeve të projektit.
- **Output:** `reports/column_importance.md`.
- **Commit:** `Add analytical importance for the 42 columns`.
