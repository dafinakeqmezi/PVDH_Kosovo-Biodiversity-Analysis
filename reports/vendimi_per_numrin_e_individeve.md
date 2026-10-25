# Vendimi për numrin e individëve

1. **Input:** individualCount, datasetKey, basisOfRecord, class dhe district nga kopja pas trajtimit të vlerave të pavlefshme; strategjia_e_mungesave.md dhe mekanizmat_e_mungeses.md.
2. **Çka u bë:** U rillogarit mungesa dhe shpërndarja pas deduplikimit, në përgjithësi dhe sipas katër grupimeve; u vlerësua imputimi dhe u vendos ruajtja e NA.
3. **Rreshta para / pas:** 46,456 / 46,456; **kolona para / pas:** 83 / 83. Mungesa para/pas: 17,587 / 17,587; imputime: 0.
4. **Pse u bë:** Numri i individëve është matje e raportuar, jo numri i regjistrimeve; imputimi pa mbështetje do të shtonte numra të paobservuar.
5. **Output:** shperndarja_e_numrit_te_individeve.csv, numri_i_individeve_sipas_grupeve.csv, numri_i_individeve_para_pas.csv dhe cleaning_log.csv.
6. **Commit:** Analyze individual counts and document the no-imputation decision.

## Evidenca

Mungojnë **17,587 nga 46,456 (37.86%)**. Te vlerat e njohura, mediana është 2, mesatarja 23.14, Q95 34, maksimumi 10,200 dhe skewness 26.63. Shpërndarja është e anuar fort djathtas, por kjo vetëm nuk justifikon imputimin. Ekstremet ruhen; ky hap nuk bën log1p, shkallëzim ose trajtim outliers të Pjesës II.

Mungesa sipas burimit varion nga 0.00% deri 100.00%. Nga 125 burime, 82 nuk kanë asnjë numër të raportuar dhe nuk kanë medianë të brendshme. Madhësitë e grupeve dhe numrat e vlerave të njohura raportohen gjithmonë, sepse përqindja e një grupi të vogël nuk është evidencë e fortë.

## Decision + Rationale

**Keep + flag; pa imputim.** Ruhet individualCount si Int64 nullable dhe flamuri ekzistues individualCount_is_missing. Nuk shtohet was_imputed sepse nuk u imputua asnjë vlerë; numri 0 i imputimeve regjistrohet në tabelën para/pas dhe log.

- Sipas [Darwin Core](https://dwc.tdwg.org/terms/#individualCount), fusha mat individët e pranishëm në një regjistrim. Mungesa nuk do të thotë 0 ose 1; zero e raportuar mund të ketë kuptim dhe nuk trajtohet automatikisht si mungesë.
- Mediana globale do t'i caktonte të njëjtin numër regjistrimeve nga protokolle, taksone dhe burime të ndryshme. Mediana sipas class ose basisOfRecord është ende shumë e gjerë; ajo nuk kontrollon përpjekjen e vrojtimit, numërimin e tufave ose përfaqësimin e ekzemplarëve.
- Mediana sipas datasetKey nuk ekziston për burimet pa numra. Edhe kur ekziston, nuk kemi evidencë që mungesat kanë të njëjtën shpërndarje si numrat e raportuar. Rikuperimi kërkon të dhëna burimore ose metadata të protokollit; nuk ka mapping determinist në kolonat aktuale.
- Dallimet ndërmjet grupeve janë në përputhje me mungesë të lidhur me veçori të vëzhguara, por nuk provojnë MAR. MCAR/MAR/MNAR nuk identifikohen vetëm nga këto tabela; MNAR nuk përjashtohet. Pa protokoll/perpjekje vrojtimi dhe validim të modelit, imputimi do të kërkonte supozime shtesë të pambështetura.
- Regjistrimet mbeten të përdorshme për praninë dhe numërimin e regjistrimeve/specieve. Për analizën e individualCount, raporto numrin dhe përqindjen e rasteve të njohura; nëse agregohet, përdor sum(min_count=1) që grupet krejt bosh të mos bëhen 0. Shuma e numrave të raportuar nuk është vlerësim i popullatës dhe mund të përfshijë vrojtime të përsëritura.

| rreshta | te_plotesuara | mungojne | mungesa_pct | minimumi | q25 | mediana | q75 | q95 | q99 | maksimumi | mesatarja | skewness | zero | negative | jo_te_plota |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 46456 | 28869 | 17587 | 37.85732736352678 | 1.0 | 1.0 | 2.0 | 6.0 | 34.0 | 150.0 | 10200.0 | 23.142055492050297 | 26.62962256157869 | 0 | 0 | 0 |

## Sipas basisOfRecord

| grupimi | grupi | rreshta | te_plotesuara | mungojne | mungesa_pct | minimumi | q25 | mediana | q75 | q95 | q99 | maksimumi | mesatarja | skewness | zero | negative | jo_te_plota |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| basisOfRecord | HUMAN_OBSERVATION | 42185 | 28391 | 13794 | 32.69882659713168 | 1.0 | 1.0 | 2.0 | 6.0 | 34.0 | 153.09999999999854 | 10200.0 | 23.44743052375753 | 26.408331867581264 | 0 | 0 | 0 |
| basisOfRecord | MACHINE_OBSERVATION | 376 | 13 | 363 | 96.54255319148936 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 | 0 | 0 | 0 |
| basisOfRecord | MATERIAL_CITATION | 317 | 217 | 100 | 31.545741324921135 | 1.0 | 1.0 | 2.0 | 6.0 | 40.39999999999998 | 75.68 | 87.0 | 7.976958525345622 | 3.1418103443161285 | 0 | 0 | 0 |
| basisOfRecord | MATERIAL_SAMPLE | 622 | 102 | 520 | 83.60128617363344 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 | 0 | 0 | 0 |
| basisOfRecord | OBSERVATION | 1 | 0 | 1 | 100.0 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0 | 0 | 0 |
| basisOfRecord | OCCURRENCE | 1208 | 78 | 1130 | 93.54304635761589 | 1.0 | 1.0 | 2.0 | 4.0 | 30.0 | 53.0 | 53.0 | 5.948717948717949 | 3.125575725061403 | 0 | 0 | 0 |
| basisOfRecord | PRESERVED_SPECIMEN | 1747 | 68 | 1679 | 96.10761305094448 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 6.989999999999995 | 9.0 | 1.2058823529411764 | 6.052815359891445 | 0 | 0 | 0 |

Të gjitha grupet, përfshirë burimin, klasën dhe rajonin, janë në numri_i_individeve_sipas_grupeve.csv.
