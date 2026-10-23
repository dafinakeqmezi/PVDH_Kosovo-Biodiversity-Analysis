# Vlefshmëria e të dhënave

**Versioni:** 1.0  
**Data:** 21.10.2026  
**Statusi:** Kontrollet e vlefshmërisë për koordinatat, datat, pasigurinë dhe lartësinë.

## Varësia

Ky task zbaton dimensionin **Vlefshmëria** nga **Korniza e kualitetit** (`reports/korniza_e_kualitetit.md`). Kolona "Korniza" lidh çdo kontroll me ID-në atje (V1–V9, P5, A2). Kontrollet e reja, të shënuara me "–", janë shtuar këtu. Llogaritja është te seksioni 3.9 i `notebooks/01_mbledhja_kualiteti.ipynb`.

## Si matet

- **Aplikohet te:** rreshtat ku vlera ekziston. Mungesat i takojnë plotësisë (`reports/plotesia.md`).
- **% e vlefshme** = (aplikohen − të pavlefshme) / aplikohen × 100.
- Kontrollet me veprim "shëno" nuk tregojnë gabim, por vlera që kufizojnë përdorimin e rreshtit.

## Tabela e vlefshmërisë

| Rregulla | Rreshta që dështojnë | % |
|---|---:|---:|
| VL1 – Koordinatat brenda kutisë së Kosovës (lat 41.85–43.27, lon 20.01–21.80) | 0 | 0.00 |
| VL2 – Pika ka komunë të Kosovës | 0 | 0.00 |
| VL3 – Pa flamuj GBIF për koordinata të gabuara | 0 | 0.00 |
| VL4 – Koordinata me të paktën 3 shifra dhjetore (≤ ~110 m) | 784 | 1.67 |
| VL5 – Viti brenda 1758–2026 | 0 | 0.00 |
| VL6 – Viti ≥ 1900 (jo regjistrim historik) | 16 | 0.04 |
| VL7 – month 1–12 | 0 | 0.00 |
| VL8 – day 1–31 | 0 | 0.00 |
| VL9 – year-month-day formon datë reale (p.sh. jo 30 shkurt) | 0 | 0.00 |
| VL10 – eventDate lexohet si ISO 8601 | 0 | 0.00 |
| VL11 – Te intervalet: data e fundit ≥ data e fillimit | 0 | 0.00 |
| VL12 – Te intervalet: gjatësia ≤ 1 vit | 53 | 11.86 |
| VL13 – Pa flamurin GBIF RECORDED_DATE_INVALID | 508 | 1.08 |
| VL14 – coordinateUncertaintyInMeters > 0 dhe ≤ 10 km | 90 | 0.61 |
| VL15 – coordinateUncertaintyInMeters ≠ 7071 (pikë, jo qendër e qelizës 10 km) | 8,225 | 55.47 |
| VL16 – elevation ≠ 0 (0 = e panjohur) | 3,634 | 37.01 |
| VL17 – elevation brenda 297–2656 m | 9 | 0.15 |

% = rreshta që dështojnë / rreshta ku rregulla aplikohet (ku vlera ekziston) × 100. Tabela është edhe te `reports/01_vlefshmeria_rregullat.csv`.

### Detajet e kontrolleve

| ID | Korniza | Kontrolli | Kolonat | Aplikohen | Të pavlefshme | % e vlefshme | Veprimi |
|---|---|---|---|---:|---:|---:|---|
| VL1 | V1 | Koordinatat brenda kutisë së Kosovës (lat 41.85–43.27, lon 20.01–21.80) | `decimalLatitude`, `decimalLongitude` | 46,831 | 0 | **100.00** | largo rreshtin |
| VL2 | V1 | Pika ka komunë të Kosovës | `municipality`, `decimalLatitude`, `decimalLongitude` | 46,831 | 0 | **100.00** | largo rreshtin |
| VL3 | V1 | Pa flamuj GBIF për koordinata të gabuara | `issue` | 46,831 | 0 | **100.00** | largo rreshtin |
| VL4 | – | Koordinata me të paktën 3 shifra dhjetore (≤ ~110 m) | `decimalLatitude` | 46,831 | 784 | **98.33** | shëno; jo për analizë në nivel fshati |
| VL5 | V5 | Viti brenda 1758–2026 | `year` | 44,563 | 0 | **100.00** | vendos NaN |
| VL6 | A2 | Viti ≥ 1900 (jo regjistrim historik) | `year` | 44,563 | 16 | **99.96** | shëno si historik |
| VL7 | V6 | month 1–12 | `month` | 43,964 | 0 | **100.00** | vendos NaN |
| VL8 | V6 | day 1–31 | `day` | 43,612 | 0 | **100.00** | vendos NaN |
| VL9 | V6 | year-month-day formon datë reale (p.sh. jo 30 shkurt) | `year`, `month`, `day` | 43,612 | 0 | **100.00** | vendos NaN |
| VL10 | V4 | eventDate lexohet si ISO 8601 | `eventDate` | 44,641 | 0 | **100.00** | vendos NaN |
| VL11 | – | Te intervalet: data e fundit ≥ data e fillimit | `eventDate` | 447 | 0 | **100.00** | vendos NaN |
| VL12 | – | Te intervalet: gjatësia ≤ 1 vit | `eventDate` | 447 | 53 | **88.14** | shëno; jo për analizë sezonale |
| VL13 | V9 | Pa flamurin GBIF RECORDED_DATE_INVALID | `issue`, `eventDate` | 46,831 | 508 | **98.92** | data mbetet NaN |
| VL14 | V3 | coordinateUncertaintyInMeters > 0 dhe ≤ 10 km | `coordinateUncertaintyInMeters` | 14,827 | 90 | **99.39** | shëno; jo për analizë hapësinore të detajuar |
| VL15 | – | coordinateUncertaintyInMeters ≠ 7071 (pikë, jo qendër e qelizës 10 km) | `coordinateUncertaintyInMeters` | 14,827 | 8,225 | **44.53** | shëno; komuna mund të jetë e pasaktë |
| VL16 | P5 | elevation ≠ 0 (0 = e panjohur) | `elevation` | 9,820 | 3,634 | **62.99** | vendos NaN |
| VL17 | V2 | elevation brenda 297–2656 m | `elevation` | 6,186 | 9 | **99.85** | vendos NaN |

## 1. Koordinatat brenda Kosovës

- Të 46,831 rreshtat janë brenda kutisë së Kosovës (lat 41.8590–43.2417, lon 20.0208–21.7629). Të gjithë kanë komunë të Kosovës, dhe asnjë rresht nuk ka flamuj GBIF për koordinata të gabuara (`COUNTRY_COORDINATE_MISMATCH`, `ZERO_COORDINATE`, `PRESUMED_SWAPPED_COORDINATE` etj.).
- **784 rreshta kanë vetëm 1–2 shifra dhjetore**, pra precizion prej ~1–11 km. Janë të vlefshëm, por jo për analiza në nivel fshati.
- Pikat më të përsëritura nuk janë qendra artificiale të vendit, por hotspot-e të vëzhgimit: **Ligatinat e Henc** (13,047 regjistrime nga eBird) dhe **Ura e M9 mbi Sitnicë** (2,251).

## 2. Diapazoni i viteve

Rregulli: 1758 (fillimi i nomenklaturës zoologjike, Linnaeus) ≤ `year` ≤ 2026. Të gjitha 44,563 vitet janë brenda këtij diapazoni: min 1826, max 2026, median 2020.

| Periudha | Regjistrime | % |
|---|---:|---:|
| 1758–1899 | 16 | 0.04 |
| 1900–1949 | 355 | 0.80 |
| 1950–1999 | 4,131 | 9.27 |
| 2000–2009 | 1,402 | 3.15 |
| 2010–2019 | 10,223 | 22.94 |
| 2020–2026 | 28,436 | 63.81 |

16 regjistrime para vitit 1900 janë të vlefshme, por shënohen si historike.

## 3. `month` 1–12 dhe `day` 1–31

Të gjitha 43,964 vlerat e `month` janë 1–12, dhe të gjitha 43,612 vlerat e `day` janë 1–31. Edhe kombinimi year-month-day formon datë reale te të gjitha rreshtat (p.sh. asnjë 30 shkurt ose 31 prill).

## 4. Formatet e `eventDate`

`eventDate` paraqitet në **11 formate ISO 8601**. Të gjitha 44,641 vlerat e dhëna lexohen me `pd.to_datetime(format="ISO8601")`.

| Formati | Precizioni | Interval | Regjistrime | % | Të lexueshme |
|---|---|---|---:|---:|---:|
| `9999-99-99` | ditë | jo | 37,945 | 85.00 | 37,945 |
| `9999-99-99T99:99:99` | ditë | jo | 2,554 | 5.72 | 2,554 |
| `9999-99-99T99:99` | ditë | jo | 2,417 | 5.41 | 2,417 |
| `9999-99-99T99:99:99.999Z` | ditë | jo | 595 | 1.33 | 595 |
| `9999` | vit | jo | 409 | 0.92 | 409 |
| `9999-99-99/9999-99-99` | ditë | po | 398 | 0.89 | 398 |
| `9999-99` | muaj | jo | 173 | 0.39 | 173 |
| `9999-99-99T99:99:99Z` | ditë | jo | 67 | 0.15 | 67 |
| `9999/9999` | vit | po | 46 | 0.10 | 46 |
| `9999-99-99T99:99Z` | ditë | jo | 34 | 0.08 | 34 |
| `9999-99-99T99:99Z/9999-99-99T99:99Z` | ditë | po | 3 | 0.01 | 3 |

- **447 intervale** ("fillimi/fundi"): te të gjitha data e fundit është ≥ data e fillimit. **53 intervale janë më të gjata se 1 vit**, kështu që data e fillimit nuk tregon stinën e vëzhgimit.
- **508 rreshta kanë flamurin GBIF `RECORDED_DATE_INVALID`.** Te 497 prej tyre GBIF nuk e ka interpretuar datën, dhe `eventDate` është bosh. Pra shumica e 2,190 datave që mungojnë janë data të pavlefshme te burimi, jo data të pashënuara.

## 5. Vlera 7071 te `coordinateUncertaintyInMeters`

| Vlera (m) | Regjistrime | % e vlerave të dhëna | Publikuesi kryesor |
|---:|---:|---:|---|
| **7071** | 8,225 | 55.47 | HabiProt |
| 250 | 735 | 4.96 | naturgucker.de |
| 4 | 413 | 2.79 | iNaturalist.org |
| 5 | 368 | 2.48 | iNaturalist.org |
| 1000 | 299 | 2.02 | Observation.org |
| 10 | 231 | 1.56 | Observation.org |
| 3 | 200 | 1.35 | iNaturalist.org |
| 15 | 141 | 0.95 | Observation.org |
| 5000 | 131 | 0.88 | Macedonian Ecological Society |
| 8 | 129 | 0.87 | iNaturalist.org |

- **7071 m është vlera më e shpeshtë: 8,225 regjistrime, 55.47% e vlerave të dhëna.** 7071 ≈ 5000·√2 është gjysma e diagonales së një qelize 10 × 10 km. Pra koordinata është **qendra e qelizës së rrjetës 10 km**, jo vendi i vëzhgimit.
- 8,122 nga këto regjistrime vijnë nga **HabiProt**. Kanë vetëm **122 pika të ndryshme**, dhe 99.99% e tyre kanë flamurin `COORDINATE_ROUNDED`.
- Vlera është e vlefshme (> 0 dhe ≤ 10 km), por **komuna e këtyre rreshtave mund të jetë e pasaktë**: vëzhgimi mund të jetë deri në 7 km larg pikës, në një komunë fqinje. Rreshtat shënohen dhe nuk përdoren për analiza hapësinore të detajuara.
- 90 rreshta kanë pasiguri mbi 10 km (deri në 4,226 km).

## 6. Diapazoni i `elevation`

Rregulli: 297 m (pika më e ulët e Kosovës, Drini i Bardhë në kufi) ≤ `elevation` ≤ 2,656 m (Gjeravica). Vlerat e dhëna janë 9,820, nga 0 deri në 3,050 m.

| Lartësia | Regjistrime | % e vlerave të dhëna |
|---|---:|---:|
| = 0 | 3,634 | 37.01 |
| 1 – 296 | 4 | 0.04 |
| 297 – 800 | 3,713 | 37.81 |
| 801 – 1500 | 1,330 | 13.54 |
| 1501 – 2656 | 1,134 | 11.55 |
| > 2656 | 5 | 0.05 |

- **3,634 vlera 0** (3,624 nga HabiProt) janë mungesa të fshehura, jo lartësi reale.
- **9 lartësi janë jashtë diapazonit:**

| gbifID | elevation (m) | Koordinatat | Komuna | basisOfRecord | Publikuesi |
|---|---:|---|---|---|---|
| 1837879632 | 100 | 42.66657, 21.1724 | Prishtinë / Priština | PRESERVED_SPECIMEN | Museum of Comparative Zoology, Harvard University |
| 41659662 | 198 | 42.2, 20.71667 | Prizren | OCCURRENCE | USDA Agricultural Research Service (ARS) |
| 5284801271 | 250 | 42.675509, 20.328745 | Pejë / Peć | HUMAN_OBSERVATION | HabiProt |
| 5284610427 | 293 | 42.226778, 20.697054 | Prizren | HUMAN_OBSERVATION | HabiProt |
| 5794847480 | 2750 | 42.20667, 21.11917 | Kaçanik / Kačanik | PRESERVED_SPECIMEN | University of Vienna - Herbarium WU |
| 2028433750 | 2800 | 42.20667, 21.11917 | Kaçanik / Kačanik | PRESERVED_SPECIMEN | University of Vienna - Herbarium WU |
| 1830967944 | 2800 | 42.20667, 21.11917 | Kaçanik / Kačanik | PRESERVED_SPECIMEN | University of Vienna - Herbarium WU |
| 1831004196 | 2800 | 42.20667, 21.11917 | Kaçanik / Kačanik | PRESERVED_SPECIMEN | University of Vienna - Herbarium WU |
| 1830967907 | 3050 | 42.20667, 21.11917 | Kaçanik / Kačanik | PRESERVED_SPECIMEN | University of Vienna - Herbarium WU |

Pesë ekzemplarët e Herbarium WU në të njëjtën pikë në Kaçanik kanë 2,750–3,050 m. Lartësi të tilla nuk ekzistojnë në Kosovë, kështu që ose lartësia ose koordinata është gabim. Katër vlerat 100–293 m janë nën pikën më të ulët të vendit.

## Vendimi dhe arsyetimi

- **Koordinatat janë të vlefshme dhe nuk largohet asnjë rresht.** Ato me precizion të ulët (784) dhe me 7071 m (8,225) shënohen me flamur, sepse vlejnë për analizë në nivel rajoni, por jo në nivel komune ose fshati.
- **Vitet, muajt, ditët dhe formatet e datave janë 100% të vlefshme.** Data e fillimit të intervalit është vendim i saktë, por 53 intervalet më të gjata se 1 vit nuk përdoren për analizë sezonale.
- **Lartësitë 0 dhe ato jashtë 297–2,656 m bëhen NaN** te pastrimi (3,634 + 9 = 3,643 vlera). Ato nuk mund të korrigjohen pa një model lartësie (DEM).
- **Rregullat mbështeten te gjeografia e Kosovës dhe te standardet** (ISO 8601, Darwin Core, nomenklatura e vitit 1758), jo te shpërndarja e të dhënave. Kështu nuk largohen vlera të rralla, por të vërteta.

## Dokumentimi i detyrës

- **Input:** `dataset/kosovo_overall_biodiversity.csv`, `processed/gbif_datasets_cache.csv` (publikuesit), `reports/korniza_e_kualitetit.md`.
- **Çka u bë:** U kontrolluan koordinatat brenda Kosovës, diapazoni i viteve, `month` dhe `day`, formatet e `eventDate`, frekuenca e vlerës 7071 te `coordinateUncertaintyInMeters` dhe diapazoni i `elevation`, me 17 kontrolle.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 / 42.
- **Pse u bë:** Për të gjetur vlerat që janë të pranishme, por të gabuara ose të pasakta, para pastrimit.
- **Output:** `reports/vlefshmeria.md`, `reports/01_vlefshmeria_rregullat.csv`, `reports/01_vlefshmeria.csv`, `reports/01_formatet_e_datave.csv`, `reports/01_pasiguria_vlerat.csv`, `reports/01_lartesia_jashte_diapazonit.csv`, seksioni 3.9 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Add validity checks for coordinates, dates, uncertainty and elevation`.
