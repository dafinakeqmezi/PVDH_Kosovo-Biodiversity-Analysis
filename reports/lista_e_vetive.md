# Lista finale e vetive

**Versioni:** 1.0  
**Data:** 27.10.2026  
**Statusi:** Nëntë hapat e vetive janë ekzekutuar mbi dataset-in e pastruar.

## Varësia

Hyrja është checkpoint-i i 25 tetorit, `processed/biodiversity_clean.csv`: 46,456 rreshta dhe 83 kolona. Publikuesi për `is_citizen_science` lexohet nga `processed/gbif_datasets_cache.csv`, sepse nuk është kolonë e rreshtit.

Funksioni nuk e ndryshon këtë CSV dhe nuk e ndryshon CSV-në origjinale. Matrica komunë × `taxon_group` dhe PCA e saj mbeten hapa më vete. Ato nuk shtohen si kolona të çdo regjistrimi.

Rishikimi i variancës dhe i korrelacionit nuk hoqi asnjë kolonë, prandaj të 45 kolonat e reja mbeten.

## Vendimi

`build_features(df, datasets)` i thërret hapat në rendin e detyrave:

1. `add_time_features`
2. `add_taxon_features`
3. `add_source_spatial_features`
4. `add_elevation_zone`
5. `add_period`
6. `add_count_class`
7. `add_one_hot`
8. `add_iucn_and_flags`
9. `add_log1p`

Rezultati është `processed/biodiversity_features.csv`: 46,456 rreshta dhe 128 kolona. Rendi i `gbifID` është i njëjtë me checkpoint-in. 83 kolonat e pastruara qëndrojnë. Shtohen 45.

Ku burimi mungon, vlera e re mbetet bosh. `season` mungon pikërisht ku mungon `month`. `decade`, `is_recent` dhe `period` mungojnë pikërisht ku mungon `year`. `count_class` dhe `individualCount_log1p` mungojnë në 17,587 rreshta, sa `individualCount`. `coordinateUncertaintyInMeters_log1p` mungon në 31,813 rreshta, sa burimi.

## Lista e 45 kolonave

| Hapi | Kolonat |
|---|---|
| Koha | `season`, `decade`, `is_recent` |
| Taksonomia | `taxon_group`, `is_threatened` |
| Burimi dhe hapësira | `in_protected_area`, `is_citizen_science`, `n_issues` |
| Lartësia | `elevation_zone` |
| Periudha | `period` |
| Numri i individëve | `count_class` |
| One-hot | 6 për `taxon_group`, 7 për `district`, 7 për `basisOfRecord` |
| IUCN dhe flamujt | `iucn_rank`, `iucn_evaluated`, 10 kolona `flag_` |
| `log1p` | `individualCount_log1p`, `coordinateUncertaintyInMeters_log1p` |

One-hot mbetet 20 kolona. `basisOfRecord_Tjera` mbetet koshi i kategorisë me 1 rresht. Çdo rresht ka saktësisht një 1 në secilin nga tri grupet dummy.

## Kontrollet mbi të dhënat e pastra

| Vetia | Rezultati |
|---|---|
| `taxon_group` | Zogj 28,532, Insekte 11,447, Bimë 3,723, Tjera 1,396, Kërpudha 970, E panjohur 388 |
| `is_threatened` | 1 = 649, 0 = 28,981, bosh = 16,826 |
| `EX` | 1 rresht, `is_threatened` bosh, `iucn_rank` = 6 |
| `in_protected_area` | 1 = 20,876, 0 = 25,580 |
| `is_citizen_science` | 1 = 40,984, 0 = 5,472, bosh = 0 |
| `n_issues` | shuma 2,049 |
| `elevation_zone` | E panjohur 40,297, Fushë 3,711, Kodrinore 1,314, Malore 1,134 |
| `period` | 1826–1899 = 16, 1900–1949 = 304, 1950–1999 = 4,111, 2000–2009 = 1,402, 2010–2019 = 10,187, 2020–2026 = 28,168, bosh = 2,268 |
| `count_class` | 1–2 = 15,815, 3–6 = 6,335, 7–10200 = 6,719, bosh = 17,587 |
| `iucn_evaluated` | 1 = 29,631, 0 = 16,825 |
| `log1p` | skewness e numrit 26.63 → 2.07, e pasigurisë 101.73 → −1.00 |

## Dokumentimi i detyrës

- **Varësia:** checkpoint-i i 25 tetorit dhe nëntë funksionet e vetive.
- **Input:** `processed/biodiversity_clean.csv` dhe cache-i i publikuesve.
- **Çka u bë:** U shkrua `build_features(df, datasets)` dhe u ruajt rezultati.
- **Rreshta para / pas:** 46,456 / 46,456.
- **Kolona para / pas:** 83 / 128.
- **Pse u bë:** Hapat e vetive bëhen një ekzekutim mbi të dhënat e pastra. Asnjë kolonë nuk hiqet.
- **Output:** `reports/lista_e_vetive.md`, `processed/biodiversity_features.csv` dhe funksioni te `notebooks/03_vetite.ipynb`.
- **Commit:** `Build feature columns on the cleaned biodiversity dataset`.
