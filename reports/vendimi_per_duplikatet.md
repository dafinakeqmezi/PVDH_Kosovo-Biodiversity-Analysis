# Vendimi për duplikatet

## Evidenca

Analiza e Dafinës: commit `d2708c640de830014edf4c4f35a528849c98455f`, `reports/uniqueness.md`, `reports/01_duplikatet_shqyrtimi.csv` dhe `processed/duplicate_candidates.csv`. Këto lexohen me git show nga versioni i fiksuar, pa i ndryshuar. Nëse mungon commit-i, kërkohet git fetch origin. SHA-256 e kandidatëve: `65632c8f989f1d70caac47d9338127e7518bb747ac749db2fbb99ff7c25e09a3`. Dataset-i burimor i atij commit-i përputhet me origjinalin lokal.

Ka 3,132 rreshta në 1,288 grupe kandidatë. Dafina propozon 378 rreshta të tepërt. Vendimi këtu pranon 235 grupe dhe liston 375 rreshta për fshirjen e ardhshme. Asnjë rresht nuk është fshirë.

## Decision + Rationale

Njësia e analizës është vëzhgimi/grumbullimi, jo numri i publikimeve të tij. Kriteri kandidat është species + eventDate origjinale + koordinata pa rrumbullakim + recordedBy me hapësira të normalizuara dhe casefold. Kandidatët me çelës jo të plotë nuk bashkohen; identitetet alternative të të njëjtit person nuk hamendësohen. Nuk bashkohen timestamp-e të ndryshme vetëm pse bien në të njëjtën ditë.

Pranohen vetëm grupet e propozuara nga Dafina që kanë precizion ditor, vëzhgues të njohur, scientificName dhe basisOfRecord konsistent, pa qendër rrjete 7071 m dhe pa konflikt në individualCount. Intervalet/datat e pjesshme ruhen. Specimenët me catalogNumber të ndryshëm ruhen, përveç grupeve ndërburimore të konfirmuara shprehimisht nga shqyrtimi i Dafinës. Vetëm fakti që datasetKey ndryshon nuk provon dyfishim. Përjashtimet ndaj propozimit të saj dokumentohen grup më grup në vendimet_e_grupeve_duplikate.csv.

Ky është rregull operacional për deduplikim të regjistrimeve të vëzhgimit; barazia e vendit, datës, vëzhguesit dhe numrit nuk provon identitetin biologjik të individëve. Vizitat e përsëritura mund të jenë vëzhgime të vlefshme. Kjo pasiguri ruhet në këtë arsyetim dhe lista është e auditueshme para largimit; nuk pretendohet verifikim manual i çdo grupi.

## Cili rresht ruhet

Ruhet rreshti me numrin më të madh të fushave semantikisht të plotësuara në këtë listë fikse: scientificName, species, kingdom, phylum, class, order, family, genus, taxonRank, eventDate, year, month, day, decimalLatitude, decimalLongitude, coordinateUncertaintyInMeters, elevation, locality, municipality, district, protectedArea, protectedAreaDesignation, strictlyProtected, basisOfRecord, individualCount, recordedBy, identifiedBy, iucnRedListCategory. Mungesat efektive përfshijnë tokenët e konfirmuar dhe elevation=0 për vlerësim; kjo nuk e zëvendëson ende elevation në dataset. ID-të, metadata e botimit, flamujt e rinj dhe iucnRedListStatus redundant nuk japin pikë. Në barazim ruhet gbifID numerik më i vogël, vetëm për qëndrueshmëri, jo sepse është më cilësor. Mungesat e rreshtit të mbajtur nuk mbushen nga rreshta të tjerë në këtë detyrë.

## individualCount

Kur numërimet ndryshojnë, ruhet i gjithë grupi. Një numër i dhënë dhe një mungesë trajtohen gjithashtu si konflikt. Kur numërimet janë të njëjta ruhet numri i rreshtit të përzgjedhur, pa mbledhje, mesatare apo maksimum. Kur të gjitha mungojnë, mbeten NaN. Numërimet e ndryshme mund të jenë vizita të ndryshme: as ruajtja e tyre nuk autorizon mbledhjen e tyre si bollëk biologjik.

## Dokumentimi i detyrës

1. **Input:** kandidatët dhe shqyrtimi i Dafinës nga commit-i i mësipërm, df_raw dhe df_clean.
2. **Çka u bë:** U vendos rregulli, përjashtimet dhe renditja e kandidatëve; u përgatit lista e rreshtave për fshirje.
3. **Rreshta para/pas:** 46,831 / 46,831; **kolona para/pas:** 79 / 79.
4. **Pse u bë:** Për të shmangur fshirjen e ekzemplarëve/numërimeve të ndryshme dhe për të pasur përzgjedhje të auditueshme.
5. **Output:** reports/vendimi_per_duplikatet.md, reports/vendimet_e_grupeve_duplikate.csv, reports/renditja_e_kandidateve_duplikate.csv, processed/rreshtat_per_fshirje_duplikate.csv.
6. **Commit:** Document duplicate decisions and select removal candidates (mesazh i propozuar).

Largimi i rreshtave është detyrë tjetër. cleaning_log.csv nuk merr transformim fshirjeje për këtë vendim, sepse df_clean nuk ndryshon. protectedArea është plotësuar sipas sqarimit semantik të përdorueses; shih vendimet_per_mungesat_strukturore.md për burimin dhe kufizimet.
