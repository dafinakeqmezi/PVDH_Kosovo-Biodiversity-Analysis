# Rikalkulimi mbi të dhënat e pastra

**Versioni:** 1.0  
**Data:** 29.10.2026  
**Statusi:** CSV-të e agreguara v2 dhe tabela e diferencave.

## Varësia

Input-i është **`processed/biodiversity_clean.csv`** i Delizës, checkpoint-i i 25 tetorit, me statusin `frozen` te `biodiversity_clean_manifest.json`. Llogaritja është te seksioni 8 i `notebooks/01_mbledhja_kualiteti.ipynb`.

Para përdorimit, SHA-256 i skedarit kontrollohet me manifestin. Në Windows, Git (`core.autocrlf = true`) i kthen rreshtat nga LF në CRLF, kështu që hash-i llogaritet pasi CRLF të kthehet në LF. Në git, skedari ruhet me LF dhe hash-i përputhet saktësisht.

## Çka ndryshon te të dhënat e pastra

- **375 rreshta më pak** (46,831 → 46,456): duplikatët e larguar nga Deliza (`processed/rreshtat_e_larguar_duplikate.csv`).
- Të 375 bëjnë pjesë te definicioni i propozuar te `reports/unikaliteti.md`: Deliza pranoi 235 nga 238 grupet e propozuara, me kriteret shtesë te `reports/vendimi_per_duplikatet.md`.
- Sipas publikuesit: eBird 143, Observation.org 117, Macedonian Ecological Society 61, iNaturalist 22, BOLD 19, Xeno-canto 10.
- **Në rreshtat e mbetur, kolonat që përdorin agregimet janë identike** me origjinalin: `species`, `class`, `kingdom`, `iucnRedListCategory`, `municipality`, `district`, `year`, `month`, `day`, `datasetKey`, koordinatat. `year` dhe `month` nuk u plotësuan (`year_was_filled` dhe `month_was_filled` janë `False` kudo), sepse Deliza vendosi të mos imputojë.

Pra diferencat ndërmjet v1 dhe v2 vijnë **vetëm nga largimi i duplikatëve**.

## Si u ri-ekzekutua

1. Logjika e seksioneve 5.2 (bashkimi), 6, 6.2 dhe 6.3 (agregimet) u shkrua si funksione.
2. **Kontroll:** funksionet u ekzekutuan mbi dataset-in origjinal dhe dhanë **saktësisht** 5 CSV-të v1. Kështu v2 ndryshon vetëm për shkak të të dhënave, jo të kodit.
3. Funksionet u ekzekutuan mbi `biodiversity_clean.csv`. Bashkimi me komunat: 38/38, 46,456 rreshta para dhe pas.
4. Rezultati u ruajt si `*_v2.csv`, pa e mbishkruar v1.

| v1 (dataset-i origjinal) | v2 (të dhënat e pastra) |
|---|---|
| `processed/agg_municipality.csv` | `processed/agg_municipality_v2.csv` |
| `processed/agg_municipality_taxon.csv` | `processed/agg_municipality_taxon_v2.csv` |
| `processed/agg_time.csv` | `processed/agg_time_v2.csv` |
| `processed/agg_class_district.csv` | `processed/agg_class_district_v2.csv` |
| `processed/agg_species.csv` | `processed/agg_species_v2.csv` |

## Tabela e diferencave

| Treguesi | Origjinal | I pastër | Diferenca | Diferenca % |
|---|---:|---:|---:|---:|
| rreshta | 46,831 | 46,456 | -375 | -0.80 |
| rreshta me species | 45,618 | 45,243 | -375 | -0.82 |
| specie unike | 4,095 | 4,095 | +0 | +0.00 |
| specie të kërcënuara (VU, EN, CR) | 37 | 37 | +0 | +0.00 |
| klasa (me (mungon)) | 69 | 69 | +0 | +0.00 |
| rreshta me vit | 44,563 | 44,188 | -375 | -0.84 |
| vite me regjistrime | 102 | 102 | +0 | +0.00 |
| komuna (bashkimi 38/38) | 38 | 38 | +0 | +0.00 |
| regjistrime Graçanicë | 14,672 | 14,563 | -109 | -0.74 |
| regjistrime zogj (Aves) | 28,785 | 28,532 | -253 | -0.88 |
| data 30 nëntor (HabiProt) | 3,598 | 3,598 | +0 | +0.00 |

### Sipas komunës

21 nga 38 komuna ndryshojnë. Speciet unike, speciet e kërcënuara dhe specie/km² nuk ndryshojnë në asnjë komunë.

| Komuna | Regjistrime (origjinal) | Regjistrime (i pastër) | Diferenca | Regj./1,000 banorë (origjinal) | Regj./1,000 banorë (i pastër) |
|---|---:|---:|---:|---:|---:|
| Graçanicë | 14,672 | 14,563 | -109 | 793.68 | 787.79 |
| Kamenicë | 2,724 | 2,616 | -108 | 119.12 | 114.40 |
| Kaçanik | 694 | 655 | -39 | 25.04 | 23.63 |
| Prishtinë | 5,924 | 5,893 | -31 | 26.04 | 25.91 |
| Prizren | 3,993 | 3,969 | -24 | 27.12 | 26.95 |
| Dragash | 939 | 924 | -15 | 32.50 | 31.98 |
| Ranillug | 984 | 973 | -11 | 396.61 | 392.18 |
| Pejë | 2,449 | 2,443 | -6 | 29.60 | 29.52 |
| Fushë Kosovë | 3,567 | 3,562 | -5 | 55.78 | 55.70 |
| Shtërpcë | 1,160 | 1,155 | -5 | 107.70 | 107.23 |
| Obiliq | 303 | 299 | -4 | 13.28 | 13.11 |
| Deçan | 1,403 | 1,399 | -4 | 50.51 | 50.37 |
| Rahovec | 219 | 216 | -3 | 5.24 | 5.17 |
| Malishevë | 165 | 163 | -2 | 3.76 | 3.71 |
| Gllogoc | 140 | 138 | -2 | 2.91 | 2.87 |
| Istog | 341 | 339 | -2 | 10.33 | 10.27 |
| Lipjan | 465 | 464 | -1 | 8.45 | 8.43 |
| Mitrovicë e Jugut | 479 | 478 | -1 | 7.40 | 7.38 |
| Podujevë | 316 | 315 | -1 | 4.45 | 4.44 |
| Gjakovë | 526 | 525 | -1 | 6.68 | 6.67 |
| Junik | 549 | 548 | -1 | 139.23 | 138.98 |

### Sipas klasës

10 klasa ndryshojnë, vetëm në numrin e regjistrimeve. Numri i specieve mbetet i njëjtë.

| Klasa | Regjistrime (origjinal) | Regjistrime (i pastër) | Diferenca |
|---|---:|---:|---:|
| Aves | 28,785 | 28,532 | -253 |
| Insecta | 11,543 | 11,447 | -96 |
| Magnoliopsida | 2,701 | 2,687 | -14 |
| Arachnida | 358 | 353 | -5 |
| Malacostraca | 23 | 21 | -2 |
| Mammalia | 273 | 272 | -1 |
| Agaricomycetes | 187 | 186 | -1 |
| Gastropoda | 279 | 278 | -1 |
| Pinopsida | 35 | 34 | -1 |
| Squamata | 190 | 189 | -1 |

### Sipas vitit

22 vite ndryshojnë, vetëm në numrin e regjistrimeve.

| Viti | Regjistrime (origjinal) | Regjistrime (i pastër) | Diferenca |
|---:|---:|---:|---:|
| 1905 | 21 | 9 | -12 |
| 1906 | 102 | 68 | -34 |
| 1917 | 39 | 35 | -4 |
| 1918 | 37 | 36 | -1 |
| 1954 | 13 | 11 | -2 |
| 1967 | 30 | 24 | -6 |
| 1977 | 13 | 12 | -1 |
| 1979 | 787 | 777 | -10 |
| 1997 | 52 | 51 | -1 |
| 2010 | 49 | 47 | -2 |
| 2013 | 990 | 989 | -1 |
| 2015 | 505 | 502 | -3 |
| 2017 | 590 | 585 | -5 |
| 2018 | 4,295 | 4,272 | -23 |
| 2019 | 1,533 | 1,531 | -2 |
| 2020 | 8,451 | 8,370 | -81 |
| 2021 | 6,843 | 6,729 | -114 |
| 2022 | 5,091 | 5,066 | -25 |
| 2023 | 1,947 | 1,939 | -8 |
| 2024 | 3,758 | 3,730 | -28 |
| 2025 | 1,061 | 1,054 | -7 |
| 2026 | 1,285 | 1,280 | -5 |

### Tabela e specieve

| Ndryshimi | Specie |
|---|---:|
| specie me më pak regjistrime | 112 |
| specie që humbën plotësisht | 0 |
| specie me më pak komuna | 0 |
| specie me vit të parë/fundit tjetër | 0 |

## Interpretimi

- **Pastrimi i ndryshon numrat e regjistrimeve me 0.80% dhe nuk e ndryshon pasurinë.** Asnjë specie, klasë, vit ose komunë nuk humbet. Te secili grup duplikatësh mbetet një rresht, kështu që speciet, viti i parë dhe i fundit dhe numri i komunave mbeten të njëjtë.
- **Ndryshimet më të mëdha janë te Graçanica (−109, eBird) dhe Kamenica (−108, kryesisht Observation.org, 97 rreshta).** Regjistrimet për 1,000 banorë bien përkatësisht me 5.89 dhe 4.72.
- **Vitet 2020–2021 humbasin më shumë** (−81 dhe −114), sepse aty janë shumica e listave të përsëritura të eBird. Vitet 1905–1906 humbasin 46 rreshta nga Macedonian Ecological Society: rreshta të përsëritur të koleksioneve të vjetra (Apfelbeck 34, Buljubašić 10, Purkyné 2).
- **Përfundimet e agregimeve v1 mbeten të vlefshme.** Graçanica ka ende 31.35% të regjistrimeve, zogjtë 61.42%, dhe renditja e komunave sipas specieve nuk ndryshon. Anshmëria nuk vjen nga duplikatët.

## Vendimi dhe arsyetimi

- **Për rezultatet finale përdoren CSV-të v2.** Ato mbështeten te të dhënat e pastra dhe të verifikuara.
- **CSV-të v1 ruhen.** Ato janë baza e krahasimit dhe e gjurmueshmërisë për raportin.
- **Logjika e agregimeve është një, e verifikuar.** Pa kontrollin "funksionet mbi origjinalin = v1", një diferencë ndërmjet v1 dhe v2 mund të vinte edhe nga një ndryshim i kodit.
- **Mostrat e 24 tetorit nuk u rinxorrën**, sepse plani e kërkon këtë hap vetëm për integrimin dhe agregimet. Mostrat mund të përmbajnë disa nga 375 duplikatët. Nëse përdoren te Pjesa II, rekomandohet t'u hiqen ose të rinxirren mbi `biodiversity_clean.csv` me të njëjtin kod dhe `random_state`.

## Dokumentimi i detyrës

- **Input:** `processed/biodiversity_clean.csv` (Deliza, 25 tetor), `processed/municipalities.csv`, `add_taxon_features()` (Jeta), CSV-të v1.
- **Çka u bë:** U ri-ekzekutuan integrimi dhe agregimet mbi të dhënat e pastra, me logjikë të verifikuar kundrejt v1, dhe u krahasuan numrat me ata të dataset-it origjinal.
- **Rreshta para / pas:** 46,831 (origjinal) → 46,456 (i pastër).
- **Kolona para / pas:** CSV-të v2 kanë të njëjtat kolona si v1.
- **Pse u bë:** Që agregimet finale të mbështeten te të dhënat e pastra, dhe që të dokumentohet sa ndikon pastrimi.
- **Output:** 5 CSV-të `processed/*_v2.csv`, `reports/rikalkulimi.md`, `reports/01_rikalkulimi_diferencat.csv`, `01_rikalkulimi_komunat.csv`, `01_rikalkulimi_klasat.csv`, `01_rikalkulimi_vitet.csv`, `01_rikalkulimi_speciet.csv`, seksioni 8 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Recompute integration and aggregates on the cleaned dataset`, `Add difference tables between original and cleaned aggregates`, `Document the recalculation on the cleaned data`.
