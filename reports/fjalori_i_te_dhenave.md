# Fjalori i të dhënave

**Autor:** Jeta Syla  
**Versioni:** 1.0  
**Data:** 16.10.2026  
**Statusi:** Fjalori i 42 kolonave.

## Qëllimi

Qëllimi i këtij fjalori është të shkruajë, për secilën nga 42 kolonat, kuptimin sipas Darwin Core, kuptimin sipas dokumentacionit të GBIF dhe një shembull vlere nga dataseti.

## Fjalori

| Kolona | Darwin Core | GBIF | Shembull |
|---|---|---|---|
| `gbifID` | Nuk është term i Darwin Core. | Çelësi unik i GBIF për vëzhgimin. GBIF përpiqet ta mbajë të qëndrueshëm, por kjo nuk është e mundur në çdo rast. | `6500474327` |
| `taxonKey` | Nuk është term i Darwin Core. | Çelësi i taksonit në GBIF Backbone për rangun më të saktë të këtij vëzhgimi. Mund të jetë sinonim. | `6258028` |
| `speciesKey` | Nuk është term i Darwin Core. | Çelësi i species në GBIF Backbone për këtë vëzhgim. | `6258028` |
| `datasetKey` | Nuk është term i Darwin Core. | UUID e datasetit të GBIF që e përmban këtë vëzhgim. | `50c9509d-22c7-4a22-a47d-8c48425ef4a7` |
| `catalogNumber` | Identifikues, mundësisht unik, i një burimi brenda një koleksioni. | Identifikues, mundësisht unik, i rreshtit brenda datasetit ose koleksionit. | `393203275` |
| `scientificName` | Emri shkencor i plotë, me autorësinë dhe datën nëse njihen. Te identifikimi, është emri i rangut më të ulët që mund të përcaktohet. | Emri shkencor, me autorësi, i taksonit nga GBIF Backbone i përputhur me këtë vëzhgim. Mund të jetë sinonim. | `Mantis religiosa (Linne, 1758)` |
| `species` | Nuk ekziston termi `species` në listën aktuale të Darwin Core. Pjesa e emrit të species është `specificEpithet`, kurse emri i plotë është `scientificName`. | Emri i species pa autorësi, nga GBIF Backbone i përputhur me këtë vëzhgim. | `Mantis religiosa` |
| `vernacularName` | Emër i zakonshëm. | Emër i zakonshëm. | `Praying Mantis` |
| `kingdom` | Emri shkencor i plotë i mbretërisë në të cilën klasifikohet taksoni. | Emri i mbretërisë, pa autorësi, nga GBIF Backbone i përputhur me këtë vëzhgim. | `Animalia` |
| `phylum` | Emri shkencor i plotë i filumit ose i divizionit në të cilin klasifikohet taksoni. | Emri i filumit, pa autorësi, nga GBIF Backbone i përputhur me këtë vëzhgim. | `Arthropoda` |
| `class` | Emri shkencor i plotë i klasës në të cilën klasifikohet taksoni. | Emri i klasës, pa autorësi, nga GBIF Backbone i përputhur me këtë vëzhgim. | `Insecta` |
| `order` | Emri shkencor i plotë i rendit në të cilin klasifikohet taksoni. | Emri i rendit, pa autorësi, nga GBIF Backbone i përputhur me këtë vëzhgim. | `Mantodea` |
| `family` | Emri shkencor i plotë i familjes në të cilën klasifikohet taksoni. | Emri i familjes, pa autorësi, nga GBIF Backbone i përputhur me këtë vëzhgim. | `Mantidae` |
| `genus` | Emri shkencor i plotë i gjinisë në të cilën klasifikohet taksoni. | Emri i gjinisë, pa autorësi, nga GBIF Backbone i përputhur me këtë vëzhgim. | `Mantis` |
| `taxonRank` | Rangu taksonomik i emrit më të saktë te `scientificName`. | Rangu taksonomik i emrit më të saktë te `scientificName`. | `SPECIES` |
| `iucnRedListCategory` | Nuk është term i Darwin Core. | Kategoria e Listës së Kuqe të IUCN për taksonin e këtij vëzhgimi. | `LC` |
| `iucnRedListStatus` | Nuk është term i Darwin Core. | Nuk është kolonë e formatit standard të shkarkimit. Në këtë dataset është i njëjti status i IUCN, i shkruar me fjalë. | `Least Concern` |
| `eventDate` | Datë-orë ose interval kohe gjatë të cilit ka ndodhur një ngjarje. Nuk është e përshtatshme për kohë gjeologjike. | Data-ora gjatë të cilës ka ndodhur ngjarja. Te vëzhgimet, kjo është data-ora kur ngjarja është regjistruar. Nuk është e përshtatshme për kohë gjeologjike. | `2026-08-21T16:41:17` |
| `year` | Viti katërshifror në të cilin ka ndodhur ngjarja, sipas kalendarit të erës sonë. | Viti katërshifror në të cilin ka ndodhur ngjarja, sipas kalendarit të erës sonë. | `2026` |
| `month` | Muaji, si numër i plotë, në të cilin ka ndodhur ngjarja. | Muaji, si numër i plotë, në të cilin ka ndodhur ngjarja. | `8` |
| `day` | Dita e muajit, si numër i plotë, në të cilën ka ndodhur ngjarja. | Dita e muajit, si numër i plotë, në të cilën ka ndodhur ngjarja. | `21` |
| `decimalLatitude` | Gjerësia gjeografike në gradë dhjetore. Vlerat e vlefshme janë nga -90 deri në 90. | Gjerësia gjeografike, në gradë dhjetore dhe sipas WGS84, e qendrës gjeografike të vendndodhjes. | `42.359947` |
| `decimalLongitude` | Gjatësia gjeografike në gradë dhjetore. Vlerat e vlefshme janë nga -180 deri në 180. | Gjatësia gjeografike, në gradë dhjetore dhe sipas WGS84, e qendrës gjeografike të vendndodhjes. | `20.993528` |
| `coordinateUncertaintyInMeters` | Distanca horizontale në metra nga gjerësia dhe gjatësia e dhënë. Rrethi më i vogël me këtë rreze e përmban të gjithë vendndodhjen. Zero nuk është vlerë e vlefshme. | E njëjta distancë horizontale në metra nga `decimalLatitude` dhe `decimalLongitude`, që përshkruan rrethin më të vogël që e përmban të gjithë vendndodhjen. | `2` |
| `elevation` | Nuk është term aktual i Darwin Core. Termi i afërt është `minimumElevationInMeters`: kufiri i poshtëm i lartësisë, zakonisht mbi nivelin e detit, në metra. | Lartësia, ose altituda, në metra mbi nivelin e detit. GBIF e shënon se nuk është term aktual i Darwin Core. | `575` |
| `locality` | Përshkrimi i saktë i vendit. | Përshkrimi i saktë i vendit. | `Nik Nika, křoviny při kraji silnice, 1,8 km SZ od obce` |
| `municipality` | Emri i plotë dhe i pashkurtuar i njësisë administrative më të vogël se county, si qyteti ose komuna, ku ndodhet vendndodhja. Nuk përdoret për një vend të emërtuar afër që nuk e përmban pikën. | Nuk është kolonë e tabelës "Simple download" të GBIF. Termi ekziston te Darwin Core. Në këtë dataset vlerat janë komunat e Kosovës, shpesh dygjuhëshe. | `Ferizaj / Uroševac` |
| `district` | Nuk është term i Darwin Core. Termat e afërt janë `stateProvince` dhe `county`. | Nuk është kolonë e formatit standard të shkarkimit. Në këtë dataset është rajoni i Kosovës. | `Ferizaj / Uroševac` |
| `protectedArea` | Nuk është term i Darwin Core. | Nuk është kolonë e formatit standard të shkarkimit. Në këtë dataset është zona e mbrojtur e shënuar për pikën, kur qelia është e plotësuar. | `Parku Kombëtar "Sharri"` |
| `protectedAreaDesignation` | Nuk është term i Darwin Core. | Nuk është kolonë e formatit standard të shkarkimit. Në këtë dataset është lloji i zonës së mbrojtur. | `National Park` |
| `strictlyProtected` | Nuk është term i Darwin Core. | Nuk është kolonë e formatit standard të shkarkimit. Në këtë dataset është `TRUE` ose `FALSE` për mbrojtjen e rreptë. | `TRUE` |
| `basisOfRecord` | Natyra e saktë e rreshtit të të dhënave. | Vlerat e termit Darwin Core Basis of Record që u aplikohen vëzhgimeve. | `HUMAN_OBSERVATION` |
| `individualCount` | Numri i individëve të pranishëm në kohën e vëzhgimit. | Numri i individëve të pranishëm në kohën e vëzhgimit. | `1` |
| `establishmentMeans` | Pohim nëse organizmi është futur në një vend dhe kohë përmes veprimit të drejtpërdrejtë ose jo të drejtpërdrejtë të njeriut. | I njëjti pohim. Vlerat përputhen me fjalorin EstablishmentMeans të GBIF, të nxjerrë nga fjalori i Darwin Core. | `introduced` |
| `recordedBy` | Emri i agjentit përgjegjës për regjistrimin e vëzhgimit. | Personi, grupi ose organizata përgjegjëse për regjistrimin fillestar. GBIF i ndan disa emra me `;`. | `arberzaimi` |
| `identifiedBy` | Emri i agjentit përgjegjës për identifikimin. | Lista e emrave të personave, grupeve ose organizatave që ia kanë caktuar taksonin vëzhgimit. GBIF i ndan disa emra me `;`. | `arberzaimi` |
| `institutionCode` | Emri ose shkurtesa e institucionit që e ka në kujdestari burimin. | Emri ose shkurtesa e institucionit që e ka në kujdestari objektin ose informacionin e rreshtit. | `iNaturalist` |
| `collectionCode` | Emri, shkurtesa ose kodi që identifikon koleksionin. | Emri, shkurtesa ose kodi i koleksionit apo datasetit nga ku rrjedh rreshti. | `Observations` |
| `license` | Nuk është term i Darwin Core. | Dokument ligjor që jep lejen zyrtare për të bërë diçka me vëzhgimin. | `CC_BY_NC_4_0` |
| `issue` | Nuk është term i Darwin Core. | Problemi i interpretimit i gjetur gjatë përpunimit të rreshtit. Disa flamuj ndahen me `;`. | `COORDINATE_ROUNDED;COUNTRY_DERIVED_FROM_COORDINATES;CONTINENT_DERIVED_FROM_COORDINATES;TAXON_ID_NOT_FOUND` |
| `iasUnionConcern` | Nuk është term i Darwin Core. | Nuk është kolonë e formatit standard të shkarkimit. Në këtë dataset, `TRUE` do të thotë se specia është në listën e specieve të huaja pushtuese të shqetësimit për Bashkimin Evropian. | `TRUE` |
| `iasAppliesFrom` | Nuk është term i Darwin Core. | Nuk është kolonë e formatit standard të shkarkimit. Në këtë dataset është data nga e cila ajo listë vlen për specien. | `2019-08-15` |

## Dokumentimi i detyrës

- **Input:** `dataset/kosovo_overall_biodiversity.csv`, [Darwin Core](https://dwc.tdwg.org/list/) dhe [formatet e shkarkimit të GBIF](https://techdocs.gbif.org/en/data-use/download-formats).
- **Çka u bë:** Për secilën nga 42 kolonat u shkrua kuptimi sipas Darwin Core, kuptimi sipas GBIF dhe një shembull vlere.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 / 42.
- **Pse u bë:** Për të dokumentuar kuptimin e atributeve para hapave të pastrimit dhe të preprocessing-ut.
- **Output:** `reports/fjalori_i_te_dhenave.md`.
- **Commit:**`Add data dictionary for the 42 columns`.
