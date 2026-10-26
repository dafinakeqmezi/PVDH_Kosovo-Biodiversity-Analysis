# Shkallëzimi për PCA

**Versioni:** 1.0  
**Data:** 26.10.2026  
**Statusi:** Z-score i përpjesëtimeve të regjistrimeve në matricën komunë × `taxon_group`.

## Varësia

Matrica është `processed/agg_municipality_taxon.csv`: 38 komuna dhe 46,831 regjistrime. Shënimi për PCA te `reports/agregimi_sipas_komunes.md` thotë të përdoret një bllok, `regjistrime_*` ose `specie_*`, dhe numrat të kthehen në përpjesëtime ose `log1p` para standardizimit. Funksioni nuk e ndryshon atë matricë dhe nuk e ndryshon CSV-në e regjistrimeve.

`year`, `decimalLatitude` dhe `decimalLongitude` nuk janë kolona të kësaj matrice. Nuk standardizohen. Viti mbetet vit kalendarik. Koordinatat mbeten në gradë për hartë.

## Vendimi

Hyn vetëm blloku `regjistrime_*`: Zogj, Insekte, Bimë, Kërpudha, Tjera, E panjohur. Blloku `specie_*` nuk përzihet, sepse pasuria e specieve është pyetje tjetër.

Për çdo komunë, numri i grupit pjesëtohet me regjistrimet e asaj komune. Çdo rresht mblidhet në 1. Komuna më e vogël, Mamushë, ka 1 regjistrim, prandaj asnjë rresht nuk pjesëtohet me 0.

Pastaj çdo përpjesëtim merr Z-score: `(vlera − mesatarja) / devijimi standard`, me pjesëtues 38. Pas kësaj, secila nga gjashtë kolonat ka mesatare 0 dhe devijim standard 1.

## Pse përpjesëtimet, jo numrat absolutë

Te numrat absolutë, kolona e zogjve mban 95.53% të variancës së gjashtë grupeve. Graçanica ka 14,672 regjistrime, 98.56% zogj. Fushë Kosova ka 3,567, 98.01% zogj. Ato do ta tërhiqnin PCA-në me madhësinë e përpjekjes, jo me përbërjen.

`log1p` e ul pjesën e variancës së zogjve në 23.25%, por vlera mbetet numër regjistrimesh. Komuna me shumë regjistrime qëndron më lart se komuna me pak. Përpjesëtimi e heq totalin e rreshtit, prandaj krahasohen profilet.

Z-score bëhet pas përpjesëtimit. Pa të, përpjesëtimi i zogjve ka devijim standard 0.2603 dhe `E panjohur` 0.0360, prandaj zogjtë do të peshonin më shumë.

## Matrica

`processed/matrica_pca_komuna_taxon.csv` ka 38 rreshta dhe kolonat `komuna`, `rajoni`, `z_Zogj`, `z_Insekte`, `z_Bimë`, `z_Kërpudha`, `z_Tjera`, `z_E panjohur`.

| Kolona | Mesatarja | Devijimi standard |
|---|---:|---:|
| `z_Zogj` | 0 | 1 |
| `z_Insekte` | 0 | 1 |
| `z_Bimë` | 0 | 1 |
| `z_Kërpudha` | 0 | 1 |
| `z_Tjera` | 0 | 1 |
| `z_E panjohur` | 0 | 1 |

Graçanica, pas përpjesëtimit, ka 0.9856 zogj. Z-score i saj për zogjtë është 2.272.

## Dokumentimi i detyrës

- **Varësia:** `processed/agg_municipality_taxon.csv` dhe shënimi për PCA te `reports/agregimi_sipas_komunes.md`.
- **Input:** gjashtë kolonat `regjistrime_*`.
- **Çka u bë:** U shkrua `standardize_pca_matrix()` dhe matrica e standardizuar.
- **Rreshta para / pas:** 38 / 38.
- **Kolona para / pas:** matrica burimore mbetet. Rezultati ka komunën, rajonin dhe 6 kolona Z.
- **Pse u bë:** PCA merr profilet e grupeve, me peshë të barabartë. `year`, gjerësia dhe gjatësia nuk standardizohen.
- **Output:** `reports/shkallezimi_pca.md`, `processed/matrica_pca_komuna_taxon.csv` dhe `standardize_pca_matrix()` te `notebooks/03_vetite.ipynb`.
- **Commit:** `Standardize the municipality by taxon group matrix for PCA`.
