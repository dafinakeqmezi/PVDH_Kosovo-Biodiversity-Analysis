# Vetitë e burimit dhe hapësinore

**Versioni:** 1.0  
**Data:** 23.10.2026  
**Statusi:** `in_protected_area` nga `protectedArea`, `is_citizen_science` nga publikuesi dhe `basisOfRecord`, `n_issues` nga flamujt seriozë.

## Varësia

Analiza e burimeve e 11.10.2026 (`processed/gbif_datasets_cache.csv`, `notebooks/01b_analiza_burimeve.ipynb`). Publikuesi merret nga `publishingOrg`, jo nga `institutionCode`. Klasifikimi i flamujve është te `reports/gbif_flags.md` dhe `reports/01_gbif_issues.csv`. Për zonën e mbrojtur, strategjia e mungesave e mbajti boshllëkun të panjohur derisa u sqarua kuptimi; sqarimi i 23.10.2026 është te `reports/vendimet_per_mungesat_strukturore.md`. `protectedArea`, `basisOfRecord`, `datasetKey` dhe `issue` mbahen te `reports/feature_selection.md`. Funksioni i lexon këto kolona dhe nuk e ndryshon CSV-në.

## Tabela e kritereve

| Veti | 1 ose vlera | 0 | NaN |
|---|---|---|---|
| `in_protected_area` | `protectedArea` ka emër zone | bosh, ose `Jashtë zonës së mbrojtur` | nuk mbetet NaN |
| `is_citizen_science` | publikuesi është në listën më poshtë dhe `basisOfRecord` është `HUMAN_OBSERVATION` | çdo kombinim tjetër i njohur | vetëm nëse `datasetKey` nuk është në cache |
| `n_issues` | numri i flamujve seriozë në `issue` | qelia bosh, ose vetëm flamuj informativë | nuk mbetet NaN |

`strictlyProtected` nuk përdoret. 20,307 rreshta kanë emër zone dhe `strictlyProtected = FALSE`: zona ekziston, por nuk është strikte.

## `in_protected_area`

| Vlera | Rreshta |
|---|---:|
| 1 | 21,069 |
| 0 | 25,762 |

Boshllëku në CSV-në origjinale është 0, sepse më 23.10.2026 u sqarua se `protectedArea` bosh do të thotë jashtë zonave të regjistruara në këtë dataset. Në kopjen e pastruar i njëjti kuptim është teksti `Jashtë zonës së mbrojtur`, prandaj edhe ai bëhet 0. Kjo nuk është verifikim i pavarur GIS.

## `is_citizen_science`

Të dy kushtet duhen njëkohësisht. `HUMAN_OBSERVATION` vetëm nuk mjafton: 90.71% e regjistrimeve e kanë këtë `basisOfRecord`, por një pjesë vijnë nga institute, muze ose projekte survejimi.

| Publikuesi | Rreshta |
|---|---:|
| Cornell Lab of Ornithology | 26,009 |
| HabiProt | 8,122 |
| iNaturalist.org | 4,286 |
| Observation.org | 1,436 |
| naturgucker.de | 721 |
| Pl@ntNet | 660 |
| Xeno-canto Foundation for Nature Sounds | 20 |
| Mushroom Observer, Inc. | 17 |
| izeltlabuak.hu | 3 |
| Birda | 3 |
| **Gjithsej 1** | **41,277** |

`HUMAN_OBSERVATION` që mbetet 0:

| Publikuesi | Rreshta |
|---|---:|
| VectorNet | 587 |
| European Bird Census Council (EBCC) | 348 |
| ENOVA d.o.o. Sarajevo | 111 |
| CREAF | 59 |
| Universitat de les Illes Balears | 52 |
| Biological Records Centre | 20 |
| European Food Safety Authority | 10 |
| Newcastle University | 9 |
| Staatliche Naturwissenschaftliche Sammlungen Bayerns | 6 |

Rreshtat e tjerë, muze dhe herbariume, mbeten 0 sepse `basisOfRecord` nuk është `HUMAN_OBSERVATION` ose publikuesi nuk është në listë. 0 janë 5,554 rreshta. Asnjë `datasetKey` nuk mungon në cache, prandaj NaN është 0.

HabiProt mbetet në listë, sepse Alciphron dhe Orhideje janë baza vëzhgimesh te analiza e burimeve. 3,598 prej tyre janë literaturë me datën zëvendësuese 30 nëntor (`reports/aggregation_time.md`). `basisOfRecord` i tyre është prapë `HUMAN_OBSERVATION`, prandaj kriteri i kësaj detyre nuk i ndan.

## `n_issues`

Numërohen vetëm 10 flamujt seriozë të `reports/gbif_flags.md`. Flamujt informativë nuk hyjnë: i kanë 93.44% e rreshtave dhe do ta mbulonin sinjalin. Qelia bosh është 0, jo cilësi e garantuar.

`TAXON_MATCH_HIGHERRANK`, `RECORDED_DATE_INVALID`, `INDIVIDUAL_COUNT_INVALID`, `TAXON_MATCH_FUZZY`, `BASIS_OF_RECORD_INVALID`, `RECORDED_DATE_MISMATCH`, `TAXON_MATCH_NONE`, `COORDINATE_UNCERTAINTY_METERS_INVALID`, `TAXON_MATCH_NAME_AND_ID_AMBIGUOUS`, `SCIENTIFIC_NAME_AND_ID_INCONSISTENT`.

| `n_issues` | Rreshta |
|---|---:|
| 0 | 45,186 |
| 1 | 1,251 |
| 2 | 384 |
| 3 | 10 |

Shuma e flamujve seriozë është 2,049. Rreshta me të paktën një janë 1,645. Të dyja përputhen me tabelën e flamujve.

## Vendimi dhe arsyetimi

`in_protected_area` është 1 vetëm kur `protectedArea` ka emër zone. Boshllëku dhe teksti `Jashtë zonës së mbrojtur` janë 0, sipas sqarimit të 23.10.2026. Strategjia e mëparshme e linte të panjohur derisa të sqarohej kuptimi; ai sqarim tani është në vendimet për mungesat strukturore.

`is_citizen_science` është 1 vetëm për platformat e shkencës qytetare të analizës së burimeve, dhe vetëm kur `basisOfRecord` është `HUMAN_OBSERVATION`. VectorNet, EBCC, universitetet dhe muzetë mbeten 0 edhe kur vëzhgimi është njerëzor.

`n_issues` numëron flamujt seriozë, jo të gjithë flamujt e ndarë me `;`. Kështu 0 do të thotë «pa flamur serioz», jo «pa asnjë flamur».

## Dokumentimi i detyrës

- **Varësia:** `processed/gbif_datasets_cache.csv` (11.10.2026), `reports/gbif_flags.md`, `reports/vendimet_per_mungesat_strukturore.md` (23.10.2026).
- **Input:** `protectedArea`, `datasetKey`, `basisOfRecord`, `issue`, dhe `publishingOrg` nga cache.
- **Çka u bë:** U shkrua `add_source_spatial_features()` dhe tabela e kritereve për tri vetitë.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 në CSV. Funksioni shton tri kolona te rezultati.
- **Pse u bë:** Zona, lloji i burimit dhe flamujt seriozë dalin pa e kthyer boshllëkun e zonës në të panjohur dhe pa i numëruar flamujt informativë si problem.
- **Output:** `reports/vetite_e_burimit.md` dhe `add_source_spatial_features()` te `notebooks/03_vetite.ipynb`.
- **Commit:** `Add in_protected_area, is_citizen_science and n_issues` 