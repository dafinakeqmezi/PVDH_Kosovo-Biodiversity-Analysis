# PCA e komunave

**Versioni:** 1.0  
**Data:** 26.10.2026  
**Statusi:** Tri komponentë nga matrica e standardizuar komunë × `taxon_group`.

## Varësia

Hyrja është `processed/matrica_pca_komuna_taxon.csv`: 38 komuna dhe gjashtë kolona Z. Ajo vjen nga `standardize_pca_matrix()`. Mostërimi i regjistrimeve nuk hyn, sepse ai prodhon mostra të rreshtave, jo këtë matricë. `individualCount` nuk hyn.

Funksioni nuk e ndryshon matricën e standardizuar dhe nuk e ndryshon CSV-në e regjistrimeve.

## Vendimi

PCA bëhet me `sklearn.decomposition.PCA`, `svd_solver="full"`. Të gjashtë kolonat Z hyjnë. Zgjidhen komponentët me `explained_variance_` mbi 1. Këta janë PC1, PC2 dhe PC3. Varianca kumulative është 0.770411.

PC4 ka `explained_variance_` 0.804951, nën 1, prandaj nuk mbahet. PC6 ka variancë 0. Gjashtë përpjesëtimet e një komune mblidhen në 1, prandaj një kolonë përcaktohet nga pesë të tjerat. Pas Z-score kjo varësi mbetet dhe komponenti i gjashtë nuk mban informacion.

Shenja e një komponenti është drejtim. Nëse kthehen të gjitha loadings dhe të gjitha rezultatet e atij komponenti, kuptimi mbetet i njëjtë.

## Varianca

| Komponenti | explained_variance_ | explained_variance_ratio_ | Kumulative |
|---|---:|---:|---:|
| PC1 | 2.177166 | 0.353312 | 0.353312 |
| PC2 | 1.474247 | 0.239242 | 0.592554 |
| PC3 | 1.095986 | 0.177857 | 0.770411 |
| PC4 | 0.804951 | 0.130628 | 0.901039 |
| PC5 | 0.609812 | 0.098961 | 1.000000 |
| PC6 | 0.000000 | 0.000000 | 1.000000 |

Tri të parët janë mbi 1. Katër komponentë do të arrinin 0.901039, por i katërti është nën 1 dhe udhëhiqet nga `E panjohur` (loading +0.706) kundrejt bimëve (−0.556). Ai mbetet jashtë rezultatit.

## Loadings

Pesha është loading i komponentit te kolona Z. Vlera më e madhe në vlerë absolute peshon më shumë.

| Grupi | PC1 | PC2 | PC3 |
|---|---:|---:|---:|
| Zogj | +0.655 | −0.189 | −0.124 |
| Insekte | −0.452 | +0.583 | −0.161 |
| Bimë | −0.319 | −0.538 | +0.092 |
| Kërpudha | −0.074 | +0.148 | +0.902 |
| Tjera | −0.317 | −0.541 | +0.115 |
| E panjohur | −0.398 | −0.138 | −0.352 |

- **PC1:** zogjtë +0.655. Në anën tjetër insektet −0.452 dhe `E panjohur` −0.398. Rezultat i lartë do të thotë përpjesëtim zogjsh mbi mesatare. Graçanica është 3.203 dhe Fushë Kosovë 3.138. Të dyja kanë rreth 98% zogj.
- **PC2:** insektet +0.583. Në anën tjetër Tjera −0.541 dhe bimët −0.538. Mamusha është 3.358 sepse ka 1 regjistrim dhe ai është insekt, prandaj përpjesëtimi i insekteve është 1. Kamenica është 2.420, me 77.75% insekte.
- **PC3:** kërpudhat +0.902. Në anën tjetër `E panjohur` −0.352. Dragashi është 3.646 dhe Juniku 3.245. Përpjesëtimi i kërpudhave është 0.2982 dhe 0.2623.

## Rezultati

`processed/pca_municipalities.csv` ka 38 rreshta dhe kolonat `komuna`, `rajoni`, `PC1`, `PC2`, `PC3`. Rendi i komunave është i njëjtë me matricën e standardizuar. `specie_*`, `year`, gjerësia dhe gjatësia nuk janë kolona.

## Dokumentimi i detyrës

- **Varësia:** `processed/matrica_pca_komuna_taxon.csv` nga hapi i 23 tetorit.
- **Input:** gjashtë kolonat `z_*`.
- **Çka u bë:** U shkrua `run_municipality_pca()` dhe u llogarit PCA.
- **Rreshta para / pas:** 38 / 38.
- **Kolona para / pas:** hyrja mbetet. Rezultati ka komunën, rajonin dhe 3 komponentë.
- **Pse u bë:** Për të parë sa drejtime i mjaftojnë profileve të grupeve dhe cili grup peshon te secili.
- **Output:** `reports/pca_komunat.md`, `processed/pca_municipalities.csv` dhe `run_municipality_pca()` te `notebooks/03_vetite.ipynb`.
- **Commit:** `Run PCA on the standardized municipality matrix`.
