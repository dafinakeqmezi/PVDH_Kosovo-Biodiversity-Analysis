# Plani i detektimit të përjashtuesve

**Versioni:** 1.0
**Data:** 18.11.2026
**Statusi:** Plani. Metodat zbatohen 19–28 nëntor në `notebooks/04_perjashtuesit.ipynb`.

## Varësia

Input: `processed/biodiversity_features.csv` (46,456 rreshta, Pjesa I) dhe `processed/agg_municipality_v2.csv` (38 komuna). Kufijtë fizikë vijnë nga Pjesa I: lartësia 297–2,656 m (`reports/vlefshmeria.md`) dhe kutia e Kosovës (`reports/korniza_e_kualitetit.md`). Pamja e parë e kolonave është te `reports/04_kolonat_kandidate.csv`.

## Tabela e planit

| Kolona | Metoda | Gabim i mundshëm | Vlerë reale e rrallë |
|---|---|---|---|
| `individualCount` | IQR me k = 1.5 dhe 3 mbi `log1p`, sepse shpërndarja është shumë e anuar (mediana 2, maksimumi 10,200; IQR lineare shënon 3,628 vlera, mbi `log1p` 1,093). Z-score i modifikuar (MAD, \|Mz\| > 3.5). IQR brenda `taxon_group` dhe specieve. Isolation Forest / LOF me `log1p`. Z-score klasik vetëm për krahasim. | Shifër e tepërt ose gabim shtypi (p.sh. 102 → 10,200). Numri i tufës i shkruar te çdo specie e listës. Numër i futur si kod. GBIF shënoi `INDIVIDUAL_COUNT_INVALID` te 351 rreshta. Te të gjithë vlera mungon tashmë, prandaj nuk hyjnë në detektim. | Tufa dimërore shturësh: 79 rreshta kanë ≥ 1,000 individë, 73 prej tyre *Sturnus vulgaris*, 70 në Graçanicë dhe 78 nga eBird. 23 vlera janë 10,000–10,200: vlerësim i rrumbullakët i vëzhguesit, jo numërim. Te insektet deri në 600 individë. |
| `elevation` | Rregulla fizike 297–2,656 m nga Pjesa I. IQR dhe MAD brenda `taxon_group` dhe `class` (përjashtues kontekstual). Isolation Forest / LOF bashkë me koordinatat. IQR globale nuk mjafton: shënon 595 vlera mbi 1,915 m, kryesisht regjistrime malore. | Mbi Gjeravicën (2,656 m): 5 ekzemplarë të herbariumit WU nga viti 1890, në të njëjtën pikë në Kaçanik, me 2,750–3,050 m. Nën 297 m: 4 vlera (100, 198, 250, 293 m). Lartësi nga etiketa e vjetër, në këmbë në vend të metrave, ose që nuk i përket koordinatës. 3,634 zerot u kthyen në NaN në Pjesën I. | Kërpudhat dhe likenet kanë medianë 2,173 m, insektet 605 m: regjistrohen kryesisht në male (te PCA e Pjesës I, Dragashi dhe Juniku kanë pjesën më të madhe të kërpudhave). Vlerat 1,915–2,656 m janë të rralla për bimët dhe insektet, por janë brenda relievit të Kosovës. |
| `coordinateUncertaintyInMeters` | IQR mbi `log1p` (lineare shënon 66 vlera, `log1p` 1). MAD. Krahasim me pragun hapësinor të komunës nga Pjesa I (1,866 m). Moda 7,071 m trajtohet si kod i përgjithësimit, jo si përjashtues. | 5 vlera mbi 100 km (462,462–4,226,661 m), më të mëdha se vetë Kosova. Të gjitha janë nga iNaturalist: ka gjasë gabim njësie ose vlerë e pajisjes. Pasiguri më e madhe se komuna e shënuar. | 7,071 m (8,225 rreshta, 56.2% e të plotësuarave) është gjysma e diagonales së katrorit 10 × 10 km: koordinatë e përgjithësuar me qëllim. 10–100 km: 85 rreshta, 79 nga iNaturalist, ndoshta koordinata të fshehura për specie të ndjeshme. ≤ 5 m (1,068 rreshta): GPS i saktë. |
| `year` | Jo IQR ose Z global: vitet 2018–2022 kanë 58.8% të regjistrimeve, prandaj IQR shënon çdo vit para 2012 (6,180 rreshta). IQR / MAD brenda `basisOfRecord`. Kontroll kundrejt `event_start` dhe `date_precision`. Për numrin e regjistrimeve sipas vitit/muajit: rolling median ± k·MAD te `agg_time_v2.csv`. | Vit pas datës së shkarkimit (regjistrimi i fundit: 2026-08-22). Viti i digjitalizimit në vend të vitit të mbledhjes. Vit që kundërshton `event_start` ose `date_precision`. 2,268 rreshta nuk kanë vit. | 16 regjistrime para vitit 1900 (më i vjetri 1826), 15 prej tyre ekzemplarë herbariumi (`PRESERVED_SPECIMEN`). Janë dëshmi historike. Rritja pas 2018 vjen nga përpjekja e mbledhjes (eBird), jo nga ndryshim real. |
| `decimalLatitude` / `decimalLongitude` | Kontroll i kutisë së Kosovës (lat 41.85–43.27, lon 20.01–21.80). Distanca haversine deri te k = 5 fqinjët më të afërt, DBSCAN. Isolation Forest / LOF. IQR veç e veç mbi lat dhe lon nuk i gjen pikat e izoluara. | Pikë jashtë Kosovës (0 tani: lat 41.859–43.242, lon 20.021–21.763). Lat dhe lon të ndërruara. Koordinata me ≤ 2 shifra dhjetore (586 rreshta), qendër komune ose rrjeti. Pikë që nuk përputhet me `municipality`. | Pika e Ligatinave të Henc (42.579243, 21.048304) ka 12,943 rreshta (27.9%): hotspot real, por i mbipërfaqësuar. Pikat e izoluara në male ose afër kufirit janë zona pak të vizituara, jo gabime. |
| `n_issues` | Nuk detektohet statistikisht: vlerat janë diskrete 0–3 dhe Q1 = Q3 = 0, prandaj IQR do të shënonte çdo rresht me ≥ 1 flamur (1,645). Përdoret si variabël konteksti: krahasohet me `n_metoda` te flamujt. | Numri vetë nuk është matje e gabuar. Gabimi është te kolona që e ka flamurin (data, taksoni, pasiguria). 394 rreshta me ≥ 2 flamuj kanë gjasë më të madhe gabimi. | 10 rreshta me 3 flamuj janë të rrallë, por GBIF i ka pranuar. Flamujt informues, p.sh. `TAXON_MATCH_HIGHERRANK`, nuk e bëjnë regjistrimin të gabuar. |
| `regjistrime` (komuna) | Mahalanobis mbi 38 komunat (regjistrime, specie unike, specie/km², regjistrime/1,000 banorë, % e kërcënuara), pas `log1p` dhe Z-score, me prag χ² (p = 0.975). IQR mbi `log1p` si krahasim (3 komuna). | Regjistrime në komunë të gabuar ose të numëruara dy herë. Duplikatet u hoqën në v2, prandaj mbetet rasti i komunës së gabuar. | Graçanicë 14,563 regjistrime (31.35%), nga pika e Henc-it. Mamushë 1 regjistrim: komunë e vogël dhe pak e vizituar. |
| `specie_unike` (komuna) | Mahalanobis si më lart. IQR mbi `log1p` (4 komuna). | Sinonime ose emra në trajtime taksonomike të ndryshme që numërohen si specie të ndryshme (p.sh. *Lasiommata* / *Pararge* nga Pjesa I). | Më shumë: Prizren 1,243, Prishtinë 1,149. Më pak: Mamushë 1, Kllokot 13. Prizreni ka Sharrin. Komunat e vogla kanë pak specie sepse kanë pak regjistrime. |
| `specie_per_km2` (komuna) | Mahalanobis si më lart. IQR mbi `log1p` (0 komuna). | Sipërfaqe e gabuar ose e përbashkët: Mitrovicë e Jugut dhe Mitrovicë e Veriut kanë një njësi sipërfaqeje të përbashkët. | Më shumë: Junik 3.37, Ranillug 3.18. Sipërfaqe e vogël dhe vende me shumë specie. |
| `regjistrime_per_1000_banore` (komuna) | Mahalanobis si më lart. IQR mbi `log1p` (0 komuna). | Popullsia është vlerësim i ASK për 4 komuna (Leposaviq, Zveçan, Zubin Potok, Mitrovicë e Veriut), prandaj raporti është më pak i sigurt aty. | Më shumë: Graçanicë 787.79, Ranillug 392.18. Përpjekje e lartë vëzhgimi në komuna me pak banorë. |
| `specie_te_kercenuara` / `regjistrime_te_kercenuara` (komuna) | Mahalanobis si më lart, me % e regjistrimeve të kërcënuara. IQR mbi `log1p` (0 dhe 2 komuna). | Kategoria IUCN është globale, jo për Kosovën. Një identifikim i gabuar i një specieje të kërcënuar e rrit numrin. | Regjistrime: Graçanicë 365, Fushë Kosovë 81. Specie: Prishtinë 13, Prizren 12. 9 komuna nuk kanë asnjë. |

## Vendimi dhe arsyetimi

- **Asnjë vlerë nuk fshihet këtu.** Çdo metodë jep një flamur 0/1. Vlera largohet vetëm kur Deliza provon se është gabim (`05_menjanimi.ipynb`, 24–25 nëntor).
- **`log1p` për kolonat e anuara.** `individualCount`, `coordinateUncertaintyInMeters` dhe agregatet e komunave kanë bisht të gjatë djathtas. IQR lineare te `individualCount` shënon 3,628 vlera, mbi `log1p` 1,093.
- **Metodat kontekstuale para atyre globale.** Lartësia dhe numri i individëve varen nga grupi: kërpudhat jetojnë më lart se insektet, zogjtë fluturojnë në tufa. Vlera ekstreme globalisht mund të jetë normale brenda grupit.
- **`year` nuk kontrollohet me IQR globale.** Anshmëria e eBird e bën IQR të shënojë 6,180 rreshta para vitit 2012, përfshirë ekzemplarët historikë.
- **`n_issues` nuk është kolonë për detektim.** Është numër flamujsh, jo matje. Përdoret për të parë nëse përjashtuesit kanë më shumë flamuj GBIF.
- **7,071 m është kod, jo përjashtues.** Është vlera më e shpeshtë e pasigurisë dhe tregon përgjithësim në rrjet 10 × 10 km.
- **Komunat kontrollohen me Mahalanobis.** Me 38 komuna, Isolation Forest dhe LOF nuk kanë mjaft pika. Mahalanobis i sheh variablat së bashku, p.sh. Graçanicën me shumë regjistrime, por jo me shumë specie.

## Dokumentimi i detyrës

- **Input:** `processed/biodiversity_features.csv` (`individualCount`, `elevation`, `coordinateUncertaintyInMeters`, `year`, `decimalLatitude`, `decimalLongitude`, `n_issues`) dhe `processed/agg_municipality_v2.csv`.
- **Çka u bë:** U krijua `notebooks/04_perjashtuesit.ipynb` dhe folderi `reports/figures/`. U profilizuan 13 kolona kandidate dhe për secilën u shkrua metoda, gabimi i mundshëm dhe vlera reale e rrallë.
- **Rreshta para / pas:** 46,456 / 46,456. Asnjë vlerë nuk u shënua ende.
- **Pse u bë:** Që para detektimit të dihet çka kërkohet në secilën kolonë dhe që vlerat reale ekstreme të mos fshihen si gabime.
- **Output:** `reports/perjashtuesit_plani.md`, `reports/04_kolonat_kandidate.csv`, `reports/figures/`, seksioni 1 i `notebooks/04_perjashtuesit.ipynb`.
- **Commit:** `Dafina: plani i detektimit të përjashtuesve`.
- **Decision + Rationale:** shih seksionin "Vendimi dhe arsyetimi".
