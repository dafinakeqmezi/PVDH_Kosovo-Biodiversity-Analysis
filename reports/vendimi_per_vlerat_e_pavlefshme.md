# Vlerat e pavlefshme dhe kufizimet analitike

1. **Input:** kopja pas deduplikimit/kategorive; vendimi_per_lartesine_zero.md, vlefshmeria.md dhe processed/municipalities.csv.
2. **Çka u bë:** 3,634 zero në elevation u bënë NA. U shtuan statusi i pasigurisë dhe is_species_level.
3. **Rreshta para / pas:** 46,456 / 46,456; **kolona para / pas:** 81 / 83.
4. **Pse u bë:** Të dallohen mungesat e fshehura nga kufizimet analitike, pa fshirë vlera ekstreme reale.
5. **Output:** rregullat_e_vlerave_te_pavlefshme.csv, shperndarja_e_pasigurise.csv, frekuencat_e_pasigurise.csv, shkalla_hapesinore_e_komunave.csv, ndjeshmeria_e_pragut_te_pasigurise.csv, pasiguria_sipas_komunes.csv, niveli_taksonomik.csv, kopja e pastruar dhe cleaning_log.csv.
6. **Commit:** Apply invalid-value rules and flag spatial and taxonomic limits.

## Decision + Rationale

**Lartësia:** Zbatohet vendimi i mëparshëm vetëm për zero. Raporti i Dafinës propozon edhe heqjen jashtë 297–2656 m, por raporti ynë citon minimum tjetër zyrtar (270 m). Pa verifikim DEM/burimor, lartësitë e tjera ruhen, përfshirë ekstremet; nuk imputohen me minimum ose mesatare. Origjinali dhe elevation_was_zero ruajnë gjurmueshmërinë.

**Pasiguria:** Mediana pozitive është 7,071.00 m; moda është 7,071.00 m. Mediana vetëm është shumë e gjerë për komuna të vogla. Zgjedhim si politikë kontrolli pragu = min(mediana pozitive, 1000*sqrt(min(sipërfaqja_km2)/pi)) = **1,866.09 m**. Mediana kufizon ndikimin e vlerave ekstreme; sipërfaqja më e vogël e njohur e lidh pragun me një analizë të përbashkët të komunave. Kjo është zgjedhje analitike konservative, jo prag zyrtar dhe jo kufi gabimi i provuar statistikisht. Shih krahasimin Q25/Q50/Q75 më poshtë. Krahasimi përdor pragun e plotë, jo numrin e rrumbullakuar në tekst.

Rrezja ekuivalente është vetëm tregues i shkallës, jo largësi nga kufiri. Dy Mitrovicat nuk kanë sipërfaqe individuale në burim dhe përjashtohen nga llogaritja e minimumit; mungesa duket në tabelë. Edhe nën prag, pika pranë kufirit mund t'i takojë komunës tjetër. Pa poligone dhe distancë nga kufiri, **asnjë rresht nuk certifikohet si i saktë për komunën**. Mbi prag shënohet për shqyrtim; asnjë pasiguri nuk fshihet, pritet ose imputohet. Mungesa është unknown, jo zero. Grupi 7071 m i identifikuar nga Dafina ruhet dhe shënohet mbi prag.

Sipas [Darwin Core](https://dwc.tdwg.org/terms/#coordinateUncertaintyInMeters), pasiguria është rreze horizontale në metra; zero nuk është vlerë e vlefshme. Kjo mbështet dallimin invalid/unknown; formula e pragut është vendim i projektit.

**Taksonomia:** is_species_level do të thotë identifikim në nivel specie **ose më të hollësishëm** me emër species të pranishëm. SPECIES, SUBSPECIES, VARIETY, FORM (dhe nënrangjet përkatëse) -> True; rangjet e njohura mbi specie -> False. UNRANKED, rang bosh/i panjohur dhe specie e paplotësuar në rang të hollësishëm -> NA. Ky flamur nuk verifikon saktësinë e identifikimit biologjik. Nuk fshihen regjistrime.

| kolona | rregulla | veprimi | rreshta |
| --- | --- | --- | --- |
| elevation | = 0 | NA; ruaj elevation_was_zero | 3634 |
| coordinateUncertaintyInMeters | > 1866.094894 m | above_screening_threshold; ruaj vlerën dhe rreshtin | 9091 |
| coordinateUncertaintyInMeters | mungon | unknown; jo pasiguri zero | 31813 |
| coordinateUncertaintyInMeters | <=0 ose jo finite | invalid; ruaj për auditim | 0 |
| taxonRank | rang i njohur mbi specie | is_species_level=False; ruaj rreshtin | 1082 |
| taxonRank/species | rang i paqartë ose species mungon në rang specie/më poshtë | is_species_level=NA | 234 |

## Ndjeshmëria e pragut

| kuantili | kuantili_m | kufiri_hapesinor_m | pragu_m | nen_ose_baraz_pragut | mbi_prag | mungojne | pavlefshme | zgjedhur |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.25 | 250.0 | 1866.0948943852427 | 250.0 | 4369 | 10274 | 31813 | 0 | False |
| 0.5 | 7071.0 | 1866.0948943852427 | 1866.0948943852427 | 5552 | 9091 | 31813 | 0 | True |
| 0.75 | 7071.0 | 1866.0948943852427 | 1866.0948943852427 | 5552 | 9091 | 31813 | 0 | False |