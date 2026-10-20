# Vendimi për elevation = 0

Ka 3,634 zero (7.76% të rreshtave; 37.01% të 9,820 lartësive të plotësuara).
Burimi kryesor është Arthropod observations derived from HabiProt Alciphron database in Serbia (`d92e92e0-8d20-4756-a60b-3746f408c14c`), me 3,624 zero.
Zerot shfaqen në 7 rajone dhe 32 komuna; nuk përfaqësojnë një vend të vetëm të ulët.
Tabelat `lartesia_zero_sipas_grupeve.csv` japin numrin dhe emëruesin sipas burimit, basisOfRecord, rajonit, komunës dhe locality; `regjistrimet_me_lartesi_zero.csv` ruan koordinatat dhe ID-të për auditim.

**Decision + Rationale:** 0 m nuk trajtohet si lartësi reale e sipërfaqes në Kosovë. ASK raporton minimum 270 m në luginën e Drinit të Bardhë ([Some Facts on the Environment 2021–2022, f. 10](https://askapi.rks-gov.net/Custom/d9b7ae43-c68e-49a4-b713-5ec33c3a9c25.pdf#page=10)). Përqendrimi te një burim sugjeron placeholder ose problem eksportimi, por pa metadata të botuesit nuk mund të provohet shkaku për çdo rresht.

Në analizën e mungesave zero përfshihet në maskën efektive; në pastrimin e ardhshëm rekomandohet NaN dhe flamur `elevation_was_zero`, duke ruajtur origjinalin. Nuk zëvendësohet me 270 m ose me mesatare. Mungesa efektive bëhet 40,645 (86.79%).

Kufizime: nuk është bërë kontroll GIS/DEM për çdo pikë; lartësitë e tjera të dyshimta (përfshirë maksimumin 3050 m) kërkojnë kontroll të veçantë. Referenca kombëtare nuk është prag automatik për të fshirë të gjitha vlerat nën 270 m. Këtu krijohen vetëm raporte, jo dataset i pastruar.
