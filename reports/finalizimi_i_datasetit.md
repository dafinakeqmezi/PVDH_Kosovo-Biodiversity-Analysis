# Finalizimi i dataset-it të pastruar

1. **Input:** dataset/kosovo_overall_biodiversity.csv; të gjithë hapat e notebooks/02_pastrimi.ipynb, nga origjinali deri te vendimi individualCount.
2. **Çka u bë:** Ekzekutim i plotë; verifikim i log-ut, ID-ve, mungesave, datave dhe rikthimit të tipeve; ruajtje e checkpoint-it të ngrirë me SHA-256.
3. **Rreshta para / pas:** 46,831 / 46,456; **kolona para / pas:** 42 / 83. Vetë finalizimi nuk ndryshon rreshta ose kolona.
4. **Pse u bë:** Dafina dhe Jeta duhet të përdorin të njëjtin version të pastruar për rezultatet përfundimtare.
5. **Output:** processed/biodiversity_clean.csv, processed/biodiversity_clean_schema.json, processed/biodiversity_clean_manifest.json, processed/cleaning_log.csv dhe reports/kontrolli_i_finalizimit.csv.
6. **Commit:** Finalize and freeze the cleaned biodiversity dataset (mesazh i propozuar).
7. **Decision + Rationale:** Pastrimi ngrihet. Riekzekutimi me të njëjtin rezultat lejohet, por nuk mbishkruhet checkpoint-i me përmbajtje tjetër. Ndryshimet e ardhshme kërkojnë miratim të ekipit, dokumentim dhe version të ri.

## Gjurmueshmëria

- Hapa të log-ut të notebook-ut 02: **102**, pa përsëritje, në rend, me vazhdimësi rreshtash/kolonash dhe arsye/output/commit të plotësuar.
- Rreshta të hequr si duplikate: **375**. Nuk fshihen rreshta të tjerë.
- Mungesa individualCount: **17,587**, pa imputim.
- SHA-256 i CSV final: `e83b0cab86ef5021cc23fbd1029071883c16a203d61cdc118bdafac6cb30117a`.
- SHA-256 i origjinalit: `68593b9e19dbfcb8cfff9d5b74ae947bb60e794d8d5d11ecd3df542d51296b8e`.
- Manifesti kontrollon edhe schema dhe rreshtat e log-ut me prefiks 02_clean:. Hapat e notebook-ëve të tjerë nuk përfshihen në hash-in e këtij log-u.

## Dorëzimi te ekipi

**Njoftim i përgatitur për Dafinën dhe Jetën; dërgimi nuk konfirmohet nga notebook-u:**

Pastrimi është finalizuar. Përdorni `processed/biodiversity_clean.csv` (46,456 rreshta, 83 kolona). Origjinali nuk ka ndryshuar. Dafina: rigjenero agregimet dhe mostrat nga ky version. Jeta: rigjenero vetitë nga ky version dhe PCA-në nga matrica e rigjeneruar e komunave. Rezultatet e mëparshme nga origjinali nuk janë rezultatet finale mbi të dhënat e pastruara. Mos ndryshoni këtë CSV drejtpërdrejt; çdo korrigjim diskutohet dhe versionohet.

Për rikthim të saktë të tipeve përdoret funksioni `load_clean_dataset(path, schema_path)` në notebook 02, me rrugët e CSV/schema finale. CSV vetëm nuk ruan category, nullable boolean ose Int64. IUCN mbetet kategori pa renditje; kodimi i Jetës bëhet veçmas. year/month nuk imputohen nga intervalet e paqarta. Flamujt hapësinorë nuk provojnë saktësinë e komunës; protectedArea mbështetet në sqarimin e përdorueses, jo në kontroll të pavarur GIS.

Kopja `kosovo_biodiversity_clean.csv` mbetet dalje e ndërmjetme për përputhshmëri; në këtë checkpoint është identike me CSV finale. Skedarët e Dafinës dhe Jetës nuk ndryshohen nga ky notebook.
