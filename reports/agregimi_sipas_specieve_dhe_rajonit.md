# Agregimi: speciet dhe rajoni

**Versioni:** 1.0  
**Data:** 25.10.2026  
**Statusi:** `processed/agg_class_district.csv` dhe `processed/agg_species.csv`.

## Varësia

`taxon_group` dhe `is_threatened` merren nga funksioni `add_taxon_features()` i Jetës (`03_vetite.ipynb`, 15 tetor). Rajoni dhe komuna merren nga emrat shqip të `district` dhe `municipality`. Llogaritja është te seksioni 6.3 i `notebooks/01_mbledhja_kualiteti.ipynb`. Puna bëhet mbi dataset-in origjinal, dhe më 26 tetor ri-ekzekutohet mbi `biodiversity_clean.csv`.

## 1. Tabela klasë × rajon

`processed/agg_class_district.csv`: 69 rreshta (68 klasa dhe `(mungon)`). Për çdo klasë ka `taxon_group`, totalet, dhe dy blloqe me 7 rajonet: `regjistrime_<rajoni>` dhe `specie_<rajoni>`. E gjithë tabela mblidhet në 46,831 regjistrime.

Regjistrimet, 15 klasat kryesore:

| Klasa | taxon_group | Gjithsej | Specie | Ferizaj | Gjakovë | Gjilan | Mitrovicë | Pejë | Prishtinë | Prizren |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Aves | Zogj | 28,785 | 255 | 772 | 747 | 1,403 | 646 | 1,064 | 22,607 | 1,546 |
| Insecta | Insekte | 11,543 | 2,226 | 1,273 | 874 | 2,526 | 1,945 | 1,054 | 1,548 | 2,323 |
| Magnoliopsida | Bimë | 2,701 | 760 | 277 | 284 | 79 | 101 | 454 | 912 | 594 |
| Liliopsida | Bimë | 940 | 143 | 68 | 99 | 79 | 207 | 78 | 266 | 143 |
| Lecanoromycetes | Kërpudha | 612 | 238 | 1 | 306 | 0 | 2 | 32 | 7 | 264 |
| (mungon) | E panjohur | 388 | 63 | 4 | 58 | 8 | 154 | 85 | 9 | 70 |
| Arachnida | Tjera | 358 | 63 | 13 | 33 | 24 | 22 | 107 | 70 | 89 |
| Gastropoda | Tjera | 279 | 48 | 76 | 19 | 3 | 11 | 72 | 72 | 26 |
| Mammalia | Tjera | 273 | 51 | 43 | 13 | 11 | 23 | 38 | 69 | 76 |
| Squamata | Tjera | 190 | 19 | 17 | 18 | 8 | 9 | 23 | 66 | 49 |
| Agaricomycetes | Kërpudha | 187 | 75 | 14 | 93 | 3 | 3 | 22 | 41 | 11 |
| Amphibia | Tjera | 109 | 14 | 10 | 21 | 3 | 2 | 26 | 27 | 20 |
| Eurotiomycetes | Kërpudha | 49 | 15 | 0 | 33 | 0 | 0 | 6 | 0 | 10 |
| Polypodiopsida | Bimë | 49 | 16 | 5 | 6 | 5 | 1 | 17 | 2 | 13 |
| Clitellata | Tjera | 43 | 20 | 5 | 4 | 1 | 15 | 9 | 3 | 6 |

Pjesa e klasave brenda çdo rajoni (%), 8 klasat kryesore:

| Klasa | Ferizaj | Gjakovë | Gjilan | Mitrovicë | Pejë | Prishtinë | Prizren |
|---|---:|---:|---:|---:|---:|---:|---:|
| Aves | 29.8 | 27.7 | 33.8 | 20.2 | 33.4 | 87.8 | 29.3 |
| Insecta | 49.1 | 32.4 | 60.8 | 60.9 | 33.1 | 6.0 | 44.1 |
| Magnoliopsida | 10.7 | 10.5 | 1.9 | 3.2 | 14.2 | 3.5 | 11.3 |
| Liliopsida | 2.6 | 3.7 | 1.9 | 6.5 | 2.4 | 1.0 | 2.7 |
| Lecanoromycetes | 0.0 | 11.3 | 0.0 | 0.1 | 1.0 | 0.0 | 5.0 |
| (mungon) | 0.2 | 2.2 | 0.2 | 4.8 | 2.7 | 0.0 | 1.3 |
| Arachnida | 0.5 | 1.2 | 0.6 | 0.7 | 3.4 | 0.3 | 1.7 |
| Gastropoda | 2.9 | 0.7 | 0.1 | 0.3 | 2.3 | 0.3 | 0.5 |

- **Rajoni i Prishtinës ka 22,607 regjistrime zogjsh**, 78.5% e të gjithë zogjve, kryesisht nga Ligatinat e Henc (`reports/konsistenca_dhe_anshmeria.md`). Në 5 nga 6 rajonet e tjera insektet janë grupi më i madh. Në Pejë zogjtë (1,064) janë pak para insekteve (1,054).
- **Likenet (`Lecanoromycetes`) janë pothuajse vetëm në Gjakovë (306) dhe Prizren (264).** 589 nga 612 regjistrime vijnë nga University of Graz. Kjo tregon ku ka mbledhur një herbarium, jo shpërndarjen natyrore të likeneve.
- **Klasa mungon te 388 regjistrime, dhe 264 prej tyre janë peshq** (rendet Cypriniformes, Perciformes, Salmoniformes etj.), sepse GBIF nuk u jep klasë peshqve me rrezatim (Actinopterygii) në këtë dataset. Prandaj ata dalin te `taxon_group = "E panjohur"`, megjithëse specia dihet.

## 2. Tabela në nivel specieje

`processed/agg_species.csv`: një rresht për secilën nga 4,095 speciet.

| Kolona | Kuptimi |
|---|---|
| `kingdom`, `class`, `family`, `taxon_group` | klasifikimi; çdo specie ka një klasë dhe një kategori IUCN |
| `iucnRedListCategory` | kategoria IUCN (edhe NE dhe DD) |
| `regjistrime` | numri i regjistrimeve |
| `viti_i_pare`, `viti_i_fundit` | viti më i hershëm dhe më i vonë me regjistrim |
| `vite_me_regjistrime` | sa vite të ndryshme kanë regjistrim |
| `regjistrime_pa_vit` | regjistrime pa `year` (nuk hyjnë te viti i parë dhe i fundit) |
| `komuna`, `rajone` | në sa komuna dhe rajone është regjistruar |

Përmbledhje:

| | Specie |
|---|---:|
| specie gjithsej | 4,095 |
| specie me 1 regjistrim (singletons) | 1,727 |
| specie në vetëm 1 komunë | 2,155 |
| specie në të 7 rajonet | 156 |
| specie pa asnjë vit | 416 |
| specie të parë për herë të fundit para 2000 | 754 |
| specie të parë për herë të fundit para 1950 | 68 |
| specie të reja (viti i parë ≥ 2020) | 779 |

20 speciet me më shumë regjistrime:

| Specia | Klasa | taxon_group | IUCN | Regjistrime | Viti i parë | Viti i fundit | Komuna | Rajone |
|---|---|---|---|---:|---:|---:|---:|---:|
| *Columba livia* | Aves | Zogj | LC | 1,025 | 1,998 | 2,026 | 31 | 7 |
| *Pica pica* | Aves | Zogj | LC | 949 | 1,999 | 2,026 | 25 | 7 |
| *Anas platyrhynchos* | Aves | Zogj | LC | 714 | 1,984 | 2,026 | 25 | 7 |
| *Corvus cornix* | Aves | Zogj | NE | 676 | 2,001 | 2,026 | 28 | 7 |
| *Passer montanus* | Aves | Zogj | LC | 669 | 2,002 | 2,026 | 24 | 7 |
| *Ardea cinerea* | Aves | Zogj | LC | 669 | 1,984 | 2,026 | 23 | 7 |
| *Corvus corax* | Aves | Zogj | LC | 645 | 2,001 | 2,026 | 30 | 7 |
| *Sturnus vulgaris* | Aves | Zogj | LC | 645 | 1,999 | 2,026 | 21 | 7 |
| *Buteo buteo* | Aves | Zogj | LC | 624 | 2,001 | 2,026 | 31 | 7 |
| *Coloeus monedula* | Aves | Zogj | NE | 617 | 1,999 | 2,026 | 27 | 7 |
| *Hirundo rustica* | Aves | Zogj | LC | 595 | 1,999 | 2,026 | 28 | 7 |
| *Falco tinnunculus* | Aves | Zogj | LC | 574 | 2,000 | 2,026 | 28 | 7 |
| *Parus major* | Aves | Zogj | LC | 565 | 2,002 | 2,026 | 29 | 7 |
| *Fulica atra* | Aves | Zogj | LC | 560 | 1,998 | 2,026 | 10 | 4 |
| *Streptopelia decaocto* | Aves | Zogj | LC | 497 | 1,984 | 2,026 | 25 | 7 |
| *Circus aeruginosus* | Aves | Zogj | LC | 437 | 2,001 | 2,026 | 10 | 6 |
| *Vanellus vanellus* | Aves | Zogj | NT | 423 | 2,001 | 2,026 | 11 | 5 |
| *Passer domesticus* | Aves | Zogj | LC | 418 | 1,999 | 2,026 | 24 | 7 |
| *Motacilla flava* | Aves | Zogj | LC | 416 | 2,001 | 2,026 | 15 | 7 |
| *Tachybaptus ruficollis* | Aves | Zogj | LC | 411 | 2,001 | 2,026 | 9 | 5 |

### Speciet e kërcënuara

37 specie kanë kategorinë VU, EN ose CR:

| Specia | Klasa | taxon_group | IUCN | Regjistrime | Viti i parë | Viti i fundit | Komuna | Rajone |
|---|---|---|---|---:|---:|---:|---:|---:|
| *Anguilla anguilla* | – | E panjohur | CR | 3 | 1,992 | 1,992 | 3 | 3 |
| *Cheilosia balkana* | Insecta | Insekte | EN | 11 | 1,997 | 2,016 | 1 | 1 |
| *Schistostege decussata* | Insecta | Insekte | EN | 2 | 1,979 | 1,979 | 2 | 2 |
| *Alburnoides prespensis* | – | E panjohur | EN | 2 | 1,985 | 1,992 | 1 | 1 |
| *Phoxinus strymonicus* | – | E panjohur | EN | 1 | 2,010 | 2,010 | 1 | 1 |
| *Pipizella bispina* | Insecta | Insekte | EN | 1 | 2,016 | 2,016 | 1 | 1 |
| *Anser cygnoides* | Aves | Zogj | EN | 1 | 2,025 | 2,025 | 1 | 1 |
| *Aythya ferina* | Aves | Zogj | VU | 382 | 2,001 | 2,026 | 4 | 2 |
| *Streptopelia turtur* | Aves | Zogj | VU | 110 | 1,984 | 2,026 | 22 | 7 |
| *Salamandra salamandra* | Amphibia | Tjera | VU | 24 | 2,012 | 2,026 | 12 | 7 |
| *Morimus funereus* | Insecta | Insekte | VU | 22 | 1,954 | 2,026 | 8 | 5 |
| *Testudo hermanni* | Testudines | Tjera | VU | 21 | 2,007 | 2,026 | 9 | 6 |
| *Falco vespertinus* | Aves | Zogj | VU | 13 | 2,015 | 2,026 | 6 | 3 |
| *Astacus astacus* | Malacostraca | Tjera | VU | 12 | 2,009 | 2,014 | 2 | 2 |
| *Dinaromys bogdanovi* | Mammalia | Tjera | VU | 7 | 1,978 | 1,978 | 4 | 4 |
| *Aesculus hippocastanum* | Magnoliopsida | Bimë | VU | 4 | 2,021 | 2,026 | 1 | 1 |
| *Triturus macedonicus* | Amphibia | Tjera | VU | 3 | 2,018 | 2,023 | 2 | 2 |
| *Heliothis maritima* | Insecta | Insekte | VU | 3 | 1,979 | 1,979 | 3 | 3 |
| *Salmo marmoratus* | – | E panjohur | VU | 3 | 1,992 | 1,992 | 3 | 2 |
| *Rosalia alpina* | Insecta | Insekte | VU | 3 | 2,009 | 2,025 | 3 | 2 |
| *Diaphora sordida* | Insecta | Insekte | VU | 2 | 1,972 | 1,995 | 2 | 2 |
| *Calidris ferruginea* | Aves | Zogj | VU | 2 | 2,021 | 2,022 | 1 | 1 |
| *Cerambyx cerdo* | Insecta | Insekte | VU | 2 |  |  | 2 | 2 |
| *Monachoides kosovoensis* | Gastropoda | Tjera | VU | 2 |  |  | 1 | 1 |
| *Montana macedonica* | Insecta | Insekte | VU | 2 | 1,966 | 1,966 | 1 | 1 |
| *Merodon virgatus* | Insecta | Insekte | VU | 1 | 1,994 | 1,994 | 1 | 1 |
| *Nebula nebulata* | Insecta | Insekte | VU | 1 |  |  | 1 | 1 |
| *Bythinella istoka* | Gastropoda | Tjera | VU | 1 |  |  | 1 | 1 |
| *Oropodisma macedonica* | Insecta | Insekte | VU | 1 | 1,995 | 1,995 | 1 | 1 |
| *Panchrysia vargenteum* | Insecta | Insekte | VU | 1 | 1,979 | 1,979 | 1 | 1 |
| *Perizoma lugdunaria* | Insecta | Insekte | VU | 1 | 1,981 | 1,981 | 1 | 1 |
| *Plagigeyeria steffeki* | Gastropoda | Tjera | VU | 1 |  |  | 1 | 1 |
| *Anser erythropus* | Aves | Zogj | VU | 1 | 2,000 | 2,000 | 1 | 1 |
| *Andreiniimon nuptialis* | Insecta | Insekte | VU | 1 | 2,022 | 2,022 | 1 | 1 |
| *Eupithecia undata* | Insecta | Insekte | VU | 1 | 1,979 | 1,979 | 1 | 1 |
| *Terranigra kosovica* | Gastropoda | Tjera | VU | 1 |  |  | 1 | 1 |
| *Unio carneus* | Bivalvia | Tjera | VU | 1 | 2,017 | 2,017 | 1 | 1 |

## Interpretimi dhe kufizimet

- **42.2% e specieve (1,727) kanë vetëm një regjistrim, dhe 52.6% (2,155) janë vetëm në një komunë.** Shumica e specieve janë regjistruar rrallë. Numri i komunave për specie mat më shumë përpjekjen e vëzhgimit sesa përhapjen reale.
- **754 specie nuk janë regjistruar pas vitit 2000** (68 para vitit 1950). Kjo nuk do të thotë se janë zhdukur: shumë vijnë nga koleksione dhe literaturë të vjetër, dhe ato grupe nuk janë vëzhguar sistematikisht më pas.
- **779 specie janë regjistruar për herë të parë në vitin 2020 e më vonë.** Regjistrimi i parë i tyre vjen kryesisht nga iNaturalist (405), HabiProt (168) dhe Pl@ntNet (80). Mediana është 1 regjistrim për specie, shumica janë insekte (344) dhe bimë me lule (219), dhe 617 nuk janë të vlerësuara nga IUCN (NE). Kjo pasqyron hyrjen e platformave të reja, jo domosdoshmërisht specie të reja për Kosovën.
- **Viti i parë dhe i fundit ndikohen nga data zëvendësuese 30 nëntor** te 3,598 regjistrime të HabiProt (`reports/agregimi_sipas_kohes.md`), sepse viti i tyre i përket vitit të burimit në literaturë.
- **Speciet e kërcënuara përfshijnë raste që duhen kontrolluar.** *Anser cygnoides* (EN, 1 regjistrim, Pejë 2025) nuk jeton i egër në Ballkan dhe ka shumë gjasa të jetë shpend shtëpiak. Disa peshq të kërcënuar (*Anguilla anguilla*, *Alburnoides prespensis*, *Phoxinus strymonicus*) kanë `class` bosh, për arsyen e mësipërme.

## Shënime për grupin

- **Jeta (`taxon_group`):** 264 regjistrime peshqish dalin "E panjohur" sepse `class` mungon. Mund të shtosh një rregull sipas `order` (p.sh. Cypriniformes, Perciformes, Salmoniformes → "Tjera" ose grup i veçantë "Peshq"). Vendimi është i yti. Agregimet e mia do ta ndjekin vetë funksionin tënd.
- **Deliza (validimi):** *Anser cygnoides* dhe data 30 nëntor janë kandidatë për flamur.

## Dokumentimi i detyrës

- **Input:** `dataset/kosovo_overall_biodiversity.csv`, `add_taxon_features()` nga `03_vetite.ipynb`.
- **Çka u bë:** U krijua tabela klasë × rajon me regjistrime dhe specie unike, dhe tabela në nivel specieje me vitin e parë dhe të fundit, numrin e komunave dhe numrin e regjistrimeve.
- **Rreshta para / pas:** 46,831 rreshta → 69 rreshta (klasa) dhe 4,095 rreshta (specie).
- **Kolona para / pas:** `agg_class_district.csv` 18 kolona; `agg_species.csv` 14 kolona (`species` + 13).
- **Pse u bë:** Për të parë cilat grupe janë regjistruar ku, dhe për të pasur për çdo specie përhapjen dhe periudhën e regjistrimit.
- **Output:** `processed/agg_class_district.csv`, `processed/agg_species.csv`, `reports/agregimi_sipas_specieve_dhe_rajonit.md`, `reports/01_specie_permbledhje.csv`, `reports/01_specie_te_kercenuara.csv`, seksioni 6.3 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Add class x district and species-level aggregates`.
