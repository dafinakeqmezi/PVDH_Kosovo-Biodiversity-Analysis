# Largimi i duplikateve

1. **Input:** df_clean dhe lista processed/rreshtat_per_fshirje_duplikate.csv, e rindërtuar në seksionin e vendimit.
2. **Çka u bë:** U larguan 375 rreshta nga 235 grupe të pranuara.
3. **Rreshta para/pas:** 46,831 / 46,456; **kolona para/pas:** 79 / 79.
4. **Pse u bë:** Zbatim i vendimit të dokumentuar, pa ndryshuar numërimet dhe pa bashkuar të dhënat e rreshtave.
5. **Output:** processed/rreshtat_e_larguar_duplikate.csv, reports/kontrolli_i_largimit_te_duplikateve.csv, processed/cleaning_log.csv dhe kopja e pastruar.
6. **Commit:** Remove approved duplicates and normalize categories (mesazh i propozuar).
7. **Decision + Rationale:** Çdo grup i pranuar ka saktësisht një rresht, atë të përzgjedhur. Çdo grup i përjashtuar ruan të gjithë rreshtat. Nuk mbeten duplikate sipas definicionit të pranuar; kjo nuk pretendon se nuk ekzistojnë dyfishime të tjera jashtë kriterit. Numërimet konfliktuale nuk mblidhen dhe nuk fshihen.

Kontrolli i 1,288 grupeve kaloi. Rreshtat e larguar ruhen veçmas për auditim; origjinali mbetet i paprekur.
