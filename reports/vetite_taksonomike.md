# Vetitë taksonomike dhe të ruajtjes

**Versioni:** 1.0  
**Data:** 22.10.2026  
**Statusi:** `taxon_group` nga `class` dhe `is_threatened` nga `iucnRedListCategory`.

## Varësia

Zgjedhja e vetive e 13.10.2026 (`reports/feature_selection.md`). `class` dhe `iucnRedListCategory` mbahen. Funksioni i lexon ato kolona dhe nuk e ndryshon CSV-në.

## Tabela e mapping-ut për `taxon_group`

Grupi merret nga `class`. Nëse `class` mungon, grupi është `E panjohur`, edhe kur `kingdom` është i plotë.

| `class` | `taxon_group` |
|---|---|
| `Aves` | Zogj |
| `Insecta` | Insekte |
| `Magnoliopsida`, `Liliopsida`, `Polypodiopsida`, `Pinopsida`, `Bryopsida`, `Lycopodiopsida`, `Marchantiopsida`, `Chlorophyceae`, `Trebouxiophyceae`, `Charophyceae`, `Glaucophyceae` | Bimë |
| `Lecanoromycetes`, `Agaricomycetes`, `Eurotiomycetes`, `Dothideomycetes`, `Pezizomycetes`, `Leotiomycetes`, `Sordariomycetes`, `Rhizophydiomycetes`, `Chytridiomycetes`, `Arthoniomycetes`, `Candelariomycetes`, `Lobulomycetes`, `Saccharomycetes`, `Dacrymycetes`, `Cystobasidiomycetes`, `Orbiliomycetes`, `Pucciniomycetes`, `Laboulbeniomycetes`, `Mesochytriomycetes`, `Sareomycetes`, `Taphrinomycetes`, `Tremellomycetes` | Kërpudha |
| `Arachnida`, `Gastropoda`, `Mammalia`, `Squamata`, `Amphibia`, `Clitellata`, `Bivalvia`, `Malacostraca`, `Testudines`, `Diplopoda`, `Chilopoda`, `Petromyzonti`, `Branchiopoda`, `Chromadorea`, `Copepoda`, `Eurotatoria`, `Cephalopoda`, `Polychaeta`, `Oligohymenophorea`, `Chrysophyceae`, `Bacillariophyceae`, `Peronosporea`, `Prymnesiophyceae`, `Cyrtophoria`, `Gymnostomatea`, `Phytomyxea`, `Dictyochophyceae`, `Dinophyceae`, `Litostomatea`, `Perkinsea`, `Tubothalamea`, `Alphaproteobacteria`, `Euglenoidea` | Tjera |
| mungon | E panjohur |

Algat e gjelbra që në këtë dataset janë nën `Plantae` hyjnë te Bimë, sepse detyra nuk ka grup më vete për to.

| `taxon_group` | Rreshta |
|---|---:|
| Zogj | 28,785 |
| Insekte | 11,543 |
| Bimë | 3,738 |
| Kërpudha | 971 |
| Tjera | 1,406 |
| E panjohur | 388 |

## Tabela e mapping-ut për `is_threatened`

| `iucnRedListCategory` | `is_threatened` | Rreshta |
|---|---|---:|
| `VU`, `EN`, `CR` | 1 | 650 |
| `LC`, `NT` | 0 | 29,245 |
| `NE`, `DD`, NaN | NaN | 16,935 |
| `EX` | NaN, e dokumentuar veçmas | 1 |

## Vendimi dhe arsyetimi

`VU`, `EN` dhe `CR` janë kategoritë e rrezikuara, prandaj bëhen 1. `LC` dhe `NT` nuk janë të rrezikuara, prandaj bëhen 0. `NE` dhe `DD` nuk janë vlerësim rreziku, dhe NaN nuk dihet, prandaj mbeten NaN. Nuk bëhen 0.

`EX` është një rresht: `Calathus mollis`, `gbifID` 5284839027, klasa `Insecta`, pa vit. Nuk është as 1, sepse specia është e zhdukur dhe jo në `VU`/`EN`/`CR`, as 0, sepse zhdukja nuk do të thotë «e parrezikuar». `is_threatened` mbetet NaN për këtë rresht.

## Dokumentimi i detyrës

- **Varësia:** `reports/feature_selection.md`, 13.10.2026.
- **Input:** `class`, `iucnRedListCategory`.
- **Çka u bë:** U shkrua mapping-u dhe funksioni për `taxon_group` dhe `is_threatened`. `EX` u dokumentua veçmas.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 në CSV. Funksioni shton dy kolona te rezultati.
- **Pse u bë:** Grupi biologjik dhe statusi i rrezikimit dalin nga `class` dhe kategoria IUCN, pa e kthyer të panjohurën në 0.
- **Output:** `reports/vetite_taksonomike.md` dhe `add_taxon_features()` te `notebooks/03_vetite.ipynb`.
- **Commit:** `Add taxon_group and is_threatened from class and IUCN category`.
