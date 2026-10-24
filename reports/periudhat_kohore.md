# Periudhat kohore

**Versioni:** 1.0  
**Data:** 24.10.2026  
**Statusi:** `period` nga `year` origjinal.

## Varësia

Kolona origjinale `year`. Nuk plotësohet nga `eventDate`. `decade` mbetet kolonë më vete: ajo është viti i rrumbullakosur në dhjetëshe, kurse `period` është grup më i gjerë. Funksioni nuk e ndryshon CSV-në.

## Tabela e periudhave

| `year` | `period` | n | % e viteve të plota |
|---|---|---:|---:|
| 1826–1899 | 1826–1899 | 16 | 0.04 |
| 1900–1949 | 1900–1949 | 355 | 0.80 |
| 1950–1999 | 1950–1999 | 4,131 | 9.27 |
| 2000–2009 | 2000–2009 | 1,402 | 3.15 |
| 2010–2019 | 2010–2019 | 10,223 | 22.94 |
| 2020–2026 | 2020–2026 | 28,436 | 63.81 |
| mungon | mbetet bosh | 2,268 | – |

16 + 355 + 4,131 + 1,402 + 10,223 + 28,436 = 44,563. Me 2,268 boshllëqet janë 46,831.

## Kufijtë

Viti më i vjetër është 1826 dhe më i riu 2026. Gjysma e viteve të plota është 2020 ose më vonë.

Para 1900 ka vetëm 16 rreshta. Janë të vlefshëm, por historikë, prandaj qëndrojnë veçmas.

1900–1949 ka 355 rreshta, të shpërndarë dhe të rrallë. 1950–1999 është blloku i parë i qëndrueshëm, 4,131 rreshta, para platformave digjitale.

2000–2009 bie në 1,402. Nuk bashkohet me dekadën pasuese, sepse 2010–2019 ka 10,223 dhe 2020–2026 ka 28,436. Nga 2010 deri në 2026 janë 86.75% e viteve të plota. Kjo vjen nga rritja e eBird dhe iNaturalist, jo nga rritja e biodiversitetit.

## Vendimi dhe arsyetimi

`period` merr gjashtë periudha. Kufiri i vitit hyn në periudhën që fillon aty: 1900, 1950, 2000, 2010 dhe 2020.

Rreshti pa `year` nuk merr periudhë. Mungesa nuk kthehet në një vit të supozuar.

`decade` nuk zëvendësohet. Ajo ruan dhjetëshen. `period` ruan ndarjen që e tregon shpërndarja: pak të dhëna historike, një bllok 1950–1999, një dekadë e hollë 2000–2009, dhe dy periudha të mëdha pas 2010.

## Dokumentimi i detyrës

- **Varësia:** `year` origjinal.
- **Input:** `year`.
- **Çka u bë:** U shkrua `add_period()` dhe tabela e periudhave.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 në CSV. Funksioni shton `period` te rezultati.
- **Pse u bë:** Vitet e plota ndahen sipas shpërndarjes dhe kontekstit. Ku `year` mungon, `period` mbetet bosh.
- **Output:** `reports/periudhat_kohore.md` dhe `add_period()` te `notebooks/03_vetite.ipynb`.
- **Commit:** `Add period from the original year`.
