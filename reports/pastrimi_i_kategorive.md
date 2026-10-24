# Pastrimi i kategorive

1. **Input:** 46,456 rreshta pas largimit të duplikateve; 17 kolona kategorike.
2. **Çka u bë:** NFC, heqje/ngjeshje hapësirash dhe unifikim i varianteve që ndryshojnë vetëm në shkronja. Kodet standarde bëhen uppercase; emrat ruajnë variantin më të shpeshtë. Identifikuesit dhe teksti i lirë nuk harmonizohen si kategori.
3. **Rreshta para/pas:** 46,456 / 46,456; **kolona para/pas:** 79 / 81.
4. **Pse u bë:** Që variante mekanike të të njëjtit emër të mos krijojnë grupe të ndara, pa bashkuar taksone ose vende të ndryshme.
5. **Output:** kategorite_para_pas.csv (edhe vlerat e pandryshuara), permbledhja_e_pastrimit_te_kategorive.csv, emrat_shqip_te_komunave.csv dhe cleaning_log.csv.
6. **Commit:** Remove approved duplicates and normalize categories (mesazh i propozuar).
7. **Decision + Rationale:** Nuk përdoret fuzzy matching ose heqje diakritikash. Gabimet e mundshme të shkrimit përtej case/hapësirave kërkojnë fjalor autoritativ, jo korrigjim automatik. municipality_original ruan burimin; municipality_sq ruan emrin shqip. IUCN mbetet category pa renditje.

Gjithsej 0 qeliza u ndryshuan. Numri i ndryshimeve matet pas deduplikimit.

| kolona | vlera_unike_para | vlera_unike_pas | rreshta_te_ndryshuar | mungesa_para | mungesa_pas |
| --- | --- | --- | --- | --- | --- |
| scientificName | 4647 | 4647 | 0 | 37 | 37 |
| species | 4095 | 4095 | 0 | 1213 | 1213 |
| vernacularName | 3314 | 3314 | 0 | 3807 | 3807 |
| kingdom | 7 | 7 | 0 | 37 | 37 |
| phylum | 25 | 25 | 0 | 69 | 69 |
| class | 68 | 68 | 0 | 388 | 388 |
| order | 226 | 226 | 0 | 333 | 333 |
| family | 683 | 683 | 0 | 158 | 158 |
| genus | 2421 | 2421 | 0 | 195 | 195 |
| taxonRank | 11 | 11 | 0 | 37 | 37 |
| iucnRedListCategory | 8 | 8 | 0 | 1213 | 1213 |
| municipality | 38 | 38 | 0 | 0 | 0 |
| district | 7 | 7 | 0 | 0 | 0 |
| protectedArea | 21 | 21 | 0 | 0 | 0 |
| protectedAreaDesignation | 6 | 6 | 0 | 0 | 0 |
| basisOfRecord | 7 | 7 | 0 | 0 | 0 |
| license | 3 | 3 | 0 | 0 | 0 |