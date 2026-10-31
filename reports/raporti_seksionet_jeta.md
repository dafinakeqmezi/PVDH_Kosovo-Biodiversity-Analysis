# Raporti i Pjesës I – Zgjedhja, krijimi, diskretizimi, binarizimi, transformimi dhe reduktimi

**Data:** 31.10.2026  
**Burimi i numrave:** `notebooks/03_vetite.ipynb`. Vetitë e rreshtave janë ndërtuar mbi `processed/biodiversity_clean.csv` (46,456 rreshta). PCA finale është mbi `processed/agg_municipality_taxon_v2.csv`.

CSV-ja origjinale mbetet me 42 kolona dhe 46,831 rreshta. Kolonat e reja lindin vetëm te rezultati.

## 1. Zgjedhja

Nga 42 kolonat, 29 mbahen dhe 13 largohen. Numri doli nga rëndësia, redundanca, mungesat, tipi dhe pyetjet e projektit. Nuk u caktua paraprakisht.

I vetmi çift vërtet i dyfishtë është statusi i IUCN. `iucnRedListStatus` largohet. `iucnRedListCategory` mbahet. `taxonKey` dhe `scientificName` nuk janë e njëjta gjë, prandaj të dyja mbeten. `elevation` dhe `individualCount` dalin nga nënbashkësia analitike, por detyrat e mëvonshme krijojnë veti prej tyre pa i kthyer në atë nënbashkësi dhe pa e shkruar CSV-në origjinale.

Burimi: `reports/fjalori_i_te_dhenave.md`, `reports/redundanca.md`, `reports/rendesia_e_kolonave.md`, `reports/zgjedhja_e_vetive.md`.

## 2. Krijimi

`build_features(df, datasets)` i bashkon nëntë hapat dhe i ruan te `processed/biodiversity_features.csv`: 46,456 rreshta dhe 128 kolona. 83 kolonat e pastruara qëndrojnë. Shtohen 45.

| Vetia | Burimi | Rregulli |
|---|---|---|
| `season` | `month` | dimër 12, 1, 2; pranverë 3–5; verë 6–8; vjeshtë 9–11 |
| `decade` | `year` | `(year // 10) * 10` |
| `is_recent` | `year` | `year >= 2017` |
| `taxon_group` | `class` | Zogj, Insekte, Bimë, Kërpudha, Tjera; klasa bosh = `E panjohur` |
| `is_threatened` | kodi IUCN | VU, EN, CR = 1; LC, NT = 0; NE, DD, bosh dhe EX mbeten bosh |
| `in_protected_area` | `protectedArea` | 1 kur ka emër zone; 0 kur është bosh ose «Jashtë zonës së mbrojtur» |
| `is_citizen_science` | publikuesi dhe `basisOfRecord` | 1 vetëm për publikues të shkencës qytetare dhe `HUMAN_OBSERVATION` |
| `n_issues` | `issue` | numëron 10 flamujt seriozë |

Ku mungon viti, `decade` dhe `is_recent` mbeten bosh. Ku mungon muaji, `season` mbetet bosh. Te të dhënat e pastra, grupet janë Zogj 28,532, Insekte 11,447, Bimë 3,723, Tjera 1,396, Kërpudha 970 dhe E panjohur 388. Rreshti i vetëm EX ka `is_threatened` bosh dhe `iucn_rank` 6. `is_citizen_science` është 1 për 40,984 rreshta dhe 0 për 5,472. Asnjë `datasetKey` nuk mbetet pa publikues.

Burimi: `reports/vetite_kohore.md`, `reports/vetite_taksonomike.md`, `reports/vetite_e_burimit.md`, `reports/lista_e_vetive.md`.

## 3. Diskretizimi

Lartësia ndahet në Fushë (297–800 m), Kodrinore (801–1,500 m) dhe Malore (1,501–2,656 m). 0 m nuk është lartësi reale e Kosovës. Te të dhënat e pastra, zeroja është bërë bosh nga pastrimi. E panjohur është 40,297, Fushë 3,711, Kodrinore 1,314 dhe Malore 1,134.

Viti origjinal ndahet në periudha: 1826–1899 (16), 1900–1949 (304), 1950–1999 (4,111), 2000–2009 (1,402), 2010–2019 (10,187) dhe 2020–2026 (28,168). 2,268 vite bosh mbeten bosh. `decade` mbetet kolonë më vete.

`individualCount` krahasoi `pd.cut` me `pd.qcut`. Gjerësia e barabartë fut pothuajse të gjitha vlerat e njohura në një grup, prandaj u zgjodh `pd.qcut` me 4 grupe. Te të dhënat e pastra: 1–2 = 15,815, 3–6 = 6,335, 7–10200 = 6,719, bosh = 17,587. Boshllëku nuk imputohet.

Burimi: `reports/zona_e_lartesise.md`, `reports/periudhat_kohore.md`, `reports/klasa_e_numrit.md`.

## 4. Binarizimi

One-hot bëhet për `taxon_group`, `district` dhe `basisOfRecord`. Kategoria me më pak se 47 rreshta shkon te `Tjera`. Vetëm `OBSERVATION` u bashkua, si `basisOfRecord_Tjera`. `drop_first` është false, sepse heqja e parë alfabetike do të hiqte Bimë, Ferizajn dhe `HUMAN_OBSERVATION`. Dalin 20 kolona. Çdo rresht ka një 1 në secilin grup.

IUCN kodohet një herë nga `iucnRedListCategory`: LC=1, NT=2, VU=3, EN=4, CR=5, EX=6. NE, DD dhe boshllëku mbeten bosh, me `iucn_evaluated` 0. Te të dhënat e pastra, të vlerësuara janë 29,631 dhe të pavlerësuara 16,825. Dhjetë flamujt seriozë janë kolona 0/1. Shuma e tyre është 2,049. Flamujt informativë nuk bëhen kolona.

`kingdom` nuk merr one-hot, sepse grupi biologjik merret nga `class`. `iasUnionConcern` doli nga nënbashkësia. `strictlyProtected` mbetet bool, siç e la pastrimi.

Burimi: `reports/kolonat_dummy.md`, `reports/kodimi_iucn_dhe_flamujve.md`.

## 5. Transformimi

`individualCount` dhe `coordinateUncertaintyInMeters` janë të anuara djathtas. Te të dhënat e pastra, `log1p` e ul skewness nga 26.63 në 2.07 dhe nga 101.73 në −1.00. Boshllëku mbetet bosh: 17,587 për numrin dhe 31,813 për pasigurinë. Shenja negative e pasigurisë pas `log1p` vjen sepse shumica e vlerave të njohura janë 7,071 m dhe bishti shkon deri në miliona metra. Vlera 7,071 mbahet.

`elevation` nuk shkallëzohet. Viti dhe koordinatat mbeten në njësinë e tyre.

Për krahasimin e komunave përdoren përpjesëtimet e `regjistrime_*`, pastaj Z-score me pjesëtues 38. Blloku `specie_*` nuk përzihet. Pas Z-score, secila nga gjashtë kolonat ka mesatare 0 dhe devijim standard 1.

Burimi: `reports/transformimi_log1p.md`, `reports/shkallezimi_pca.md`.

## 6. Reduktimi

Redundanca hoqi vetëm `iucnRedListStatus`. Varianca dhe korrelacioni u kontrolluan te 34 kolonat e one-hot, IUCN, flamujve dhe `log1p`. Pesë kolona kanë më pak se 47 njësha. I vetmi çift me korrelacion të paktën 0.80 është `flag_RECORDED_DATE_INVALID` dhe `flag_INDIVIDUAL_COUNT_INVALID`, +0.8227 te dataset-i origjinal dhe +0.8226 te i pastri. 348 rreshta i kanë të dyja, 160 vetëm datën dhe 3 vetëm numrin. Asnjë kolonë nuk u hoq. Tri grupet dummy mblidhen në 1, por asnjë çift i tyre nuk kalon 0.80.

### PCA finale

Hyrja është matrica v2 e Dafinës: 38 komuna dhe 46,456 regjistrime. `run_pca_on_clean_matrix()` përdor `standardize_pca_matrix()` dhe `run_municipality_pca()`. Komponentët me `explained_variance_` mbi 1 mbahen.

| Komponenti | explained_variance_ | explained_variance_ratio_ | Kumulative |
|---|---:|---:|---:|
| PC1 | 2.166778 | 0.351626 | 0.351626 |
| PC2 | 1.476464 | 0.239602 | 0.591228 |
| PC3 | 1.097941 | 0.178175 | 0.769403 |
| PC4 | 0.806205 | 0.130831 | 0.900234 |
| PC5 | 0.614774 | 0.099766 | 1.000000 |
| PC6 | 0.000000 | 0.000000 | 1.000000 |

Mbeten PC1, PC2 dhe PC3. Varianca kumulative është 0.769403. PC6 është 0, sepse gjashtë përpjesëtimet mblidhen në 1. Te matrica v1 kumulative ishte 0.770411 dhe po ashtu mbetën tri komponentë. Largimi i 375 duplikateve nuk e ndryshon vendimin.

| Grupi | PC1 | PC2 | PC3 |
|---|---:|---:|---:|
| Zogj | +0.657 | −0.183 | −0.125 |
| Insekte | −0.457 | +0.580 | −0.155 |
| Bimë | −0.316 | −0.540 | +0.078 |
| Kërpudha | −0.075 | +0.137 | +0.903 |
| Tjera | −0.308 | −0.548 | +0.118 |
| E panjohur | −0.398 | −0.140 | −0.352 |

PC1 peshon te zogjtë, PC2 te insektet kundrejt Tjera dhe bimëve, PC3 te kërpudhat. Graçanica është 3.201 te PC1: 14,351 nga 14,563 regjistrimet e saj janë zogj, 98.54%. Mamusha është 3.346 te PC2, sepse ka një regjistrim dhe ai është insekt. Dragashi është 3.712 te PC3.

`processed/pca_municipalities_v2.csv` ka 38 rreshta dhe kolonat `komuna`, `rajoni`, `PC1`, `PC2`, `PC3`. `processed/matrica_pca_komuna_taxon_v2.csv` ruan Z-score. Rezultati i v1 mbetet te `processed/pca_municipalities.csv` për krahasim.

Burimi: `reports/varianca_dhe_korrelacioni.md`, `reports/pca_komunat.md`, `reports/rikalkulimi.md`.

## Dokumentimi i detyrës

- **Varësia:** `processed/agg_municipality_taxon_v2.csv` nga rikalkulimi i 26 tetorit.
- **Input:** blloku `regjistrime_*` i 38 komunave.
- **Çka u bë:** PCA u ri-ekzekutua mbi matricën e pastruar dhe u shkruan gjashtë seksionet.
- **Rreshta para / pas:** 38 / 38. Regjistrimet janë 46,456.
- **Kolona para / pas:** matrica v2 mbetet. Rezultati final ka komunën, rajonin dhe 3 komponentë.
- **Pse u bë:** Rezultati final i PCA dhe seksionet e raportit mbështeten te të dhënat e pastra.
- **Output:** `reports/raporti_seksionet_jeta.md`, `processed/pca_municipalities_v2.csv`, `processed/matrica_pca_komuna_taxon_v2.csv` dhe `run_pca_on_clean_matrix()` te `notebooks/03_vetite.ipynb`.
- **Commit:** `Re-run municipality PCA on the cleaned aggregate matrix`.
