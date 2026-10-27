# Mostrimi

**Versioni:** 1.1  
**Data:** 27.10.2026  
**Statusi:** `processed/sample_random.csv`, `processed/sample_stratified.csv` dhe tabela e krahasimit.

## Varësia

Mostrat nxirren nga dataset-i origjinal (46,831 rreshta), si gjithë puna deri te checkpoint-i. Llogaritja është te seksioni 7 i `notebooks/01_mbledhja_kualiteti.ipynb`. Mostrat ruajnë 42 kolonat ashtu siç janë në CSV-në burimore. Interpretimi (kur përdoret secila mostër dhe si ndikon anshmëria) është te seksioni "Përfundimi" më poshtë.

## Metoda

| | Mostra e rastësishme | Mostra e shtresëzuar |
|---|---|---|
| Madhësia | 10,000 rreshta | 10,000 rreshta |
| `random_state` | 42 | 42 |
| Si zgjidhen rreshtat | `df.sample(n=10_000)`: çdo rresht ka të njëjtën gjasë | brenda çdo klase, `sample(n=n_k)` |
| Shtresat | – | 69: 68 klasa + `(mungon)` për rreshtat pa `class` |
| Shpërndarja | – | proporcionale: n_k = 10,000 × (rreshtat e klasës / 46,831), rrumbullakuar me mbetjen më të madhe që totali të jetë saktësisht 10,000 |
| Skedari | `processed/sample_random.csv` | `processed/sample_stratified.csv` |

## Tabela e krahasimit: % sipas klasës

Përmbledhje (pp = pikë përqindjeje):

| Mostra | Rreshta | Klasa të përfaqësuara (nga 69) | Diferenca maksimale (pp) | TVD (pp) |
|---|---:|---:|---:|---:|
| dataset-i i plotë | 46,831 | 69 | 0.000 | 0.000 |
| mostra e rastësishme | 10,000 | 46 | 0.222 | 0.703 |
| mostra e shtresëzuar | 10,000 | 42 | 0.006 | 0.104 |

- **Diferenca maksimale:** diferenca më e madhe absolute ndërmjet % së një klase në mostër dhe në dataset-in e plotë.
- **TVD** (distanca e variacionit total) = ½ × Σ |% mostër − % plotë|, pra sa pikë përqindjeje duhet zhvendosur që shpërndarjet të jenë identike.

15 klasat kryesore (tabela e plotë me 69 klasa është te `reports/01_mostrimi_krahasimi_klasa.csv`):

| Klasa | Regjistrime (plotë) | % plotë | % rastësishme | % shtresëzuar | n rastësishme | n shtresëzuar | Dif. rastësishme (pp) | Dif. shtresëzuar (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Aves | 28,785 | 61.466 | 61.580 | 61.470 | 6,158 | 6,147 | +0.114 | +0.004 |
| Insecta | 11,543 | 24.648 | 24.500 | 24.650 | 2,450 | 2,465 | -0.148 | +0.002 |
| Magnoliopsida | 2,701 | 5.768 | 5.990 | 5.770 | 599 | 577 | +0.222 | +0.002 |
| Liliopsida | 940 | 2.007 | 1.900 | 2.010 | 190 | 201 | -0.107 | +0.003 |
| Lecanoromycetes | 612 | 1.307 | 1.280 | 1.310 | 128 | 131 | -0.027 | +0.003 |
| (mungon) | 388 | 0.829 | 0.780 | 0.830 | 78 | 83 | -0.049 | +0.001 |
| Arachnida | 358 | 0.764 | 0.760 | 0.770 | 76 | 77 | -0.004 | +0.006 |
| Gastropoda | 279 | 0.596 | 0.540 | 0.600 | 54 | 60 | -0.056 | +0.004 |
| Mammalia | 273 | 0.583 | 0.670 | 0.580 | 67 | 58 | +0.087 | -0.003 |
| Squamata | 190 | 0.406 | 0.470 | 0.410 | 47 | 41 | +0.064 | +0.004 |
| Agaricomycetes | 187 | 0.399 | 0.340 | 0.400 | 34 | 40 | -0.059 | +0.001 |
| Amphibia | 109 | 0.233 | 0.270 | 0.230 | 27 | 23 | +0.037 | -0.003 |
| Eurotiomycetes | 49 | 0.105 | 0.100 | 0.110 | 10 | 11 | -0.005 | +0.005 |
| Polypodiopsida | 49 | 0.105 | 0.080 | 0.110 | 8 | 11 | -0.025 | +0.005 |
| Clitellata | 43 | 0.092 | 0.110 | 0.090 | 11 | 9 | +0.018 | -0.002 |

**Sa varet mostra e rastësishme nga rastësia:** me 200 vlera të ndryshme të `random_state`, TVD e mostrës së rastësishme është mesatarisht 0.89 pp, dhe në 95% të rasteve nën 1.36 pp. Mostra e shtresëzuar ka 0.104 pp. Ky dallim nuk varet nga fara e zgjedhur.

**Klasat e rralla:**
- Mostra e shtresëzuar nuk ka 27 klasa. Të gjitha kanë **1–2 regjistrime** në tërë dataset-in (36 regjistrime, 0.072%), dhe pjesa e tyre proporcionale është nën 0.5 rresht. **Të 35 klasat me ≥5 regjistrime janë të përfaqësuara.**
- Mostra e rastësishme nuk ka 23 klasa, deri në 6 regjistrime secila. Klasat që përfshin ose jo varen nga rastësia.

Kontroll dytësor, rajoni, që nuk është variabël shtresëzimi:

| Rajoni | % plotë | % rastësishme | % shtresëzuar |
|---|---:|---:|---:|
| Prishtinë | 54.95 | 54.91 | 55.54 |
| Prizren | 11.25 | 11.53 | 11.01 |
| Gjilan | 8.87 | 9.33 | 8.60 |
| Mitrovicë | 6.82 | 6.72 | 7.03 |
| Pejë | 6.81 | 6.97 | 6.62 |
| Gjakovë | 5.76 | 5.44 | 5.74 |
| Ferizaj | 5.54 | 5.10 | 5.46 |

Shtresëzimi sipas klasës nuk e përmirëson shpërndarjen sipas rajonit: të dyja mostrat ndryshojnë deri në ~0.6 pp nga dataset-i i plotë.

## Kontrollet

| Kontrolli | Rezultati |
|---|---|
| Secila mostër ka 10,000 rreshta | kalon |
| Pa rreshta të përsëritur | kalon |
| Shpërndarja proporcionale mblidhet në 10,000 | kalon |
| Çdo shtresë merr ±1 nga pjesa e saj e saktë | kalon |
| E njëjta farë jep të njëjtën mostër | kalon |
| Çdo `gbifID` i mostrave ekziston në dataset | kalon |

## Vendimi dhe arsyetimi

- **Madhësia: 10,000 rreshta (21.4% e dataset-it).** Sipas planit. Mjafton që klasat kryesore të kenë qindra deri në mijëra rreshta: zogj 6,147, insekte 2,465, bimë me lule 577.
- **`random_state = 42` fiks.** Kështu mostrat dalin identike në çdo ekzekutim, edhe më 26 tetor dhe te kontrolli me Restart & Run All. Kjo kontrollohet me `assert`.
- **Shtresëzimi sipas klasës, me shpërndarje proporcionale.** Qëllimi është të ruhet përbërja taksonomike e dataset-it. Shpërndarja proporcionale e ruan % e çdo klase brenda ±0.006 pp. Shpërndarja e barabartë (e njëjta n për çdo klasë) do ta ndryshonte qëllimisht përbërjen, kështu që nuk zgjidhet.
- **Rreshtat pa `class` janë shtresë më vete.** Kështu mostra i ruan edhe mungesat në të njëjtën përqindje (0.83%), në vend që t'i hedhë ose t'i përzjejë me klasat e tjera.
- **Pa minimum prej 1 rreshti për klasë.** Me minimum, 27 klasa me 1–2 regjistrime do të futeshin me peshë deri në 5 herë më të madhe se në dataset. Shpërndarja do të prishej për të fituar klasa që nuk mund të analizohen me 1 rresht. Për grupe të rralla përdoret dataset-i i plotë.
- **Përfundimi i krahasimit:** **mostra e shtresëzuar e ruan më mirë shpërndarjen sipas klasës.** TVD e saj është 0.104 pp kundrejt 0.703 pp, dhe diferenca maksimale 0.006 pp kundrejt 0.222 pp. Mostra e rastësishme mbetet si referencë pa supozime për variablat që nuk janë të shtresëzuara.

## Përfundimi: kur përdoret secila mostër dhe anshmëria (25 tetor)

Numrat janë nga dataset-i origjinal (46,831 rreshta) dhe nga tabelat e seksioneve 7 dhe 7.2.

### Cila mostër e ruan më mirë shpërndarjen

**Mostra e shtresëzuar sipas klasës.** Ajo e ruan % e çdo klase brenda **0.006 pp**, me TVD **0.104 pp**. Mostra e rastësishme ka diferencë maksimale **0.222 pp** dhe TVD **0.703 pp**. Dallimi nuk varet nga fara: me 200 vlera të `random_state`, mostra e rastësishme ka mesatarisht 0.89 pp TVD, dhe në 95% të rasteve nën 1.36 pp. Te variablat që nuk janë të shtresëzuara, si rajoni, të dyja mostrat janë njësoj afër dataset-it (deri në ~0.6 pp).

### Kur përdoret secila

| Përdorimi | Mostra |
|---|---|
| Eksplorim dhe grafikë sipas grupit taksonomik; provë e shpejtë e kodit të Pjesës II | **e shtresëzuar** (përbërja taksonomike e saktë) |
| Vlerësime për variabla që nuk janë të shtresëzuara (rajoni, koha, burimi) dhe si referencë pa supozime | **e rastësishme** |
| Numri i specieve, speciet e kërcënuara, speciet e rralla, speciet për komunë, numrat finalë të raportit | **asnjëra, dataset-i i plotë** |

Arsyeja e rreshtit të fundit: secila mostër ruan vetëm **1,909 nga 4,095 specie (46.6%)**, **14 nga 37 speciet e kërcënuara**, dhe vetëm 365–378 nga 1,727 speciet me një regjistrim. Mostrimi i ruan përqindjet e regjistrimeve, por jo pasurinë e specieve.

### Si ndikon anshmëria

Të dyja mostrat e **përsërisin anshmërinë** e dataset-it, sepse e marrin atë nga burimi:

| Treguesi | Dataset-i | E rastësishme | E shtresëzuar |
|---|---:|---:|---:|
| Graçanicë | 31.33% | 31.19% | 31.49% |
| pika e Ligatinave të Henc | 27.86% | 27.66% | 28.01% |
| eBird | 55.54% | 55.71% | 55.72% |
| një vëzhgues (obsr1505715) | 35.18% | 35.44% | 35.35% |
| zogj (Aves) | 61.47% | 61.58% | 61.47% |

Një mostër përfaqësuese e dataset-it është përfaqësuese edhe e anshmërisë së tij. Graçanica mbetet me rreth një të tretën e regjistrimeve në çdo mostër. Mostrimi nuk e korrigjon anshmërinë. Për ta zvogëluar, Pjesa II mund të përdorë:
- shtresëzim sipas rajonit ose burimit;
- kufi për numrin e regjistrimeve për pikë dhe ditë;
- analizë të kontrollit pa eBird ose pa pikën e Henc-it.

Por atëherë mostra nuk përfaqëson më dataset-in, por një dizajn të zgjedhur, dhe kjo duhet shkruar.

### Përfundimi

**Mostra e shtresëzuar është zgjedhja e parazgjedhur për eksplorim.** Mostra e rastësishme përdoret si referencë, dhe dataset-i i plotë për çdo numër final dhe për çdo analizë të specieve. Asnjë mostër nuk e heq anshmërinë e vëzhgimit. Ajo trajtohet me normalizim (seksioni 6: specie/km², regjistrime/1,000 banorë) dhe me kontrolle pa burimet dominuese.

Tabelat: `reports/01_mostrimi_anshmeria.csv` dhe `reports/01_mostrimi_speciet.csv` (seksioni 7.2 i notebook-ut).

## Dokumentimi i detyrës

- **Input:** `dataset/kosovo_overall_biodiversity.csv` (kolona `class` për shtresat).
- **Çka u bë:** U nxorr një mostër e rastësishme dhe një e shtresëzuar sipas klasës, secila me 10,000 rreshta dhe `random_state = 42`. U krahasua % sipas klasës, dhe si kontroll edhe sipas rajonit, me dataset-in e plotë.
- **Rreshta para / pas:** 46,831 → 10,000 (secila mostër).
- **Kolona para / pas:** 42 / 42.
- **Pse u bë:** Për eksplorim më të shpejtë me një nënbashkësi që ruan përbërjen e dataset-it, dhe për të treguar sa ndikon metoda e mostrimit në përfaqësimin e klasave.
- **Output:** `processed/sample_random.csv`, `processed/sample_stratified.csv`, `reports/mostrimi.md`, `reports/01_mostrimi_krahasimi_klasa.csv`, `reports/01_mostrimi_permbledhje.csv`, `reports/01_mostrimi_krahasimi_rajoni.csv`, seksioni 7 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Add random and class-stratified samples`, `Add sampling comparison tables`, `Document sampling decision and rationale`.
