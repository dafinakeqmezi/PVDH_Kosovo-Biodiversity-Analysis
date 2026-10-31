# Verifikimi i të dhënave të përpunuara

**Data:** 31.10.2026  
**Rezultati:** 22 PASS / 0 FAIL në kontrollin e rezultateve; 14 teste ekzistuese kalojnë.

Ky është kontroll vetëm për lexim. Nuk u ndryshua asnjë skedar në `dataset/` ose `processed/`. Hash-et e të gjithë skedarëve ekzistues në këto dy dosje u krahasuan para dhe pas kontrollit.

## Metoda dhe rezultatet

U ekzekutua [skripti i verifikimit](../scripts/verify_processed.py), i cili lexon funksionet e notebook-ëve pa ekzekutuar qelizat që shkruajnë skedarë. Vetitë, agregimet dhe PCA u rindërtuan në memorie. Krahasimi i agregimeve bëhet sipas çelësit unik, jo sipas renditjes së rreshtave me numërime të barabarta. Krahasimi i PCA lejon ndryshimin ekuivalent të shenjës së komponentëve dhe tolerancë numerike.

| Kontrolli | Rezultati | Evidenca |
| --- | --- | --- |
| Integriteti i checkpoint-it | PASS | Hash-et e burimit, CSV-së dhe schema-s përputhen me manifestin; origjinali përputhet me Git HEAD. |
| Dimensionet dhe identifikuesit | PASS | 46,831 × 42 në origjinal; 46,456 × 83 në të pastruar; saktësisht 375 ID të miratuara largohen. |
| Schema dhe rregullat e vlerave | PASS | Rileximi me schema dhe rregullat numerike/kalendarike të implementuara kalojnë. |
| Duplikatet | PASS | Fituesit dhe grupet e përjashtuara përputhen me vendimin dhe referencën historike. |
| Kolonat bazë në dataset-in e vetive | PASS | Të 83 kolonat e checkpoint-it ruhen, me të njëjtat ID dhe vlera. |
| Ndërtimi i vetive | PASS | Rindërtimi jep 46,456 × 128 dhe përputhet me skedarin e ruajtur. |
| Pesë agregimet v1 | PASS | Komunë, komunë × grup, kohë, klasë × rajon dhe specie përputhen me origjinalin. |
| Pesë agregimet v2 | PASS | Të njëjtat agregime përputhen me dataset-in e pastruar. |
| Matricat e standardizuara dhe PCA, v1/v2 | PASS | Z-score dhe rezultatet e tre komponentëve përputhen me llogaritjet nga matricat përkatëse. |
| One-hot, IUCN dhe log1p | PASS | Kontrolle shtesë të formulave: një 1 për grup dummy, NE/DD pa rang, log1p dhe mungesat të ruajtura. |
| Inventari i mungesave dhe burimet | PASS | Numërimet NaN dhe përqindjet përputhen me origjinalin; totalet për datasetKey përputhen me përmbledhjen e publikuesve. |
| Integrimi i komunave | PASS | Kolonat origjinale ruhen; atributet e bashkuara përputhen me tabelën e komunave. |
| Kopja e ndërmjetme dhe rreshtat e larguar | PASS | Kopja e ndërmjetme është identike me CSV-në e checkpoint-it; ID-të e larguara përputhen me listën e vendimit. |
| Dy mostrat | PASS për origjinalin | Secila ka 10,000 ID unike dhe vlera identike me rreshtat përkatës të origjinalit. |

Tabela grupon kontrollet; numri 22 i referohet grupeve të kontrollit të ekzekutuara nga skripti. [Validimi ekzistues](validimi.md) me 23 PASS është kontroll tjetër i checkpoint-it, jo i njëjti numër testesh.

## Mostrat: kufizim i rëndësishëm

| Skedari | Burimi | Rreshta | ID të larguara më vonë si duplikate |
| --- | --- | ---: | ---: |
| sample_random.csv | Origjinali | 10,000 | 85 |
| sample_stratified.csv | Origjinali | 10,000 | 89 |

Këto nuk janë mostra të pastrimit. Janë të vlefshme për krahasimin e metodave të mostrimit mbi origjinalin. Nëse duhen përdorur për analizë mbi checkpoint-in, duhen rinxjerrë me metodën dhe farën e dokumentuar dhe të ruhen si version i ri. Nuk mjafton të fshihen këto ID nga mostrat: kjo do të ndryshonte madhësinë dhe shpërndarjen pa e përsëritur mostrimin.

## Kufijtë e verifikimit

- Krahasimi konfirmon konsistencën me kodin dhe input-et lokale; nuk provon saktësinë biologjike ose gjeografike të burimit.
- Nuk u rikontrolluan burimet e jashtme/API dhe nuk u krye verifikim GIS i zonave të mbrojtura.
- Për shumicën e daljeve përdoren funksionet ekzistuese për rindërtim, krahas kontrolleve të pavarura për ID, one-hot, rangun IUCN dhe log1p. Një gabim konceptual i përbashkët mes kodit dhe vendimit mund të kërkojë shqyrtim tjetër.
- Notebook-u 03 përmban funksionet por jo një qelizë fundore që lexon input-et, i thërret dhe eksporton të gjitha daljet. Verifikimi i rezultateve të ruajtura kalon, por kjo nuk është provë e riprodhueshmërisë me Restart & Run All në mjedis të pastër.
- Vlerat ekstreme të ruajtura, NaN-të e lejuara, kufijtë e diskretizimit dhe supozimi semantik për protectedArea mbeten kufizime të dokumentuara, jo gabime që korrigjohen automatikisht këtu.

## Riekzekutimi

Nga rrënja e repo-s, me varësitë të instaluara:

```bash
python scripts/verify_processed.py
python -m unittest discover -s tests -v
```

## Dokumentimi i detyrës

1. **Input:** dataset-i origjinal, skedarët në `processed/`, manifesti/schema, vendimi i duplikateve dhe funksionet e notebook-ëve.
2. **Çka u bë:** Kontroll i integritetit dhe rindërtim në memorie i daljeve kryesore, pa eksportim mbi to.
3. **Rreshta para / pas:** 46,456 / 46,456; **kolona para / pas:** 83 / 83 në checkpoint.
4. **Pse u bë:** Të verifikohet përputhja e rezultateve para përfshirjes në raportin e përbashkët.
5. **Output:** ky raport dhe `scripts/verify_processed.py`.
6. **Commit:** `Consolidate Part I report and verify processed outputs` (mesazh i propozuar).

**Decision + Rationale:** Nuk u gjet mospërputhje numerike në kontrollet e listuara, prandaj nuk u ndryshuan të dhënat. Mostrat etiketohen sipas burimit të tyre real; kufizimet e riprodhueshmërisë nuk fshihen nga rezultati PASS.
