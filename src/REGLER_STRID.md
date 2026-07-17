# Strid & Vapen — D&DE Expert

> **Källa:** REG s.47–63 · RP s.35 (vapenfärdighet) · KH (detaljerade stridsregler)

D&DE Expert har **två stridssystem**: grundsystemet (snabbt, enkelt) och det alternativa (detaljerat, med kroppsdelar). SL väljer vilket som används — det alternativa rekommenderas inte för nybörjare.

---

## Snabbreferens — En stridsrunda

```
1. Bestäm turordning (initiativ)
2. Anfallaren slår 1T20 ≤ FV → träff
3. Försvararen slår 1T20 ≤ FV → parering (sköld/vapen)
4. Om träff: slå vapenskada + SB − ABS = faktisk skada på KP
5. Kontrollera KP-status
```

**1 Stridsrunda (SR) = ca 5 sekunder**

---

## Turordning (Initiativ)

- Turordningen baseras på **SMI** — högst SMI agerar först
- Lika SMI: slå 1T6, högst slår först
- **Vapenlängd** påverkar striden första SR: längre vapen slår ALLTID FÖRST i stridernas första SR; från SR 2 används normal turordning (REG s.56)

### Initiativmodifikationer

| Situation | Modifikation |
|-----------|-------------|
| Krigare (yrkesförmåga) | +5 på alla initiativslag |
| Karate (färdighet aktiv) | +5 på SMI vid initiativ |
| Hoppspark | −2 på initiativslaget |
| Rundspark | −2 på initiativslaget |
| Stridskonst: Initiativbonus (teknik) | +5 till SMI |

---

## Anfallsslag

**Slå 1T20 ≤ FV** för att anfallet lyckas.

FV = Färdighetsvärde i aktuellt vapen (modifierat av CL-modifikationer).

### Resultat

| Tärningsutfall | Resultat |
|----------------|----------|
| **1** → slå igen ≤ FV | **Perfekt träff** |
| **1** → slå igen > FV | Vanlig träff |
| 2–19 ≤ FV | Lyckat anfallsslag — träff |
| 2–19 > FV | Misslyckat — miss |
| **20** → slå igen > FV | **Fummel** |
| **20** → slå igen ≤ FV | Vanlig miss |

### CL-modifikationer (urval)

| Situation | Modifikation |
|-----------|-------------|
| Siktar på specifik kroppsdel | −5 |
| Anfaller liggande mål | +5 |
| Sköldhand används (ej tränad) | CL × 1/3 |
| Fiende bär metallrustning (Slagsmål) | +1 KP extra skada vid träff |
| Avståndsvapen: mål går | CL × 3/4 |
| Avståndsvapen: mål springer | CL × 1/2 |
| Avståndsvapen: mål flyger | CL × 1/4 |

---

## Parering

- Parering görs med samma FV som anfallet (vapenfärdigheten kombinerar anfall och parering)
- **Slå 1T20 ≤ FV** för att parera
- Man kan bara parera **en attack** per SR (om inte FV 20+ ger extra bitar)
- **Sköld** ger separat parering utöver vapnets

### Sköldar
| Sköldtyp | Storlek |
|----------|---------|
| Liten sköld | − |
| Medelstor sköld | − |
| Stor sköld | − |

*(I det alternativa stridssystemet täcker sköldar specifika kroppsdelar — REG s.56)*

### Parering av kastvapen
- Möjligt **om** sköldbäraren ser kastet utföras
- Fungerar som vanlig parering

### Sköldars tålighet
- Om skölden framgångsrikt parerar ett anfall finns **1/20 chans** att skölden förstörs (slå 1T20 direkt efter pareringen — REG s.57)

---

## Skada & Absorption

### Skada

1. Slå vapenskada (t.ex. Bredsvärd: 1T8+1)
2. Lägg till **Skadebonus (SB)** (baserat på STY + STO — se REGLER_EGENSKAPER.md)
3. Dra av **ABS** (rustningens Absorption)
4. Återstående minskar motståndarens **KP**

### Absorption (ABS)

Rustning minskar skada med sitt Abs-värde VARJE GÅNG man träffas.

| Rustning | Abs |
|----------|-----|
| Tjockt tyg | 1 |
| Läder | 2 |
| Nitläder | 3 |
| Lätt fjällpansar | 4 |
| Fjällpansar | 5 |
| Ringbrynja | 6 |
| Förstärkt ringbrynja | 7 |
| Helrustning (metall) | 8 |

*(Fullständig tabell: REG s.53. Abs gäller för HELA kroppen i grundsystemet.)*

---

## KP och Skadetillstånd

| KP | Tillstånd |
|----|-----------|
| ≥1 | Stridfärdig |
| ≤0 | Orkar krypa och göra Första Hjälpen (halverad CL). Faller till marken |
| 0 till −FYS | Blöder: 1 KP extra var 6 SR (halvminut). Förblir medvetslös 40−FYS minuter |
| ≤ −FYS | **Dör** av skadorna |

**Om ingen läkning:** rollpersonen med KP ≤ 0 behöver **Första Hjälpen** för att stoppa blödning. Besvärjelsen HELA fungerar också.

---

## Fallen rollperson och dödsfall

### Blödning
En rollperson med Totala KP ≤ 0 faller till marken och är oförmögen att agera. Han blöder och tar **1 KP extra var 6 SR** (halvminut) tills:
- Någon lyckas med **Första Hjälpen** (stoppar blödningen), eller
- Besvärjelsen **HELA** läggs på honom

Rollpersonen är medvetslös **40 − FYS minuter** efter att blödningen stoppats. När han vaknar kan han inte agera aktivt förrän huvudets KP är positivt igen.

### Kritiska skador (alternativa systemet)
- En kroppsdel som tar **dubbelt sin KP** i skada är **kritiskt skadad** — arm/ben/vinge är avhuggen eller måste amputeras (slå 1T100 för procentandelen som tas bort)
- Kritiskt skadad **bröstkorg/mage/kropp** → omedelbar medvetslöshet, blöder inom FYS SR
- Kritiskt skadat **huvud** → rollpersonen dör omedelbart

### Infektion
Vapen är sällan rena — varje gång en rollperson träffas av ett djurs naturliga vapen finns risk för sårinfektion. Alvfolk är immuna. SL slår hemligt; symptom och allvar varierar.

---

## Helande

### Första Hjälpen
En lyckad Första Hjälpen-kontroll stoppar blödning (KP ≤ 0). Kräver **två fungerande armar**. Rollpersonen kan försöka på sig själv med **halverad CL**.

### Läkekonst
En person med Läkekonst kan påskynda tillfrisknandet. Slå ett färdighetsslag per patient per **full vecka** av vård. Lyckat slag → patienten läker **dubbelt så många KP** som normalt under veckan.

### Besvärjelsen HELA
Läggs på en specifik kroppsdel — den kroppsdelen läker. Överskjutande KP placeras valfritt på annan kroppsdel.

### Naturlig läkning
| Aktivitetsnivå | Läkning |
|----------------|---------|
| Total vila (sängliggande) | Normal takt per dag (⚠ exakt värde — verifiera mot REG) |
| Lätt aktivitet | Halverad takt |

*(REG s.50–52, Läkekonst: REG s.23)*

---

## Strid i mörker

En rollperson **utan mörkersyn** måste reducera sin CL vid anfall och parering:

| Ljusförhållande | CL-modifikation |
|-----------------|-----------------|
| Skymning / fackelsken | −5 |
| Mörker | −15 |
| Minsta möjliga CL | 1 (aldrig lägre) |

En varelse **med mörkersyn** som slåss mot varmblodiga varelser har **inga** av dessa modifikationer.

### Mörkersyn per ras
| Ras | Mörkersyn |
|-----|-----------|
| Dvärg | Mörkerseende (ser i kolmörker utan ljuskälla) |
| Orch | Perfekt mörkersyn |
| Rese | Begränsad mörkersyn (ser i kolmörker ungefär som människa med fackla) |
| Halvorch | Mörkersyn |
| Grottalv, Mörkeralv | Mörkersyn |

*(SL-boken s.21, Strid i mörker s.21)*

---

## Gift

Gift hanteras med ett **motståndslag**: offrets FYS mot giftets STY (Motståndstabellen).

### Effektnivåer

| Motståndslaget | Effekt |
|----------------|--------|
| Lyckas | Lindrig effekt |
| Misslyckas med 1–5 | Måttlig effekt |
| Misslyckas med 6–10 | Allvarlig effekt |
| Misslyckas med mer än 10 | Dödlig effekt |

Effekterna är **kumulativa** — dödlig effekt innebär att alla lägre nivåers effekter också inträffar.

### Tidsfördröjning (STY under 30)
| Effektnivå | Tid till debut |
|------------|---------------|
| Lindrig | 20 SR |
| Måttlig | +20 minuter |
| Allvarlig | +20 timmar |
| Dödlig | +20 dygn |

Från alla tider dras giftets **STY** bort (STY 15 → "20" byts mot "5").

### Tidsfördröjning (STY 30+)
| Effektnivå | Tid till debut |
|------------|---------------|
| Lindrig | 1 SR |
| Måttlig | 2 SR |
| Allvarlig | 3 SR |
| Dödlig | 1 minut |

### Gifttyper
- **Muskelgift** — förlamar, SMI-förlust, KP-förlust
- **Nervgift** — påverkar FYS och STY (minskar med 50% under verkningstid)
- **Blodgift** — feber, svullnad, SMI-förlust, KP per minut vid allvarlig nivå

### Motgift
Specifika motgifter och örter kan minska ett gifts STY (t.ex. minskar ett örtemotgift STY med 15). Färdigheten **Giftkunskap** används för att tillverka och använda gifter; **Örtkunskap** för läkedroger.

*(SL-boken s.50–51)*

---

## Perfekt och Fummel

### Perfekt träff (specialregler)
- **Alternativa stridssystemet:** maximal vapenskada + maximal SB, och målet får inte tillgodoräkna sig rustning/skydd
- **Grundsystemet:** SL ger någon form av bonus

### Fummeltabell — Närstridsvapen och sköldar

Slå 1T20 när fummel inträffar:

| 1T20 | Händelse |
|------|----------|
| 1 | Tappar delar av rustningen |
| 2–7 | Vacklar — missar nästa attack eller parering |
| 8 | Helt ur balans — missar nästa attacker OCH pareringar |
| 9–10 | Snubblar — tar 1 SR att resa sig |
| 11–13 | Snubblar (variant) — tar 1 SR att resa sig |
| 12–13 | Vrickar foten — förflyttning −1 resten av striden |
| 14–16 | Tappar vapnet/skölden i rutan |
| 17 | Tappar vapnet — slungas 1T3 rutor bort |
| 18 | Träffar närmaste vän med vapnet |
| 19 | Klumpig rörelse — nästa fientliga attack träffar automatiskt |
| 20 | Rejäl klantighet — slå DEUX gånger på tabellen |

*(REG s.60–61)*

### Fummeltabell — Naturliga vapen (nävar/sparkar)

| 1T20 | Händelse |
|------|----------|
| 1 | Tappar delar av rustningen |
| 2 | Tappar delar av rustningen (se ovan för detaljer) |
| 3 | Vacklar — missar nästa attack |
| 4 | Tappar delar av rustningen |
| 11–13 | Snubblar — tar 1 SR att resa sig |
| 14–15 | Vrickar foten |
| 16–17 | Alla fiender har +3 CL nästa SR (distraherad) |
| 18 | Träffar närmaste vän |
| 19 | Klumpig rörelse — nästa fiende-attack träffar automatiskt |
| 20 | Rejäl klantighet — slå DEUX gånger |

*(REG s.60)*

### Fummeltabell — Avståndsvapen

| 1T20 | Händelse |
|------|----------|
| 1–12 | Distraherad — kan inte agera denna SR |
| 13–15 | Tappar vapnet, kastvapen faller 1T6 rutor bort |
| 16–17 | Snubblar — tar 1 SR att resa sig |
| 18 | Träffar närmaste vän i skottfältet |
| 19 | Vapnet går sönder |
| 20 | Rejäl klantighet — slå DEUX gånger |

*(REG s.61)*

---

## Flera attacker

En rollperson med **FV 20+** på ett vapen kan dela upp sin FV i flera "bitar":
- Varje bit måste ha minst CL 10
- Fördelas fritt mellan attacker och pareringar
- Kan anfalla samma motståndare flera gånger
- Kan parera **en** attack per motståndare, aldrig mer
- Första attacken på sin sedvanliga plats i SR; resterande sist (REG s.57)

---

## Alternativa stridssystemet — Sammanfattning

Aktiveras av SL som ett val. Ger mer realism men tar längre tid.

### Totala KP vs. kroppsdelars KP

- **Totala KP** = (STO + FYS) / 2 — same formula
- Varje kroppsdel har egna KP (beräknade från Totala KP enligt tabell)
- Skadan räknas BÅDE från Totala KP och från den träffade kroppsdelen

### Vilken kroppsdel träffas

SL slår tärning beroende på om anfallet är framifrån/bakifrån/projektil:

**Humanoid (tabell 4 — REG s.49):**

| 1T8 (A: projektil/bakifrån) | 1T10 (B: närstrid mot försvararare) | Träffområde |
|-----------------------------|------------------------------------|-------------|
| 1 | 1 | Höger ben |
| 2 | 2 | Vänster ben |
| 3 | 3 | Mage |
| 4–5 | 4 | Bröstkorg |
| 6 | 5–6 | Höger arm |
| 7 | 7–8 | Vänster arm |
| 8 | 9–10 | Huvud |

### Effekter av skada per kroppsdel

| KP i kroppsdel | Effekt |
|----------------|--------|
| 0 eller lägre | Kroppsdelen obrukbar (arm/ben/vinge ger inte mer skada) |
| Bröstkorg/mage ≤ 0 | Faller, kan inte göra något, blöder 1 KP/halvminut |
| Huvud ≤ 0 | Medvetslös 40−FYS minuter; kan inte göra något |
| Dubbla kroppsdels-KP | Kritisk skada (amputation/krossat) |
| Huvud: kritisk | Rollpersonen **dör omedelbart** |

### Rustning i alternativa systemet
- Rustningsdelar täcker specifika kroppsdelar
- Man kan bara ha en rustningsdel per kroppsdel
- Vikt beror på bärarens STO (vikttabell A–K, REG s.54)

### Smärtpoäng (SP)
*(Krigarens Handbok, detaljerade regler)*
SP tilläggs i KH:s utökade system — ⚠ verifiera mot KH.

---

## Strid mot flera motståndare

- Rollpersonen får normalt ett anfallsslag per SR
- Med FV 20+ kan man dela FV (se ovan)
- En motståndare med FV 20–29 "kräver" 2 FV-bitar för att hanteras; FV 30–39 kräver 3 bitar (REG s.57)

---

## Stridsmoral

Reglerar hur **SLP:er** (inte spelarpersoner) beter sig i strid.

### Grundmoral

| Varelsetyp | Grundmoral |
|-----------|------------|
| Vanliga ointelligenta varelser | 10 |
| Aggressiva ointelligenta varelser | 15 |
| Anka (vit) | 7 |
| Anka (svart/brun) | 12 |
| Människa, halvlängdsman | 10 |
| Kattman | 14 |
| Kentaur | 13 |
| Orch, rese | 12 |
| Svartalf, svartnisse | 6 |
| Troll, varulv, vampyr | 18 |
| Vargman | 11 |
| Alvfolk, karkion, enhörning | 15 |
| Övriga intelligenta varelser | 14 |

*(REG s.61–62)*

### Modifikationer

| Situation | Mod |
|-----------|-----|
| Fiendernas totala STO överstiger gruppens med minst 33% | −5 |
| Gruppens totala STO överstiger fiendernas med minst 33% | +5 |
| Angrips från två eller flera håll | −5 |
| Ledaren sårats | −3 |
| Ledaren stupar/ger sig/tas till fånga | −5 |
| Hälften av gruppen oförmögna | −5 |
| Hälften av fienderna oförmögna | +5 |
| Förstärkning inom synhåll | +3 |
| Fiendens förstärkning inom synhåll | −3 |
| Varelsen har förlorat >½ av sina KP | −3 |
| Varelsen är en duglig kämpe | +3 |

### Moralslag

Vid kritiska lägen: slå 1T20 ≤ moral. Misslyckas slag → flyr eller går bärsärk. Fummel → ger upp helt. Perfekt → gör bärsärkkontroll.

---

## Bärsärk

| Varelse | Bärsärksvärde |
|---------|---------------|
| Anka | 3 |
| Människa | 1 |
| Kentaur | 1 |
| Minotaur | 13 |
| Reptilman | 4 |
| Cyklop | 5 |
| Dvärg | 2 |
| Jätte | 4 |
| Orch | 2 |
| Rese | 3 |
| Vargman | 2 |

*(REG s.63)*

**Bärsärkens regler:**
- Angriper vettlöst närmaste fiende
- Bryr sig inte om skador (riskerar att förblöda)
- **Två attacker per SR** (den andra sist i SR, efter alla andras attacker)
- Parerar INTE, ens med sköld
- Håller på tills alla fiender flyr/slås ut → ny bärsärkskontroll: lyckas = förföljer i FYS antal SR

**Frivillig bärsärk:** Spelaren kan låta rollpersonen stå stilla 1 SR och "arbeta upp sig". Slå bärsärkskontroll med **dubbelt bärsärksvärde**.

---

## Specialvapen — Regler

### Judo
- Kastomkullen: FV + SMI mot motståndarens STO + SMI (Motståndstabellen)
- Offret kastas 0–2 rutor; misslyckat SMI-slag → 1 KP skada
- Fasthållning: övervinner motståndarens SMI med egna FV
- Parerar 1T6 skada av ett närstridsvapen (absorbering, inte total parering)
- Kan inte bäras ringbrynja eller tyngre

### Karate
- Slag/sparkar gör **+1 skada**
- +5 på SMI för turordning
- Kan välja att blockera istället för att anfalla — minskar fientlig skada med 1T6
- Kan inte bäras läder eller tyngre

### Bola
- Träff: slå normalt anfallsslag; sedan FV-slag
- FV-slag lyckas → det avsedda händer (snor kring ben = fall; arm = obrukbar; huvud = omtumlad 1T3 SR)
- FV-slag misslyckas → 1T4 skada, inget mer
- Snuren arm/huvud: 1T3 SR att ta bort

### Lasso
- Träff: slå anfallsslag, sedan FV-slag
- FV-slag lyckas → slå STY mot motståndarens medelvärde STO/SMI för att rycka omkull
- Lasso kring halsen eller kring **två ben** dubblerar STY

### Oxpiska
- 1T2 skada även om FV-slag misslyckas
- Grepp varar bara den SR den träffar

### Spjut mot springande varelser
- Spjut/långspjut kan "stoppas upp" en springande varelse — ger vapnets skada + målets skadebonus
- Gäller bara stridernas första SR

---

## Avståndsvapen — Modifikationer

### Avstånd (FV 0–15)

| Avstånd (rutor) | Kastvapen | Projektilvapen |
|-----------------|-----------|----------------|
| 1 | Går ej | Går ej |
| 2–3 | ±0 | ±0 |
| 4–6 | −1 | ±0 |
| 7–10 | −2 | −1 |
| 11–15 | −3 | −1 |
| 16–20 | −4 | −2 |
| Varje +10m | −1 | −1 |

### Avstånd (FV 16+)

| Avstånd (rutor) | Kastvapen | Projektilvapen |
|-----------------|-----------|----------------|
| 2–3 | ±0 | ±0 |
| 4–6 | −1 | ±0 |
| 7–10 | −2 | −1 |
| 11–15 | −3 | −1 |
| 16–20 | −4 | −2 |
| 31–50 | −5 | −3 |
| 51–75 | −6 | −4 |
| 76–100 | −7 | −5 |
| 101–150 | −8 | −6 |
| 151–200 | −9 | −7 |

*(REG s.57)*

### Målrörelse

| Mål rör sig | CL-modifikation |
|-------------|-----------------|
| Stilla | × 1 |
| Går | × 3/4 |
| Springer | × 1/2 |
| Flyger | × 1/4 |

---

## Vapentyngd

- Om vapnets **STY-grupp är 1 steg för hög**: halveras CL
- Om vapnet är **1-2H** (kan tas med en eller två händer): STY-kravet är 1 steg lägre för tvåhandsvapen; som enhandsvapen är kravet 1 steg **högre** (REG s.57)
- Enhandsvapen med för högt STY-krav: kan användas som **tvåhandsvapen** om fästet räcker → ny separat färdighet

---

## Fasthållning

- Angriparen försöker hålla fast motståndaren
- Kräver lyckat anfallsslag (sker **sist i SR**)
- Sedan: anfallaren slår STY mot motståndarens STY (Motståndstabellen)
- Varje SR angriparen vill hålla fast: slå STY igen
- Motståndaren kan inte göra något under fasthållning

---

## Fotnot: Grundsystemet vs. Alternativa

| | Grundsystem | Alternativt |
|---|---|---|
| Kropp | En samlad KP | Tillgång till individuella kroppsdels-KP |
| Skada | Direkt mot KP | Mot kroppsdel + totala KP |
| Rustning | En Abs siffra | Rustningsdelar per kroppsdel |
| Tid | Snabbt | Tar längre tid |
| Rekommenderas | Nybörjare / stora strider | Viktiga dueller / dramatiska strider |
