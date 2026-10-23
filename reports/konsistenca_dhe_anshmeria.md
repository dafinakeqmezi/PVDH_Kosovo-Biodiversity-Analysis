# Konsistenca dhe anshmëria

**Versioni:** 1.0  
**Data:** 22.10.2026  
**Statusi:** Tabela e konsistencës dhe paragrafi për anshmërinë.

## Varësia

Ky task zbaton dimensionin **Konsistenca** nga **Korniza e kualitetit** (`reports/korniza_e_kualitetit.md`, K2–K6) dhe përdor publikuesit nga **Analiza e burimeve** (`processed/sources_summary.csv`, 11 tetor). Llogaritja është te seksioni 3.11 i `notebooks/01_mbledhja_kualiteti.ipynb`.

## Tabela e konsistencës

Një rregull është konsistente kur çdo vlerë e kolonës majtas lidhet me **një** vlerë të kolonës djathtas. "Vlera" = vlera të ndryshme të kolonës majtas. "Aplikohen" = rreshta ku të dyja kolonat janë të plota.

| Rregulla | Vlera | Vlera jokonsistente | Aplikohen | Rreshta jokonsistentë | % konsistente | Shembuj |
|---|---:|---:|---:|---:|---:|---|
| species → genus (çdo specie ka një gjini) | 4,095 | 0 | 45,618 | 0 | 100.00 |  |
| species → genus (fjala e parë e species = genus) | 4,095 | 9 | 45,618 | 78 | 99.83 | Dicallomera fascelina → Calliteara; Hippurites archiaci → Vaccinites; Hippurites vesiculosus → Vaccinites |
| genus → family (pa kusht) | 2,408 | 3 | 46,615 | 119 | 99.74 | Aspicilia → Hymeneliaceae / Megasporaceae; Linaria → Fringillidae / Plantaginaceae; Prunella → Lamiaceae / Prunellidae |
| genus → family (brenda kingdom) | 2,410 | 1 | 46,615 | 4 | 99.99 | Aspicilia → Hymeneliaceae / Megasporaceae |
| family → order → class → phylum → kingdom | 980 | 0 | 185,868 | 0 | 100.00 |  |
| municipality → district (çdo komunë një rajon) | 38 | 0 | 46,831 | 0 | 100.00 |  |
| municipality → district (sipas ndarjes zyrtare, 7 rajone / 38 komuna) | 38 | 0 | 46,831 | 0 | 100.00 |  |

- **species → genus:** çdo specie ka saktësisht një gjini. Megjithatë, te **78 rreshta (9 specie)** emri i species nuk fillon me gjininë e kolonës `genus`. Emri dhe klasifikimi vijnë nga trajtime taksonomike të ndryshme: p.sh. GBIF e klasifikon *Lasiommata* nën gjininë *Pararge*, por emri i species mbetet *Lasiommata maera*. Shumica janë flutura dhe fosile:

| species | genus në dataset | Rreshta |
|---|---|---:|
| *Lasiommata maera* | *Pararge* | 39 |
| *Lasiommata megera* | *Pararge* | 28 |
| *Dicallomera fascelina* | *Calliteara* | 4 |
| *Spiris striata* | *Coscinia* | 2 |
| *Hippurites vesiculosus* | *Vaccinites* | 1 |
| *Hippurites archiaci* | *Vaccinites* | 1 |
| *Mastodon angustidens* | *Gomphotherium* | 1 |
| *Petrophora chlorosata* | *Pterophorus* | 1 |
| *Posidonomya moussoni* | *Daonella* | 1 |

- **genus → family:** pa kusht dalin 3 gjini me dy familje. `Linaria` dhe `Prunella` nuk janë gabime, sepse janë emra gjinish edhe te zogjtë edhe te bimët. Brenda të njëjtit `kingdom` mbetet vetëm **`Aspicilia`** (likene, 4 rreshta), që ka dy familje për shkak të një rishikimi taksonomik.
- **Pjesa tjetër e hierarkisë** (family → order → class → phylum → kingdom) është 100% konsistente.
- **municipality → district:** të 38 komunat i përkasin një rajoni, dhe ndarja përputhet 100% me ndarjen zyrtare të Kosovës në 7 rajone.

## Anshmëria

**Anshmëria.** Dataseti nuk është mostër e rastësishme e biodiversitetit të Kosovës. Ai pasqyron se ku dhe çka vëzhgojnë disa vëzhgues dhe platforma. **Sipas klasës**, zogjtë (Aves) japin 61.47% të regjistrimeve, por vetëm 6.23% të specieve. Insektet japin 24.65% të regjistrimeve dhe 54.36% të specieve, kurse bimët me lule (Magnoliopsida) 5.77% dhe 18.56%. **Sipas rajonit**, rajoni i Prishtinës ka 54.95% të regjistrimeve, dhe vetëm komuna e Graçanicës 31.33%. Arsyeja është që 27.86% e të gjithë datasetit vjen nga një pikë e vetme, hotspot-i i eBird te Ligatinat e Henc. Pa këtë pikë, pjesa e rajonit bie në 37.55%. Megjithatë, më shumë specie ka rajoni i Prizrenit (1,582 specie), me vetëm 11.25% të regjistrimeve. **Sipas burimit**, eBird jep 55.54% të regjistrimeve dhe 90.4% të regjistrimeve të zogjve. Një vëzhgues i vetëm (obsr1505715) ka 35.18% të të gjithë regjistrimeve. Prandaj numri i regjistrimeve për komunë, rajon ose klasë mat kryesisht përpjekjen e vëzhgimit, jo bollëkun ose pasurinë reale. Krahasimet duhet të mbështeten te numri i specieve unike ose te vlera të normalizuara (p.sh. për km², pas integrimit më 19–20 tetor), dhe rezultatet kryesore duhet të kontrollohen edhe pa eBird dhe pa pikën e Henc-it.

### Sipas klasës (10 klasat kryesore)

| Klasa | Regjistrime | % e regjistrimeve | Specie | % e specieve | Regjistrime për specie |
|---|---:|---:|---:|---:|---:|
| Aves | 28,785 | 61.47 | 255 | 6.23 | 112.9 |
| Insecta | 11,543 | 24.65 | 2,226 | 54.36 | 5.2 |
| Magnoliopsida | 2,701 | 5.77 | 760 | 18.56 | 3.6 |
| Liliopsida | 940 | 2.01 | 143 | 3.49 | 6.6 |
| Lecanoromycetes | 612 | 1.31 | 238 | 5.81 | 2.6 |
| (mungon) | 388 | 0.83 | 63 | 1.54 | 6.2 |
| Arachnida | 358 | 0.76 | 63 | 1.54 | 5.7 |
| Gastropoda | 279 | 0.60 | 48 | 1.17 | 5.8 |
| Mammalia | 273 | 0.58 | 51 | 1.25 | 5.4 |
| Squamata | 190 | 0.41 | 19 | 0.46 | 10.0 |
| të tjera (59) | 762 | 1.63 | 229 | 5.59 | 3.3 |

### Sipas rajonit

| Rajoni | Regjistrime | % e regjistrimeve | % pa Henc-in | Specie | % e specieve | Regjistrime për specie |
|---|---:|---:|---:|---:|---:|---:|
| Prishtinë / Priština | 25,734 | 54.95 | 37.55 | 1,491 | 36.41 | 17.3 |
| Prizren | 5,268 | 11.25 | 15.59 | 1,582 | 38.63 | 3.3 |
| Gjilan / Gnjilane | 4,156 | 8.87 | 12.30 | 974 | 23.79 | 4.3 |
| Mitrovicë / Kosovska Mitrovica | 3,196 | 6.82 | 9.46 | 1,034 | 25.25 | 3.1 |
| Pejë / Peć | 3,187 | 6.81 | 9.43 | 1,226 | 29.94 | 2.6 |
| Gjakovë / Đakovica | 2,697 | 5.76 | 7.98 | 1,090 | 26.62 | 2.5 |
| Ferizaj / Uroševac | 2,593 | 5.54 | 7.68 | 937 | 22.88 | 2.8 |

### Sipas burimit (10 publikuesit kryesorë)

| Publikuesi | Regjistrime | % e regjistrimeve | Specie | % e specieve | Klasa kryesore |
|---|---:|---:|---:|---:|---|
| Cornell Lab of Ornithology | 26,009 | 55.54 | 219 | 5.35 | Aves (100%) |
| HabiProt | 8,122 | 17.34 | 1,865 | 45.54 | Insecta (100%) |
| iNaturalist.org | 4,286 | 9.15 | 1,481 | 36.17 | Insecta (29%) |
| Observation.org | 1,436 | 3.07 | 395 | 9.65 | Aves (73%) |
| naturgucker.de | 721 | 1.54 | 398 | 9.72 | Magnoliopsida (45%) |
| Pl@ntNet | 660 | 1.41 | 279 | 6.81 | Magnoliopsida (94%) |
| University of Graz | 659 | 1.41 | 258 | 6.30 | Lecanoromycetes (89%) |
| VectorNet | 587 | 1.25 | 36 | 0.88 | Insecta (95%) |
| Macedonian Ecological Society | 483 | 1.03 | 137 | 3.35 | Insecta (74%) |
| Centro Internacional de Agricultura Tropical - CIAT | 386 | 0.82 | 32 | 0.78 | Liliopsida (91%) |
| të tjerë (70) | 3,482 | 7.44 | 733 | 17.90 |  |

### Përqendrimi

Sa regjistrime jep vlera më e shpeshtë e secilës kolonë, dhe sa japin 3 vlerat më të shpeshta.

| Dimensioni | Vlera më e shpeshtë | % | Top 3 % | Vlera të ndryshme |
|---|---|---:|---:|---:|
| klasa | Aves | 61.47 | 91.88 | 68 |
| rajoni | Prishtinë / Priština | 54.95 | 75.07 | 7 |
| komuna | Graçanicë / Gračanica | 31.33 | 52.51 | 38 |
| publikuesi | Cornell Lab of Ornithology | 55.54 | 82.03 | 80 |
| vëzhguesi (recordedBy) | obsr1505715 | 35.18 | 44.21 | 1,519 |
| pika (koordinatat) | 42.579243, 21.048304 | 27.86 | 36.77 | 7,567 |

## Vendimi dhe arsyetimi

- **Konsistenca është e lartë dhe nuk kërkon ndryshime të mëdha.** Rastet jokonsistente janë të pakta dhe të njohura: 78 rreshta te species/genus dhe 4 te `Aspicilia`. Propozimi: këto 9 specie të shënohen dhe të mos ndryshohen automatikisht, sepse të dy trajtimet ekzistojnë në literaturë. Për agregimet sipas gjinisë mjafton të përdoret një trajtim i vetëm, ai i kolonës `genus`.
- **Hierarkia kontrollohet brenda `kingdom`.** Emrat e gjinive përsëriten ndërmjet mbretërive, kështu që pa këtë kusht `Linaria` dhe `Prunella` do të dilnin gabimisht si gabime.
- **Anshmëria matet me dy përqindje: regjistrimet dhe speciet.** Raporti ndërmjet tyre tregon ku ka shumë regjistrime për pak specie. Te zogjtë janë 112.9 regjistrime për specie, te insektet 5.2.
- **Anshmëria nuk korrigjohet këtu.** Ajo dokumentohet, sepse ndikon interpretimin e agregimeve (21–23 tetor) dhe zgjedhjen e mostrës së shtresëzuar (24 tetor). Për këto hapa propozohet:
  - krahasimi i komunave me numrin e specieve unike, jo me regjistrimet;
  - normalizimi për km² dhe banorë pas integrimit;
  - kontrolli i rezultateve edhe pa eBird dhe pa pikën e Henc-it.

## Dokumentimi i detyrës

- **Input:** `dataset/kosovo_overall_biodiversity.csv` (`species`, `genus`, `family` deri `kingdom`, `municipality`, `district`, `class`, `recordedBy`, koordinatat), `processed/gbif_datasets_cache.csv` (publikuesit).
- **Çka u bë:** U kontrollua konsistenca species → genus → family dhe municipality → district, edhe kundrejt ndarjes zyrtare. U llogarit anshmëria si % e regjistrimeve dhe e specieve sipas klasës, rajonit dhe burimit, si dhe përqendrimi te vëzhguesi dhe pika.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 / 42.
- **Pse u bë:** Mospërputhjet taksonomike dhe administrative do të prishnin agregimet sipas gjinisë dhe rajonit. Anshmëria tregon çka mat realisht numri i regjistrimeve.
- **Output:** `reports/konsistenca_dhe_anshmeria.md`, `reports/01_konsistenca.csv`, `reports/01_anshmeria_klasa.csv`, `reports/01_anshmeria_rajoni.csv`, `reports/01_anshmeria_burimi.csv`, `reports/01_anshmeria_perqendrimi.csv`, `reports/01_anshmeria_paragrafi.md`, seksioni 3.11 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Add consistency checks and bias by class, region and source`.
