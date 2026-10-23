# Agregimi: komuna dhe grupi taksonomik

**Versioni:** 1.0  
**Data:** 22.10.2026  
**Statusi:** `processed/agg_municipality.csv` dhe `processed/agg_municipality_taxon.csv`.

## Varësia

- **Integrimi** (20 tetor): `processed/biodiversity_municipalities.csv` jep sipërfaqen dhe popullsinë e çdo komune.
- **`taxon_group` dhe `is_threatened`** (Jeta, 15 tetor): funksioni i Jetës ende nuk është te `03_vetite.ipynb`. Prandaj përdoret një version i përkohshëm, që ndjek saktësisht definicionin e planit, dhe zëvendësohet kur Jeta ta shtojë funksionin e saj.

Llogaritja është te seksioni 6 i `notebooks/01_mbledhja_kualiteti.ipynb`. Puna bëhet mbi dataset-in origjinal. Më 26 tetor ri-ekzekutohet mbi `biodiversity_clean.csv`.

## Definicionet

| Metrika | Definicioni |
|---|---|
| `regjistrime` | numri i rreshtave në komunë |
| `specie_unike` | numri i vlerave të ndryshme të `species` (vetëm identifikimet deri në species) |
| `specie_te_kercenuara` | specie unike me `iucnRedListCategory` VU, EN ose CR. NE, DD dhe NaN nuk numërohen. EX (1 rresht) nuk numërohet. |
| `specie_per_km2` | `specie_unike` / `siperfaqja_njesise_km2`. Te dy Mitrovicat llogaritet për njësinë e përbashkët (336.18 km²), që speciet e përbashkëta të mos numërohen dy herë. |
| `regjistrime_per_1000_banore` | `regjistrime` / `popullsia_2024` × 1,000. Te 4 komunat veriore, popullsia është vlerësim i ASK. |

**`taxon_group`** (sipas planit, nga `class`):

| taxon_group | Rregulla | Regjistrime | Klasa | Klasat kryesore |
|---|---|---:|---:|---|
| Zogj | `class` = Aves | 28,785 | 1 | Aves |
| Insekte | `class` = Insecta | 11,543 | 1 | Insecta |
| Bimë | `kingdom` = Plantae (me `class`) | 3,738 | 11 | Magnoliopsida, Liliopsida, Polypodiopsida |
| Kërpudha | `kingdom` = Fungi (me `class`, përfshirë likenet) | 971 | 22 | Lecanoromycetes, Agaricomycetes, Eurotiomycetes |
| Tjera | çdo klasë tjetër | 1,406 | 33 | Arachnida, Gastropoda, Mammalia |
| E panjohur | `class` mungon | 388 | 0 |  |

## Agregimi sipas komunës

Renditur sipas numrit të regjistrimeve.

| Komuna | Rajoni | Regjistrime | % | Specie unike | Specie të kërcënuara | Popullsia 2024 | Sipërfaqja e njësisë (km²) | Specie/km² | Regjistrime/1,000 banorë |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Graçanicë | Prishtinë | 14,672 | 31.33 | 334 | 3 | 18,486 | 122.41 | 2.729 | 793.68 |
| Prishtinë | Prishtinë | 5,924 | 12.65 | 1,149 | 13 | 227,466 | 523.13 | 2.196 | 26.04 |
| Prizren | Prizren | 3,993 | 8.53 | 1,243 | 12 | 147,246 | 626.86 | 1.983 | 27.12 |
| Fushë Kosovë | Prishtinë | 3,567 | 7.62 | 180 | 4 | 63,949 | 84.09 | 2.141 | 55.78 |
| Kamenicë | Gjilan | 2,724 | 5.82 | 792 | 4 | 22,868 | 416.61 | 1.901 | 119.12 |
| Pejë | Pejë | 2,449 | 5.23 | 1,049 | 9 | 82,745 | 602.63 | 1.741 | 29.60 |
| Leposaviq | Mitrovicë | 1,625 | 3.47 | 647 | 3 | 9,485* | 539.05 | 1.200 | 171.32 |
| Deçan | Gjakovë | 1,403 | 3.00 | 729 | 5 | 27,775 | 293.97 | 2.480 | 50.51 |
| Shtërpcë | Ferizaj | 1,160 | 2.48 | 582 | 7 | 10,771 | 247.70 | 2.350 | 107.70 |
| Ranillug | Gjilan | 984 | 2.10 | 247 | 2 | 2,481 | 77.62 | 3.182 | 396.61 |
| Dragash | Prizren | 939 | 2.01 | 475 | 3 | 28,896 | 433.85 | 1.095 | 32.50 |
| Kaçanik | Ferizaj | 694 | 1.48 | 367 | 3 | 27,716 | 211.28 | 1.737 | 25.04 |
| Junik | Gjakovë | 549 | 1.17 | 262 | 2 | 3,943 | 77.78 | 3.368 | 139.23 |
| Gjakovë | Gjakovë | 526 | 1.12 | 265 | 5 | 78,699 | 586.62 | 0.452 | 6.68 |
| Mitrovicë e Jugut | Mitrovicë | 479 | 1.02 | 253 | 2 | 64,742 | 336.18† | 0.797 | 7.40 |
| Lipjan | Prishtinë | 465 | 0.99 | 237 | 5 | 55,044 | 338.41 | 0.700 | 8.45 |
| Klinë | Pejë | 397 | 0.85 | 240 | 4 | 30,503 | 309.02 | 0.777 | 13.02 |
| Hani i Elezit | Ferizaj | 347 | 0.74 | 191 | 2 | 8,533 | 83.11 | 2.298 | 40.67 |
| Novobërdë | Prishtinë | 347 | 0.74 | 206 | 0 | 4,493 | 203.98 | 1.010 | 77.23 |
| Istog | Pejë | 341 | 0.73 | 152 | 3 | 33,008 | 454.36 | 0.335 | 10.33 |
| Ferizaj | Ferizaj | 337 | 0.72 | 158 | 3 | 109,255 | 344.61 | 0.458 | 3.08 |
| Zveçan | Mitrovicë | 333 | 0.71 | 197 | 0 | 2,867* | 123.01 | 1.601 | 116.15 |
| Podujevë | Prishtinë | 316 | 0.67 | 187 | 0 | 70,975 | 632.59 | 0.296 | 4.45 |
| Obiliq | Prishtinë | 303 | 0.65 | 114 | 1 | 22,815 | 104.84 | 1.087 | 13.28 |
| Vushtrri | Mitrovicë | 301 | 0.64 | 172 | 3 | 61,528 | 344.85 | 0.499 | 4.89 |
| Zubin Potok | Mitrovicë | 270 | 0.58 | 117 | 2 | 3,385* | 334.38 | 0.350 | 79.76 |
| Gjilan | Gjilan | 263 | 0.56 | 164 | 1 | 82,980 | 391.84 | 0.419 | 3.17 |
| Rahovec | Gjakovë | 219 | 0.47 | 132 | 1 | 41,799 | 275.90 | 0.478 | 5.24 |
| Suharekë | Prizren | 170 | 0.36 | 94 | 0 | 45,749 | 361.04 | 0.260 | 3.72 |
| Malishevë | Prizren | 165 | 0.35 | 111 | 0 | 43,888 | 306.42 | 0.362 | 3.76 |
| Skenderaj | Mitrovicë | 164 | 0.35 | 114 | 2 | 40,664 | 374.37 | 0.305 | 4.03 |
| Viti | Gjilan | 148 | 0.32 | 41 | 0 | 35,566 | 269.69 | 0.152 | 4.16 |
| Gllogoc | Prishtinë | 140 | 0.30 | 95 | 1 | 48,079 | 275.63 | 0.345 | 2.91 |
| Shtime | Ferizaj | 55 | 0.12 | 45 | 2 | 24,308 | 134.42 | 0.335 | 2.26 |
| Mitrovicë e Veriut | Mitrovicë | 24 | 0.05 | 22 | 0 | 7,920* | 336.18† | 0.797 | 3.03 |
| Partesh | Gjilan | 24 | 0.05 | 23 | 0 | 3,240 | 28.67 | 0.802 | 7.41 |
| Kllokot | Gjilan | 13 | 0.03 | 13 | 1 | 3,041 | 23.39 | 0.556 | 4.27 |
| Mamushë | Prizren | 1 | 0.00 | 1 | 0 | 5,607 | 10.94 | 0.091 | 0.18 |

\* popullsia është vlerësim i ASK.  
† Mitrovicë e Jugut + Mitrovicë e Veriut bashkë.

## Matrica komunë × taxon_group

`processed/agg_municipality_taxon.csv` ka 38 rreshta (komunat) dhe dy blloqe kolonash:

- `regjistrime_<grupi>`: numri i regjistrimeve;
- `specie_<grupi>`: numri i specieve unike.

Shuma e `regjistrime_*` në çdo rresht është e barabartë me `regjistrime` e komunës, dhe e gjithë matrica mblidhet në 46,831.

Regjistrimet sipas grupit (blloku `regjistrime_*`):

| Komuna | Zogj | Insekte | Bimë | Kërpudha | Tjera | E panjohur |
|---|---:|---:|---:|---:|---:|---:|
| Graçanicë | 14,460 | 129 | 57 | 0 | 26 | 0 |
| Prishtinë | 3,806 | 1,009 | 846 | 51 | 209 | 3 |
| Prizren | 1,437 | 1,734 | 563 | 14 | 186 | 59 |
| Fushë Kosovë | 3,496 | 16 | 21 | 0 | 34 | 0 |
| Kamenicë | 532 | 2,118 | 38 | 3 | 33 | 0 |
| Pejë | 766 | 892 | 427 | 104 | 204 | 56 |
| Leposaviq | 166 | 1,320 | 59 | 0 | 38 | 42 |
| Deçan | 289 | 512 | 173 | 343 | 66 | 20 |
| Shtërpcë | 290 | 630 | 180 | 13 | 47 | 0 |
| Ranillug | 713 | 251 | 18 | 0 | 2 | 0 |
| Dragash | 73 | 433 | 93 | 280 | 58 | 2 |
| Kaçanik | 199 | 314 | 83 | 4 | 94 | 0 |
| Junik | 190 | 96 | 95 | 144 | 21 | 3 |
| Gjakovë | 195 | 204 | 58 | 4 | 33 | 32 |
| Mitrovicë e Jugut | 75 | 176 | 139 | 3 | 36 | 50 |
| Lipjan | 306 | 83 | 54 | 1 | 21 | 0 |
| Klinë | 135 | 95 | 99 | 1 | 39 | 28 |
| Hani i Elezit | 138 | 167 | 22 | 0 | 16 | 4 |
| Novobërdë | 135 | 168 | 37 | 0 | 6 | 1 |
| Istog | 163 | 67 | 39 | 1 | 70 | 1 |
| Ferizaj | 142 | 132 | 54 | 0 | 9 | 0 |
| Zveçan | 8 | 243 | 9 | 0 | 15 | 58 |
| Podujevë | 106 | 66 | 118 | 3 | 19 | 4 |
| Obiliq | 246 | 43 | 10 | 0 | 3 | 1 |
| Vushtrri | 156 | 84 | 38 | 2 | 20 | 1 |
| Zubin Potok | 141 | 74 | 34 | 0 | 20 | 1 |
| Gjilan | 85 | 99 | 54 | 0 | 17 | 8 |
| Rahovec | 73 | 62 | 68 | 0 | 13 | 3 |
| Suharekë | 6 | 110 | 51 | 0 | 3 | 0 |
| Malishevë | 30 | 45 | 53 | 0 | 28 | 9 |
| Skenderaj | 94 | 43 | 23 | 0 | 4 | 0 |
| Viti | 43 | 56 | 48 | 0 | 1 | 0 |
| Gllogoc | 52 | 34 | 44 | 0 | 10 | 0 |
| Shtime | 3 | 30 | 19 | 0 | 3 | 0 |
| Mitrovicë e Veriut | 6 | 5 | 9 | 0 | 2 | 2 |
| Partesh | 18 | 1 | 5 | 0 | 0 | 0 |
| Kllokot | 12 | 1 | 0 | 0 | 0 | 0 |
| Mamushë | 0 | 1 | 0 | 0 | 0 | 0 |

## Kontrollet

| Kontrolli | Rezultati |
|---|---|
| 38 komuna në të dyja tabelat | kalon |
| Regjistrimet mblidhen në 46,831 | kalon |
| Matrica: shuma e rreshtit = regjistrimet e komunës | kalon |
| Matrica mblidhet në 46,831 | kalon |
| Speciet e kërcënuara ≤ speciet unike | kalon |
| Pa vlera bosh te specie/km² dhe regjistrime/1,000 banorë | kalon |

Disa vlera u rillogaritën edhe me kod të pavarur nga CSV-ja origjinale (Graçanicë, Prizren, Junik, Zveçan, Mitrovicë e Veriut, dhe njësia e Mitrovicës) dhe përputhen.

## Interpretimi dhe kufizimet

- **Graçanica ka 31.33% të regjistrimeve dhe 793.68 regjistrime për 1,000 banorë**, por vetëm 334 specie. Shkaku është hotspot-i i eBird te Ligatinat e Henc, ku 98.6% e regjistrimeve janë zogj. Numri i regjistrimeve mat përpjekjen e vëzhgimit, jo pasurinë.
- **Më shumë specie kanë Prizren (1,243), Prishtinë (1,149), Pejë (1,049).** Këto janë komuna të mëdha (523–627 km²), me shumë burime dhe vëzhgues. Në 28 nga 38 komunat ka 0–3 specie të kërcënuara.
- **`specie_per_km2` varet nga madhësia e komunës.** Numri i specieve nuk rritet në proporcion me sipërfaqen (marrëdhënia specie–sipërfaqe), kështu që komunat e vogla, si Junik dhe Ranillug, dalin më lart. Krahasimet duhet të bëhen ndërmjet komunave me madhësi të ngjashme, ose të interpretohen me kujdes.
- **Speciet e kërcënuara janë të pakta: 37 specie në tërë Kosovën.** Shumica e komunave kanë 0–3, kështu që dallimet ndërmjet komunave janë të paqëndrueshme.

## Shënime për Jetën (PCA, 23 tetor)

- Për PCA-në përdor njërin bllok: `regjistrime_*` (përpjekja/bollëku) ose `specie_*` (pasuria). Mos i përziej.
- Siç thotë plani, kthej numrat në proporcione ose `log1p` para standardizimit. Graçanica dhe Fushë Kosova kanë mbi 3,400 regjistrime zogjsh secila dhe do ta dominonin PCA-në me numra absolutë.
- Kur ta shtosh `taxon_group` te `03_vetite.ipynb`, ma thuaj, që ta zëvendësoj versionin e përkohshëm në seksionin 6.

## Dokumentimi i detyrës

- **Input:** `dataset/kosovo_overall_biodiversity.csv`, `processed/biodiversity_municipalities.csv` (sipërfaqja dhe popullsia).
- **Çka u bë:** U llogaritën për çdo komunë regjistrimet, speciet unike, speciet e kërcënuara, specie/km² dhe regjistrime për 1,000 banorë. U krijua matrica komunë × taxon_group me regjistrime dhe specie.
- **Rreshta para / pas:** 46,831 rreshta → 38 rreshta (komuna).
- **Kolona para / pas:** `agg_municipality.csv` 13 kolona; `agg_municipality_taxon.csv` 13 kolona (rajoni + 6 grupe × 2).
- **Pse u bë:** Për të krahasuar komunat dhe për të përgatitur inputin e PCA-së.
- **Output:** `processed/agg_municipality.csv`, `processed/agg_municipality_taxon.csv`, `reports/agregimi_sipas_komunes.md`, `reports/01_hartezimi_i_grupeve_taksonomike.csv`, seksioni 6 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Add municipality aggregates and municipality x taxon group matrix`.
