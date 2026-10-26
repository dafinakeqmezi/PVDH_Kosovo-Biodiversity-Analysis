# Kodimi i flamujve dhe i IUCN

**Versioni:** 1.0  
**Data:** 26.10.2026  
**Statusi:** Dhjetë flamuj seriozë në 0/1, `iucn_rank` një herë nga `iucnRedListCategory`, dhe `iucn_evaluated`.

## Varësia

Te konvertimi i tipeve, `iucnRedListCategory` mbetet kategori pa renditje dhe `NE` me `DD` ruhen. Kodimi ordinal i mbetet këtij notebook-u. `iucnRedListStatus` është i njëjti status me fjalë (`Least Concern` për `LC`, dhe kështu me radhë) dhe te dataset-i i pastruar është hequr. Prandaj rangu lexohet vetëm nga kodi.

Flamujt janë ata seriozë te `reports/flamujt_gbif.md`. Flamujt informativë nuk bëhen kolona: i kanë 93.44% e rreshtave dhe do ta mbulonin sinjalin. `n_issues` mbetet numri i tyre. `strictlyProtected` mbetet bool, si te pastrimi. `iasUnionConcern` është jashtë nënbashkësisë. Funksioni nuk e ndryshon asnjë CSV.

## Tabela e IUCN

| `iucnRedListCategory` | `iucn_rank` | `iucn_evaluated` | n te CSV origjinale | n te dataset-i i pastruar |
|---|---:|---:|---:|---:|
| `LC` | 1 | 1 | 28,484 | 28,224 |
| `NT` | 2 | 1 | 761 | 757 |
| `VU` | 3 | 1 | 629 | 628 |
| `EN` | 4 | 1 | 18 | 18 |
| `CR` | 5 | 1 | 3 | 3 |
| `EX` | 6 | 1 | 1 | 1 |
| `NE` | bosh | 0 | 15,705 | 15,595 |
| `DD` | bosh | 0 | 17 | 17 |
| bosh | bosh | 0 | 1,213 | 1,213 |

28,484 + 761 + 629 + 18 + 3 + 1 + 15,705 + 17 + 1,213 = 46,831. Te dataset-i i pastruar, pasi janë hequr 375 rreshta të dyfishtë, shuma është 46,456. Nuk ka `EW`.

`EX` është një rresht, `gbifID` 5284839027, edhe pas heqjes së dyfishimeve. Te `is_threatened` ai rresht mbetet bosh. Këtu merr rangun 6, sepse shkalla e kërkuar e përfshin `EX`.

## Tabela e flamujve

Kolona është `flag_` plus emri. 1 do të thotë se flamuri është në `issue`. 0 do të thotë se nuk është. Boshllëku i `issue` bëhet 0, jo bosh. I njëjti n del te të dy dataset-et.

| Flamuri | Kolona | n |
|---|---|---:|
| `TAXON_MATCH_HIGHERRANK` | `flag_TAXON_MATCH_HIGHERRANK` | 756 |
| `RECORDED_DATE_INVALID` | `flag_RECORDED_DATE_INVALID` | 508 |
| `INDIVIDUAL_COUNT_INVALID` | `flag_INDIVIDUAL_COUNT_INVALID` | 351 |
| `TAXON_MATCH_FUZZY` | `flag_TAXON_MATCH_FUZZY` | 190 |
| `BASIS_OF_RECORD_INVALID` | `flag_BASIS_OF_RECORD_INVALID` | 120 |
| `RECORDED_DATE_MISMATCH` | `flag_RECORDED_DATE_MISMATCH` | 87 |
| `TAXON_MATCH_NONE` | `flag_TAXON_MATCH_NONE` | 28 |
| `COORDINATE_UNCERTAINTY_METERS_INVALID` | `flag_COORDINATE_UNCERTAINTY_METERS_INVALID` | 7 |
| `TAXON_MATCH_NAME_AND_ID_AMBIGUOUS` | `flag_TAXON_MATCH_NAME_AND_ID_AMBIGUOUS` | 1 |
| `SCIENTIFIC_NAME_AND_ID_INCONSISTENT` | `flag_SCIENTIFIC_NAME_AND_ID_INCONSISTENT` | 1 |

756 + 508 + 351 + 190 + 120 + 87 + 28 + 7 + 1 + 1 = 2,049. Kaq është shuma e kolonave 0/1, sepse një rresht mund të ketë më shumë se një flamur serioz.

## Vendimi dhe arsyetimi

Rangu shkruhet një herë: `LC` = 1, `NT` = 2, `VU` = 3, `EN` = 4, `CR` = 5, `EX` = 6. Nuk ka kolonë të dytë nga `iucnRedListStatus`.

`NE`, `DD` dhe boshllëku nuk janë shkallë rreziku. `iucn_rank` mbetet bosh. `iucn_evaluated` është 0 për këta rreshta dhe 1 kur ka rang. Te CSV-ja origjinale, 1 janë 29,896 dhe 0 janë 16,935. Te dataset-i i pastruar, 1 janë 29,631 dhe 0 janë 16,825.

Flamujt binarë janë dhjetë flamujt seriozë. Një flamur informativ nuk merr kolonë 0/1.

## Dokumentimi i detyrës

- **Varësia:** konvertimi i tipeve, ku kodimi ordinal mbetet për këtë notebook, dhe `reports/flamujt_gbif.md`.
- **Input:** `iucnRedListCategory` dhe `issue`.
- **Çka u bë:** U shkrua `add_iucn_and_flags()` për `iucn_rank`, `iucn_evaluated` dhe dhjetë kolonat `flag_`.
- **Rreshta para / pas:** 46,831 / 46,831 te CSV-ja origjinale. 46,456 / 46,456 te dataset-i i pastruar.
- **Kolona para / pas:** CSV-ja origjinale mbetet me 42 kolona. Funksioni shton 12 kolona te rezultati.
- **Pse u bë:** Rangu i IUCN shkruhet një herë. `NE`, `DD` dhe boshllëku nuk marrin rang. Flamujt seriozë bëhen 0/1.
- **Output:** `reports/kodimi_iucn_dhe_flamujve.md` dhe `add_iucn_and_flags()` te `notebooks/03_vetite.ipynb`.
- **Commit:** `Add IUCN rank and serious-flag columns`.
