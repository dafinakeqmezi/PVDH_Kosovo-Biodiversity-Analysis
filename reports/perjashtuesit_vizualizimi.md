# Vizualizimi fillestar i kolonave kandidate

**Versioni:** 1.0
**Data:** 19.11.2026
**Statusi:** Pamje e parë. Asnjë vlerë nuk shënohet ose fshihet. IQR zbatohet më 20 nëntor.

## Si lexohen figurat

Çdo kolonë kandidate ka një figurë te `reports/figures/04_vizualizimi_<kolona>.png` (13 figura). Majtas është shkalla lineare, djathtas shkalla log. Sipër është histogrami, poshtë boxplot-i me të njëjtin bosht.

- Mustaqet janë Q1 − 1.5·IQR dhe Q3 + 1.5·IQR. Në panelin log llogariten mbi `log1p(x)` dhe boshti tregon vlerat origjinale. Kolonat me zero (`n_issues`, `specie_te_kercenuara`, `regjistrime_te_kercenuara`) kanë bosht `symlog`.
- Te kolonat në nivel rreshti boshti i numrit të rreshtave është log, që të shihen edhe shtyllat me 1–10 rreshta. Te komunat (38) është linear.
- Numrat e pikave jashtë mustaqeve përputhen me `reports/04_kolonat_kandidate.csv`.

## Shënimet

| Kolona | Figura | Jashtë mustaqeve (lineare) | Jashtë mustaqeve (log) | Çka duket ekstreme në pamje të parë |
|---|---|---|---|---|
| `individualCount` | `reports/figures/04_vizualizimi_individualCount.png` | 3,628 | 1,093 | Lineare: e gjithë kutia është te 1–6 dhe nuk shihet; 3,628 vlera mbi 13.5 dalin si pika. Log: mbeten 1,093 vlera mbi 45. Ekstreme duken 79 vlerat ≥ 1,000 dhe sidomos grupi i veçuar 10,000–10,200 (23 rreshta), pas një zbrazëtie nga 6,000. Shihen shtylla te numrat e rrumbullakët (2,000, 5,000, 10,000). |
| `elevation` | `reports/figures/04_vizualizimi_elevation.png` | 595 | 1 | Shpërndarje me bisht djathtas dhe një shtyllë të lartë te 481 m (749 rreshta). Lineare: 595 vlera mbi 1,915 m. Log: mbetet 1 vlerë, nën 159 m, dhe asnjë lart. Ekstreme duken 5 pikat e fundit djathtas (2,750–3,050 m, mbi Gjeravicën) dhe, në shkallë log, 4 vlerat e veçuara majtas (100, 198, 250, 293 m). |
| `coordinateUncertaintyInMeters` | `reports/figures/04_vizualizimi_coordinateUncertaintyInMeters.png` | 66 | 1 | Lineare: të gjitha vlerat bien në shtyllën e parë dhe shihen vetëm 5 pika larg, deri në 4,226,661 m. Log: vlerat shtrihen nga 1 m deri 32,112 m, me shtylla te 4–5 m (GPS), 250 m dhe sidomos 7,071 m (8,225 rreshta, kod i përgjithësimit). Mediana = Q3 = 7,071, prandaj kutia është e ngushtë. Ekstreme duken 5 vlerat mbi 100 km, të ndara nga pjesa tjetër me zbrazëti (32,112 → 462,462 m). |
| `year` | `reports/figures/04_vizualizimi_year.png` | 6,180 | 7,088 | Bisht i gjatë majtas: kutia është 2018–2022 dhe 6,180 rreshta para vitit 2012 dalin si pika. Shkalla log nuk ndihmon: diapazoni 1826–2026 është shumë i ngushtë dhe forma mbetet e njëjtë (7,088 jashtë mustaqeve). Ekstreme duken 16 regjistrimet para vitit 1900 (më i vjetri 1826); grupet e viteve 1905–1918 janë të dendura, jo të veçuara. Djathtas nuk ka asgjë pas vitit 2026. |
| `decimalLatitude` | `reports/figures/04_vizualizimi_decimalLatitude.png` | 11,476 | 11,474 | Një shtyllë e lartë te pika e Henc-it (42.579243, 12,943 rreshta). Ajo e ngushton kutinë, prandaj 11,476 rreshta dalin jashtë mustaqeve, por janë shpërndarje e vazhdueshme nga 41.859 deri 43.242, brenda Kosovës. Asnjë pikë e veçuar nuk shihet. Shkalla log nuk ndihmon: forma mbetet e njëjtë. |
| `decimalLongitude` | `reports/figures/04_vizualizimi_decimalLongitude.png` | 4,338 | 4,709 | E njëjta pamje: shtyllë te 21.048304 (Henc) dhe 4,338 rreshta jashtë mustaqeve, 3,914 në perëndim dhe 424 në lindje. Vlerat mbeten brenda kutisë 20.01–21.80, pa pika të veçuara. Për koordinatat duhet pamje 2D (distanca te fqinjët), jo boxplot. |
| `n_issues` | `reports/figures/04_vizualizimi_n_issues.png` | 1,645 | 1,645 | Katër shtylla diskrete: 0 (44,811), 1 (1,251), 2 (384), 3 (10). Kutia është vijë te 0, prandaj çdo rresht me ≥ 1 flamur (1,645) del si pikë, në të dy shkallët. Të rralla duken vetëm 10 rreshtat me 3 flamuj. |
| `regjistrime` (komuna) | `reports/figures/04_vizualizimi_regjistrime.png` | 6 | 3 | Lineare: Graçanicë (14,563), Prishtinë (5,893), Prizren (3,969), Fushë Kosovë (3,562), Kamenicë (2,616), Pejë (2,443) dalin jashtë mustaqeve; Graçanica është shumë larg të tjerave. Log: Graçanicë (14,563), Kllokot (13), Mamushë (1). Në log shfaqet edhe skaji i poshtëm (Mamushë me 1 regjistrim), që në lineare nuk shihet. |
| `specie_unike` (komuna) | `reports/figures/04_vizualizimi_specie_unike.png` | 6 | 4 | Lineare: Prizren (1,243), Prishtinë (1,149), Pejë (1,049), Kamenicë (792), Deçan (729), Leposaviq (647). Log: Partesh (23), Mitrovicë e Veriut (22), Kllokot (13), Mamushë (1). Skaji i sipërm pas log nuk duket më ekstrem; mbeten komunat me shumë pak specie. |
| `specie_per_km2` (komuna) | `reports/figures/04_vizualizimi_specie_per_km2.png` | 0 | 0 | Asnjë komunë jashtë mustaqeve, as në lineare as në log. Bishti djathtas (Junik 3.368, Ranillug 3.182) është i vazhdueshëm. Asgjë nuk duket ekstreme. |
| `regjistrime_per_1000_banore` (komuna) | `reports/figures/04_vizualizimi_regjistrime_per_1000_banore.png` | 4 | 0 | Lineare: Graçanicë (787.79), Ranillug (392.18), Leposaviq (171.32), Junik (138.98). Graçanica është e ndarë qartë nga të tjerat. Log: asnjë; shpërndarja bëhet afërsisht simetrike. |
| `specie_te_kercenuara` (komuna) | `reports/figures/04_vizualizimi_specie_te_kercenuara.png` | 3 | 0 | Vlera diskrete 0–13, 9 komuna me 0. Lineare: Prishtinë (13), Prizren (12), Pejë (9). Log: asnjë. Bishti është i vazhdueshëm, pa zbrazëti. |
| `regjistrime_te_kercenuara` (komuna) | `reports/figures/04_vizualizimi_regjistrime_te_kercenuara.png` | 6 | 2 | Lineare: Graçanicë (365), Fushë Kosovë (81), Prishtinë (38), Prizren (31), Pejë (18), Shtërpcë (18). Log: Graçanicë (365), Fushë Kosovë (81). Graçanica (365) është e veçuar në të dy shkallët, shumë larg të dytës. |

## Përmbledhje

- **Shkalla log ndihmon te kolonat e anuara.** Te `individualCount` pikat jashtë mustaqeve bien nga 3,628 në 1,093, te `coordinateUncertaintyInMeters` nga 66 në 1, te `regjistrime` nga 6 në 3 komuna.
- **Vlerat që duken vërtet të veçuara** (pas një zbrazëtie): `individualCount` 10,000–10,200 (23 rreshta), `coordinateUncertaintyInMeters` mbi 100 km (5), `elevation` mbi 2,656 m (5) dhe nën 297 m (4), `year` para 1900 (16), dhe Graçanica te agregatet e komunave.
- **Boxplot-i mashtron te `year`, koordinatat dhe `n_issues`.** Pikat jashtë mustaqeve atje (6,180, 11,476, 4,338, 1,645) vijnë nga kutia e ngushtë (eBird 2018–2022, pika e Henc-it, Q1 = Q3 = 0), jo nga vlera të veçuara. Shkalla log nuk ndihmon te këto kolona: forma mbetet e njëjtë.
- Pamja përputhet me planin e 18 nëntorit: `log1p` për kolonat e anuara, metoda kontekstuale për lartësinë dhe vitin, metoda hapësinore për koordinatat.

## Dokumentimi i detyrës

- **Input:** `processed/biodiversity_features.csv` (46,456 rreshta, 7 kolona) dhe `processed/agg_municipality_v2.csv` (38 komuna, 6 kolona).
- **Çka u bë:** Për secilën nga 13 kolonat kandidate u vizatua histogram dhe boxplot në shkallë lineare dhe log, dhe u shënua çka duket ekstreme në pamje të parë.
- **Rreshta para / pas:** 46,456 / 46,456. Asnjë vlerë nuk u shënua ose u ndryshua.
- **Pse u bë:** Që para metodave statistikore të shihet forma e çdo shpërndarjeje dhe cila shkallë i përshtatet secilës kolonë.
- **Output:** `reports/figures/04_vizualizimi_*.png` (13 figura), `reports/perjashtuesit_vizualizimi.md`, `reports/04_vizualizimi_shenimet.csv`, seksioni 2 i `notebooks/04_perjashtuesit.ipynb`.
- **Commit:** `Dafina: vizualizimi fillestar i kolonave kandidate`.
