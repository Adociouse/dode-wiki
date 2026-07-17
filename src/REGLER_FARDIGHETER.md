# Färdighetssystemet — D&DE Expert

> **Källa:** REG s.15–43 · RP s.28–30, s.34–64 · KH s.3

---

## Snabbreferens

**Slå 1T20 ≤ FV (Färdighetsvärde)** för att lyckas med en färdighet.

| Utfall | Resultat |
|--------|----------|
| "1" + nytt ≤ FV | **Perfekt slag** |
| 2–19 ≤ FV | Lyckat |
| 2–19 > FV | Misslyckat |
| "20" + nytt > FV | **Fummel** |

- **CL** (Chans att Lyckas) = FV modifierat av situationen
- **"1" lyckas alltid** om CL ≥ 1
- **"20" misslyckas alltid**

---

## Kategorier

### Kategori A — Standard (FV 1–20+)
- Använd FV direkt
- De flesta färdigheter
- Kan ha FV över 20 (regler för detta — se nedan)
- Betecknas INTE med extra symbol

### Kategori B — Kan/Kan-Inte (FV 1–5)
- Färdigheter där slumpen spelar liten roll
- Antingen kan man göra det, eller inte
- Exempel: **Tala språk** (Tala ett språk väl = B4–5; halvhjärtat = B2–3)
- Skrivs som "B4" etc.
- Om man behöver omvandla B-FV till A-FV: multiplicera med 5

### Primära färdigheter (alla har, grundkostnad 2 EP/FV-steg)

Alla rollpersoner börjar med dessa som primära:

| Färdighet | Grundegenskap |
|-----------|---------------|
| Bluffa | KAR |
| Finna dolda ting | INT |
| Första hjälpen | INT |
| Gömma sig | INT |
| Hoppa | SMI |
| Klättra | SMI |
| Köpslå | KAR |
| Lyssna | INT |
| Läsa/skriva modersmål | INT (spec.) |
| Rida | SMI |
| Spåra | INT |
| Stjäla föremål | SMI |
| Tala modersmål | INT (spec.) |
| Upptäcka fara | PSY |
| Värdera | INT |
| Övertala | KAR |

*(RP s.36)*

---

## Baschans (BC)

Varje färdighet har en **baschans (BC)** — det FV som alla får GRATIS utan att spendera EP.

- **BC = Grupp av grundegenskapen** (se REGLER_EGENSKAPER.md)
  - Exempel: SMI 14 (grupp 3) → BC 3 i alla SMI-färdigheter du är tillåten att ha
- Om BC = 0 → färdigheten är för svår för en otränad person
- Primära färdigheter: de flesta har BC = grundegenskapens grupp
- Vissa färdigheter har fast BC (t.ex. "BC: 0" = ingen gratis FV)

### Rasmodifikationer på BC

| Ras | Färdighet | Bonus |
|-----|-----------|-------|
| Alvfolk | Finna dolda ting | +1T3 |
| Dvärg | Finna dolda ting | +1T4 |
| Kattman | Finna dolda ting | +1T3 |
| Grottalv | Lyssna | +1T2 |
| Vargman | Lyssna | +1T3 |
| Kattman | Lyssna | +1T3 |
| Halvlängdsman | Provsmaka | +1T3 |
| Vargman | Provsmaka | +1T3 |
| Kattman | Upptäcka fara | +1T2 |
| Vargman | Upptäcka fara | +1T2 |
| Kattman | Spåra | +1T2 |
| Vargman | Spåra | +1T3 |
| Skogsalv | Orientering | +1T2 |
| Silveralv | Orientering | +1 |

*(REG s.10)*

---

## EP-budget och startfärdigheter

### EP-budget (KH s.3 / RP s.28)

Antal EP vid rollpersonsskapande (beror på nivå och ålder):

| Ålder | Vanlig | Extraordinär | Hjälte |
|-------|--------|--------------|--------|
| Ung | 150 | 175 | 200 |
| Mogen | 200 | 225 | 250 |
| Medelålders | 250 | 275 | 300 |
| Gammal | 300 | 325 | 350 |

**Kvarvarande BP × 5** läggs till EP-budgeten (RP s.28).

### Max FV från start (KH s.3)

| Ålder | Vanlig | Extraordinär | Hjälte |
|-------|--------|--------------|--------|
| Ung | 13 | 15 | 17 |
| Mogen | 15 | 17 | 19 |
| Medelålders | 17 | 19 | 20 |
| Gammal | 19 | 20 | 20 |

---

## Kostnader — EP per FV

### Grundkostnader

| Typ | Grundkostnad (EP per FV-steg) |
|-----|-------------------------------|
| **Primär** färdighet | 2 |
| **Yrkesfärdighet** (vald bland de 12) | 3 |
| **Sekundär** färdighet (ej vald som yrke) | 5 |

### Besvärjelse-kostnader

| Skolvärde | EP/S-steg |
|-----------|-----------|
| 1–3 | 4 |
| 4–6 | 6 |
| 7–9 | 6 |
| 10–12 | 8 |
| 13–15 | 10 |
| 16–18 | 12 |
| 19–21 | 14 |

*(RP s.30)*

### Multiplikatortabell

Kostnaden att höja en färdighet från FV `a` till FV `b`:

> **Kostnad = grundkostnad × (C(b) − C(a))**

Kumulativa C-värden:

```
FV:  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21
C:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12,14,16,18,21,24,27,31,35,39,44]
```

**FV multipliceras (vid FV 20+):** För kategori A ökar multipeln med +1 per 3 steg:
- FV 21–23: multipel ×5
- FV 24–26: multipel ×6
- FV 27–29: multipel ×7
- etc.

**Verifierat exempel:** Klättra (primär, grundkostnad 2) från FV 4 → FV 10:
C(10) − C(4) = 10 − 4 = 6 → 2 × 6 = **12 EP** (stämmer med bokens exempel — RP s.30)

### Exempel på kostnadsberäkning

Höja Svärd (yrkesfärdighet, grundkostnad 3) från FV 5 till FV 12:
- C(12) − C(5) = 14 − 5 = 9
- Kostnad = 3 × 9 = **27 EP**

---

## Färdighetslistan — primära och sekundära

### Primära färdigheter
*(Alla rollpersoner har dessa — se tabell ovan)*

### Sekundära färdigheter (urval med grundegenskap)

| Färdighet | Grundegenskap | Kostnad | BC |
|-----------|---------------|---------|-----|
| Akrobatik | SMI | 3 | 0 |
| Alkemi | INT | 4 | 0 |
| Animism (magiskola) | INT | — | 0 |
| Astrologi | INT | 3 | 0 |
| Avväpna | SMI | 3 | 0 |
| Bärsärkagång | PSY | 3 | 0 |
| Buktala | PSY | 3 | 0 |
| Dans | SMI | 2 | 0 |
| Djurhelning | PSY | 3 | 0 |
| Djurträning | PSY | 3 | 0 |
| Dolk | SMI | 2 | SMI |
| Dra vapen | SMI | 3 | 0 |
| Drogkunskap | INT | 3 | 0 |
| Elementarmagi (magiskola) | INT | — | 0 |
| Finna dolda ting | INT | 2 | INT |
| Förfalskning | INT | 3 | 0 |
| Geografi | INT | 2 | 0 |
| Geologi | INT | 2 | 0 |
| Giftkunskap | INT | 3 | 0 |
| Gycklekonster | SMI | 3 | 0 |
| Gömma sig | INT | 2 | INT |
| Hantera fällor | SMI | 3 | 0 |
| Hantverk (spec.) | varierar | 2 | 0 |
| Hasardspel | INT | 2 | 0 |
| Heraldik | INT | 2 | 0 |
| Historia | INT | 2 | 0 |
| Hoppa | SMI | 2 | SMI |
| Hypnotisera | PSY | 3 | 0 |
| Judo | SMI | 2 | 0 |
| Karate | SMI | 3 | 0 |
| Klättra | SMI | 2 | SMI |
| Knopar | SMI | 2 | 0 |
| Kulturkännedom | INT | 2 | 0 |
| Kunskap om demoner | INT | 3 | 0 |
| Kunskap om magi | INT | 3 | 0 |
| Kunskap om odöda | INT | 3 | 0 |
| Köpslå | KAR | 3 | 0 |
| Låsdyrkning | SMI | 3 | 0 |
| Läkekonst | INT | 3 | 0 |
| Läppläsning | INT | 3 | 0 |
| Läsa/Skriva språk | INT | varierar | 0 |
| Lyssna | INT | 2 | INT |
| Magisk kanalisering | INT | 3 | 0 |
| Massage | SMI | 2 | 0 |
| Mentalism (magiskola) | INT | — | 0 |
| Muta | KAR | 2 | 0 |
| Målning | SMI | 2 | 0 |
| Navigation | INT | 3 | 0 |
| Orientering | INT | 2 | 0 |
| Räkning | INT | 2 | 0 |
| Schack & Brädspel | INT | 2 | 0 |
| Simma | FYS | 2 | 0 |
| Sjökunnighet | INT | 3 | 0 |
| Sjunga | KAR | 8 | 0 |
| Skådespeleri | KAR | 3 | 0 |
| Slagsmål | STY | 2 | STY+SMI |
| Smyga | SMI | 2 | SMI |
| Spela instrument | KAR | 8 | 0 |
| Spåra | INT | 2 | INT |
| Spå väder | INT | 3 | 0 |
| Språkkunskap | INT | 3 | 0 |
| Stavhopp | SMI | 2 | 0 |
| Stjäla föremål | SMI | 2 | SMI |
| Stridskonster | SMI | varierar | 0 |
| Taktik | INT | 3 | 0 |
| Tala språk (Kate. B) | INT | varierar | 0 |
| Teckenspråk | INT | 6 | 0 |
| Trästav | SMI | 2 | SMI |
| Två vapen | SMI | 4 | 0 |
| Undre världen | INT | 3 | 0 |
| Uppfattningsfärdigheter | — | — | — |
| Vapenfärdigheter | SMI | 2 | SMI |
| Värdera | INT | 2 | INT |
| Zoologi | INT | 3 | 0 |
| Änterhake | SMI | 2 | 0 |
| Örtkunskap | INT | 3 | 0 |
| Övertala | KAR | 2 | KAR |
| Överlevnad | INT | 3 | 0 |

*(⚠ Grundkostnader och BC — verifiera mot RP s.34–64 och REG s.19–43)*

---

## Sköldhand

- Sköldhand = motstånds-handen (normalt vänster)
- Att använda en färdighet (tränad i svärdshanden) med sköldhand: **CL × 1/3**
- Träna en färdighet specifikt för sköldhand: **dubbelt kostsamt**, räknas som separat färdighet
- Kategori B med sköldhand: **FV −2**
- **Dubbelhänt:** kan använda båda händerna lika bra men inte SAMTIDIGT
- **Ambidextriös:** kan använda båda händerna till OLIKA saker SIMULTANT

---

## Vapenfärdigheter — Vapengrupper

Varje vapen är en separat färdighet, men alla vapen inom en vapentyp:
> Om du har FV X i ett vapen **har du alltid minst FV X/3 (avrunda nedåt)** i alla andra vapen inom samma vapentyp.

| Vapentyp | Vapen (urval) |
|----------|----------------|
| Dolkar | Dolk, Dirk, Parerdolk, Tanto |
| Enhandssvärd | Kortsvärd, Bredsvärd, Wakizashi |
| Övriga svärd | Kroksabel, Katana, Slagsvärd, Ninjato |
| Stavar | Trästav |
| Yxor | Handyxa, Bredyxa, Tvåhandsyxa |
| Klubbor & Hammare | Hammare, Stridsklubba, Stridshammare, Kofot |
| Spjut | Kortspjut, Långspjut, Lans, Treudd, Spetum, Naginata |
| Stångvapen | Hillebard, Pik |
| Slagor & Gissel | Stridsslagan, Stridsgissel, Morgonstjärna |
| Sköldar | Alla sköldtyper |
| Bågar | Liten, Kort, Lång, Sammansatt |
| Armborst | Lätt, Tungt, Arbalest |
| Slungor | Slunga, Stavslunga |
| Kastvapen | Kaststjärna, Kastspjut, Kastkniv, Kastyxa, Bola |
| Lasso | Lasso |
| Piskor | Oxpiska |
| Slagsmål & Judo | Näve, Spark |
| Karate | Näve (karate), Spark (karate) |

*(REG s.25–28)*

---

## Slagsmål — specialregler

- Grundegenskap: STY
- BC = STY-grupp + SMI-grupp (kombinerat)
- Träff mot person i metallrustning: **+1 KP extra skada**
- Judo och Karate räknas som separata vapengrupper

---

## Erfarenhetspoäng i spel

- Varje gång man lyckas med en färdighet i ett stressigt läge (SL bedömer) noteras ett **streck** vid färdigheten
- 1 lyckad användning (stressigt läge) = 1 EP
- **Perfekt slag** ger 1T3+1 EP
- EP kan bara användas efter en sammanhängande viloperiod på minst **7 dagar**
- Under ett äventyr kan EP inte omsättas — man sparar dem
- SL kan dela ut **bonuspoäng** (1–4) efter äventyr för uppdragsframgång; (1–2) för svåra gärningar; (1–4) för god rollspelning. Max 10 bonuspoäng per äventyr.
- Bonuspoäng är INTE bundna till en viss färdighet — kan användas fritt

*(REG s.45–46)*

---

## Differensnummer

Differensnumret = CL − tärningens utfall.

Exempel: CL 17, tärning visar 12 → Differensnummer = 17−12 = **5**.

Differensnumret används bl.a. i Köpslå och Gömma sig för att mäta graden av framgång.

---

## Stridskonster

Stridskonster är en familj av vapenfärdigheter (RP s.55–59 / KH s.5). De innehåller **tekniker** som köps separat.

| Teknik | Kostnad | Effekt |
|--------|---------|--------|
| Awäpna | 1,0 | Parerar + tar motståndarens vapen |
| Bedövningsslag | 1,0 | 1T3 skada; Svårt FYS-slag eller tillfälligt bedövad |
| Blind strid | — | Kan slåss i mörker utan FV-avdrag |
| Dubbelslag | — | Två knytnävsattacker mot OLIKA mål i 1 SR |
| Dubbelspark | — | Hoppspark mot DEUX mål (1T6 skada/mål) |
| Fallteknik/Rullning | 1,0 | Halverar skada vid fall; rullning ger +5 rutor |
| Fint | — | Halverar motståndarens parerings-CL om den lyckas |
| Hoppspark | — | 1T8 skada; −2 initiativ; landar i motståndarens ruta |
| Högt kast | — | Utförs alltid sist i SR; offret kastas 1T3 rutor och är liggande |
| Initiativbonus | — | +5 till SMI för turordning (alltid aktiv) |
| Krosslag | — | 1T6 skada, riktat mot känsliga punkter |
| Liggande strid | 1,0 | Kan anfalla/parera liggandes |
| Läsning/Neddragning | 1,0 | — |
| Normal spark | — | 1T6 skada |
| Rundspark | 1,0 | 1T8 skada; missar = förlorar nästa runda; −2 initiativ |
| Slå medvetslös | — | (KH — se Krigarens Handbok) |
| Stålsättning | — | Lyckad FV-slag → halv skada (ej mot huvudet) |
| Uppresning | — | Reser sig omedelbart efter att ha kastas omkull (FV-slag) |
| Vidvinkelsyn | — | Ser 270° runt sig, alltid aktiv |

*(Kostnader = RP s.55–59; KH s.5 för fler tekniker)*

---

## Kategori B — FV-skalan

| B-FV | Innebörd |
|------|----------|
| 0 | Ingenting; inte ens kommunicera |
| 1 | Kan göra sig förstådd på ett primitivt sätt |
| 2 | Talar med stark accent, enkla meningar |
| 3 | Talar flytande men med accent |
| 4 | Talar det som modersmål i praktiken |
| 5 | Absolut flytande |

*(Baserat på Sjunga & Spela-beskrivningen — RP/REG. Exakt skala bör verifieras för Tala Språk)*

---

## Okunskapsanvändande

Om en rollperson INTE har lärt sig en färdighet men den har en BC (baschans) > 0:
- Rollpersonen har ändå FV = BC i den färdigheten
- Kan bara slå på det FV, inga förbättringar utan EP-investering
