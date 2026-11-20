# Metoda IQR

**Versioni:** 1.0
**Data:** 20.11.2026
**Statusi:** Kufijtë janë llogaritur dhe për secilën kolonë është zgjedhur k dhe shkalla. Asnjë vlerë nuk fshihet.

## Metoda

Për secilën kolonë kandidate llogariten kufijtë Q1 − k·IQR dhe Q3 + k·IQR me k = 1.5 dhe k = 3. Vlera jashtë kufijve numërohet si përjashtues i mundshëm.

- Për kolonat e anuara (skewness > 1 në shkallë lineare) kufijtë llogariten edhe mbi `log1p(x)` dhe kthehen në njësi origjinale me `expm1`. Kufiri i poshtëm negativ do të thotë se në praktikë nuk ka kufi të poshtëm.
- % llogaritet mbi vlerat e plotësuara të kolonës, jo mbi 46,456 rreshtat.
- Të gjitha numërimet janë te `reports/04_iqr_kufijte.csv` (44 rreshta: 26 lineare, 18 mbi `log1p`).

## Kolonat e anuara

| Kolona | Skewness (lineare) | Skewness (log1p) | E anuar (> 1) |
|---|---|---|---|
| `individualCount` | 26.63 | 2.07 | po |
| `elevation` | 1.39 | 0.74 | po |
| `coordinateUncertaintyInMeters` | 101.73 | -1.00 | po |
| `year` | -3.77 | — | jo |
| `decimalLatitude` | -0.12 | — | jo |
| `decimalLongitude` | -0.75 | — | jo |
| `n_issues` | 6.18 | 5.49 | po |
| `regjistrime` (komuna) | 4.25 | -0.64 | po |
| `specie_unike` (komuna) | 1.76 | -1.22 | po |
| `specie_per_km2` (komuna) | 0.87 | — | jo |
| `regjistrime_per_1000_banore` (komuna) | 4.22 | 0.58 | po |
| `specie_te_kercenuara` (komuna) | 1.84 | 0.04 | po |
| `regjistrime_te_kercenuara` (komuna) | 5.64 | 1.15 | po |

Lista del nga skewness, jo nga lista paraprake e 18 nëntorit: shtohen `elevation` dhe `n_issues`, del `specie_per_km2`. `year` është e anuar majtas, prandaj `log1p` nuk i përshtatet.

## Tabela e kufijve

| Kolona | k | Kufijtë (lineare) | n (lineare) | % (lineare) | Kufijtë (log1p) | n (log1p) | % (log1p) |
|---|---|---|---|---|---|---|---|
| `individualCount` | 1.5 | [-6.5, 13.5] | 3,628 | 12.57 | [-0.7, 44.8] | 1,093 | 3.79 |
| `individualCount` | 3 | [-14.0, 21.0] | 2,258 | 7.82 | [-1.0, 299.1] | 180 | 0.62 |
| `elevation` | 1.5 | [-352.0, 1,914.6] | 595 | 9.65 | [158.9, 3,324.6] | 1 | 0.02 |
| `elevation` | 3 | [-1,201.9, 2,764.6] | 4 | 0.06 | [50.2, 10,377.4] | 0 | 0.00 |
| `coordinateUncertaintyInMeters` | 1.5 | [-9,981.5, 17,302.5] | 66 | 0.45 | [0.7, 1,057,656.5] | 1 | 0.01 |
| `coordinateUncertaintyInMeters` | 3 | [-20,213.0, 27,534.0] | 54 | 0.37 | [-1.0, 158,178,641.3] | 0 | 0.00 |
| `year` | 1.5 | [2012, 2028] | 6,180 | 13.99 | — | — | — |
| `year` | 3 | [2006, 2034] | 5,044 | 11.41 | — | — | — |
| `decimalLatitude` | 1.5 | [42.415, 42.806] | 11,476 | 24.70 | — | — | — |
| `decimalLatitude` | 3 | [42.268, 42.952] | 8,929 | 19.22 | — | — | — |
| `decimalLongitude` | 1.5 | [20.323, 21.636] | 4,338 | 9.34 | — | — | — |
| `decimalLongitude` | 3 | [19.830, 22.129] | 0 | 0.00 | — | — | — |
| `n_issues` | 1.5 | [0.0, 0.0] | 1,645 | 3.54 | [0.0, 0.0] | 1,645 | 3.54 |
| `n_issues` | 3 | [0.0, 0.0] | 1,645 | 3.54 | [0.0, 0.0] | 1,645 | 3.54 |
| `regjistrime` (komuna) | 1.5 | [-987.4, 2,129.6] | 6 | 15.79 | [13.9, 11,723.5] | 3 | 7.89 |
| `regjistrime` (komuna) | 3 | [-2,156.2, 3,298.5] | 4 | 10.53 | [0.2, 142,964.9] | 0 | 0.00 |
| `specie_unike` (komuna) | 1.5 | [-190.1, 620.9] | 6 | 15.79 | [24.2, 1,441.0] | 4 | 10.53 |
| `specie_unike` (komuna) | 3 | [-494.2, 925.0] | 3 | 7.89 | [4.5, 6,574.4] | 1 | 2.63 |
| `specie_per_km2` (komuna) | 1.5 | [-1.851, 4.088] | 0 | 0.00 | — | — | — |
| `specie_per_km2` (komuna) | 3 | [-4.078, 6.315] | 0 | 0.00 | — | — | — |
| `regjistrime_per_1000_banore` (komuna) | 1.5 | [-71.1, 129.6] | 4 | 10.53 | [-0.9, 1,925.4] | 0 | 0.00 |
| `regjistrime_per_1000_banore` (komuna) | 3 | [-146.4, 204.9] | 2 | 5.26 | [-1.0, 67,086.1] | 0 | 0.00 |
| `specie_te_kercenuara` (komuna) | 1.5 | [-3.1, 7.9] | 3 | 7.89 | [-0.4, 16.2] | 0 | 0.00 |
| `specie_te_kercenuara` (komuna) | 3 | [-7.2, 12.0] | 1 | 2.63 | [-0.8, 61.5] | 0 | 0.00 |
| `regjistrime_te_kercenuara` (komuna) | 1.5 | [-9.1, 17.9] | 6 | 15.79 | [-0.8, 78.8] | 2 | 5.26 |
| `regjistrime_te_kercenuara` (komuna) | 3 | [-19.2, 28.0] | 4 | 10.53 | [-1.0, 728.0] | 0 | 0.00 |

## Kontrolli kundrejt vlerave të njohura

Sa nga vlerat e njohura (plani i 18 nëntorit, figurat e 19 nëntorit) i kap secili kombinim:

| Kolona | Vlerat e njohura | Gjithsej | lineare, k = 1.5 | lineare, k = 3 | log1p, k = 1.5 | log1p, k = 3 |
|---|---|---|---|---|---|---|
| `individualCount` | ≥ 1,000 individë | 79 | 79 | 79 | 79 | 79 |
| `elevation` | > 2,656 m (mbi Gjeravicën) | 5 | 5 | 4 | 0 | 0 |
| `elevation` | < 297 m | 4 | 0 | 0 | 1 | 0 |
| `coordinateUncertaintyInMeters` | > 100 km | 5 | 5 | 5 | 1 | 0 |

## Vendimi dhe arsyetimi

| Kolona | Shkalla | k | Kufijtë | n | % | Arsyetimi |
|---|---|---|---|---|---|---|
| `individualCount` | log1p | 3 | [-1.0, 299.1] | 180 | 0.62 | Skewness 26.63 → 2.07 pas `log1p`. Në shkallë lineare shënohen 12.57% e vlerave (mbi 13.5) ose 7.82% (mbi 21.0): bishti i shpërndarjes, jo përjashtuesit. Mbi `log1p` me k = 1.5 mbeten 3.79%, mbi 44.8 individë, që është tufë e zakonshme. Me k = 3 kufiri është 299.1 dhe shënohen 180 vlera nga 300 individë e lart, përfshirë të 79 vlerat ≥ 1,000. 179 prej tyre janë zogj. |
| `elevation` | lineare | 3 | [-1,201.9, 2,764.6] | 4 | 0.06 | Anim i moderuar (skewness 1.39). Lineare me k = 1.5 shënon 595 vlera mbi 1,914.6 m, regjistrime malore reale. Me k = 3 kufiri është 2,764.6 m, afër Gjeravicës (2,656 m), dhe shënohen 4 vlera (2,800–3,050 m), të gjitha mbi Gjeravicën. `log1p` e ngjesh skajin e sipërm: kufiri del 3,324.6 m, mbi maksimumin (3,050 m), dhe nuk kap asnjë nga 5 vlerat mbi Gjeravicën. Vlera 2,750 m dhe 4 vlerat nën 297 m nuk kapen nga IQR; i mbulon rregulla fizike. |
| `coordinateUncertaintyInMeters` | lineare | 3 | [-20,213.0, 27,534.0] | 54 | 0.37 | Skewness 101.73 vjen nga 5 vlera: pa vlerat mbi 100 km është 0.66. Mbi `log1p` kutia është shumë e gjerë (Q1 = 250 m, Q3 = 7,071 m) dhe kufiri del 1,057,656.5 m, më i madh se Kosova: kap vetëm 1 nga 5 vlerat mbi 100 km. Lineare me k = 3 ka kufirin 27,534.0 m dhe shënon 54 vlera, të gjitha nga iNaturalist: 5 mbi 100 km dhe 49 ndërmjet 27,537 dhe 32,112 m, që ka gjasë të jenë koordinata të fshehura. k = 1.5 do të shtonte edhe 12 vlera ndërmjet 17,302.5 dhe 27,534.0 m. |
| `year` | — | — | — | — | — | IQR globale nuk mbahet. Kutia është 2018–2022, prandaj kufiri bie te viti 2012 (k = 1.5) ose 2006 (k = 3) dhe shënohen 6,180 (13.99%) ose 5,044 (11.41%) rreshta, përfshirë ekzemplarët historikë. Skewness është negative (-3.77), prandaj `log1p` nuk ndihmon. Sipas planit, viti kontrollohet brenda `basisOfRecord` dhe me metodën kohore. |
| `decimalLatitude` | — | — | — | — | — | IQR globale nuk mbahet. Pika e Henc-it ka 27.9% të rreshtave dhe e ngushton kutinë, prandaj shënohen 11,476 (24.70%) ose 8,929 (19.22%) rreshta, të gjithë brenda Kosovës. Përjashtuesit hapësinorë kërkohen më 24 nëntor. |
| `decimalLongitude` | — | — | — | — | — | IQR globale nuk mbahet. Me k = 1.5 shënohen 4,338 (9.34%) rreshta, të gjithë brenda Kosovës. Me k = 3 kufijtë (19.830–22.129) dalin jashtë kutisë së Kosovës (20.01–21.80) dhe nuk shënohet asgjë. Përjashtuesit hapësinorë kërkohen më 24 nëntor. |
| `n_issues` | — | — | — | — | — | IQR nuk mbahet. Q1 = Q3 = 0, prandaj kufijtë janë [0, 0] për çdo k dhe çdo shkallë dhe shënohet çdo rresht me ≥ 1 flamur (1,645). Mbetet variabël konteksti. |
| `regjistrime` (komuna) | log1p | 1.5 | [13.9, 11,723.5] | 3 | 7.89 | Skewness 4.25 → -0.64. Lineare shënon 6 ose 4 komuna, vetëm ato me më shumë regjistrime. Mbi `log1p` me k = 1.5 shënohen të dy skajet: Graçanicë (14,563), Kllokot (13), Mamushë (1). Me k = 3: asnjë. |
| `specie_unike` (komuna) | log1p | 1.5 | [24.2, 1,441.0] | 4 | 10.53 | Skewness 1.76 → -1.22. Lineare shënon vetëm komunat me më shumë specie (6 ose 3). Mbi `log1p` me k = 1.5 shënohen komunat me shumë pak specie: Partesh (23), Mitrovicë e Veriut (22), Kllokot (13), Mamushë (1). Me k = 3: Mamushë (1). |
| `specie_per_km2` (komuna) | lineare | 1.5 | [-1.851, 4.088] | 0 | 0.00 | Skewness 0.87: nuk është e anuar, prandaj mbetet lineare. Nuk shënohet asnjë komunë, as me k = 1.5 as me k = 3. |
| `regjistrime_per_1000_banore` (komuna) | log1p | 1.5 | [-0.9, 1,925.4] | 0 | 0.00 | Skewness 4.22 → 0.58. Lineare shënon 4 ose 2 komuna (Graçanicë (787.79), Ranillug (392.18), Leposaviq (171.32), Junik (138.98)). Mbi `log1p` asnjë komunë nuk del jashtë kufijve: maksimumi (787.79, Graçanicë) është nën kufirin 1,925.4. |
| `specie_te_kercenuara` (komuna) | log1p | 1.5 | [-0.4, 16.2] | 0 | 0.00 | Skewness 1.84 → 0.04. Lineare shënon 3 ose 1 komuna (Prishtinë (13), Prizren (12), Pejë (9)). Mbi `log1p` me k = 1.5: asnjë. |
| `regjistrime_te_kercenuara` (komuna) | log1p | 1.5 | [-0.8, 78.8] | 2 | 5.26 | Skewness 5.64 → 1.15. Lineare shënon 6 ose 4 komuna. Mbi `log1p` me k = 1.5 shënohen Graçanicë (365), Fushë Kosovë (81). Me k = 3: asnjë. |

- **k = 3 te kolonat në nivel rreshti.** Në shpërndarje normale k = 1.5 shënon rreth 0.7% të vlerave. Te `individualCount` (mbi `log1p`), `elevation` dhe `coordinateUncertaintyInMeters` kufiri i k = 1.5 bie brenda bishtit të vazhdueshëm dhe shënon 1,093, 595 dhe 66 vlera. Me k = 3 mbeten 180, 4 dhe 54: gjithsej 238 rreshta (0.51% e 46,456), që mund të shqyrtohen një nga një.
- **k = 1.5 te agregatet e komunave.** Me 38 komuna, k = 3 do të shënonte gjithsej 1 rast. k = 1.5 shënon 9 raste te 6 komuna, që shikohen me emër.
- **`log1p` mbahet vetëm ku animi është veti e shpërndarjes.** `individualCount` dhe numërimet e komunave ndryshojnë me rend madhësie. Te `coordinateUncertaintyInMeters` animi vjen nga 5 vlera, dhe te `elevation` gabimet priten në skajin e sipërm, të cilin `log1p` e ngjesh. Kjo ndryshon nga plani i 18 nëntorit, që parashihte `log1p` për pasigurinë.
- **IQR globale nuk mbahet te `year`, koordinatat dhe `n_issues`.** Te këto kolona kufijtë i cakton forma e kutisë (eBird 2018–2022, pika e Henc-it, Q1 = Q3 = 0), jo vlerat e veçuara.
- **Flamuri nuk është vendim.** Kombinimi i mbajtur bëhet flamur 0/1 (`iqr_<kolona>`) dhe bashkohet me metodat tjera më 23 nëntor. 179 nga 180 vlerat te `individualCount` janë zogj në tufa dhe 49 nga 54 te pasiguria ka gjasë të jenë koordinata të fshehura: këto i takojnë kontrollit sipas grupit (22 nëntor) dhe shqyrtimit të Delizës (24 nëntor).

## Dokumentimi i detyrës

- **Input:** `processed/biodiversity_features.csv` (46,456 rreshta, 7 kolona) dhe `processed/agg_municipality_v2.csv` (38 komuna, 6 kolona).
- **Çka u bë:** Kufijtë IQR me k = 1.5 dhe k = 3 për 13 kolonat në shkallë lineare, dhe mbi `log1p` për 9 kolonat e anuara (skewness > 1). U numëruan përjashtuesit dhe % për çdo kombinim dhe u zgjodh k dhe shkalla për secilën kolonë.
- **Rreshta para / pas:** 46,456 / 46,456. U shënuan 238 rreshta (`individualCount` 180, `elevation` 4, `coordinateUncertaintyInMeters` 54) dhe 9 raste te 6 komuna. Asnjë vlerë nuk u fshi ose u ndryshua.
- **Pse u bë:** IQR është metoda bazë që nuk varet nga mesatarja dhe devijimi standard. Krahasimi i dy k-ve dhe dy shkallëve tregon ku metoda kap vlera të veçuara dhe ku shënon vetëm bishtin e shpërndarjes.
- **Output:** tabela Kolona | k | Kufijtë | n | % (lineare dhe log) te `reports/perjashtuesit_iqr.md`, `reports/04_iqr_kufijte.csv`, seksioni 3 i `notebooks/04_perjashtuesit.ipynb`.
- **Commit:** `Dafina: metoda IQR`.
- **Decision + Rationale:** shih seksionin "Vendimi dhe arsyetimi".
