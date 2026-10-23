# Integrimi: bashkimi i dataset-it me të dhënat e komunave

**Versioni:** 1.0  
**Data:** 22.10.2026  
**Statusi:** Dataset-i me sipërfaqe dhe popullsi, me kontrollin e bashkimit.

## Varësia

Ky task përdor `processed/municipalities.csv` nga **Të dhënat e jashtme** (19 tetor, `reports/burimet_e_te_dhenave_te_komunave.md`). Bashkimi është te seksioni 5.2 i `notebooks/01_mbledhja_kualiteti.ipynb`. Rezultati, `processed/biodiversity_municipalities.csv`, është input për agregimet e 21–23 tetorit.

## Çelësi i komunës

Dataset-i i ka komunat me emër dygjuhësh (`Ferizaj / Uroševac`). 3 komuna kanë vetëm një emër (`Junik`, `Prizren`, `Zubin Potok`). Çelësi krijohet kështu:

1. merret pjesa para ` / ` (emri shqip);
2. hiqen hapësirat e tepërta;
3. shkronjat bëhen të vogla;
4. hiqen diakritikët (`ç` → `c`, `ë` → `e`).

| Emri në dataset | Çelësi |
|---|---|
| `Graçanicë / Gračanica` | `gracanice` |
| `Mitrovicë e Jugut / Kosovska Mitrovica` | `mitrovice e jugut` |
| `Junik` | `junik` |

I njëjti funksion zbatohet te kolona `komuna` e `processed/municipalities.csv`.

| Emri në dataset | Çelësi | Rreshta | Komuna te `municipalities.csv` | Emri te ASK | Përputhet | Emri i ASK përputhet pa korrigjim |
|---|---|---:|---|---|---|---|
| Deçan / Dečan | `decan` | 1,403 | Deçan | Deçan | po | po |
| Dragash / Dragaš | `dragash` | 939 | Dragash | Dragash | po | po |
| Ferizaj / Uroševac | `ferizaj` | 337 | Ferizaj | Ferizaj | po | po |
| Fushë Kosovë / Kosovo Polje | `fushe kosove` | 3,567 | Fushë Kosovë | Fushë Kosovë | po | po |
| Gjakovë / Đakovica | `gjakove` | 526 | Gjakovë | Gjakovë | po | po |
| Gjilan / Gnjilane | `gjilan` | 263 | Gjilan | Gjilan | po | po |
| Gllogoc / Glogovac | `gllogoc` | 140 | Gllogoc | Gllogoc | po | po |
| Graçanicë / Gračanica | `gracanice` | 14,672 | Graçanicë | Graçanicë | po | po |
| Hani i Elezit / Elez Han | `hani i elezit` | 347 | Hani i Elezit | Hani i Elezit | po | po |
| Istog / Istok | `istog` | 341 | Istog | Istog | po | po |
| Junik | `junik` | 549 | Junik | Junik | po | po |
| Kaçanik / Kačanik | `kacanik` | 694 | Kaçanik | Kaçanik | po | po |
| Kamenicë / Kamenica | `kamenice` | 2,724 | Kamenicë | Kamenicë | po | po |
| Klinë / Klina | `kline` | 397 | Klinë | Klinë | po | po |
| Kllokot / Klokot | `kllokot` | 13 | Kllokot | Kllokot | po | po |
| Leposaviq / Leposavić | `leposaviq` | 1,625 | Leposaviq | Leposaviq | po | po |
| Lipjan / Lipljan | `lipjan` | 465 | Lipjan | Lipjan | po | po |
| Malishevë / Mališevo | `malisheve` | 165 | Malishevë | Malishevë | po | po |
| Mamushë / Mamuša | `mamushe` | 1 | Mamushë | Mamushë | po | po |
| Mitrovicë e Jugut / Kosovska Mitrovica | `mitrovice e jugut` | 479 | Mitrovicë e Jugut | Mitrovicë | po | **jo** |
| Mitrovicë e Veriut / Severna Kosovska Mitrovica | `mitrovice e veriut` | 24 | Mitrovicë e Veriut | Mitrovicë e Veriut | po | po |
| Novobërdë / Novo Brdo | `novoberde` | 347 | Novobërdë | Novobërdë | po | po |
| Obiliq / Obilić | `obiliq` | 303 | Obiliq | Obiliq | po | po |
| Partesh / Parteš | `partesh` | 24 | Partesh | Partesh | po | po |
| Pejë / Peć | `peje` | 2,449 | Pejë | Pejë | po | po |
| Podujevë / Podujevo | `podujeve` | 316 | Podujevë | Podujevë | po | po |
| Prishtinë / Priština | `prishtine` | 5,924 | Prishtinë | Prishtinë | po | po |
| Prizren | `prizren` | 3,993 | Prizren | Prizren | po | po |
| Rahovec / Orahovac | `rahovec` | 219 | Rahovec | Rahovec | po | po |
| Ranillug / Ranilug | `ranillug` | 984 | Ranillug | Ranillug | po | po |
| Shtërpcë / Štrpce | `shterpce` | 1,160 | Shtërpcë | Shtërpcë | po | po |
| Shtime / Štimlje | `shtime` | 55 | Shtime | Shtime | po | po |
| Skenderaj / Srbica | `skenderaj` | 164 | Skenderaj | Skënderaj | po | po |
| Suharekë / Suva Reka | `suhareke` | 170 | Suharekë | Suharekë | po | po |
| Viti / Vitina | `viti` | 148 | Viti | Viti | po | po |
| Vushtrri / Vučitrn | `vushtrri` | 301 | Vushtrri | Vushtrri | po | po |
| Zubin Potok | `zubin potok` | 270 | Zubin Potok | Zubin Potok | po | po |
| Zveçan / Zvečan | `zvecan` | 333 | Zveçan | Zveqan | po | **jo** |

Me çelësin, emrat e ASK përputhen në 36/38 raste pa korrigjim. ASK shkruan `Mitrovicë` (për Mitrovicën e Jugut) dhe `Zveqan`, kurse dataset-i `Mitrovicë e Jugut` dhe `Zveçan`. Prandaj `municipalities.csv` ka kolonën `komuna` me emrat shqip të dataset-it, kurse emri origjinal i ASK ruhet te `emri_ask`.

## Rezultati i kontrollit të bashkimit

Bashkimi: `left join` i dataset-it (46,831 rreshta) me `municipalities.csv` (38 rreshta) sipas `komuna_key`, me `validate="many_to_one"`. Pandas ndalet nëse një çelës përsëritet te tabela e komunave.

| Kontrolli | Vlera | Pritet | Kalon |
|---|---:|---:|---|
| rreshta para | 46,831 | 46,831 | po |
| rreshta pas | 46,831 | 46,831 | po |
| kolona para | 42 | 42 | po |
| kolona pas | 50 | 50 | po |
| komuna në dataset | 38 | 38 | po |
| komuna te municipalities.csv | 38 | 38 | po |
| komuna që përputhen | 38 | 38 | po |
| rreshta pa përputhje | 0 | 0 | po |
| rreshta me popullsi bosh pas bashkimit | 0 | 0 | po |
| rreshta me sipërfaqe njësie bosh pas bashkimit | 0 | 0 | po |
| popullsia e 38 komunave pas bashkimit | 1,602,515 | 1,602,515 | po |
| emra të ASK që përputhen pa korrigjim | 36 | – | – |

Kontrollet janë `assert` në notebook. Kontrollohet edhe që `gbifID` mbetet në të njëjtin rend, pra që bashkimi nuk ka shtuar, hequr ose rirenditur rreshta.

## Dataset-i me sipërfaqe dhe popullsi

`processed/biodiversity_municipalities.csv`: 46,831 rreshta, 50 kolona: 42 origjinale dhe 8 të reja. Kolonat origjinale ruhen tekstualisht si në CSV-në burimore, p.sh. `2026` dhe `TRUE`, jo `2026.0` dhe `True`. U kontrollua që janë identike me burimin.

| Kolona e re | Kuptimi |
|---|---|
| `komuna_key` | çelësi i komunës |
| `popullsia_2024` | popullsia e komunës (ASK 2024, me vlerësimin për 4 komunat veriore) |
| `popullsia_e_regjistruar_2024` | numri i regjistruar në regjistrim |
| `popullsia_vleresim_ask` | `True` për Leposaviq, Mitrovicë e Veriut, Zubin Potok, Zveçan |
| `siperfaqja_km2` | sipërfaqja e komunës (bosh për dy Mitrovicat) |
| `njesia_e_siperfaqes` | njësia për normalizim për km² (dy Mitrovicat bashkë) |
| `siperfaqja_njesise_km2` | sipërfaqja e njësisë (336.18 për dy Mitrovicat) |
| `dendesia_banore_km2` | banorë për km² të njësisë |

Madhësia: 24.7 MB, nën kufirin prej 100 MB të GitHub.

## Vendimi dhe arsyetimi

- **Çelësi merret nga emri shqip, pa diakritikë.** Emri serb mungon te 3 komuna, dhe diakritikët shkruhen ndryshe në burime të ndryshme (p.sh. `Skënderaj` te ASK, `Skenderaj` në dataset). Me këtë çelës, ndryshimet e shkrimit nuk e prishin bashkimin.
- **Bashkimi bëhet me `left join` dhe `validate="many_to_one"`.** `left` i mban të gjitha 46,831 vëzhgimet edhe nëse një komunë nuk do të gjendej. `many_to_one` garanton që asnjë vëzhgim nuk dyfishohet nga një çelës i përsëritur. Kontrolli 38/38 dhe 0 rreshta pa përputhje tregojnë që `left` dhe `inner` japin të njëjtin rezultat këtu.
- **Për normalizim për km² përdoret `siperfaqja_njesise_km2`, jo `siperfaqja_km2`.** Te dy Mitrovicat sipërfaqja e veçantë mungon, dhe njësia e përbashkët shmang NaN në agregime.
- **Dataset-i origjinal nuk preket.** Rezultati ruhet në `processed/`. Më 26 tetor bashkimi ri-ekzekutohet mbi `biodiversity_clean.csv` të Delizës me të njëjtin kod.

## Dokumentimi i detyrës

- **Input:** `dataset/kosovo_overall_biodiversity.csv` (kolona `municipality`), `processed/municipalities.csv`.
- **Çka u bë:** U krijua çelësi i komunës nga emrat dygjuhësh. Dataset-i u bashkua me sipërfaqen dhe popullsinë me left join. U kontrollua 38/38 përputhje dhe numri i rreshtave para e pas.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 / 50.
- **Pse u bë:** Që agregimet sipas komunës (21 tetor) të llogarisin specie për km² dhe regjistrime për 1,000 banorë.
- **Output:** `processed/biodiversity_municipalities.csv`, `reports/bashkimi_i_komunave.md`, `reports/01_bashkimi_celesat.csv`, `reports/01_bashkimi_kontrolli.csv`, seksioni 5.2 i `notebooks/01_mbledhja_kualiteti.ipynb`.
- **Commit:** `Join the dataset with municipality area and population`.
