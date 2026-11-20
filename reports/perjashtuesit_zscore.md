# Z-score dhe Z-score i modifikuar

**Versioni:** 1.0
**Data:** 21.11.2026
**Statusi:** Të dy metodat janë llogaritur dhe krahasuar me IQR. Asnjë vlerë nuk fshihet.

## Metoda

- **Z-score:** Z = (x − mesatarja) / std. Shënohet |Z| > 3.
- **Z-score i modifikuar:** Mz = 0.6745 · (x − mediana) / MAD, ku MAD është mediana e |x − mediana|. Shënohet |Mz| > 3.5 (Iglewicz dhe Hoaglin, 1993).
- **Kur MAD = 0** (më shumë se gjysma e vlerave janë të barabarta me medianën), përdoret devijimi mesatar absolut: Mz = (x − mediana) / (1.253314 · MeanAD). Kjo ndodh te `coordinateUncertaintyInMeters` dhe `n_issues`.
- Në shpërndarje normale |Z| > 3 shënon 0.27% të vlerave dhe |Mz| > 3.5 rreth 0.05%.
- % llogaritet mbi vlerat e plotësuara të kolonës. Të gjitha numërimet, në shkallë lineare dhe mbi `log1p`, janë te `reports/04_zscore_kufijte.csv` (44 rreshta).

## Tabela e krahasimit

Të tri metodat krahasohen në të njëjtën shkallë, atë të mbajtur më 20 nëntor (në kllapa). IQR është kombinimi i mbajtur: k = 3 në nivel rreshti, k = 1.5 te komunat. Te `year`, koordinatat dhe `n_issues` IQR nuk u mbajt; tregohet k = 1.5 vetëm për krahasim. Çdo qelizë është numri i vlerave të shënuara dhe % e tyre.

| Kolona | IQR | Z | Mz |
|---|---|---|---|
| `individualCount` (log1p) | 180 (0.62%) | 419 (1.45%) | 2,111 (7.31%) |
| `elevation` (lineare) | 4 (0.06%) | 25 (0.41%) | 948 (15.37%) |
| `coordinateUncertaintyInMeters` (lineare) | 54 (0.37%) | 5 (0.03%) | 60 (0.41%) |
| `year` (lineare) | 6,180 (13.99%) | 756 (1.71%) | 5,833 (13.20%) |
| `decimalLatitude` (lineare) | 11,476 (24.70%) | 987 (2.12%) | 10,324 (22.22%) |
| `decimalLongitude` (lineare) | 4,338 (9.34%) | 0 (0.00%) | 5,198 (11.19%) |
| `n_issues` (lineare) | 1,645 (3.54%) | 1,645 (3.54%) | 1,645 (3.54%) |
| `regjistrime` (komuna, log1p) | 3 (7.89%) | 1 (2.63%) | 1 (2.63%) |
| `specie_unike` (komuna, log1p) | 4 (10.53%) | 1 (2.63%) | 1 (2.63%) |
| `specie_per_km2` (komuna, lineare) | 0 (0.00%) | 0 (0.00%) | 1 (2.63%) |
| `regjistrime_per_1000_banore` (komuna, log1p) | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| `specie_te_kercenuara` (komuna, log1p) | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| `regjistrime_te_kercenuara` (komuna, log1p) | 2 (5.26%) | 1 (2.63%) | 1 (2.63%) |

Kufijtë në njësi origjinale:

| Kolona | IQR | Z | Mz |
|---|---|---|---|
| `individualCount` (log1p) | [-1.0, 299.1] | [-0.8, 100.9] | [-0.6, 23.6] |
| `elevation` (lineare) | [-1,201.9, 2,764.6] | [-785.1, 2,633.6] | [-290.3, 1,620.6] |
| `coordinateUncertaintyInMeters` (lineare) | [-20,213.0, 27,534.0] | [-107,009.5, 116,820.1] | [-7,579.8, 21,721.8] |
| `year` (lineare) | [2012, 2028] | [1973, 2058] | [2010, 2030] |
| `decimalLatitude` (lineare) | [42.415, 42.806] | [41.920, 43.209] | [42.328, 42.831] |
| `decimalLongitude` (lineare) | [20.323, 21.636] | [19.935, 22.006] | [20.456, 21.640] |
| `n_issues` (lineare) | [0.0, 0.0] | [-0.7, 0.8] | [-0.2, 0.2] |
| `regjistrime` (komuna, log1p) | [13.9, 11,723.5] | [1.3, 62,161.9] | [6.5, 15,808.3] |
| `specie_unike` (komuna, log1p) | [24.2, 1,441.0] | [2.6, 7,928.0] | [12.1, 2,752.5] |
| `specie_per_km2` (komuna, lineare) | [-1.851, 4.088] | [-1.613, 3.911] | [-1.600, 3.194] |
| `regjistrime_per_1000_banore` (komuna, log1p) | [-0.9, 1,925.4] | [-0.8, 1,777.2] | [-0.9, 2,036.5] |
| `specie_te_kercenuara` (komuna, log1p) | [-0.4, 16.2] | [-0.7, 27.5] | [-0.7, 31.3] |
| `regjistrime_te_kercenuara` (komuna, log1p) | [-0.8, 78.8] | [-0.9, 265.2] | [-1.0, 360.8] |

## Pse Z-score klasik nuk i përshtatet shpërndarjeve shumë të anuara

Z-score i përsëritur në shkallë lineare te dy kolonat më të anuara. Raundi 1 përdor të gjitha vlerat; në çdo raund tjetër hiqen vlerat e shënuara dhe kufiri rillogaritet.

| Kolona | Raundi | Vlera | Mesatarja | Std | Kufiri i sipërm i Z | Të shënuara | Mediana | MAD |
|---|---|---|---|---|---|---|---|---|
| `individualCount` | 1 | 28,869 | 23.14 | 323.95 | 995.0 | 79 | 2 | 1 |
| `individualCount` | 2 | 28,790 | 9.17 | 33.93 | 111.0 | 306 | 2 | 1 |
| `individualCount` | 3 | 28,484 | 6.43 | 12.46 | 43.8 | 729 | 2 | 1 |
| `coordinateUncertaintyInMeters` | 1 | 14,643 | 4,905.31 | 37,304.94 | 116,820.1 | 5 | 7,071 | 0 |
| `coordinateUncertaintyInMeters` | 2 | 14,638 | 4,418.16 | 3,624.69 | 15,292.2 | 71 | 7,071 | 0 |
| `coordinateUncertaintyInMeters` | 3 | 14,567 | 4,317.24 | 3,318.29 | 14,272.1 | 3 | 7,071 | 0 |

- **Kufirin e caktojnë vetë përjashtuesit.** Te `individualCount` mesatarja është 23.14 kurse mediana 2, dhe std është 324. Kufiri del 995 dhe shënohen 79 vlera. Pa këto 79 vlera (0.27% e kolonës) std bie në 34 dhe kufiri në 111; në raundin e tretë bie në 44. Vlerat ekstreme e fryjnë std dhe e fshehin pjesën tjetër të bishtit (maskimi).
- **E njëjta gjë te pasiguria.** Kufiri bie nga 116,820 m në 15,292 m kur hiqen 5 vlerat mbi 100 km.
- **Rregulla është simetrike.** Kufiri i poshtëm te `individualCount` është -949, pra Z nuk mund të shënojë asnjë vlerë të ulët. Pragu 3 vjen nga shpërndarja normale, kurse skewness këtu është 26.63 dhe 101.73.
- **Mediana dhe MAD nuk lëvizin.** Në të tri raundet mbeten 2 dhe 1 te `individualCount`, 7,071 dhe 0 te pasiguria. Prandaj kufiri i Mz nuk varet nga vlerat që kërkohen.

## Vendimi dhe arsyetimi

| Kolona | Flamujt | Arsyetimi |
|---|---|---|
| `individualCount` (log1p) | `z_individualCount`, `mz_individualCount` | Kufijtë janë të radhitur: Mz mbi 23.6 individë (2,111 vlera), Z mbi 100.9 (419), IQR mbi 299.1 (180). Çdo vlerë që e shënon IQR e shënojnë edhe Z dhe Mz. Mz shënon 7.31% sepse MAD mat vetëm qendrën e ngjeshur (63% e vlerave janë 1–3 individë), dhe 23.6 individë është tufë e zakonshme. Në shkallë lineare Mz do të shënonte 20.99% (mbi 7.2). |
| `elevation` (lineare) | `z_elevation`, `mz_elevation` | Z ka kufirin 2,633.6 m, pak nën Gjeravicën (2,656 m): shënon 25 vlera, 5 mbi Gjeravicën dhe 20 brenda relievit të Kosovës. Mz ka kufirin 1,620.6 m dhe shënon 948 vlera (15.37%), regjistrime malore reale. IQR me k = 3 mbetet më i kujdesshmi (4 vlera). Për lartësinë, Mz ka kuptim vetëm brenda grupit (22 nëntor). |
| `coordinateUncertaintyInMeters` (lineare) | `z_coordinateUncertaintyInMeters`, `mz_coordinateUncertaintyInMeters` | MAD = 0, sepse 56.2% e vlerave janë saktësisht 7,071 m; Mz llogaritet me devijimin mesatar absolut. Z ka kufirin 116,820.1 m dhe shënon vetëm 5 vlerat mbi 100 km, sepse std (37,305 m) vjen nga po këto vlera: pa to kufiri bie në 15,292 m. Mz (mbi 21,721.8 m, 60 vlera) dhe IQR (mbi 27,534.0 m, 54) pajtohen pothuajse plotësisht. |
| `year` (lineare) | asnjë | Nuk mbahet asnjë flamur global, si te IQR. Z shënon 756 rreshta (1.71%) nën kufirin 1973, Mz 5,833 (13.20%) nën kufirin 2010; IQR me k = 1.5 shënonte 6,180. Të tria shënojnë regjistrime të vjetra reale, sepse qendra e shpërndarjes është periudha e eBird (2018–2022). |
| `decimalLatitude` (lineare) | asnjë | Nuk mbahet asnjë flamur global. Z shënon 987 rreshta (2.12%) jashtë [41.920, 43.209], Mz 10,324 (22.22%); IQR me k = 1.5 shënonte 11,476. Të gjitha pikat janë brenda Kosovës: kufijtë i cakton pika e Henc-it. |
| `decimalLongitude` (lineare) | asnjë | Nuk mbahet asnjë flamur global. Z nuk shënon asgjë: kufijtë (19.935–22.006) janë jashtë kutisë së Kosovës. Mz shënon 5,198 rreshta (11.19%), të gjithë brenda Kosovës. |
| `n_issues` (lineare) | asnjë | Nuk mbahet. MAD = 0, sepse 96.5% e vlerave janë 0; Z dhe Mz shënojnë çdo rresht me ≥ 1 flamur (1,645), njësoj si IQR. |
| `regjistrime` (komuna, log1p) | `z_regjistrime`, `mz_regjistrime` | Z: Mamushë (1). Mz: Mamushë (1). IQR: Graçanicë (14,563), Kllokot (13), Mamushë (1). |
| `specie_unike` (komuna, log1p) | `z_specie_unike`, `mz_specie_unike` | Z: Mamushë (1). Mz: Mamushë (1). IQR: Partesh (23), Mitrovicë e Veriut (22), Kllokot (13), Mamushë (1). |
| `specie_per_km2` (komuna, lineare) | `z_specie_per_km2`, `mz_specie_per_km2` | Z: asnjë. Mz: Junik (3.368). IQR: asnjë. |
| `regjistrime_per_1000_banore` (komuna, log1p) | `z_regjistrime_per_1000_banore`, `mz_regjistrime_per_1000_banore` | Z: asnjë. Mz: asnjë. IQR: asnjë. |
| `specie_te_kercenuara` (komuna, log1p) | `z_specie_te_kercenuara`, `mz_specie_te_kercenuara` | Z: asnjë. Mz: asnjë. IQR: asnjë. |
| `regjistrime_te_kercenuara` (komuna, log1p) | `z_regjistrime_te_kercenuara`, `mz_regjistrime_te_kercenuara` | Z: Graçanicë (365). Mz: Graçanicë (365). IQR: Graçanicë (365), Fushë Kosovë (81). |

- **E njëjta shkallë për të tri metodat.** Z dhe Mz llogariten në shkallën e mbajtur më 20 nëntor, që dallimi në tabelë të vijë nga metoda, jo nga shkalla.
- **Z-score klasik mbahet vetëm për krahasim.** Kufiri i tij varet nga vlerat që duhet t'i gjejë. Edhe mbi `log1p`, `individualCount` mbetet e anuar (skewness 2.07). Flamuri `z_<kolona>` ruhet për tabelën e mbivendosjes, jo si arsye për të dyshuar një vlerë.
- **Mz është robust, por jo i kujdesshëm.** Rregulla është simetrike rreth medianës dhe MAD mat vetëm qendrën e ngjeshur, prandaj në anën e bishtit shënon 7.31% te `individualCount` dhe 15.37% te `elevation`. IQR i nis kufijtë nga Q1 dhe Q3, jo nga mediana, dhe i përshtatet më mirë bishtit të gjatë. Flamuri i Mz lexohet si "larg qendrës", jo si gabim.
- **IQR mbetet metoda kryesore univariate.** Te tri kolonat në nivel rreshti kufijtë janë të radhitur, prandaj numri i metodave që e shënojnë një vlerë tregon sa ekstreme është ajo. Të tri metodat pajtohen te 180 vlera të `individualCount`, 4 të `elevation` dhe 5 të `coordinateUncertaintyInMeters`.
- **MAD = 0 zgjidhet me devijimin mesatar absolut.** Pa të, Mz nuk mund të llogaritet te pasiguria, ku 56.2% e vlerave janë 7,071 m.
- **Asnjë vlerë nuk fshihet.** Flamujt `z_<kolona>` dhe `mz_<kolona>` bashkohen me IQR më 23 nëntor.

## Dokumentimi i detyrës

- **Input:** `processed/biodiversity_features.csv` (46,456 rreshta, 7 kolona) dhe `processed/agg_municipality_v2.csv` (38 komuna, 6 kolona). Shkalla dhe k e IQR vijnë nga detyra e 20 nëntorit.
- **Çka u bë:** Z-score (|Z| > 3) dhe Z-score i modifikuar me MAD (|Mz| > 3.5) për 13 kolonat, në shkallë lineare dhe mbi `log1p` për 9 kolonat e anuara. Krahasim me IQR në të njëjtën shkallë dhe Z-score i përsëritur në 3 raunde te dy kolonat më të anuara.
- **Rreshta para / pas:** 46,456 / 46,456. Z shënoi `individualCount` 419, `elevation` 25, `coordinateUncertaintyInMeters` 5. Mz shënoi `individualCount` 2,111, `elevation` 948, `coordinateUncertaintyInMeters` 60. Me IQR bashkë, 3,118 rreshta (6.71%) kanë së paku një flamur. Te komunat: Z 3 raste, Mz 4 raste. Asnjë vlerë nuk u fshi ose u ndryshua.
- **Pse u bë:** Që të shihet sa ndryshon rezultati kur qendra dhe shpërndarja maten me mesatare dhe std në vend të medianës dhe MAD, dhe pse Z-score klasik nuk përdoret te kolonat shumë të anuara.
- **Output:** tabela e krahasimit Kolona | IQR | Z | Mz te `reports/perjashtuesit_zscore.md`, `reports/04_zscore_kufijte.csv`, seksioni 4 i `notebooks/04_perjashtuesit.ipynb`.
- **Commit:** `Dafina: Z-score dhe Z-score i modifikuar`.
- **Decision + Rationale:** shih seksionin "Vendimi dhe arsyetimi".
