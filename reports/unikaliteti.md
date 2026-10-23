# Unikaliteti i të dhënave

**Versioni:** 1.0  
**Data:** 22.10.2026  
**Statusi:** Numri real i duplikateve, kandidatët dhe definicioni i propozuar.

## Varësia

Ky task zbaton dimensionin **Unikaliteti** nga **Korniza e kualitetit** (`reports/korniza_e_kualitetit.md`, U1–U5). Llogaritja është te seksioni 3.10 i `notebooks/01_mbledhja_kualiteti.ipynb`. **Vendimin final dhe largimin e duplikateve i bën Deliza** (20–21 tetor), duke u nisur nga ky definicion dhe nga `processed/duplicate_candidates.csv`.

## Si matet

- **Kriteri i planit:** `species` + `eventDate` + `decimalLatitude` + `decimalLongitude` + vëzhguesi (`recordedBy`, pa hapësira të tepërta dhe me shkronja të vogla).
- Kriteri aplikohet vetëm te rreshtat me të 5 fushat të plota: 41,395 rreshta. 3,853 rreshta nuk kanë `recordedBy`.
- **Grup** = rreshta me të njëjtat 5 vlera. **Rreshta të tepërta** = rreshta në grupe − grupe, pra një rresht mbetet për çdo grup.
- Numri nuk u supozua paraprakisht. U llogarit nga të dhënat dhe u krahasua me kritere të tjera.

## Numri real

| Kriteri | Grupe | Rreshta në grupe | Rreshta të tepërta | % e të gjithë rreshtave |
|---|---:|---:|---:|---:|
| gbifID | 0 | 0 | 0 | 0.00 |
| rreshta identikë (të 42 kolonat) | 0 | 0 | 0 | 0.00 |
| species + data + koordinata (pa vëzhgues) | 1,927 | 4,592 | 2,665 | 5.69 |
| **species + data + koordinata + vëzhgues (kriteri i planit)** | 1,288 | 3,132 | **1,844** | 3.94 |
| **definicioni i propozuar** | 238 | 616 | **378** | 0.81 |

- **`gbifID` është unik** dhe nuk ka asnjë rresht identik në të 42 kolonat.
- **Me kriterin e planit: 1,288 grupe, 3,132 rreshta në grupe, 1,844 rreshta të tepërta (3.94%).**
- Pa vëzhguesin, numri rritet në 2,665, sepse vëzhgues të ndryshëm në të njëjtin vend dhe ditë nuk janë duplikatë.
- Me definicionin e propozuar mbeten **378 rreshta të tepërta (0.81%)** në 238 grupe.

## Grupet sipas llojit

Çdo grup i kriterit të planit u klasifikua automatikisht, me rregullat në këtë radhë:

| Lloji | Duplikat i propozuar | Grupe | Rreshta | Rreshta të tepërta |
|---|---|---:|---:|---:|
| vëzhgim i përsëritur me numër të njëjtë | **po** | 236 | 612 | 376 |
| i njëjti rresht në dataset-e të ndryshme | **po** | 2 | 4 | 2 |
| numërime të ndryshme të së njëjtës ditë | jo | 735 | 1,510 | 775 |
| qendër e rrjetës 10 km (7071 m) | jo | 239 | 708 | 469 |
| ekzemplarë të ndryshëm (catalogNumber) | jo | 51 | 169 | 118 |
| datë jo ditore (vit/muaj) | jo | 25 | 129 | 104 |

| Lloji | Rregulla | Burimi kryesor |
|---|---|---|
| i njëjti rresht në dataset-e të ndryshme | grupi ka më shumë se një `datasetKey` | ENA + BOLD, herbariumet e Vjenës |
| datë jo ditore (vit/muaj) | të paktën një rresht ka datë vetëm me vit ose muaj | ENA, Adam Mickiewicz Univ. |
| ekzemplarë të ndryshëm (catalogNumber) | të gjithë janë ekzemplarë (`PRESERVED_SPECIMEN`, `MATERIAL_SAMPLE` …) me `catalogNumber` të ndryshëm | ENA, Adam Mickiewicz Univ. |
| qendër e rrjetës 10 km (7071 m) | `coordinateUncertaintyInMeters` = 7071 | HabiProt |
| vëzhgim i përsëritur me numër të njëjtë | `individualCount` i njëjtë (ose bosh) te të gjithë rreshtat e grupit | eBird, Observation.org |
| numërime të ndryshme të së njëjtës ditë | çdo grup tjetër: `individualCount` ndryshon | eBird (1,477 rreshta) |

## Shqyrtimi manual

U shqyrtuan me dorë 18 grupe nga 9 burime dhe nga të gjitha llojet. Për secilin u panë `catalogNumber`, `individualCount`, `basisOfRecord`, `locality`, publikuesi dhe pasiguria e koordinatave.

| # | Rasti | gbifID | Rreshta në grup | Vendimi | Arsyeja |
|---:|---|---|---:|---|---|
| 1 | eBird, Garrulus glandarius, Liqeni i Badovcit | 5688208496 | 2 | **duplikat** | I njëjti vëzhgues, vend dhe ditë, numri 1 në dy lista (OBS të ndryshme): i njëjti shpend në dy lista. |
| 2 | eBird, Picus viridis, Bozevce | 5304671044 | 2 | **duplikat** | Dy lista të të njëjtit vëzhgues në të njëjtën ditë; numri 1 te të dyja. |
| 3 | eBird, Poecile palustris, Bozevce | 5505753852 | 2 | **duplikat** | Të njëjtat dy lista si rasti i mësipërm, numri 2 te të dyja: lista e përsëritur, jo shpendë të tjerë. |
| 4 | Observation.org, Phoenicurus ochruros, Mitrovicë | 6447736029 | 2 | **duplikat** | I njëjti përdorues, pikë (35 m) dhe ditë, numri 1 te të dy: vëzhgimi i ngarkuar dy herë. |
| 5 | Macedonian Ecological Society, Nebria attemsi, Ljuboten 1906 | 3071190713 | 4 | **duplikat** | 4 rreshta pa asnjë dallim (pa numër, pa catalogNumber): i njëjti grumbullim i shënuar disa herë. |
| 6 | ENA + BOLD, Euscorpius hadzii, 2021 | 6434425548 | 2 | **duplikat** | S00009 dhe UP SC00009: i njëjti ekzemplar në dy databaza. |
| 7 | Herbarium WU + NHM Wien, Paramoltkia doerfleri, 1918 | 1584382204 | 2 | **duplikat** | Dörfler nr. 848 në dy herbariume: dublikatë herbariumi të të njëjtit grumbullim. |
| 8 | Observation.org, Chlidonias niger, Liqeni 1 | 6448581086 | 2 | jo duplikat | I njëjti vend dhe ditë, por 15 dhe 20 individë: dy numërime të ndara. |
| 9 | HabiProt, Caliaeschna microstigma | 5284987599 | 2 | jo duplikat | 7 dhe 10 individë, koordinata = qendra e qelizës 10 km: ka gjasa dy vende brenda qelizës. |
| 10 | HabiProt, Carpocoris purpureipennis | 5284716226 | 4 | jo duplikat | 4 rreshta me 10, 1, 1, 1 individë në qelizën 10 km: vende ose numërime të ndryshme. |
| 11 | HabiProt, Everes sebrus | 5284977542 | 2 | jo duplikat | Numri 1 te të dy, por pa koordinata të sakta (7071 m) nuk dihet nëse është i njëjti vend; mbahen. |
| 12 | Macedonian Ecological Society, Otiorhynchus relictus, 1906 | 3071190766 | 8 | jo duplikat | 8 rreshta me 1 ose 2 individë: ekzemplarë ose burime literature të ndryshme. |
| 13 | ENA, Rhyacophila fasciata, 2024 | 6471379490 | 2 | jo duplikat | MNCN-ADN 200133 dhe 200132: dy ekzemplarë të ndryshëm nga i njëjti grumbullim. |
| 14 | ENA, Rhyacophila macedonica, 2023 | 6471376553 | 2 | jo duplikat | MNCN-ADN 200131 dhe 200130: dy ekzemplarë të ndryshëm. |
| 15 | Adam Mickiewicz Univ., Alinda fallax, 1935-06-01 | 3478785497 | 16 | jo duplikat | 16 ekzemplarë me catalogNumber të njëpasnjëshëm: individë të ndryshëm të një grumbullimi. |
| 16 | Adam Mickiewicz Univ., Alinda biplicata, 1906 | 3478937662 | 24 | jo duplikat | 24 ekzemplarë të ndryshëm; data ka vetëm vitin. |
| 17 | ENA, Phlebotomus perfiliewi, 2022 | 6191368728 | 2 | jo duplikat | Data vetëm me vit dhe ekzemplarë të ndryshëm (77_63, 07_3). |
| 18 | ENA, Phlebotomus tobbi, 2022 | 6191513544 | 5 | jo duplikat | 5 ekzemplarë të ndryshëm; data vetëm me vit. |

Rregulla automatike jep të njëjtin vendim si shqyrtimi manual te 18/18 raste. **Kjo nuk është validim i pavarur**, sepse rregullat u nxorën nga këto raste. Është kontroll që rregullat e shkruara në kod zbatojnë saktë vendimet e marra me dorë.

## Definicioni i propozuar

> **Duplikat** janë dy ose më shumë rreshta me të njëjtën `species`, datë me precizion ditor, koordinata dhe vëzhgues, që përshkruajnë **të njëjtin vëzhgim ose ekzemplar**. Kjo ndodh kur:
>
> 1. rreshtat vijnë nga **dataset-e të ndryshme** (i njëjti ekzemplar ose vëzhgim i publikuar dy herë), ose
> 2. rreshtat vijnë nga i njëjti dataset dhe kanë **`individualCount` të njëjtë** (ose bosh te të gjithë), pa qenë ekzemplarë me `catalogNumber` të ndryshëm dhe pa koordinata të qendrës së rrjetës 10 km.
>
> **Nuk janë duplikatë:**
> - ekzemplarë me `catalogNumber` të ndryshëm: individë të ndryshëm nga i njëjti grumbullim;
> - rreshtat me datë vetëm me vit ose muaj: kriteri është shumë i gjerë për ta;
> - rreshtat në qendër të rrjetës 10 km (7071 m): mund të jenë vende të ndryshme brenda qelizës;
> - rreshtat me `individualCount` të ndryshëm: numërime të ndara të së njëjtës ditë.

Me këtë definicion: **238 grupe, 616 rreshta, 378 rreshta të tepërta** (në `processed/duplicate_candidates.csv`: `duplikat_i_propozuar = True`).

## Vendimi dhe arsyetimi

- **Kriteri i planit (species + data + koordinata + vëzhgues) është i nevojshëm, por jo i mjaftueshëm.** Ai gjen 1,844 rreshta të tepërta, por shqyrtimi tregoi se shumica nuk janë i njëjti vëzhgim. Janë ekzemplarë të ndryshëm, pika të përbashkëta të rrjetës 10 km, ose numërime të ndara.
- **`individualCount` dallon vëzhgimin e përsëritur nga numërimi i ri.** Dy lista të eBird me numrin 1 për të njëjtin shpend janë i njëjti vëzhgim. 15 dhe 20 individë janë dy numërime.
- **`catalogNumber` dallon ekzemplarët.** 16 kërmij me numra të njëpasnjëshëm janë 16 individë, jo një rresht i përsëritur 16 herë.
- **Rreshtat me 7071 m mbahen.** Pa koordinatat e sakta nuk mund të provohet që janë i njëjti vend. Fshirja e tyre do ta zvogëlonte pa arsye kontributin e HabiProt.
- **Rreshtat pa `recordedBy` (3,853) nuk kontrollohen** me këtë kriter. Edhe dyfishimet ndërmjet platformave ku i njëjti person ka emra të ndryshëm (p.sh. përdorues te iNaturalist dhe emër i plotë te Observation.org) nuk gjenden. Këto janë kufizime të metodës.

## Shënime për Delizën (20–21 tetor)

- Propozimi: nga çdo grup me `duplikat_i_propozuar = True` mbahet rreshti me më shumë fusha të plota. Vendimi është i yti.
- **Numërimet e ndryshme të së njëjtës ditë (775 rreshta të tepërta, kryesisht eBird) nuk janë duplikatë**, por **mos i mblidhni për bollëkun**. Për prani mjafton një rresht për specie, vend dhe ditë. Për bollëk duhet maksimumi ose një numërim, jo shuma.

## Dokumentimi i detyrës

- **Input:** `dataset/kosovo_overall_biodiversity.csv` (`gbifID`, `species`, `eventDate`, koordinatat, `recordedBy`, `individualCount`, `catalogNumber`, `basisOfRecord`, `coordinateUncertaintyInMeters`, `datasetKey`), `processed/gbif_datasets_cache.csv` (publikuesit).
- **Çka u bë:** U kontrollua `gbifID`. U numëruan duplikatet logjike me kriterin e planit dhe me kritere krahasuese, u klasifikuan grupet sipas llojit, u shqyrtuan me dorë 18 grupe dhe u propozua definicioni.
- **Rreshta para / pas:** 46,831 / 46,831. Asnjë rresht nuk u fshi.
- **Kolona para / pas:** 42 / 42.
- **Pse u bë:** Duplikatet e fryjnë numrin e vëzhgimeve dhe të specieve për komunë. Fshirja pa definicion të qartë do të hiqte ekzemplarë dhe numërime të vërteta.
- **Output:** `processed/duplicate_candidates.csv`, `reports/unikaliteti.md`, `reports/01_unikaliteti.csv`, `reports/01_duplikatet_sipas_llojit.csv`, `reports/01_duplikatet_shqyrtimi.csv`, seksioni 3.10 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Add uniqueness check, duplicate candidates and proposed definition`.
