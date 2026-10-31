# Riprodhueshmëria e Pjesës I

**Data:** 31.10.2026  
**Rezultati:** të gjitha fazat kaluan në një mjedis virtual të ri, me Python 3.13.5 në macOS arm64.

Varësitë u instaluan nga `requirements.txt` në një venv të ri, pa përdorur paketat e mjedisit ekzistues. Versionet e varësive të drejtpërdrejta janë të fiksuara; `requirements-lock.txt` regjistron edhe varësitë transitore të këtij mjedisi. Instalimi në platforma të tjera nuk është testuar.

## Procedura

[run_pipeline.py](../scripts/run_pipeline.py) krijon një klon lokal të përkohshëm dhe kopjon notebook-ët, skriptet dhe testet aktuale. Të dhënat e repo-s së punës nuk ndryshohen. Kernel-i i çdo notebook-u përdor pikërisht Python-in me të cilin thirret skripti, jo një kernel tjetër të instaluar globalisht.

Në klonin e provës largohen daljet e derivuara nga `processed/`, përveç cache-it të publikuesve dhe CSV/schema/manifestit të ngrirë që shërbejnë si referencë krahasimi. Kështu, tabela e komunave, inventarët, log-u, kopja e ndërmjetme, agregimet, mostrat, vetitë dhe PCA rigjenerohen nga kodi. Burimet e jashtme përdoren nga cache-i dhe tabelat referuese të dokumentuara, jo nga një shkarkim i ri API.

| Rendi | Faza | Rezultati |
| --- | --- | --- |
| 1 | Notebook-u 01b: përmbledhja e burimeve nga cache-i | PASS |
| 2 | Notebook-u 01, para seksionit 8: diagnostikimi dhe tabela e komunave | PASS |
| 3 | Notebook-u 02: pastrimi, checkpoint-i dhe validimi | PASS |
| 4 | Notebook-u 01 i plotë: agregimet origjinale dhe v2 | PASS |
| 5 | Notebook-u 03 i plotë: vetitë dhe eksportimi i matricave/PCA v1/v2 | PASS |
| 6 | Verifikimi i daljeve të rigjeneruara | 22 PASS / 0 FAIL |
| 7 | Testet ekzistuese | 14 kalojnë |

Faza paraprake e notebook-ut 01 zgjidh varësinë e pastrimit nga `municipalities.csv`. Seksioni 8 i notebook-ut 01 ekzekutohet vetëm pasi ekziston checkpoint-i i pastruar. Gjurmët e fazave janë në [ekzekutimi_pipeline.json](ekzekutimi_pipeline.json).

## Notebook-u 03

Qeliza `execute-feature-pipeline` lexon checkpoint-in me schema-n ekzistuese, kontrollon hash-et dhe ndërton vetitë. Ajo thërret standardizimin dhe PCA-në për të dy versionet e agregimit dhe shkruan pesë skedarë:

- `processed/biodiversity_features.csv`: 46,456 × 128.
- `processed/matrica_pca_komuna_taxon.csv` dhe versionin `_v2`: 38 × 8.
- `processed/pca_municipalities.csv` dhe versionin `_v2`: 38 × 5.

Kontrollohen ID-të unike, 83 kolonat bazë të pandryshuara, mbulimi i publikuesve, kodimi one-hot dhe standardizimi. Loader-i i schema-s importohet nga notebook-u 02 si përkufizim funksioni; qelizat e pastrimit nuk ekzekutohen nga notebook-u 03.

## Riekzekutimi

Nga rrënja e repo-s, pas aktivizimit të një mjedisi me Python 3.13.5:

```bash
python -m pip install -r requirements.txt
python scripts/run_pipeline.py
```

Për të riprodhuar të njëjtin grup versionesh në macOS arm64 përdoret `requirements-lock.txt`. Skripti shfaq vendndodhjen e klonit, notebook-ëve të ekzekutuar dhe log-eve të testimit. Duhet historiku Git që përmban commit-in e referencës së duplikateve `d2708c640de830014edf4c4f35a528849c98455f`; një kopje vetëm me skedarë ose shallow clone pa këtë commit nuk mjafton.

## Kufizimet

- Nuk është testuar instalimi në Windows/Linux ose një version tjetër të Python-it.
- Prova riprodhon analizën nga CSV-ja e projektit dhe cache-i i ruajtur. Nuk provon riprodhimin e shkarkimit origjinal GBIF, sepse data dhe DOI-ja mungojnë.
- Mostrat mbeten mbi origjinalin, sipas eksperimentit të dokumentuar.
- Rregullat dhe supozimet biologjike/hapësinore nuk bëhen të vërteta vetëm sepse kodi ekzekutohet.

## Dokumentimi

1. **Input:** dataset-i origjinal, cache-i GBIF, referenca Git, notebook-ët dhe checkpoint-i i ngrirë për krahasim.
2. **Çka u bë:** Plotësimi i ekzekutimit në notebook-un 03, instalim i pastër dhe rigjenerim në klon të izoluar.
3. **Rreshta para/pas:** 46,831 / 46,456 në pastrim; 46,456 / 46,456 në ndërtimin e vetive. Repo-ja e punës nuk ndryshoi të dhëna.
4. **Pse u bë:** Për të provuar që rezultatet mund të prodhohen nga kodi me varësi të dokumentuara.
5. **Output:** notebook-u 03, skripti i pipeline-it, kërkesat e fiksuara dhe ky raport.
6. **Commit:** `Make Part I pipeline reproducible and prepare submission` (mesazh i propozuar).

**Decision + Rationale:** Prova kryhet në kopje të izoluar për të ruajtur checkpoint-in. Daljet e rigjeneruara verifikohen para çdo propozimi për zëvendësim; këtu nuk nevojitet ndryshim i të dhënave të ruajtura.
