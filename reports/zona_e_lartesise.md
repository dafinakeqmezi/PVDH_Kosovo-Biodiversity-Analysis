# Diskretizimi i lartësisë

**Versioni:** 1.0  
**Data:** 24.10.2026  
**Statusi:** `elevation_zone` nga `elevation`.

## Varësia

Vendimi për `elevation = 0` (`reports/vendimi_per_lartesine_zero.md`). 0 m nuk është lartësi reale në Kosovë dhe nuk zëvendësohet me 270 m apo me mesatare. Diapazoni 297–2,656 m është te `reports/vlefshmeria.md`: 297 m është pika më e ulët (Drini i Bardhë), 2,656 m është Gjeravica. Funksioni e lexon `elevation` dhe nuk e ndryshon CSV-në.

## Tabela e zonave

| `elevation` | `elevation_zone` | n |
|---|---|---:|
| 297–800 m | Fushë | 3,713 |
| 801–1,500 m | Kodrinore | 1,330 |
| 1,501–2,656 m | Malore | 1,134 |
| mungon | E panjohur | 37,011 |
| 0 m | E panjohur | 3,634 |
| jashtë 297–2,656 m | E panjohur | 9 |

`E panjohur` është 40,654 rreshta. Prej tyre 37,011 (79.03%) nuk kanë lartësi. Kjo është pjesa që detyra e quan rreth 79%.

## Kufijtë

800 m e ndan fushën nga kodrat. Rrafshi i Dukagjinit dhe Fusha e Kosovës mbeten nën këtë kufi. 1,500 m është kufiri i brezit malor. Mbi 2,656 m nuk ka majë në Kosovë, prandaj nuk hapet zonë e re.

Vlera 800 hyn te Fushë (24 rreshta). Vlera 1,500 hyn te Kodrinore (3 rreshta).

## Vendimi dhe arsyetimi

Rreshtat pa `elevation` marrin `E panjohur`. Nuk u jepet zona më e shpeshtë.

`elevation = 0` hyn te e njëjta kategori. Janë 3,634 rreshta, 3,624 prej tyre nga HabiProt, në 7 rajone dhe 32 komuna. Nuk është një vend i ulët. Nuk bëhet Fushë.

Nëntë vlerat jashtë 297–2,656 m mbeten `E panjohur`, jo Fushë apo Malore. Katër janë 100–293 m. Pesë ekzemplarë të Herbarium WU në të njëjtën pikë në Kaçanik kanë 2,750–3,050 m. Ato janë shënuar te `reports/vlefshmeria.md`. Pragu 297 m nuk përdoret për të fshirë çdo vlerë pak nën 270 m. Këtu përjashtohen vetëm këto nëntë, sepse janë kontrolluar veç e veç.

## Dokumentimi i detyrës

- **Varësia:** `reports/vendimi_per_lartesine_zero.md`.
- **Input:** `elevation`.
- **Çka u bë:** U shkrua `add_elevation_zone()` dhe tabela e zonave.
- **Rreshta para / pas:** 46,831 / 46,831.
- **Kolona para / pas:** 42 në CSV. Funksioni shton `elevation_zone` te rezultati.
- **Pse u bë:** Lartësia e njohur ndahet në fushë, kodër dhe mal. Mungesa, zeroja dhe nëntë vlerat e pamundura mbeten `E panjohur`.
- **Output:** `reports/zona_e_lartesise.md` dhe `add_elevation_zone()` te `notebooks/03_vetite.ipynb`.
- **Commit:** `Add elevation_zone from elevation`.
