# Vetitë kohore

**Versioni:** 1.0  
**Data:** 21.10.2026  
**Statusi:** `season`, `decade` dhe `is_recent` nga `year` dhe `month`.

## Varësia

Kolonat origjinale `year` dhe `month`, pasi rifreskohen më 19.10.2026. Funksioni i lexon ato kolona. Nuk i plotëson nga `eventDate` dhe nuk i ndryshon.

## Tabela e mapping-ut

Sezonet janë meteorologjike, sepse `month` është numër i muajit.

| Muaji | Emri | Sezoni |
|---|---|---|
| 1 | janar | dimër |
| 2 | shkurt | dimër |
| 3 | mars | pranverë |
| 4 | prill | pranverë |
| 5 | maj | pranverë |
| 6 | qershor | verë |
| 7 | korrik | verë |
| 8 | gusht | verë |
| 9 | shtator | vjeshtë |
| 10 | tetor | vjeshtë |
| 11 | nëntor | vjeshtë |
| 12 | dhjetor | dimër |

`season` vjen vetëm nga `month`. Nëse `month` mungon, `season` mbetet NaN.

`decade = (year // 10) * 10`. Viti 2024 bëhet 2020. Nëse `year` mungon, `decade` mbetet NaN.

## Vendimi dhe arsyetimi

Pragu i `is_recent` është `year >= 2017`. Viti më i ri te `year` është 2026 dhe më i vjetri është 1826, prandaj dhjetë vitet e fundit janë 2017–2026.

Nga 44,563 vitet e plota, 34,854 (78.21%) janë nga 2017 e tutje dhe 9,709 janë më të vjetra. Gjysma e viteve të plota është 2020 ose më vonë. Pragu 2000 do t'i shënonte 89.90% si të freskëta. Pragu 2020 do të linte jashtë 10,223 rreshtat e dekadës 2010.

Nëse `year` mungon, `is_recent` dhe `decade` mbeten NaN. Nëse `month` mungon, `season` mbetet NaN. Mungesa nuk kthehet në False.

Shtohen `season`, `decade` dhe `is_recent`. CSV-ja mbetet me 42 kolona. Te 599 rreshta ka `year` pa `month`: `decade` dhe `is_recent` plotësohen, `season` mbetet NaN. Te 2,268 rreshta mungon `year`: tri kolonat e reja mbeten NaN.

Funksioni `add_time_features()` është qelizë kodi te `notebooks/03_vetite.ipynb`. Ky raport mban tabelën dhe vendimin.

## Dokumentimi i detyrës

- **Varësia:** kolonat origjinale `year` dhe `month`, të rifreskuara më 19.10.2026.
- **Input:** `year`, `month`.
- **Çka u bë:** U shkrua `add_time_features()` dhe tabela e mapping-ut. U arsyetua pragu i `is_recent`.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 në CSV. Funksioni shton tri kolona te rezultati, pa e ndryshuar CSV-në.
- **Pse u bë:** Sezoni, dekada dhe freskia dalin nga `month` dhe `year`. Ku burimi mungon, vlera e re mbetet NaN.
- **Output:** `reports/vetite_kohore.md` dhe `add_time_features()` te `notebooks/03_vetite.ipynb`.
