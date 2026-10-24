# Kolonat dummy

**Versioni:** 1.0  
**Data:** 24.10.2026  
**Statusi:** one-hot për `taxon_group`, `district` dhe `basisOfRecord`. `drop_first` është false.

## Varësia

`taxon_group` vjen nga `add_taxon_features()`, me grupet e 15.10.2026: Zogj, Insekte, Bimë, Kërpudha, Tjera dhe E panjohur. Të njëjtat numra janë te `reports/vetite_taksonomike.md` dhe te `reports/agregimi_sipas_komunes.md`. Klasat e rralla të `class` janë bashkuar që atëherë te Tjera. `E panjohur` është klasa që mungon, jo një klasë e rrallë.

`district` dhe `basisOfRecord` lexohen nga CSV-ja origjinale. Të dyja janë të plota: 0 mungesa. `reports/konsistenca_dhe_anshmeria.md` i konfirmon 7 rajonet zyrtare. Funksioni nuk e ndryshon CSV-në dhe nuk e one-hot-on `kingdom` apo `strictlyProtected`.

## Rregulli për kategoritë e rralla

Kategori shumë e rrallë është ajo me më pak se 47 rreshta. 47 është 0.1% e 46,831. Ajo bëhet `Tjera` vetëm te kolona dummy. Vlera origjinale mbetet.

Nën këtë prag bie vetëm `OBSERVATION`, me 1 rresht. Kategoria tjetër më e vogël është `MATERIAL_CITATION`, me 317 rreshta. `E panjohur` ka 388. Rajoni më i vogël, Ferizaj / Uroševac, ka 2,593.

## Tabela e kategorive

| Burimi | Kategoria | n | % | Dummy |
|---|---|---:|---:|---|
| `taxon_group` | Zogj | 28,785 | 61.47 | `taxon_group_Zogj` |
| `taxon_group` | Insekte | 11,543 | 24.65 | `taxon_group_Insekte` |
| `taxon_group` | Bimë | 3,738 | 7.98 | `taxon_group_Bimë` |
| `taxon_group` | Tjera | 1,406 | 3.00 | `taxon_group_Tjera` |
| `taxon_group` | Kërpudha | 971 | 2.07 | `taxon_group_Kërpudha` |
| `taxon_group` | E panjohur | 388 | 0.83 | `taxon_group_E panjohur` |
| `district` | Prishtinë / Priština | 25,734 | 54.95 | `district_Prishtinë / Priština` |
| `district` | Prizren | 5,268 | 11.25 | `district_Prizren` |
| `district` | Gjilan / Gnjilane | 4,156 | 8.87 | `district_Gjilan / Gnjilane` |
| `district` | Mitrovicë / Kosovska Mitrovica | 3,196 | 6.82 | `district_Mitrovicë / Kosovska Mitrovica` |
| `district` | Pejë / Peć | 3,187 | 6.81 | `district_Pejë / Peć` |
| `district` | Gjakovë / Đakovica | 2,697 | 5.76 | `district_Gjakovë / Đakovica` |
| `district` | Ferizaj / Uroševac | 2,593 | 5.54 | `district_Ferizaj / Uroševac` |
| `basisOfRecord` | HUMAN_OBSERVATION | 42,479 | 90.71 | `basisOfRecord_HUMAN_OBSERVATION` |
| `basisOfRecord` | PRESERVED_SPECIMEN | 1,748 | 3.73 | `basisOfRecord_PRESERVED_SPECIMEN` |
| `basisOfRecord` | OCCURRENCE | 1,269 | 2.71 | `basisOfRecord_OCCURRENCE` |
| `basisOfRecord` | MATERIAL_SAMPLE | 641 | 1.37 | `basisOfRecord_MATERIAL_SAMPLE` |
| `basisOfRecord` | MACHINE_OBSERVATION | 376 | 0.80 | `basisOfRecord_MACHINE_OBSERVATION` |
| `basisOfRecord` | MATERIAL_CITATION | 317 | 0.68 | `basisOfRecord_MATERIAL_CITATION` |
| `basisOfRecord` | OBSERVATION | 1 | 0.002 | `basisOfRecord_Tjera` |

28,785 + 11,543 + 3,738 + 1,406 + 971 + 388 = 46,831. Shtatë rajonet japin po 46,831. Shtatë vlerat e `basisOfRecord` japin po 46,831.

## Lista e kolonave dummy

20 kolona. Çdo rresht ka 1 në një kolonë të secilit grup dhe 0 te të tjerat e atij grupi.

| Kolona | n |
|---|---:|
| `taxon_group_Bimë` | 3,738 |
| `taxon_group_E panjohur` | 388 |
| `taxon_group_Insekte` | 11,543 |
| `taxon_group_Kërpudha` | 971 |
| `taxon_group_Tjera` | 1,406 |
| `taxon_group_Zogj` | 28,785 |
| `district_Ferizaj / Uroševac` | 2,593 |
| `district_Gjakovë / Đakovica` | 2,697 |
| `district_Gjilan / Gnjilane` | 4,156 |
| `district_Mitrovicë / Kosovska Mitrovica` | 3,196 |
| `district_Pejë / Peć` | 3,187 |
| `district_Prishtinë / Priština` | 25,734 |
| `district_Prizren` | 5,268 |
| `basisOfRecord_HUMAN_OBSERVATION` | 42,479 |
| `basisOfRecord_MACHINE_OBSERVATION` | 376 |
| `basisOfRecord_MATERIAL_CITATION` | 317 |
| `basisOfRecord_MATERIAL_SAMPLE` | 641 |
| `basisOfRecord_OCCURRENCE` | 1,269 |
| `basisOfRecord_PRESERVED_SPECIMEN` | 1,748 |
| `basisOfRecord_Tjera` | 1 |

## Vendimi dhe arsyetimi

`drop_first` është false. `pd.get_dummies(..., drop_first=True)` heq kolonën e parë sipas rendit alfabetik, jo një bazë të zgjedhur:

| Burimi | Kolona që do të binte |
|---|---|
| `taxon_group` | `taxon_group_Bimë` |
| `district` | `district_Ferizaj / Uroševac` |
| `basisOfRecord` | `basisOfRecord_HUMAN_OBSERVATION` |

Këto tri nuk janë e njëjta lloj baze. Bimë është grup i planit, jo shumica. Ferizaj është rajoni më i vogël. `HUMAN_OBSERVATION` është 90.71% e rreshtave. Heqja e tyre do t’i fshihte nga lista, dhe rreshti do të lexohej vetëm si «të gjitha zero». Çdo kategori e mbajtur merr kolonën e vet 0/1.

`OBSERVATION` bëhet `basisOfRecord_Tjera`. Kolona origjinale `basisOfRecord` mbetet `OBSERVATION` për atë rresht. Asnjë rajon dhe asnjë `taxon_group` nuk bashkohet.

## Dokumentimi i detyrës

- **Varësia:** `taxon_group` i 15.10.2026, `district` dhe `basisOfRecord` origjinale.
- **Input:** `taxon_group`, `district`, `basisOfRecord`.
- **Çka u bë:** U shkrua `add_one_hot()` me 20 kolona dummy. `OBSERVATION` u bashkua te `Tjera`.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 në CSV. Funksioni shton 20 kolona dummy te rezultati.
- **Pse u bë:** Tri kolonat nominale bëhen 0/1. Kategoria me 1 rresht nuk merr kolonë më vete. `drop_first` mbetet false, që lista t’i tregojë të gjitha kategoritë e mbajtura.
- **Output:** `reports/kolonat_dummy.md` dhe `add_one_hot()` te `notebooks/03_vetite.ipynb`.
- **Commit:** `Add one-hot columns for taxon_group, district and basisOfRecord`.
