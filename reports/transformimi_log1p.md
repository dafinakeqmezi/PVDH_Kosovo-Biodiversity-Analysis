# Transformimi me log1p

**Versioni:** 1.0  
**Data:** 26.10.2026  
**Statusi:** `log1p` për `individualCount` dhe `coordinateUncertaintyInMeters`.

## Varësia

Skewness llogaritet vetëm te vlerat e njohura, me të njëjtën masë pandas që është te `reports/vendimi_per_numrin_e_individeve.md`. Atje, te dataset-i i pastruar, skewness e `individualCount` është 26.63 dhe është thënë se `log1p` nuk bëhet në atë hap. `reports/korniza_e_kualitetit.md` e lë `log1p` për transformimin. `reports/tipet_e_te_dhenave.md` e lë `coordinateUncertaintyInMeters` në `float64` për `log1p`.

Mungesa nuk bëhet 0. Te pasiguria, 0 m nuk është vlerë e vlefshme dhe nuk ka rreshta të tillë. Vlera 7,071 m ruhet. Funksioni nuk e ndryshon asnjë CSV dhe nuk e kthen `individualCount` në nënbashkësinë e 29 kolonave.

## Tabela e skewness

| Kolona | Dataset | n i njohur | mungon | Skewness | Skewness pas `log1p` |
|---|---|---:|---:|---:|---:|
| `individualCount` | origjinale | 29,134 | 17,697 | 26.75 | 2.08 |
| `individualCount` | i pastruar | 28,869 | 17,587 | 26.63 | 2.07 |
| `coordinateUncertaintyInMeters` | origjinale | 14,827 | 32,004 | 102.36 | −1.01 |
| `coordinateUncertaintyInMeters` | i pastruar | 14,643 | 31,813 | 101.73 | −1.00 |

Te të dyja kolonat minimumi i njohur është 1 dhe nuk ka vlera negative. Maksimumi i numrit është 10,200. Maksimumi i pasigurisë është 4,226,661 m. Mediana e pasigurisë është 7,071 m.

## Vendimi dhe arsyetimi

Të dyja kolonat marrin `log1p`. Skewness para transformimit është shumë mbi 1, pra shpërndarja është e anuar djathtas. Pas `log1p` ajo bie.

Te `individualCount`, 26.63 bëhet 2.07 te dataset-i i pastruar. Numri 1 mbetet `log(2)`. Boshllëku mbetet bosh.

Te `coordinateUncertaintyInMeters`, 101.73 bëhet −1.00. Shenja ndryshon sepse shumica e vlerave të njohura është 7,071 m, kurse bishti shkon deri në 4,226,661 m. `log1p` e ngjesh atë bisht. Vlera absolute e skewness bie nga 101.73 në 1.00. 7,071 m nuk hiqet dhe boshllëku nuk bëhet 0.

Kolonat e reja janë `individualCount_log1p` dhe `coordinateUncertaintyInMeters_log1p`. Kolonat burimore mbeten.

## Dokumentimi i detyrës

- **Varësia:** `reports/vendimi_per_numrin_e_individeve.md`, `reports/korniza_e_kualitetit.md` dhe `reports/tipet_e_te_dhenave.md`.
- **Input:** `individualCount` dhe `coordinateUncertaintyInMeters`.
- **Çka u bë:** U llogarit skewness para dhe pas `log1p`. U shkrua `add_log1p()`.
- **Rreshta para / pas:** 46,831 / 46,831 te CSV-ja origjinale. 46,456 / 46,456 te dataset-i i pastruar.
- **Kolona para / pas:** CSV-ja origjinale mbetet me 42 kolona. Funksioni shton dy kolona te rezultati.
- **Pse u bë:** Të dyja shpërndarjet e njohura janë të anuara djathtas. `log1p` e ul skewness. Mungesa mbetet bosh.
- **Output:** `reports/transformimi_log1p.md` dhe `add_log1p()` te `notebooks/03_vetite.ipynb`.
- **Commit:** `Add log1p columns for skewed counts and uncertainty`.
