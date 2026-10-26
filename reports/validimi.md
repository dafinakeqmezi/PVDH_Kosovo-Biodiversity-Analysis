# Validimi i dataset-it të pastruar

**Rezultati: 23 PASS / 0 FAIL.** Çdo kontroll vlerësohet me assert; dështimet ruhen në raport përpara assert-it përfundimtar.

1. **Input:** processed/biodiversity_clean.csv, schema, manifest, cleaning_log.csv, vendimi dhe lista e duplikateve, dataset-i origjinal dhe referenca historike Git.
2. **Çka u bë:** Validim i checkpoint-it të rilexuar nga disku; kontroll i tipeve, duplikateve, vlerave, log-ut dhe integritetit të origjinalit.
3. **Rreshta para / pas:** 46,456 / 46,456; **kolona para / pas:** 83 / 83. Validimi nuk pastron ose ndryshon të dhënat.
4. **Pse u bë:** Të kontrollohet zbatimi i vendimeve dhe përputhja e checkpoint-it me gjurmën e pastrimit.
5. **Output:** reports/validimi.md dhe reports/kontrollet_e_validimit.csv. Emri validimi.md është versioni shqip i validation.md në plan.
6. **Commit:** Add validation checks for the cleaned biodiversity dataset (mesazh i propozuar).

| kontrolli | statusi | detaje |
| --- | --- | --- |
| CSV lexohet me tipet, kategoritë dhe renditjen në schema | PASS | Kontrolli kaloi. |
| SHA-256 përputhet me manifestin: source | PASS | Kontrolli kaloi. |
| SHA-256 përputhet me manifestin: dataset | PASS | Kontrolli kaloi. |
| SHA-256 përputhet me manifestin: schema | PASS | Kontrolli kaloi. |
| dataset/ i paprekur kundrejt Git HEAD dhe origjinalit historik | PASS | Kontrolli kaloi. |
| Dimensionet përputhen me manifestin | PASS | Kontrolli kaloi. |
| gbifID unik dhe pa mungesa | PASS | Kontrolli kaloi. |
| Pa duplikate të mbetura sipas definicionit të miratuar; grupet e përjashtuara ruhen | PASS | Kontrolli kaloi. |
| ID-të finale janë saktësisht origjinali minus lista e largimit | PASS | Kontrolli kaloi. |
| Tipet e kërkuara dhe flamujt e mungesës janë të saktë | PASS | Kontrolli kaloi. |
| Numrat e plotësuar janë finite | PASS | Kontrolli kaloi. |
| Latitude brenda [-90,90], pa mungesa | PASS | Kontrolli kaloi. |
| Longitude brenda [-180,180], pa mungesa | PASS | Kontrolli kaloi. |
| Muajt e njohur janë 1-12 | PASS | Kontrolli kaloi. |
| Ditët e njohura janë 1-31 | PASS | Kontrolli kaloi. |
| Vitet e njohura janë 1 deri në vitin aktual | PASS | Kontrolli kaloi. |
| Kombinimet e plota year/month/day formojnë data reale | PASS | Kontrolli kaloi. |
| individualCount i njohur është i plotë dhe jo negativ | PASS | Kontrolli kaloi. |
| Pasiguria e njohur është pozitive | PASS | Kontrolli kaloi. |
| Nuk mbetet placeholder elevation=0 | PASS | Kontrolli kaloi. |
| Datat e njohura parsueshme, intervalet të renditura dhe flamuri taksonomik konsistent | PASS | Kontrolli kaloi. |
| Log-u: plotësia, rendi, dimensionet, rreshtat e larguar dhe hash-i | PASS | Kontrolli kaloi. |
| Validimi nuk ndryshoi origjinalin, checkpoint-in ose cleaning_log | PASS | Kontrolli kaloi. |

## Kufijtë e interpretimit

- Pa duplikate do të thotë sipas vendimit operacional: një fitues në çdo grup të pranuar dhe të gjithë rreshtat e grupeve të përjashtuara. Nuk pretendohet se janë zgjidhur të gjitha përsëritjet biologjike të mundshme.
- CSV nuk ruan tipet pandas; ato kontrollohen pas rileximit me schema, krahas hash-it të schema dhe kërkesave eksplicite për Int64, bool, datetime dhe kategori.
- Pa vlera të pamundshme vlen për rregullat e listuara: diapazone koordinatash, data reale, numërime jo negative, pasiguri pozitive dhe mungesë e elevation=0. Nuk është verifikim i saktësisë biologjike/hapësinore të çdo regjistrimi. Lartësitë jo-zero të dyshimta dhe pasiguritë e mëdha ruhen sipas vendimit; nuk hiqen vetëm që validimi të dalë PASS.
- Pragu i pasigurisë nuk certifikon komunën; protectedArea mbështetet në sqarimin e përdorueses, jo GIS të pavarur. Mungesat e lejuara (përfshirë individualCount) nuk janë dështim.
- Nuk shtohet hap transformimi në cleaning_log.csv: ky është validim vetëm për lexim, pas ngrirjes së pastrimit. Njoftimi i ekipit është detyrë më vete.
- Checkpoint SHA-256: `e83b0cab86ef5021cc23fbd1029071883c16a203d61cdc118bdafac6cb30117a`.
