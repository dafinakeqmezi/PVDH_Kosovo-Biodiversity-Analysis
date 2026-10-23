# Vendimet për mungesat strukturore

**Decision + Rationale:** Sipas sqarimit të përdorueses më 23 tetor 2026, protectedArea bosh nënkupton jashtë zonave të mbrojtura të regjistruara në këtë dataset. Ky është konfirmim semantik nga përdoruesja, jo verifikim i pavarur GIS ose dokumentacion zyrtar i prodhuesit. Prandaj vetëm boshllëqet zëvendësohen me "Jashtë zonës së mbrojtur". protectedAreaDesignation bëhet "Nuk aplikohet" vetëm te të njëjtët rreshta me emër zone fillimisht bosh; një emërtim që mungon për një zonë të njohur do të mbetej unknown. Emrat ekzistues nuk ndryshohen. Flamujt is_missing rifreskohen, ndërsa protected_area_status ruan dallimin mes zonës së raportuar dhe mungesës strukturore. Kufizim: rezultati vlen sipas kuptimit dhe mbulimit të dataset-it, jo si pretendim i verifikuar për të gjithë kufijtë zyrtarë.

Për iasAppliesFrom, kuptimi i fushës dhe crosstab-i mbështesin not_applicable kur iasUnionConcern=False. Ky është status i zbatueshmërisë së datës, jo datë e imputuar. Rreshtat True pa datë mbeten unknown; False me datë shënohen inconsistent. Çdo datë ruhet dhe validohet në seksionin e tipeve.

| kolona | mungesa | vlera_te_zevendesuara | not_applicable | unknown | statusi |
| --- | --- | --- | --- | --- | --- |
| protectedArea | 25762 | 25762 | 25762 | 0 | user_confirmed_semantics |
| protectedAreaDesignation | 25762 | 25762 | 25762 | 0 | user_confirmed_semantics |
| iasAppliesFrom | 46807 | 0 | 46807 | 0 | flag_applied |