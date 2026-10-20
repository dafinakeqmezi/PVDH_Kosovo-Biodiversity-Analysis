# Vendimet për mungesat strukturore

**Decision + Rationale:** protectedArea nuk mbushet me jashtë zonës. reports/data_dictionary.md përkufizon vetëm kuptimin e vlerave të raportuara; reports/data_types.md, reports/completeness.md dhe reports/redundancy.md bëjnë supozimin jashtë zonës, por nuk japin evidencën e spatial join. Në repo nuk u gjetën kufijtë, versioni apo kodi i këtij bashkimi. Verifikimi mbetet i hapur. Numri i zëvendësimeve është 0; statusi unknown dhe flamuri i mungesës ruhen. Nevojitet metadata e prodhuesit ose kontroll i koordinatave me një shtresë të plotë dhe të versionuar të zonave të mbrojtura.

Për iasAppliesFrom, kuptimi i fushës dhe crosstab-i mbështesin not_applicable kur iasUnionConcern=False. Ky është status i zbatueshmërisë së datës, jo datë e imputuar. Rreshtat True pa datë mbeten unknown; False me datë shënohen inconsistent. Çdo datë ruhet dhe validohet në seksionin e tipeve.

| kolona | mungesa | vlera_te_zevendesuara | not_applicable | unknown | statusi |
| --- | --- | --- | --- | --- | --- |
| protectedArea | 25762 | 0 | 0 | 25762 | pending_spatial_evidence |
| protectedAreaDesignation | 25762 | 0 | 0 | 25762 | pending_spatial_evidence |
| iasAppliesFrom | 46807 | 0 | 46807 | 0 | flag_applied |