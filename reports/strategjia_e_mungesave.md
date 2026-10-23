# Strategjia për vlerat e zbrazëta

Input: dataset-i origjinal, `raporti_i_mungesave_efektive.csv`, `mungesat_sipas_grupeve.csv`, `mekanizmat_e_mungeses.md`, `rendesia_e_kolonave.md` dhe `redundanca.md`.

**Missing %** është përqindja efektive: bashkimi i NaN, tokenëve literalë të mungesës dhe elevation = 0. Inventari fillestar mbetet në `processed/missing_report.csv`; numërimet e krahasueshme janë në `reports/raporti_i_mungesave_efektive.csv`. NE/DD janë kategori IUCN; mungesat potencialisht strukturore ende numërohen dhe interpretohen veçmas.

**Decision + Rationale:** Nuk ka prag fiks. Vendimet mbështeten në rëndësi, kuptim, mundësi rikuperimi dhe modelin e mungesës. Delete vlen vetëm për pamjen e specifikuar; keep ruan vlerën dhe NaN; flag shton në fazën e zbatimit një tregues mungese; impute lejohet vetëm për rikuperim determinist të verifikuar. Asnjë vendim në tabelë nuk është zbatuar mbi dataset-in. Nuk ka fshirje globale rreshtash për species/year. Përqindjet e larta nuk justifikojnë vetë heqjen.

| Column | Missing % | Rëndësia | Rikuperimi | Vendimi | Arsyetimi |
| --- | --- | --- | --- | --- | --- |
| gbifID | 0.00 | e ulët | Vetëm nga burimi origjinal; jo gjenerim ID-sh. | keep | Identifikues për gjurmueshmëri dhe grupim; ruhet edhe kur rëndësia direkte analitike është e ulët. |
| scientificName | 0.08 | e lartë | Validim me taksonominë e burimit. | keep + flag | Ruhen emri dhe rangu real; mungesa nuk zëvendësohet me taksonin më të shpeshtë. |
| species | 2.59 | e lartë | Vetëm lidhje e verifikuar me speciesKey/taksonominë. | keep + flag | Mos shpik species nga gjinia. Përjashto vetëm nga analiza në nivel species, jo nga dataset-i i përgjithshëm. |
| vernacularName | 8.27 | e ulët | Fjalor taksonomik me gjuhë të përcaktuar. | keep | Emri i zakonshëm është opsional; mungesa nuk pengon identifikimin shkencor. |
| kingdom | 0.08 | e lartë | Hierarki taksonomike e verifikuar nga çelësi GBIF. | keep + flag | Ruaj nivelin e identifikimit; rikuperim vetëm kur lidhja është e qartë dhe dokumentohet. |
| phylum | 0.15 | e lartë | Hierarki taksonomike e verifikuar nga çelësi GBIF. | keep + flag | Ruaj nivelin e identifikimit; rikuperim vetëm kur lidhja është e qartë dhe dokumentohet. |
| class | 0.83 | e lartë | Hierarki taksonomike e verifikuar nga çelësi GBIF. | keep + flag | Ruaj nivelin e identifikimit; rikuperim vetëm kur lidhja është e qartë dhe dokumentohet. |
| order | 0.71 | e lartë | Hierarki taksonomike e verifikuar nga çelësi GBIF. | keep + flag | Ruaj nivelin e identifikimit; rikuperim vetëm kur lidhja është e qartë dhe dokumentohet. |
| family | 0.34 | e lartë | Hierarki taksonomike e verifikuar nga çelësi GBIF. | keep + flag | Ruaj nivelin e identifikimit; rikuperim vetëm kur lidhja është e qartë dhe dokumentohet. |
| genus | 0.42 | e lartë | Hierarki taksonomike e verifikuar nga çelësi GBIF. | keep + flag | Ruaj nivelin e identifikimit; rikuperim vetëm kur lidhja është e qartë dhe dokumentohet. |
| taxonRank | 0.08 | e mesme | Validim me taksonominë e burimit. | keep + flag | Ruhen emri dhe rangu real; mungesa nuk zëvendësohet me taksonin më të shpeshtë. |
| taxonKey | 0.08 | e mesme | Hierarki taksonomike e verifikuar nga çelësi GBIF. | keep + flag | Ruaj nivelin e identifikimit; rikuperim vetëm kur lidhja është e qartë dhe dokumentohet. |
| speciesKey | 2.59 | e mesme | Vetëm lidhje e verifikuar me speciesKey/taksonominë. | keep + flag | Mos shpik species nga gjinia. Përjashto vetëm nga analiza në nivel species, jo nga dataset-i i përgjithshëm. |
| iucnRedListCategory | 2.59 | e lartë | Vetëm vlerësim IUCN i verifikuar për taksonin dhe versionin. | keep + flag | NE dhe DD janë kategori reale, jo NaN dhe jo LC; mos imputo status rreziku. |
| iucnRedListStatus | 2.59 | e ulët | Rindërtohet nga harta e kodeve të IUCN. | delete (pamja analitike) | Redundant sipas reports/redundanca.md; jo vendim i bazuar në përqindjen e mungesës. |
| eventDate | 4.68 | e lartë | Komponentë year/month/day vetëm nëse janë të vlefshëm e konsistentë. | keep + impute + flag | Ruaj intervalet dhe precision; mos krijo muaj/ditë nga data vetëm me vit. Rikuperimi i ardhshëm shënohet. |
| year | 4.84 | e lartë | Nga eventDate vetëm kur komponenti është shprehimisht i pranishëm dhe i vlefshëm. | keep + impute + flag | Mos përdor 1 janar si datë reale; rreshtat pa komponentin e nevojshëm përjashtohen vetëm nga analiza kohore përkatëse. |
| month | 6.12 | e lartë | Nga eventDate vetëm kur komponenti është shprehimisht i pranishëm dhe i vlefshëm. | keep + impute + flag | Mos përdor 1 janar si datë reale; rreshtat pa komponentin e nevojshëm përjashtohen vetëm nga analiza kohore përkatëse. |
| day | 6.87 | e mesme | Nga eventDate vetëm kur komponenti është shprehimisht i pranishëm dhe i vlefshëm. | keep + impute + flag | Mos përdor 1 janar si datë reale; rreshtat pa komponentin e nevojshëm përjashtohen vetëm nga analiza kohore përkatëse. |
| decimalLatitude | 0.00 | e mesme | Vetëm gjeoreferencim i dokumentuar. | keep + flag | Pa mesatare koordinatash; ruaj pikën dhe verifiko vlefshmërinë/hartën veçmas. |
| decimalLongitude | 0.00 | e mesme | Vetëm gjeoreferencim i dokumentuar. | keep + flag | Pa mesatare koordinatash; ruaj pikën dhe verifiko vlefshmërinë/hartën veçmas. |
| coordinateUncertaintyInMeters | 68.34 | e lartë | Metadata e gjeoreferencimit nga burimi. | keep + flag | Mungesa nuk është pasiguri zero. Analizat hapësinore duhet të raportojnë filtrat e cilësisë. |
| elevation | 86.79 | e ulët | DEM i verifikuar nga koordinatat, me rezolucion dhe proveniencë; ende jo zbatuar. | keep + flag | Zero trajtohet si NaN në kopjen e ardhshme me elevation_was_zero; pa medianë globale. Përdorim vetëm pas kontrollit të plausibilitetit. |
| locality | 32.65 | e mesme | Burimi origjinal; komuna nuk zëvendëson lokalitetin. | keep + flag | unknown dhe tokenët bosh normalizohen në kopjen e pastruar; mos shpik lokalitet specifik. |
| municipality | 0.00 | e lartë | Spatial join me kufij administrativë të verifikuar nëse nevojitet. | keep | Kolona të plota për analizë rajonale; harmonizimi i emrave është hap i veçantë. |
| district | 0.00 | e mesme | Spatial join me kufij administrativë të verifikuar nëse nevojitet. | keep | Kolona të plota për analizë rajonale; harmonizimi i emrave është hap i veçantë. |
| protectedArea | 55.01 | e lartë | Spatial join me kufijtë dhe versionin e zonave të mbrojtura. | keep + flag | Raportet ekzistuese sugjerojnë jashtë zonës, por mungesa vetëm nuk provon Not protected. Mbaj unknown derisa mbulimi hapësinor të verifikohet. |
| protectedAreaDesignation | 55.01 | e lartë | Spatial join me kufijtë dhe versionin e zonave të mbrojtura. | keep + flag | Raportet ekzistuese sugjerojnë jashtë zonës, por mungesa vetëm nuk provon Not protected. Mbaj unknown derisa mbulimi hapësinor të verifikohet. |
| strictlyProtected | 0.00 | e mesme | Metadata/hartë e mbrojtjes. | keep | False është vlerë e vlefshme; mungesa eventuale nuk zëvendësohet automatikisht me False. |
| basisOfRecord | 0.00 | e lartë | Metadata e burimit. | keep | Përcakton kuptimin e regjistrimit dhe dallimet e mungesës; nuk imputohet me modë. |
| individualCount | 37.79 | e ulët | Vetëm numër i raportuar nga burimi. | keep + flag | Mungesa nuk është 0 ose 1. Mos ngatërro numrin e regjistrimeve me numrin e individëve; pa imputim global. |
| establishmentMeans | 99.49 | e ulët | Informacion ekologjik i verifikuar. | delete (pamja kryesore) | Pothuajse bosh dhe jashtë pyetjeve kryesore sipas rëndësisë; ruaj origjinalin për analizë të specializuar. |
| recordedBy | 8.23 | e ulët | Metadata e regjistrimit. | keep + flag | unknown normalizohet; mos imputo identitetin me emrin më të shpeshtë. |
| identifiedBy | 83.49 | e ulët | Metadata e regjistrimit. | keep + flag | unknown normalizohet; mos imputo identitetin me emrin më të shpeshtë. |
| institutionCode | 7.92 | e mesme | Metadata e institucionit/koleksionit për regjistrimin. | keep | Fusha provenience opsionale; datasetKey nuk përcakton gjithmonë një institucion, prandaj jo mbushje e verbër. |
| collectionCode | 28.76 | e ulët | Metadata e institucionit/koleksionit për regjistrimin. | keep | Fusha provenience opsionale; datasetKey nuk përcakton gjithmonë një institucion, prandaj jo mbushje e verbër. |
| catalogNumber | 26.82 | e ulët | Metadata e institucionit/koleksionit për regjistrimin. | keep | Fusha provenience opsionale; datasetKey nuk përcakton gjithmonë një institucion, prandaj jo mbushje e verbër. |
| datasetKey | 0.00 | e mesme | Vetëm nga burimi origjinal; jo gjenerim ID-sh. | keep | Identifikues për gjurmueshmëri dhe grupim; ruhet edhe kur rëndësia direkte analitike është e ulët. |
| license | 0.00 | e ulët | Licenca e regjistrimit/burimit. | keep | Duhet për përdorim dhe atribuim pavarësisht rëndësisë së ulët analitike. |
| issue | 3.04 | e lartë | Flag-et e eksportit GBIF. | keep + flag | Bosh mund të nënkuptojë pa flag të raportuar, jo cilësi të garantuar; mos imputo problem. |
| iasUnionConcern | 0.00 | e ulët | Lista dhe metadata për versionin përkatës. | keep | False është vlerë e vlefshme; nuk tregon domosdoshmërisht plotësinë e njohurive ekologjike. |
| iasAppliesFrom | 99.95 | e ulët | Data e listimit vetëm kur zbatohet iasUnionConcern. | keep + flag | Mungesa mund të jetë strukturore për False. Ndaj not applicable nga unknown kur True; mos hiq vetëm për shkak të 99.95% mungesës. |

## Kontrolli i mungesës strukturore

iasAppliesFrom sipas iasUnionConcern (False/True në kolonat më poshtë tregojnë nëse data mungon):

| iasUnionConcern | False | True |
| --- | --- | --- |
| FALSE | 0 | 46807 |
| TRUE | 24 | 0 |

Për protectedArea raporti i mëparshëm e interpreton boshllëkun si jashtë zonave të mbrojtura. Këtu kjo mbetet hipotezë deri në verifikimin e mbulimit dhe versionit të spatial join; nuk caktohet automatikisht Not protected.

## Dokumentimi i detyrës

- **Input:** dataset/kosovo_overall_biodiversity.csv dhe raportet e mësipërme.
- **Çka u bë:** U vendos strategji për të 42 kolonat me rëndësi, rikuperim dhe arsyetim.
- **Rreshta para / pas:** 46,831 / 46,831; **kolona para / pas:** 42 / 42.
- **Pse u bë:** Për të shmangur humbje informacioni dhe imputime pa mbështetje semantike.
- **Output:** reports/strategjia_e_mungesave.md, 42 vendime.
- **Commit:** Add hidden missingness analysis and column strategies (mesazh i propozuar).

Këto janë hapa diagnostikimi dhe planifikimi; cleaning_log.csv ruhet për transformimet reale. Zbatimi i vendimeve duhet të regjistrojë ndryshimet me log_step().
