# Varianca dhe korrelacioni

**Versioni:** 1.0  
**Data:** 27.10.2026  
**Statusi:** Asnjë kolonë e 20–22 tetorit nuk hiqet.

## Varësia

Kontrollohen 34 kolonat që vijnë nga `add_one_hot()`, `add_iucn_and_flags()` dhe `add_log1p()`: 20 kolona dummy, `iucn_rank`, `iucn_evaluated`, 10 flamuj seriozë dhe dy kolona `log1p`. Numri i rreshtave është 46,831, si te ato tri detyra.

`processed/biodiversity_clean.csv` ka 46,456 rreshta. E njëjta kontrollë jep të njëjtat veti dhe të njëjtin vendim. Ndryshojnë vetëm shifrat e variancës, sepse pjesëtuesi është 46,456. Çifti i flamujve mbetet 348, 160 dhe 3 rreshta. Korrelacioni atje është +0.8226.

Funksioni nuk heq kolona. Nuk e ndryshon CSV-në origjinale dhe nuk e ndryshon CSV-në e pastruar.

## Pragjet

Varianca llogaritet me pjesëtues 46,831. Për një kolonë 0/1, varianca është `p × (1 − p)`. Pragu i rrallësisë është ai i 20 tetorit: më pak se 47 rreshta, nën 0.1% të 46,831. Një kolonë me 47 njësha ka variancë 0.001003. Nën këtë prag hyjnë vetëm pesë kolona.

Korrelacion i lartë është `|r|` të paktën 0.80. Çifti tjetër më i lartë është 0.7615, nën prag. Asnjë çift nuk ka `|r|` të barabartë me 1.

## Vendimi

Asnjë veti nuk hiqet. Varianca e ulët këtu do të thotë se vlera 1 është e rrallë, jo se kolona përsërit një tjetër. Korrelacioni 0.8227 vjen sepse shumë rreshta i kanë të dy flamujt, por 160 rreshta e kanë vetëm datën e pavlefshme dhe 3 vetëm numrin e pavlefshëm.

Tri grupet dummy mblidhen në 1 për çdo rresht. Kjo është varësi e grupit. Asnjë çift brenda tyre nuk kalon 0.80. `drop_first` mbetet false, si më 20 tetor.

`iucn_rank` ekziston vetëm te rreshtat ku `iucn_evaluated` është 1. Te ata rreshta `iucn_evaluated` nuk ndryshon, prandaj Pearson nuk del. Rangu ruan rendin LC–EX. `iucn_evaluated` ruan `NE`, `DD` dhe boshllëkun.

## Tabela

| Vetia | Problemi | Vendimi | Arsyetimi |
|---|---|---|---|
| `basisOfRecord_Tjera` | variancë e ulët | mbahet | Varianca është 0.000021, me 1 rresht 1. Kolona mbetet, sepse është koshi i kategorisë së rrallë. Heqja e lë atë rresht pa asnjë 1 në grup. |
| `flag_TAXON_MATCH_NAME_AND_ID_AMBIGUOUS` | variancë e ulët | mbahet | Varianca është 0.000021, me 1 rresht 1. Flamuri serioz mbetet, sepse rrallësia është sinjali. |
| `flag_SCIENTIFIC_NAME_AND_ID_INCONSISTENT` | variancë e ulët | mbahet | Varianca është 0.000021, me 1 rresht 1. Flamuri serioz mbetet, sepse rrallësia është sinjali. |
| `flag_COORDINATE_UNCERTAINTY_METERS_INVALID` | variancë e ulët | mbahet | Varianca është 0.000149, me 7 rreshta 1. Flamuri serioz mbetet, sepse rrallësia është sinjali. |
| `flag_TAXON_MATCH_NONE` | variancë e ulët | mbahet | Varianca është 0.000598, me 28 rreshta 1. Flamuri serioz mbetet, sepse rrallësia është sinjali. |
| `flag_RECORDED_DATE_INVALID` dhe `flag_INDIVIDUAL_COUNT_INVALID` | korrelacion +0.8227 | mbahen të dyja | 348 rreshta i kanë të dyja, 160 vetëm të parën dhe 3 vetëm të dytën. Nuk janë e njëjta veti. |
| `taxon_group` | shuma e kolonave është 1 | mbahet | Varësia është e grupit, jo një çift me korrelacion të paktën 0.80. Asnjë kolonë nuk hiqet. |
| `district` | shuma e kolonave është 1 | mbahet | Varësia është e grupit, jo një çift me korrelacion të paktën 0.80. Asnjë kolonë nuk hiqet. |
| `basisOfRecord` | shuma e kolonave është 1 | mbahet | Varësia është e grupit, jo një çift me korrelacion të paktën 0.80. Asnjë kolonë nuk hiqet. |
| `iucn_rank` dhe `iucn_evaluated` | rangu ekziston vetëm kur `iucn_evaluated` është 1 | mbahen të dyja | Te rreshtat me rang, `iucn_evaluated` nuk ndryshon, prandaj Pearson nuk del. Rangu ruan rendin. `iucn_evaluated` ruan `NE`, `DD` dhe boshllëkun. |

## Dokumentimi i detyrës

- **Varësia:** kolonat e 20–22 tetorit.
- **Input:** 34 kolona numerike të krijuara nga tri funksionet.
- **Çka u bë:** U shkrua `review_variance_correlation()` dhe tabela e vendimeve.
- **Rreshta para / pas:** 46,831 / 46,831. CSV-ja origjinale mbetet. Te file-i i pastruar, 46,456 / 46,456.
- **Kolona para / pas:** 34 / 34. Asnjë nuk hiqet.
- **Pse u bë:** Varianca e ulët dhe korrelacioni i lartë shënohen. Heqja bëhet vetëm kur një veti është kopje e një tjetre.
- **Output:** `reports/varianca_dhe_korrelacioni.md` dhe `review_variance_correlation()` te `notebooks/03_vetite.ipynb`.
- **Commit:** `Keep low-variance and high-correlation features after review`.
