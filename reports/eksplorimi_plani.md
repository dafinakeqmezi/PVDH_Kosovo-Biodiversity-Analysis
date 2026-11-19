# Plani i eksplorimit

**Versioni:** 1.0
**Data:** 19.11.2026
**Statusi:** Plani. Deri më 29.11.2026 eksplorimi punon mbi `processed/biodiversity_features.csv`.

## Varësia

Input: `processed/biodiversity_features.csv` (46,456 rreshta × 128 kolona). Pyetjet dhe rëndësia e kolonave vijnë nga `reports/rendesia_e_kolonave.md`. Grupi biologjik, stina, periudha, `is_threatened` dhe `in_protected_area` vijnë nga notebook-u 03. Mostrat e Pjesës I nuk përdoren: të dyja mbajnë 46.6% të specieve.

## Tabela e planit

| Pyetja | Variablat | Metoda | Vizualizimi |
| --- | --- | --- | --- |
| Shpërndarja sipas komunës dhe grupit biologjik | `municipality_sq`, `taxon_group`, `species`, `district` | Për çdo komunë dhe grup: numri i regjistrimeve dhe numri i specieve unike. Përqindja e regjistrimeve brenda komunës, që vëllimi i Graçanicës të mos fshehë profilin. | Hartë nxehtësie e përqindjes së grupeve për komunë, dhe shtylla të grupuara të specieve unike. |
| Trendi kohor | `year`, `season`, `period`, `species` | Për çdo vit me vit të njohur: numri i regjistrimeve dhe numri i specieve unike. Stina si ritëm brenda vitit. Vitet boshe nuk futen në vijë. | Dy vija sipas vitit, një për regjistrimet dhe një për speciet. Shtylla për stinën. |
| Speciet e kërcënuara në zonat e mbrojtura | `is_threatened`, `protectedArea`, `in_protected_area`, `species`, `is_species_level` | Vetëm `is_threatened = 1` (VU, EN, CR) dhe rreshta në nivel specie. Numër speciesh unike brenda dhe jashtë zonës, dhe sipas emrit të zonës. `NE` dhe `DD` mbeten jashtë, sepse nuk janë 0. | Shtylla të specieve të kërcënuara sipas zonës, dhe krahasim brenda / jashtë. |
| Lidhja përpjekje–pasuri specie | `municipality_sq`, numri i rreshtave si përpjekje, `species` si pasuri | Një pikë për komunë. Përpjekja është sa regjistrime ka komuna, jo `individualCount`. Pasuria është sa specie unike. Lidhja matet me Spearman, sepse pasuria nuk rritet në vijë të drejtë me numrin e rreshtave. | Shpërndarje pikash: përpjekja në boshtin x, pasuria në boshtin y, me emrat e komunave ekstreme. |

## Vendimi dhe arsyetimi

- **Katër pyetje, jo një grafik për çdo kolonë.** Pyetjet janë ato të Pjesës I: komuna, grup biologjik, kohë, IUCN dhe zonë e mbrojtur. Lidhja përpjekje–pasuri i bashkon komunën me specien.
- **Regjistrimi dhe specia numërohen veç.** Numri i rreshtave mat ku është vëzhguar. Numri i specieve unike mat pasurinë. Në Pjesën I, 2020 ka më shumë rreshta se 2024 dhe më pak specie. Një vijë e vetme do ta fshihte këtë.
- **Përqindja brenda komunës për grupin biologjik.** Numri bruto i rreshtave e bën Graçanicën profil zogjsh vetëm sepse aty ka shumë rreshta. Përqindja tregon përbërjen. Kjo është e njëjta arsye për të cilën PCA mori përpjesëtime, jo numra absolutë.
- **`is_threatened = 1` është VU, EN ose CR.** `NE`, `DD` dhe rreshti EX mbeten bosh. Boshllëku nuk bëhet 0 dhe nuk hyn te speciet e kërcënuara.
- **`in_protected_area` është sqarimi semantik i Pjesës I.** 0 përfshin `Jashtë zonës së mbrojtur`. Kjo nuk është verifikim i ri me hartë.
- **Përpjekja është numri i regjistrimeve të komunës.** `individualCount` ka rëndësi të ulët në Pjesën I, mungon në 17,587 rreshta dhe nuk tregon sa është kërkuar. Pasuria është `species.nunique()`. Spearman përdoret sepse një komunë e vogël mund të ketë shumë specie pa pasur shumë rreshta.
- **`district` vetëm grupon.** Përgjigjja e komunës lexohet te `municipality_sq`. Koordinatat nuk e zëvendësojnë emrin e komunës.
- **Asnjë rresht nuk ndryshon në këtë hap.** Plani fikson metodën para vizatimit.

## Dokumentimi i detyrës

- **Input:** `processed/biodiversity_features.csv` dhe `reports/rendesia_e_kolonave.md`.
- **Çka u bë:** U shkrua plani me katër pyetje, variablat, metodën dhe vizualizimin.
- **Rreshta para / pas:** 46,456 / 46,456. Tabela e vetive nuk u ndryshua.
- **Pse u bë:** Që eksplorimi deri më 29 nëntor të përgjigjet në pyetjet e projektit, jo në një grafik për çdo kolonë.
- **Output:** `reports/eksplorimi_plani.md` dhe `notebooks/06_eksplorimi.ipynb`.
- **Commit:** `Jeta: plani i eksplorimit`.
- **Decision + Rationale:** shih seksionin "Vendimi dhe arsyetimi".
