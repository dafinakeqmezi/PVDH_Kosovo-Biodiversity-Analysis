# Plotësimi i year/month

**Decision + Rationale:** Plotësimi është rikuperim determinist, jo imputim statistikor. Përdoren vetëm data të plota ose intervale me dy skaje të plota brenda të njëjtit muaj dhe vit. Data vetëm me vit ose vit-muaj përjashtohet sipas kërkesës së detyrës. Intervalet që kalojnë muaj/vite nuk plotësojnë as year, as month. Kufijtë artificialë të datave të pjesshme nuk përdoren si evidencë. Një konflikt me year/month ekzistues e ndalon plotësimin e rreshtit; vlerat ekzistuese nuk korrigjohen automatikisht. day mbetet i pandryshuar.

| kolona | mungesa_para | te_plotesuara | mungesa_pas | perqindja_para | perqindja_pas |
| --- | --- | --- | --- | --- | --- |
| year | 2268 | 0 | 2268 | 4.84 | 4.84 |
| month | 2867 | 0 | 2867 | 6.12 | 6.12 |

`gjurma_e_plotesimit_year_month.csv` përmban çdo qelizë year/month që ishte bosh, ID-në, eventDate, kufijtë, rezultatin dhe arsyen e plotësimit ose përjashtimit. `year_was_filled`/`month_was_filled` tregojnë vlerat e rikuperuara. Flamujt `*_is_missing` tregojnë mungesën aktuale pas plotësimit.

## Dokumentimi i detyrës

1. **Input:** df_clean pas parsimit të eventDate dhe konvertimit të tipeve; burimi dataset/kosovo_overall_biodiversity.csv.
2. **Çka u bë:** U plotësuan vetëm year/month të derivueshme pa paqartësi dhe u regjistruan hapat me log_step().
3. **Rreshta para/pas:** 46,831 / 46,831; dy flamuj shtesë. Numrat e kolonave janë në processed/cleaning_log.csv.
4. **Pse u bë:** Për të rikuperuar informacionin kohor të raportuar pa shpikur data dhe pa mbishkruar vlera.
5. **Output:** plotesimi_year_month_para_pas.csv, gjurma_e_plotesimit_year_month.csv, flamujt dhe dataset-i i ndërmjetëm.
6. **Commit:** Fill unambiguous missing year and month values (mesazh i propozuar).

Duplikatet nuk trajtohen në këtë hap; varen nga analiza e Dafinës.
