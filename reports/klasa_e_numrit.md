# Klasa e numrit

**Versioni:** 1.0  
**Data:** 24.10.2026  
**Statusi:** `count_class` nga `individualCount` origjinal, me `pd.qcut`.

## Varësia

Kolona origjinale `individualCount`. Nga 46,831 rreshta, 29,134 kanë numër dhe 17,697 (37.79%) janë bosh. Të gjitha vlerat e njohura janë numra të plotë nga 1 deri në 10,200. Mediana është 2. 11,192 rreshta (38.42% e numrave të plotë) janë pikërisht 1.

`reports/strategjia_e_mungesave.md` e mban këtë kolonë me `keep + flag`: mungesa nuk është 0 ose 1 dhe nuk ka imputim global. Trajtimi i mungesës është ende i hapur te pastrimi, prandaj këtu `NaN` mbetet `NaN`. Funksioni nuk e ndryshon CSV-në. `individualCount` nuk kthehet në nënbashkësinë e 29 kolonave; shtohet vetëm `count_class`.

## Tabela e krahasimit

Krahasimi është mbi 29,134 numrat e njohur. `pd.cut` dhe `pd.qcut` janë kërkuar me 4 klasa.

### `pd.cut`, gjerësi e barabartë, `bins=4`

| Klasa | n | % e numrave të plotë |
|---|---:|---:|
| (−9.199, 2550.75] | 29,081 | 99.82 |
| (2550.75, 5100.5] | 26 | 0.09 |
| (5100.5, 7650.25] | 4 | 0.01 |
| (7650.25, 10200] | 23 | 0.08 |

29,081 + 26 + 4 + 23 = 29,134. Kufiri i majtë negativ vjen nga `pd.cut`: intervali zgjerohet pak që të hyjë minimumi 1. Klasa e parë është në praktikë 1–2,550.

Me 3 klasa, klasa e parë mban 29,087 rreshta (99.84%). Me 5 klasa, klasa e parë mban 29,079 (99.81%) dhe një klasë mbetet pa asnjë rresht.

### `pd.qcut`, frekuencë e barabartë, `q=4`

Pa `duplicates="drop"` ndalet. Kufijtë dalin 1, 1, 2, 6 dhe 10,200. Një e katërta e 29,134 është 7,283.5, por 11,192 rreshta janë 1, prandaj kufiri 0% dhe kufiri 25% janë të dy 1.

Me `duplicates="drop"` mbeten tri klasa:

| `individualCount` | `count_class` | n | % e numrave të plotë |
|---|---|---:|---:|
| 1–2 | 1–2 | 16,044 | 55.07 |
| 3–6 | 3–6 | 6,360 | 21.83 |
| 7–10200 | 7–10200 | 6,730 | 23.10 |
| mungon | mbetet bosh | 17,697 | – |

16,044 + 6,360 + 6,730 = 29,134. Me 17,697 boshllëqet janë 46,831.

Frekuenca nuk del e barabartë. Klasa e parë mban 1 dhe 2, sepse vlera 1 përsëritet. Dy klasat e tjera qëndrojnë afër: 21.83% dhe 23.10%. Vlera 2 hyn te `1–2`. Vlera 6 hyn te `3–6`. Vlera 7 hyn te `7–10200`.

`q=5`, edhe pas heqjes së kufirit të përsëritur, e lë vlerën 3 vetëm në një klasë me 2,447 rreshta (8.40%). `q=4` është ndarja më e afërt me frekuencë të barabartë.

## Vendimi dhe arsyetimi

Zgjedhet `pd.qcut` me `q=4` dhe `duplicates="drop"`.

`pd.cut` me gjerësi të barabartë nuk i ndan numrat që përdoren. 99.82% e vlerave të njohura bien në 1–2,550, sepse maksimumi është 10,200 dhe mediana është 2. Tri klasat e tjera kanë 53 rreshta së bashku.

`pd.qcut` i ndan një dhe dy individë, grupet 3–6, dhe numrat mbi kuartilin e tretë (6). Klasa e fundit mbetet e gjerë: 99% e numrave të njohur janë ≤ 150, kurse maksimumi është 10,200. Ngushtimi i asaj klase i takon transformimit, jo këtij diskretizimi.

Rreshti pa `individualCount` nuk merr klasë. Nuk bëhet 0, nuk bëhet 1, dhe nuk merr klasën më të shpeshtë.

## Dokumentimi i detyrës

- **Varësia:** `individualCount` origjinal dhe `reports/strategjia_e_mungesave.md`.
- **Input:** `individualCount`.
- **Çka u bë:** U krahasua `pd.cut` me `pd.qcut` dhe u shkrua `add_count_class()`.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 në CSV. Funksioni shton `count_class` te rezultati.
- **Pse u bë:** Gjerësia e barabartë i vendos 99.82% e numrave të njohur në një klasë. Frekuenca e barabartë, pas heqjes së kufirit të përsëritur te 1, jep tri klasa. Ku `individualCount` mungon, `count_class` mbetet bosh.
- **Output:** `reports/klasa_e_numrit.md` dhe `add_count_class()` te `notebooks/03_vetite.ipynb`.
- **Commit:** `Add count_class from individualCount`.
