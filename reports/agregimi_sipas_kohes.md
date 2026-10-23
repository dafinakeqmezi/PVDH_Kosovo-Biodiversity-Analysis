# Agregimi sipas kohës

**Versioni:** 1.0  
**Data:** 22.10.2026  
**Statusi:** `processed/agg_time.csv`: regjistrimet dhe speciet unike për vit, plus tabela vit × muaj.

## Varësia

Plani e lidh këtë detyrë me **plotësimin e `year`/`month`** nga Deliza (19 tetor). Ky hap është përfunduar me **0 plotësime të lejueshme** sipas rregullit konservativ: pa data të pjesshme, intervale ndërmujore/ndërvjetore ose konflikte me komponentët ekzistues. Rezultati dhe arsyet janë te `reports/plotesimi_year_month_para_pas.csv` dhe `reports/vendimi_per_plotesimin_year_month.md`; hapat `02_clean:recover:year` dhe `02_clean:recover:month` janë në log. Vlerat year/month mbeten të njëjta me origjinalin, prandaj ky rezultat nuk ndryshon agregimet aktuale. Vlerësimi i mëparshëm për 78 vite dhe 222 muaj të rikuperueshëm nuk zbatohet sipas këtij rregulli. Agregimi duhet të ri-ekzekutohet mbi dataset-in final pas pastrimit të mëvonshëm.

Llogaritja është te seksioni 6.2 i `notebooks/01_mbledhja_kualiteti.ipynb`.

## Struktura e `processed/agg_time.csv`

Një rresht për çdo vit nga 1826 deri në 2026 (201 vite). Përfshihen edhe vitet pa regjistrime, me 0, që boshllëqet kohore të duken. 102 vite kanë të paktën një regjistrim.

| Kolona | Kuptimi |
|---|---|
| `regjistrime` | numri i rreshtave me këtë `year` |
| `specie_unike` | numri i specieve të ndryshme në këtë vit |
| `data_30_nentor_habiprot` | numri i regjistrimeve të HabiProt me month = 11 dhe day = 30; flamur shqyrtimi, jo provë e një date zëvendësuese |
| `perqindja_e_regjistrimeve` | % e të gjithë rreshtave me vit |
| `01_jan` … `12_dhj` | tabela vit × muaj: regjistrime për çdo muaj |
| `pa_muaj` | regjistrime me vit, por pa muaj (data vetëm me vit) |

Agregimi përfshin 44,563 rreshta me vit. 2,268 rreshta pa vit mbeten jashtë. 599 rreshta kanë vit, por jo muaj.

## Regjistrimet dhe speciet unike sipas dekadës

| Dekada | Regjistrime | Specie unike |
|---|---:|---:|
| 1820–1829 | 1 | 1 |
| 1830–1839 | 2 | 2 |
| 1860–1869 | 1 | 1 |
| 1880–1889 | 1 | 0 |
| 1890–1899 | 11 | 10 |
| 1900–1909 | 124 | 20 |
| 1910–1919 | 113 | 46 |
| 1920–1929 | 6 | 3 |
| 1930–1939 | 109 | 73 |
| 1940–1949 | 3 | 3 |
| 1950–1959 | 115 | 82 |
| 1960–1969 | 233 | 73 |
| 1970–1979 | 1,013 | 535 |
| 1980–1989 | 1,870 | 435 |
| 1990–1999 | 900 | 321 |
| 2000–2009 | 1,402 | 498 |
| 2010–2019 | 10,223 | 1,862 |
| 2020–2029 | 28,436 | 1,787 |

## Regjistrimet dhe speciet unike për vit, 2000 e tutje

Tabela e plotë, për të gjitha vitet, është te `processed/agg_time.csv`.

| Viti | Regjistrime | Specie unike | % | Me 30 nëntor (HabiProt) |
|---:|---:|---:|---:|---:|
| 2000 | 19 | 18 | 0.04 | 1 |
| 2001 | 42 | 40 | 0.09 | 0 |
| 2002 | 319 | 122 | 0.72 | 221 |
| 2003 | 144 | 79 | 0.32 | 0 |
| 2004 | 63 | 52 | 0.14 | 9 |
| 2005 | 26 | 24 | 0.06 | 0 |
| 2006 | 20 | 20 | 0.04 | 0 |
| 2007 | 280 | 147 | 0.63 | 95 |
| 2008 | 247 | 107 | 0.55 | 228 |
| 2009 | 242 | 179 | 0.54 | 120 |
| 2010 | 49 | 37 | 0.11 | 3 |
| 2011 | 300 | 185 | 0.67 | 0 |
| 2012 | 908 | 468 | 2.04 | 7 |
| 2013 | 990 | 525 | 2.22 | 9 |
| 2014 | 478 | 298 | 1.07 | 0 |
| 2015 | 505 | 300 | 1.13 | 0 |
| 2016 | 575 | 233 | 1.29 | 0 |
| 2017 | 590 | 352 | 1.32 | 1 |
| 2018 | 4,295 | 512 | 9.64 | 0 |
| 2019 | 1,533 | 529 | 3.44 | 0 |
| 2020 | 8,451 | 466 | 18.96 | 0 |
| 2021 | 6,843 | 364 | 15.36 | 0 |
| 2022 | 5,091 | 724 | 11.42 | 0 |
| 2023 | 1,947 | 363 | 4.37 | 0 |
| 2024 | 3,758 | 773 | 8.43 | 0 |
| 2025 | 1,061 | 511 | 2.38 | 0 |
| 2026 | 1,285 | 579 | 2.88 | 0 |

## Tabela vit × muaj, 2000 e tutje

| Viti | jan | shk | mar | pri | maj | qer | kor | gus | sht | tet | nën | dhj | pa muaj |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2000 | 0 | 0 | 0 | 0 | 1 | 0 | 7 | 0 | 0 | 10 | 1 | 0 | 0 |
| 2001 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 41 | 0 | 0 | 0 | 0 |
| 2002 | 0 | 0 | 0 | 64 | 0 | 0 | 0 | 0 | 24 | 0 | 231 | 0 | 0 |
| 2003 | 0 | 0 | 0 | 0 | 32 | 0 | 21 | 90 | 0 | 0 | 0 | 0 | 1 |
| 2004 | 0 | 0 | 5 | 28 | 0 | 0 | 18 | 1 | 2 | 0 | 9 | 0 | 0 |
| 2005 | 3 | 0 | 0 | 1 | 0 | 0 | 22 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2006 | 0 | 0 | 0 | 0 | 1 | 10 | 4 | 0 | 0 | 0 | 0 | 0 | 5 |
| 2007 | 2 | 2 | 2 | 4 | 19 | 48 | 81 | 26 | 0 | 1 | 95 | 0 | 0 |
| 2008 | 0 | 0 | 0 | 1 | 15 | 2 | 0 | 1 | 0 | 0 | 228 | 0 | 0 |
| 2009 | 0 | 0 | 0 | 61 | 0 | 1 | 2 | 58 | 0 | 0 | 120 | 0 | 0 |
| 2010 | 0 | 0 | 0 | 0 | 16 | 1 | 0 | 12 | 1 | 2 | 10 | 6 | 1 |
| 2011 | 0 | 4 | 2 | 3 | 48 | 49 | 46 | 67 | 66 | 6 | 1 | 8 | 0 |
| 2012 | 1 | 3 | 7 | 16 | 118 | 128 | 98 | 465 | 31 | 18 | 19 | 4 | 0 |
| 2013 | 1 | 63 | 9 | 275 | 216 | 27 | 14 | 23 | 296 | 40 | 24 | 1 | 1 |
| 2014 | 1 | 4 | 5 | 35 | 204 | 71 | 62 | 44 | 26 | 18 | 8 | 0 | 0 |
| 2015 | 0 | 0 | 62 | 5 | 246 | 65 | 3 | 99 | 10 | 3 | 0 | 12 | 0 |
| 2016 | 21 | 133 | 6 | 15 | 30 | 147 | 97 | 25 | 24 | 30 | 10 | 9 | 28 |
| 2017 | 3 | 10 | 19 | 46 | 74 | 87 | 166 | 13 | 12 | 75 | 26 | 5 | 54 |
| 2018 | 314 | 538 | 1,312 | 1,060 | 346 | 179 | 148 | 138 | 58 | 21 | 10 | 129 | 42 |
| 2019 | 18 | 62 | 136 | 115 | 366 | 151 | 118 | 168 | 254 | 15 | 83 | 37 | 10 |
| 2020 | 102 | 267 | 535 | 595 | 1,522 | 1,372 | 1,300 | 741 | 690 | 510 | 572 | 175 | 70 |
| 2021 | 327 | 523 | 859 | 972 | 1,405 | 847 | 623 | 102 | 518 | 394 | 162 | 109 | 2 |
| 2022 | 3 | 128 | 263 | 231 | 356 | 871 | 858 | 1,633 | 577 | 29 | 9 | 8 | 125 |
| 2023 | 5 | 2 | 31 | 351 | 34 | 135 | 91 | 463 | 309 | 159 | 158 | 208 | 1 |
| 2024 | 166 | 51 | 200 | 361 | 652 | 970 | 593 | 437 | 172 | 118 | 25 | 13 | 0 |
| 2025 | 9 | 35 | 45 | 47 | 226 | 150 | 98 | 133 | 116 | 152 | 37 | 13 | 0 |
| 2026 | 48 | 57 | 59 | 264 | 266 | 145 | 379 | 67 | 0 | 0 | 0 | 0 | 0 |

## Sipas muajit dhe datat e dyshimta "30 nëntor"

| Muaji | Regjistrime | Specie unike | % | Pa 30 nëntor | % pa 30 nëntor |
|---|---:|---:|---:|---:|---:|
| jan | 1,024 | 127 | 2.33 | 1,024 | 2.54 |
| shk | 1,924 | 182 | 4.38 | 1,924 | 4.77 |
| mar | 3,586 | 288 | 8.16 | 3,586 | 8.88 |
| pri | 4,598 | 598 | 10.46 | 4,598 | 11.39 |
| maj | 6,353 | 1,066 | 14.45 | 6,353 | 15.74 |
| qer | 5,600 | 988 | 12.74 | 5,600 | 13.87 |
| kor | 5,263 | 1,157 | 11.97 | 5,263 | 13.04 |
| gus | 5,146 | 1,028 | 11.71 | 5,146 | 12.75 |
| sht | 3,296 | 700 | 7.50 | 3,296 | 8.17 |
| tet | 1,646 | 312 | 3.74 | 1,646 | 4.08 |
| nën | 4,789 | 1,037 | 10.89 | 1,191 | 2.95 |
| dhj | 739 | 140 | 1.68 | 739 | 1.83 |

**Gjetja:** nëntori përmban 10.89% të regjistrimeve dhe 1,037 specie. **3,598 regjistrime të HabiProt kanë datën 30 nëntor**. Përqendrimi në një ditë dhe referencat e literaturës sugjerojnë një konventë të mundshme raportimi, por nuk provojnë se datat janë të pavlefshme. Flamuri në kod kontrollon vetëm publikuesin, muajin dhe ditën; nuk verifikon origjinën nga literatura për çdo rresht. Disa nga referencat e raportuara janë:

| Burimi (`recordedBy`) | `year` | Regjistrime me 30 nëntor |
|---|---:|---:|
| Jakšić, P. (1988) Karte dnevnih leptira YU | 1987 | 1,315 |
| Jakšić, P., Živić, N. (1995) Kosovo Metohija. GPMB | 1994 | 432 |
| Vasić, K. i sar. (2002) Sovice Srbije | 1979 | 431 |
| Tomić, D. i sar. (2002) Zemljomerke Srbije | 1979 | 251 |
| Jakšić, P. (2003) Crvena knjiga d leptira Srbije | 2002 | 218 |
| Zečević, M. (2002) Leptiri Timočke Krajine | 1981 | 185 |
| Ibrahimi, H. i sar. (2012) Trichoptera KiM | 2008 | 126 |
| Ibrahimi, H. i sar. (2014) Trichoptera KiM | 2008 | 96 |
| *të tjera (93)* | | 544 |

Data 30 nëntor trajtohet si **kandidate për datë zëvendësuese**, jo si gabim i konfirmuar. Nevojitet dokumentacion ose konfirmim nga publikuesi përpara se month/day të ndryshohen. Si analizë ndjeshmërie, pa këto regjistrime nëntori ka 1,191 regjistrime (2.95%), ndërsa maji ka 15.74%. Një shpërndarje që duket më e pritshme nuk vërteton se përjashtimi është i saktë. Përqendrimi shfaqet edhe në vite të vjetra: p.sh. 1987 ka 1,348 regjistrime, nga të cilat 1,321 me 30 nëntor. Datat dhe regjistrimet ruhen në agregimin kryesor.

## Interpretimi

- **Shumica e të dhënave janë të reja.** 2010–2026 kanë 86.75% të regjistrimeve me vit. Kulmi është në 2020 (8,451) dhe 2021 (6,843). Ky është efekt i rritjes së eBird dhe iNaturalist, jo i rritjes së biodiversitetit.
- **Regjistrimet dhe speciet nuk lëvizin bashkë.** 2020 ka 8,451 regjistrime dhe 466 specie, kurse 2024 ka 3,758 regjistrime dhe 773 specie. Numri i regjistrimeve për vit mat përpjekjen e vëzhgimit.
- **Para vitit 1970 të dhënat janë të rralla dhe kryesisht historike** (koleksione dhe literaturë), kështu që trendet afatgjata nuk mund të nxirren nga numri i regjistrimeve.

## Shënime për grupin

- **Deliza (vlerat e pavlefshme, 23 tetor):** mbaje flamurin për shqyrtim. Mos i zëvendëso `month`/`day` vetëm nga ky përqendrim; kërko konfirmim nga burimi përpara se të klasifikohen si data zëvendësuese.
- **Jeta (`season`):** këto data prodhojnë kategorinë "vjeshtë", por besueshmëria e datës duhet shqyrtuar. Raporto krahasimin me/pa rreshtat e shënuar si analizë ndjeshmërie, jo si provë që stina është e gabuar.

## Dokumentimi i detyrës

- **Input:** `dataset/kosovo_overall_biodiversity.csv` (`year`, `month`, `day`, `species`), `processed/gbif_datasets_cache.csv` (publikuesit).
- **Çka u bë:** U llogaritën regjistrimet dhe speciet unike për çdo vit dhe tabela vit × muaj. U shënuan për shqyrtim 3,598 regjistrime të HabiProt me datë 30 nëntor, pa ndryshuar datat ose përjashtuar rreshta nga agregimi kryesor.
- **Rreshta para / pas:** 46,831 rreshta → 201 rreshta (vite). 2,268 rreshta pa vit mbeten jashtë.
- **Kolona para / pas:** `agg_time.csv` ka 17 kolona.
- **Pse u bë:** Për të parë si ndryshojnë regjistrimet dhe speciet në kohë dhe sipas stinës, dhe për të gjetur artefaktet kohore para analizës.
- **Output:** `processed/agg_time.csv`, `reports/agregimi_sipas_kohes.md`, `reports/01_koha_sipas_dekades.csv`, `reports/01_koha_sipas_muajit.csv`, seksioni 6.2 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Add time aggregates by year and year x month`.
