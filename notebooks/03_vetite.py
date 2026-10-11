#!/usr/bin/env python
# coding: utf-8

# # 03 — Plani i preprocessing-ut
# 
# **Autor:** Jeta Syla  
# **Versioni:** 1.0  
# **Data:** 11.10.2026  
# **Statusi:** Plani fillestar; përditësohet pas 13.10.2026.

# ## Qëllimi
# 
# Qëllimi i këtij plani është të përcaktojë cilat kolona do të mbahen,
# largohen ose krijohen dhe cilat metoda do të përdoren për përgatitjen
# e datasetit për analizën e biodiversitetit në Kosovë.

# ## Plani i preprocessing-ut
# 
# | Requirement | Columns | Method | Reason |
# |---|---|---|---|
# | Reduktimi i dimensionit | `iucnRedListStatus`, `taxonKey`, `speciesKey`, `iasAppliesFrom`, `establishmentMeans`, `identifiedBy`, `gbifID`, `catalogNumber` | `iucnRedListStatus`, `taxonKey` dhe `speciesKey` largohen si redundante. `iasAppliesFrom`, `establishmentMeans` dhe `identifiedBy` largohen për shkak të mungesave. `gbifID` dhe `catalogNumber` ruhen vetëm për gjurmueshmëri, jo si veti analitike. PCA nuk përdoret në versionin e parë. | `iasAppliesFrom` mungon 99.9%, `establishmentMeans` 99.5% dhe `identifiedBy` 83.5%. ID-të nuk përmbajnë informacion analitik, ndërsa PCA do ta zvogëlonte interpretueshmërinë. |
# | Zgjedhja e nënbashkësisë | `species`, `kingdom`, `phylum`, `class`, `order`, `family`, `genus`, `iucnRedListCategory`, `year`, `month`, `decimalLatitude`, `decimalLongitude`, `coordinateUncertaintyInMeters`, `elevation`, `municipality`, `district`, `protectedArea`, `protectedAreaDesignation`, `strictlyProtected`, `basisOfRecord`, `individualCount`, `issue` | Përzgjedhje manuale sipas qëllimit të analizës. `issue` përdoret vetëm gjatë kontrollit të cilësisë dhe largohet nga dataset-i final analitik. | Dataseti nuk ka target të përcaktuar, prandaj nuk përdoret `SelectKBest`. Kolonat e zgjedhura mbulojnë taksonominë, kohën, vendndodhjen, ruajtjen dhe vrojtimet. |
# | Krijimi i vetive | `month`, `year`, `iucnRedListCategory`, `protectedArea`, `species`, `district` | `season` krijohet nga `month`; `decade = (year // 10) * 10`; `isThreatened = 1` për `VU`, `EN`, `CR`; `inProtectedArea = 1` kur `protectedArea` ka vlerë; `observationCount` llogaritet sipas `species`, `district` dhe `year`. | Këto veti mundësojnë analizën sezonale, ndryshimet sipas dekadave, identifikimin e specieve të rrezikuara, krahasimin brenda/jashtë zonave të mbrojtura dhe numrin e vrojtimeve. |
# | Diskretizimi | `elevation`, `coordinateUncertaintyInMeters`, `year` | Para grupimit, `elevation = 0` zëvendësohet me mungesë. `elevation`: 297–800 m = ultësirë, 801–1500 m = zonë kodrinore/malore, mbi 1500 m = zonë e lartë malore. `coordinateUncertaintyInMeters`: ≤100 m = e lartë, 101–1000 m = mesatare, >1000 m = e ulët. `year` grupohet në dekada. | Ndarjet përputhen me intervalin e lartësisë së Kosovës dhe e bëjnë cilësinë hapësinore e periudhat kohore më të kuptueshme në vizualizime. |
# | Binarizimi | `strictlyProtected`, `iasUnionConcern`, `kingdom`, `basisOfRecord` | `TRUE/FALSE` konvertohet në `1/0` për `strictlyProtected` dhe `iasUnionConcern`. Për `kingdom` dhe `basisOfRecord` përdoret `OneHotEncoder(handle_unknown="ignore")`. `species` nuk binarizohet. | Dy kolonat e para janë boolean. `kingdom` dhe `basisOfRecord` kanë nga 7 kategori dhe mund të kodohen pa rritje të madhe të dimensionit; `species` ka 4,095 kategori. |
# | Transformimi | `eventDate`, `iucnRedListCategory`, `individualCount`, `coordinateUncertaintyInMeters`, `elevation`, `decimalLatitude`, `decimalLongitude` | `eventDate` konvertohet me `pd.to_datetime`; për intervalet merret data e fillimit. `NE` dhe `DD` trajtohen si të pavlerësuara. Për `individualCount` dhe `coordinateUncertaintyInMeters` përdoret `np.log1p`. Për modelim përdoret `RobustScaler` mbi `elevation` dhe vlerat e transformuara. Koordinatat ruhen të pandryshuara për harta. | `individualCount` arrin 10,200 dhe pasiguria e koordinatave 4,226 km, prandaj kanë shpërndarje të anuar dhe outliers. `RobustScaler` ndikohet më pak nga outliers, ndërsa koordinatat origjinale nevojiten për hartëzim. |

# ## Decision + Rationale
# 
# **Decision:** Në versionin e parë do të përdoret përzgjedhje manuale e
# vetive dhe jo PCA. Kolonat redundante, identifikuese dhe pothuajse boshe
# nuk do të përdoren si veti analitike. Do të krijohen vetitë sezonale,
# kohore, të rrezikshmërisë dhe mbrojtjes, ndërsa transformimet numerike
# do të aplikohen vetëm në datasetin e procesuar.
# 
# **Rationale:** Dataseti përmban të dhëna të përziera numerike dhe
# kategorike, nuk ka target të përcaktuar dhe kërkon që rezultatet të
# mbeten të interpretueshme. Përzgjedhja manuale ruan kuptimin biologjik
# të atributeve, ndërsa `log1p` dhe `RobustScaler` zvogëlojnë ndikimin e
# shpërndarjeve të anueshme dhe outliers. Vendimet do të rishikohen pas
# 13.10.2026.

# ## Dokumentimi i detyrës
# 
# - **Input:** `dataset/kosovo_overall_biodiversity.csv` dhe grupet e atributeve në `README.md`.
# - **Çka u bë:** U krijua tabela e planit të preprocessing-ut.
# - **Rreshta para / pas:** 46,831 / 46,831.
# - **Kolona para / pas:** 42 / 42.
# - **Pse u bë:** Për të përcaktuar metodat para zbatimit të preprocessing-ut.
# - **Output:** `notebooks/03_vetite.py`.
# - **Commit:** `Add initial preprocessing plan`.






