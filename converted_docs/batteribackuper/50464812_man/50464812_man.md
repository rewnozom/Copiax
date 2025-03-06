![](_page_0_Picture_0.jpeg)

# Strömförsörjning

BT-5 FLX Small COM Gen2, BT-10 FLX Small COM Gen2

![](_page_0_Picture_3.jpeg)

![](_page_0_Picture_4.jpeg)

350-258 Publiceringsdatum 2023-10-30

| Revisioner och om detta dokuments utgåva  5                                                |  |
|--------------------------------------------------------------------------------------------|--|
| Du hittar manualer på: www.rco.se/file  5                                                  |  |
| Länkar till manualer och produktblad  5                                                    |  |
| Adress och kontaktuppgifter  5                                                             |  |
| Komponentöversikt  7                                                                       |  |
| Komponentöversikt BT FLX Small COM Gen2  7                                                 |  |
| Kapsling  7                                                                                |  |
| Konsol  7                                                                                  |  |
| Skjut fast konsoler  8                                                                     |  |
| Montering  9                                                                               |  |
| Tillvalskort till strömförsörjning  9                                                      |  |
| Batterier - placering och inkoppling  9                                                    |  |
| Anslut batterisäkring / bladsäkring  9                                                     |  |
| Schema - Inkoppling av batterier, 24 V  9                                                  |  |
| PRO3 moderkort  10                                                                         |  |
| Moderkort - beskrivning  10                                                                |  |
| Säkringar  11                                                                              |  |
| Elnätsanslutning  11                                                                       |  |
| Anslut last  12                                                                            |  |
| Dip-switch 1-8  13                                                                         |  |
| Omstart för att bekräfta ändringar i adress, batteri- och larminställningar mot överordnat |  |
| system  14                                                                                 |  |
| Återställning av data efter batteribyte - PRO3  15                                         |  |
| Kortbeskrivning - I2C Relay Card  15                                                       |  |
| Busskommunikation - inkoppling till UC-50 Gen2  16                                         |  |
| Bygling av UC-50 Gen2  18                                                                  |  |
| Flera enheter till ett överordnat system  19                                               |  |
| Driftsättning - hur enheten skall startas  19                                              |  |
| Driftsättning vid inkoppling till UC-50  19                                                |  |
| Systemtest  20                                                                             |  |
| Återställning  20                                                                          |  |
| Larm som visas på skåplucka / indikeringsdiod  20                                          |  |
| Justering av sabotagekontakt  21                                                           |  |
| Underhåll  21                                                                              |  |
| Batterier  22                                                                              |  |
| Batteribyte  22                                                                            |  |
| Batteriåtervinning  22                                                                     |  |
| Produktens livslängd, miljöpåverkan och återvinning  23                                    |  |
| Bilaga: Montera I2C-kort  23                                                               |  |
| Strömförsörjning - produktblad  23                                                         |  |
| SSF1014 certifierad batteribackup med kommunikation  23                                    |  |
|                                                                                            |  |
| Namn, artikelnummer, e-nummer och certifikatsnummer  24                                    |  |
| Om BT FLX COM Gen2  24                                                                     |  |
| Användningsområde  24                                                                      |  |
| Regelverk och certifieringar  25                                                           |  |
| Standarder som produkt(er) uppfyller och är godkänd för  25                                |  |

| Krav som produkten uppfyller  25                                                 |  |
|----------------------------------------------------------------------------------|--|
| Strömuttag per produkt  25                                                       |  |
| Kretskort - Tekniska data  25                                                    |  |
| Tekniska data, moderkort: PRO 3  25                                              |  |
| Tekniska data, PRO3 I2C-kort  26                                                 |  |
| Nätaggregat  27                                                                  |  |
| Nätaggregat - Tekniska Data LRS-150-24  27                                       |  |
| Nätaggregat - Tekniska Data RSP-320-24  28                                       |  |
| Tekniska data kapsling  28                                                       |  |
| Kapslingar - Tekniska Data FLX S  28                                             |  |
| Garanti, support, tillverkningsland och ursprungsland  28                        |  |
| Garanti 5 år  28                                                                 |  |
| Support  29                                                                      |  |
| Tillverkningsland  29                                                            |  |
| Tillverkare  29                                                                  |  |
| Batterier  29                                                                    |  |
| Batterier ingår ej  29                                                           |  |
| Batterikombinationer BT FLX Small COM Gen2 med Battery box 24V FLX S (14 Ah      |  |
| batterier)  29                                                                   |  |
| 14 Ah, 12 V AGM-batteri  30                                                      |  |
| Anslutning av batteribox  30                                                     |  |
| Montering Battery box 24V FLX S till batteribackup i FLX S-kapsling  30          |  |
| Inkoppling batteribox Batteribox 24V FLX S med batteribackup BT FLX COM Gen2  31 |  |
| Sabotagekontakt vid extra batteribox  32                                         |  |
|                                                                                  |  |

## <span id="page-4-0"></span>**Revisioner och om detta dokuments utgåva**

Gällande och senast publicerad utgåva av detta dokument finns på www.rco.se.

Revisionslogg kan rekvireras, se kontaktuppgifter för adress eller e-postadress.

Detta dokuments giltighet kan inte garanteras, då ny utgåva publiceras utan föregående meddelande.

Bruksanvisning i originalspråk: Svenska.

Bruksanvisning, tekniska data och översättningar av desamma kan innehålla fel. Det är alltid installatörens ansvar att installera produkten på ett säkert sätt.

## **Du hittar manualer på: www.rco.se/file**

### **Länkar till manualer och produktblad**

Du hittar manualer och produktblad på: www.rco.se/file

![](_page_4_Picture_10.jpeg)

## **Adress och kontaktuppgifter**

RCO Security AB Box 3130 169 03 Solna Sverige Växel: 08-546 560 00 info@rco.se www.rco.se

![](_page_5_Picture_1.jpeg)

#### **LÄS DETTA FÖRST!**

100 mm fritt utrymme skall lämnas på varje kortsida.

Elektronik, oavsett kapsling, är avsett för bruk i kontrollerad inomhusmiljö.

Ventilation får ej övertäckas.

Endast personer med behörighet bör installera och underhålla systemet.

Det är installatörens ansvar att systemet är lämpad för avsett bruk.

Dokument som medföljer systemet skall förvaras i det eller i dess omedelbara närhet.

Nätspänning bör vara bortkopplad under installation.

Alla uppgifter med reservation för ändringar.

Vid installation av denna produkt erkänner och accepterar installatören denna produkts begränsningar som de är beskrivna i denna manual.

Bruksanvisning på svenska i original1 .

![](_page_5_Picture_13.jpeg)

#### **OM GLASRÖRSSÄKRINGAR PÅ CERTIFIERADE ENHETER**

På kretskortets lastutgångar sitter glasrörssäkringar, dessa har en utlösningstid på ca 150 ms. I det fall en glasrörssäkring löser ut på EN lastutgång faller spänningen på ALLA lastutgångar till 0 V under 150 ms.

Installatören ansvarar för att det finns en energibuffert på minst 150 ms. i system som batteribackupen förser med ström eller acceptera ett strömavbrott på 150 ms.

<sup>1</sup>Översättning på annat språk än svenska är endast vägledande och ej säkert granskade. Översättning skall alltid kontrolleras mot det svenska originalet för att säkerställa korrekt information.

## <span id="page-6-0"></span>**Komponentöversikt**

## **Komponentöversikt BT FLX Small COM Gen2**

![](_page_6_Figure_3.jpeg)

#### Tabell 1. Komponentöversikt

| Bokstav | Förklaring                                                                              |  |
|---------|-----------------------------------------------------------------------------------------|--|
| A       | Konsol, vändbar för montering i vägg eller 19" rack.                                    |  |
| B       | Sabotagekontakt. Skall larmklass 3 (SSF) uppfyllas skall sabotagekontakt sitta på vägg. |  |
| C       | Skåp i pulverlackad plåt.                                                               |  |
| D       | Nätaggregat, plats och typ varierar med konfiguration.                                  |  |
| E       | Moderkort.                                                                              |  |
| F       | Kabelgenomföringar.                                                                     |  |
| G       | Plats för batterier.                                                                    |  |

## **Kapsling**

## **Konsol**

Medföljande konsoler kan fästas på två sätt: Vid montering på vägg skall konsolerna sitta bakåt, mot vägg. Vid montering i 19" rack skall konsolen sitta i framkant på enheten.

<span id="page-7-0"></span>![](_page_7_Figure_1.jpeg)

| Nr | Förklaring                                                        |  |
|----|-------------------------------------------------------------------|--|
| 1  | Gem i konsol som säkrar konsolen till kapslingen.                 |  |
| 2  | Hål för skruv - kan användas för att säkra konsolen i kapslingen. |  |
| 3  | Konsolen skruvas fast i vägg eller 19" rack.                      |  |

### **Skjut fast konsoler**

Enheten kan monteras i 19" rack eller på vägg. Medföljande konsoler kan fästas på två sätt: Vid montering på vägg skall konsolerna sitta bakåt, mot vägg. Vid montering i 19" rack skall konsolens sitta i framkant på enheten.

![](_page_7_Figure_5.jpeg)

Vänster konsol: vänd mot framsidan för montering i 19" rack.

Höger konsol vända mot baksidan för montering på vägg.

![](_page_7_Picture_8.jpeg)

#### **VIKTIGT**

Lämna 100 mm fritt kring luftgaller.

#### Figur 1. Montera konsoler på FLX S kapsling

### <span id="page-8-0"></span>**Montering**

Använd lämplig skruv för montering på vägg eller i 19" rack. Skruv för montering på vägg eller i rack ingår ej.

## **Tillvalskort till strömförsörjning**

#### Tabell 2. Tillvalskort till strömförsörjning

| Strömförsörjning         | Tillvalskort monterade vid leverans | Ytterligare kort som kan monteras       |
|--------------------------|-------------------------------------|-----------------------------------------|
| BT-5 MEDIUM              | -                                   | 1 st BT-Fuse 5.                         |
| BT-5 FLX Small COM Gen2  | -                                   | 1 st. BT-Fuse 5 eller 1 st. BT-Fuse 10. |
| BT-10 FLX Small COM Gen2 | -                                   | 1 st. BT-Fuse 5 eller 1 st. BT-Fuse 10. |
| BT-5 FLX Medium COM Gen2 | -                                   | 2 st. BT-Fuse 5 eller 2 st. BT-Fuse 10. |
| BT-5 FLX Large COM Gen2  | 1 st. BT-Fuse 5.                    | 1 st. BT-Fuse 5 eller 1 st. BT-Fuse 10. |
| BT-10 FLX Large COM Gen2 | 1 st. BT-Fuse 5.                    | 1 st. BT-Fuse 5 eller 1 st. BT-Fuse 10. |
| BT-15 FLX Large COM Gen2 | 1 st. BT-Fuse 10.                   | 1 st. BT-Fuse 5 eller 1 st. BT-Fuse 10. |
| BT-25 FLX Large COM Gen2 | 2 st. BT-Fuse 10.                   | -                                       |

## **Batterier - placering och inkoppling**

### **Anslut batterisäkring / bladsäkring**

![](_page_8_Picture_8.jpeg)

Figur 2. Säkringshållare med bladsäkring kopplas på + och minus på batterier

## **Schema - Inkoppling av batterier, 24 V**

Batterikablage är monterat på moderkortet vid leverans. Bilder nedan visar endast hur kablage skall kopplas.

- 1. Placera batterierna i skåpet med batteripolerna utåt, mot skåpluckan.
- <span id="page-9-0"></span>2. Anslut batterikablaget till batteriet. Röd kabel på plus och svart kabel på minus.
- Bryt, om möjligt, nätspänning vid inkoppling och batteribyte.

![](_page_9_Figure_3.jpeg)

Anslut batterikablage på rätt poler. Vid felkoppling kan utrustning skadas.

#### Figur 3. Kopplingsschema för batterier i batteribackup

## **PRO3 moderkort**

### **Moderkort - beskrivning**

![](_page_9_Picture_8.jpeg)

Moderkortet styr enheten och fördelar effekt. Se tekniska data för mer information.

### Figur 4. PRO3

| Nr      | På kretskort | Förklaring                                                         |
|---------|--------------|--------------------------------------------------------------------|
| 1       | J24          | Styrning till nätaggregat.                                         |
| 2       | J5           | 1=Oprio 2=externt larm.                                            |
| 3       | JU1          | Indikeringsdiod.                                                   |
| 4       | JU7          | Används ej.                                                        |
| 5       | J11          | Resetjumper, används vid batteribyte.                              |
| 6       | JU6          | Anslutning för reläkort / kommunikation / uppdatering av firmware. |
| 7       | J29          | Anslutning till fläkt.                                             |
| 8       | J101         | Anslutning till sabotagekontakt.                                   |
| 9       | J17          | Anslutning sabotagekontakt från batteribox.                        |
| 10      | J35          | Används ej.                                                        |
| 11      | J14          | Ingång larm från extern batterisäkring, från batteribox.           |
| 12 & 13 | J10 & J100   | Larm från externt tillvalskort.                                    |
| 14      | D18, D19     | Lysdioder visar status för kommunikation (RS-485).                 |
| 15      | S3           | Dip-switch                                                         |
| 16      | P2:1-4       | Lastutgångar                                                       |
| 17      | P3:1-3       | Anslutning kommunikation, RS-485.                                  |
| 18      | P1:1-3       | Anslutning till elnät.                                             |

#### <span id="page-10-0"></span>Tabell 3. Kretskortsöversikt, förklaring

#### **Säkringar**

#### Tabell 4. Säkringar på PRO3

| Säkring | Typ       | Förklaring                 |  |
|---------|-----------|----------------------------|--|
| F1      | T2,5A     | Elnätssäkring              |  |
| F3      | T16A      | Lastsäkring 1 - (för P2:2) |  |
| F4      | T16A      | Batterisäkring             |  |
| F5      | T3A-T10A* | Lastsäkring 1+ (för P2:1)  |  |
| F7      | T3A-T10A* | Lastsäkring 2 + (för P2:3) |  |
|         |           |                            |  |

*Säkringens storlek beror på batteribackupens strömuttag, (A).

![](_page_10_Picture_7.jpeg)

#### **VARNING FÖR BYTE AV SÄKRINGAR (A)**

Skaderisk föreligger om säkring byts till en större än vad enheten levereras med. Säkringens funktion är att skydda ansluten last och dess lastkablage mot skada och brand. Det går inte att byta säkring till en större för att öka strömuttag.

#### **Elnätsanslutning**

#### **Anslut elnät till moderkort med plint**

För elnätskablage genom kabelgenomföringen på skåpet.

Säkra F och N med buntband.

Elnätskablage skall hållas åtskilt annat kablage för att undvika EMC-störningar.

<span id="page-11-0"></span>![](_page_11_Figure_1.jpeg)

Anslut elnätskablage på plint innan den sätts tillbaka på moderkort. Säkra F och N med buntband.

#### Figur 5. Anslut elnät på moderkort

#### Tabell 5. Anslutningar elnät

| Bokstav | Förklaring |
|---------|------------|
| F       | Fas        |
| N       | Noll       |
| PE      | Skyddsjord |

![](_page_11_Picture_6.jpeg)

#### **ANSLUTNING ELNÄT 230 V AC PÅ KRETSKORT**

Kontrollera så att markeringen på kretskortet stämmer överens med kabelordningen på plinten.

#### **Anslut last**

![](_page_11_Picture_10.jpeg)

#### **MAXSTRÖM**

Maxström får ej överskridas. Maxström står angiven på [märkskylt](https://milleteknik.zendesk.com/hc/sv/articles/5785143875090-CE-märkning-märkskylt) på enheten.

![](_page_11_Picture_13.jpeg)

#### **LASTUTGÅNGAR VID SSF CERTIFIKAT**

För att certifikat skall upprätthållas får endast en lastutgång användas.

Sitter ett eller flera anslutningskort för att utöka antalet lastutgångar eller skapa lastselektivitet skall last anslutas där och inte på huvudkortet.

#### Tabell 6. Lastanslutningar

| Nummer på kretskort | Förklaring              |
|---------------------|-------------------------|
| P2:1                | Anslutning för last 1 + |
| P2:2                | Anslutning för last 1 - |
| P2:3                | Anslutning för last 2 + |
| P2:4                | Anslutning för last 2 - |

### <span id="page-12-0"></span>**Dip-switch 1-8**

Dip-Switch har flera olika konfigureringsläge:

#### Tabell 7. Dip-switch 1-8

| Dip-switch  | I nätdrift eller batteridrift                             | Kommentar                                    |
|-------------|-----------------------------------------------------------|----------------------------------------------|
| 1           | Adressinställning för extern kommunikation.               | -                                            |
| 2           | Adressinställning för extern kommunikation                | -                                            |
| 3           | Adressinställning för extern kommunikation                | -                                            |
| 4           | Adressinställning för extern kommunikation                | -                                            |
| 5           | Ställer larm för nätavbrottsfördröjning                   | Finns från mjukvara v1.5                     |
| 6           | Ställer larm för nätavbrottsfördröjning                   | Finns från mjukvara v 1.5                    |
| 7           | Ställer larmgräns för låg batterispänning i batteridrift. | Finns från mjukvara v 1.5                    |
| 8           | Stänger av eller sätter på lysdiod.                       | Kommande funktion genom mjukvaru-uppdatering |
| 8 i sekvens | Utför batteritest                                         |                                              |

### **Adressinställning för extern kommunikation (Dip-switch 1-4)**

Dip-Switch S1: 1-4 ställer adressering.

#### Tabell 8. Adressering Dip-Switch 1-4

|           | Dip: 1 | Dip: 2 | Dip: 3 | Dip:4 |
|-----------|--------|--------|--------|-------|
| Adress 1  | ON     | OFF    | OFF    | OFF   |
| Adress 2  | OFF    | ON     | OFF    | OFF   |
| Adress 3  | ON     | ON     | OFF    | OFF   |
| Adress 4  | OFF    | OFF    | ON     | OFF   |
| Adress 5  | ON     | OFF    | ON     | OFF   |
| Adress 6  | OFF    | ON     | ON     | OFF   |
| Adress 7  | ON     | ON     | ON     | OFF   |
| Adress 8  | OFF    | OFF    | OFF    | ON    |
| Adress 9  | ON     | OFF    | OFF    | ON    |
| Adress 10 | OFF    | ON     | OFF    | ON    |
| Adress 11 | ON     | ON     | OFF    | ON    |
| Adress 12 | OFF    | OFF    | ON     | ON    |
| Adress 13 | ON     | OFF    | ON     | ON    |
| Adress 14 | OFF    | ON     | ON     | ON    |
| Adress 15 | ON     | ON     | ON     | ON    |

### **Nätavbrottsfördröjning (dip 5-6)**

Det är möjligt att flytta tiden för när larm för nätavbrott skall ges. Använd matrisen för att ställa larmet.

#### Tabell 9. Nätavbrottsfördröjning

| Larm för nätavbrott ges efter: | Dip 5 | Dip 6 |
|--------------------------------|-------|-------|
| 3 sekunder                     | OFF   | OFF   |
| 30 minuter                     | OFF   | ON    |
| 60 minuter                     | ON    | OFF   |
| 240 minuter (4 timmar)         | ON    | ON    |

### <span id="page-13-0"></span>**Låg batterispänning (dip 7)**

Dip: 7 har samma funktion oavsett om enheten är i nät- eller batteridrift eller om sabotagebrytaren hålls inne.

#### Tabell 10. Låg batterispänning

| Larm för låg batterispänning ges vid | Dip 7 |
|--------------------------------------|-------|
| 22,8 V*                              | ON    |
| 24 V                                 | OFF   |
| *25% av batterikapacitet kvarstår.   |       |

### **Lysdiod (dip 8)**

Lysdiod/batteritest tänds alltid när luckan är öppen.

Dip-switch 8=ON släcker lysdiod.

Dip-switch 8=OFF tänder lysdiod.

![](_page_13_Picture_9.jpeg)

### **OBS!**

För certifierade enheter:

För att uppfylla SSF-1014 upp till larmklass 4 skall lysdiod på dörren vara släckt (Dip-switch 8 till ON).

### **Batteritest (dip 8)**

För att göra ett batteritest behöver dip 8 byta läge och fem sekunder behöver gå innan test initieras.

- Om dip 8 i ursprungsläge står på OFF slå då dip 8 till: ON (vänta 5 sekunder) och slå sedan tillbaka till OFF.
- Om dip 8 i ursprungsläge står på ON slå då dip 8 till: OFF (vänta 5 sekunder) och slå sedan tillbaka till ON.

Detta aktiverar batteritest efter 3-8 sekunder. Batteritestet pågår i ca 6 sekunder och då blinkar lysdioden snabbt gult. Larm för åldrat batteri kan indikeras under tiden batteritest utförs.

Ställ tillbaka dip 8 först när testet har slutförts.

#### **Omstart för att bekräfta ändringar i adress, batteri- och larminställningar mot överordnat system**

Efter det att dip-switch har ställts för olika parametrar behöver enhetens mjukvara startas om. Detta för att de nya inställningarna skall läsas in och träda i kraft.

![](_page_13_Picture_21.jpeg)

#### **VIKTIGT**

Omstart enligt denna procedur bryter ej utspänningen.

<span id="page-14-0"></span>Omstart av enhetens mjukvara görs genom att bygla J11 (PRO3)

![](_page_14_Picture_2.jpeg)

**VIKTIGT**

Omstart måste göras varje gång en ändring görs i enheten.

#### **Återställning av data efter batteribyte - PRO3**

Efter batteribyte behöver enheten mäta in nya batteriers kapacitet och rensa tidigare inställd batterikapacitet. Larm rensar men statistik behålls i minnet.

- Sätt i jumper på J11 och tag bort jumper på J11
Efter att ha gjort steget är batterikapaciteten rensad i kortets minne och är redo att läsa in den nya batterikapaciteten.

Denna procedur behöver göras varje gång batterier byts eller vid anslutning av batteribox.

![](_page_14_Picture_10.jpeg)

![](_page_14_Picture_11.jpeg)

**NOTERING VID UPPSTART MED KORTSLUTNA BATTERIER**

Peakström vid uppstart med kortslutna batterier: Upp till 30 A p-p under 200 ms. Följ alltid uppstartsproceduren.

## **Kortbeskrivning - I2C Relay Card**

Larmkort med kommunikation över I2C.

Kortet kopplas in på 10-polig header (6) på PRO3-kortet.

<span id="page-15-0"></span>![](_page_15_Picture_1.jpeg)

| Nr      | På kretskort                                                   | Förklaring                 |  |
|---------|----------------------------------------------------------------|----------------------------|--|
| 2C<br>I |                                                                |                            |  |
| 1       | P5:9                                                           | SDA                        |  |
| 2       | P5:8                                                           | SCL                        |  |
| 3       | P5:7                                                           | System-minus               |  |
| 4       | JU5                                                            | Anslutning till PRO3-kort. |  |
| X       | För intern programmering. Koppla inte in något på denna plint. |                            |  |

## **Busskommunikation - inkoppling till UC-50 Gen2**

Anslutning till UC-50 Gen2 görs enligt skiss.

![](_page_16_Figure_1.jpeg)

Bilden visar anslutning från batteribackup till UC-50 Gen2.

### Figur 6. Anslutning till UC-50 Gen2

| Nr | På kretskort i UC-50 Gen2 | På kretskort i ström<br>försörjning | Färg på kabel | Förklaring                                                      |
|----|---------------------------|-------------------------------------|---------------|-----------------------------------------------------------------|
| 1  | SDA, P6:42                | P5:9                                | Orange        | SDA/DATA                                                        |
| 2  | SCL, P6:41                | P5:8                                | Brun          | SCL/CLOCK                                                       |
| 3  | 2C 0V, P6:40<br>I         | P5:7                                | Svart         | V-Ground / minus                                                |
| 4  | -                         | -                                   | -             | Ej partvinnad kabel. Max tre meter.                             |
| 5  | -                         | -                                   | -             | Max avstånd mellan strömförsörjning och UC-50 Gen2: 3<br>meter. |
| 6  | DC+ IN, P4:13             | P2:3                                | Röd           | 24 V strömmatning.                                              |
| 7  | DC- IN, P4:14             | P2:4                                | Svart         | 24 V strömmatning.                                              |

![](_page_16_Picture_5.jpeg)

#### **VIKTIGT**

Kabellängd max 3 meter. Kabel skall inte vara partvinnad.

### <span id="page-17-0"></span>**Bygling av UC-50 Gen2**

Vid installation i störkänsliga miljöer kan kommunikationsavbrott förekomma. Genom att bygla till 0 V på UC-50 Gen2 kan störningar undvikas.

![](_page_17_Picture_3.jpeg)

#### **VIKTIGT**

Byglingen skall sitta: i2C, P6 till DC- IN, P6:12.

![](_page_17_Picture_6.jpeg)

## <span id="page-18-0"></span>**Flera enheter till ett överordnat system**

För att ansluta flera enheter till ett överordnat system skall last-minus mellan flera batteribackuper kopplas samman.

![](_page_18_Figure_3.jpeg)

## **Driftsättning - hur enheten skall startas**

- 1. Koppla in batterier.
- 2. Anslut / slå till säkringar.
- 3. Koppla in last, larm och ev. andra anslutningar.
- 4. Skruva fast elnätkabel i plint och sätt fast plint på moderkort.
- 5. Slå till nätspänning.

Enheten fungerar normalt då indikeringsdiod på skåpluckans utsida lyser med fast grönt sken. Se frontpanel / skåplucka, för övriga statusindikationer.

Det kan ta upp till 72 timmar innan batterier är fullt laddade.

## **Driftsättning vid inkoppling till UC-50**

Driftsätt i denna ordning vid samtida inkoppling till UC-50

- <span id="page-19-0"></span>1. Inkoppling och spänningssättning av batteridel.
- 2. Spänningssättning av elnät.
- 3. Koppla in larmsystemet enligt [inkoppling UC50 \[16\]](#page-15-0).

Enheten fungerar normalt då lysdiod på skåpluckans utsida lyser med fast grönt sken. Se frontpanel för övriga statusindikationer.

### **Systemtest**

Testa inkopplad enhet genom att göra ett systemtest efter [driftsättning \[19\]](#page-18-0).

- Slå till inkommande nätspänning.
- Lysdiod på skåpluckans utsida lyser med fast grönt sken. Bryt nätspänning för att kontrollera att enheten fungerar i batteridrift och larmar.
- Lysdiod på skåpluckan blinkar, se panel för larmtyp.
- Slå till inkommande nätspänning, lysdiod, på skåpluckans utsida lyser med fast grönt sken. Normaldrift.

### **Återställning**

Återställ enheten genom att göra enheten helt spänningslös.

Koppla bort batterikablage samt nätspänning och återanslut efter 5 sekunder.

## **Larm som visas på skåplucka / indikeringsdiod**

I normalläge visar indikeringsdioden ett fast grönt sken.

|        | BT-COM Gen2<br>Power supply AC/DC<br>Battery backup                                            |  |
|--------|------------------------------------------------------------------------------------------------|--|
| Green  | Normal operation<br>Tamper alarm (sabotage)<br>Mains failure                                   |  |
| Amber  | Low battery<br>Aged batteries<br>Disconnected batteries / battery cell shortage                |  |
| Red    | Over or under voltage / charger fault<br>Low system voltage<br>Blown load / battery fuse blown |  |
| ે ઉમ્પ | Deep discharge protection (system shutdown)                                                    |  |

| Indikeringsdioden visar | Förklaring                                        |
|-------------------------|---------------------------------------------------|
| Fast grönt sken         | Normaldrift.                                      |
| Långsamma gröna blink   | Sabotagelarm.                                     |
| Snabba gröna blink      | Nätavbrottslarm.                                  |
| Fast gult sken          | Låg batterispänning.                              |
| Långsamma gula blink    | Åldrade batterier.                                |
| Snabba gula blink       | Bortkopplade batterier / batterikortslutning.     |
| Fast rött sken          | Överspänning eller underspänning eller laddarfel. |

<span id="page-20-0"></span>

| Indikeringsdioden visar | Förklaring                                                  |
|-------------------------|-------------------------------------------------------------|
| Långsamma röda blink    | Låg systemspänning.                                         |
| Snabba röda blink       | Lastsäkring har löst ut / batterisäkring har löst ut.       |
| Svart / släckt          | Djupurladdningsskydd är aktiverat. (Enheten har stängt av.) |

Vid driftsatt system: Är indikeringsdioden släckt har djupurladdningsskydd trätt i kraft.

## **Justering av sabotagekontakt**

![](_page_20_Picture_4.jpeg)

Sabotagekontaktens hävarm skall vid stängd skåpdörr vara i slutet läge (stängd). Går larm ("tamper alarm" / larm till undercentral) kan hävarmen behöva justeras.

Hävarmen justeras genom följande steg:

- 1. Nyp åt med en plattång mitt på hävarmen.
- 2. Justera hävarmen försiktigt åt önskat håll (upp/ner).
- 3. Kontrollera genom att stänga dörren. Ett klick hörs när kontakten sluts.

![](_page_20_Picture_10.jpeg)

**OBS!**

Sabotagekontakten skall inte larma vid stängd och låst dörr.

## **Underhåll**

Systemet, med undantag för fläkt och batterier, är underhållsfritt vid installation i inomhusmiljö.

Kontrollera fläkten årligen. Fläkten skall rotera problemfritt utan missljud. Rengör fläkten ifrån damm och smuts. Fläkten skall bytas om den inte roterar problemfritt eller är så smutsig att den inte kan rengöras helt. Om fläkten inte fungera bra kommer luftflödet i enheten att hindras vilket leder till att värmen ökar

<span id="page-21-0"></span>i kapslingen, vilket kan leda till att batterikapaciteten försämras och att bytesintervall på batterier avsevärt förkortas.

## **Batterier**

Batterier alstrar elektricitet genom en kemisk process och det sker därmed en naturlig degradering av kapacitet. Den största faktorn för batteriers livslängd är temperatur. Ju högre temperatur desto kortare livslängd på batterier. Tillverkningsdatum som är präglat på batteriet och livslängden (som batteritillverkaren anger). En ideal temperatur är 20 °C både i drift och i förvaring. Högre omgivningstemperatur försämrar kraftigt livslängden. Således varierar faktisk livslängd när det används. Batterier bör bytas efter halva angiven (från batteritillverkaren) livslängd för säker drift. Batterier inköpta via batteribackupens tillverkare har en livslängd (från batteritillverkaren) på mellan 10-12 år med rekommenderat byte efter 5-6 år.

![](_page_21_Figure_4.jpeg)

## **Batteribyte**

- Bryt, om möjligt, nätspänning vid batteribyte.
- Koppla bort batterikablar. Notera hur batterikablar är monterade innan de avlägsnas.
- Tag bort batterisäkring mellan batterier.
- Sätt in fast de nya batterierna.
- Anslut batterikablarna på samma sätt som tidigare.
- Sätt fast batterisäkring mellan batterier.
- Slå till nätspänning. Eventuellt kan indikeringsdioden lysa för låg batterispänning / nätbortfall tills batterier är laddade. Det kan ta upp till 72 timmar innan batterierna är fulladdade.
- Testa systemet genom att kortvarigt koppla bort nätspänning, (= lasten skall drivas vidare av batterierna), och därefter slå till nätspänningen igen.

Har du bytt storlek på batteri? Glöm då inte att ställa om batterikapacitet, se Inställning av batterikapacitet, Dip-switch 5-7

## **Batteriåtervinning**

Alla batterier skall återvinnas. Återlämna till tillverkare eller lämna till återvinningsstation.

![](_page_21_Picture_17.jpeg)

## <span id="page-22-0"></span>**Produktens livslängd, miljöpåverkan och återvinning**

Produkten är designad och konstruerad för lång livslängd vilket minskar miljöpåverkan. Produktens livslängd (förutom slitagedelar) är beroende på, bland annat miljöfaktorer, främst omgivningstemperatur, oförutsedd belastning på komponenter som blixtnedslag, yttre åverkan, handhavandefel, med flera. Produkter återvinns genom att lämnas till närmaste återvinningsstation eller sändas åter till tillverkare. Kontakta din distributör för mer information. Kostnader som uppkommer i samband med återvinning ersätts ej.

![](_page_22_Picture_3.jpeg)

## **Bilaga: Montera I2C-kort**

![](_page_22_Picture_5.jpeg)

Kortet trycks på plats på moderkortet i strömförsörjningen.

Strömförsörjningen kan vara driftsatt.

## **Strömförsörjning - produktblad**

**SSF1014 certifierad batteribackup med kommunikation**

![](_page_22_Picture_10.jpeg)

<span id="page-23-0"></span>

| Namn                                   | Artikelnummer | E-nummer  |
|----------------------------------------|---------------|-----------|
| BT-5 FLX SMALL COM t.o.m 20231015      | 28160120      | 52 574 54 |
| BT-5 FLX Small COM Gen2 från 20231016  | 28160121      | 52 576 96 |
| BT-10 FLX SMALL COM                    | 28160122      | 52 574 55 |
| BT-10 FLX Small COM Gen2 från 20240101 | 28160123      | 52 576 97 |

### **Om BT FLX COM Gen2**

BT FLX COM Gen2 används huvudsakligen i säkerhetssystem där SSF 1014 godkänd batteribackup krävs eller där kraven är högre. Krav som bättre flexibilitet, fler larmfunktioner, längre reservdrifttider eller där batteribackupen behöver hantera högre laster.

- SSF1014, Larmklass 1-4 godkända batteribackuper / strömförsörjning.
- Kontrollerad laddnings-funktion.
- Kvalificerat batterikapacitetstest.
- Kan kompletteras med flera olika tillvalskort.
- Monteras på vägg eller i 19" rack.
- Flexibel batterikapacitet med batteriboxar utökar reservdrifttiden.

#### **Flexibilitet**

Strömförsörjning BT-5 FLX Small COM Gen 2 och BT-10 FLX Small COM Gen 2 kan utökas med en extra batteribox: Batteribox 24V FLX S med plats för fyra 14 Ah batterier. Strömförsörjning BT-5 FLX Medium COM Gen 2, BT-5 FLX Large COM Gen 2, BT-10 FLX Large COM Gen 2, BT-15 FLX Large COM Gen 2 och BT-25 FLX Large COM Gen 2 kan utökas med 1-4 extra batteriboxar*. Strömförsörjning Medium och Strömförsörjning Large kan även utökas med batterihyllor i 19" rack*. Batteriboxen Batteribox 24V FLX Mhar plats för två 45 Ah batterier. Batterihyllor har plats för två 45 Ah batterier (Medium) och två 150 Ah batterier (Large) på varje batterihylla*. *Adapter krävs.

#### **Fast installation**

Produkten är avsedd för fast installation. Installation skall utföras av behörig installatör.

### **Användningsområde**

BT FLX COM Gen2 används mest till: Passersystem, inbrottslarm, (integrerade säkerhetssystem), i offentlig miljö som skolor, kontor och kommersiella fastigheter.

![](_page_23_Figure_17.jpeg)

Enheten uppfyller kraven för installation i anläggningar som skall vara SSF 1014 godkända. SSF 1014 certifikat är endast giltigt vid certifiering tillsammans med överordnat system.

![](_page_23_Picture_19.jpeg)

#### **VIKTIGT**

För att SSF 1014 certifikat skall vara giltigt får endast en (1) lastutgång användas.

### <span id="page-24-0"></span>**Regelverk och certifieringar**

#### **Standarder som produkt(er) uppfyller och är godkänd för**

#### Tabell 11. SBF

SBF 110:8

#### Tabell 12. SSF

SSF1014 Larmklass 1-4 (inbrottslam).

### **Krav som produkten uppfyller**

| EMC:     | EMC Direktivet 2014/30EU           |  |
|----------|------------------------------------|--|
| El:      | Lågspänningsdirektivet: 2014/35/EU |  |
| CE:      | CE direktivet enligt:765/2008      |  |
| Emission | EN55032 (CISPR32) Class B          |  |

## **Strömuttag per produkt**

| Artikelnamn:               | Batterikapacitet:    | Möjlig medellast enligt LK1/LK2: | Möjlig medellast enligt LK3/LK4: |
|----------------------------|----------------------|----------------------------------|----------------------------------|
| BT-5 FLX Small COM Gen2    | 2 st. 14 Ah          | 1,1 A                            | 0,45 A                           |
| BT-5 FLX Small COM Gen2 +  | 6 st. 14 Ah (42 Ah)  | 3,4 A                            | 1,4 A                            |
| Batteribox 24V FLX S       |                      |                                  |                                  |
| BT-10 FLX Small COM Gen2   | 2 st. 14 Ah          | 1,1 A                            | 0,45 A                           |
| BT-10 FLX Small COM Gen2 + | 10 st. 14 Ah (70 Ah) | 5,7 A                            | 2,3 A                            |
| 2 st. Batteribox 24V FLX S |                      |                                  |                                  |

## **Kretskort - Tekniska data**

### **Tekniska data, moderkort: PRO 3**

| Info                                                  | Förklaring                                                                                                                                                                                                                                                                                                                                                                          |  |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Kortnamn:                                             | PRO 3.                                                                                                                                                                                                                                                                                                                                                                              |  |
| Produktbeskrivning                                    | Huvudkort i batteribackup med avancerade funktioner och kommunikation mot överordnande system.                                                                                                                                                                                                                                                                                      |  |
| Egenförbrukning, med reläkort                         | Mindre än 120 mA. Alla reläer på externt larmkort dragna i normalläge.                                                                                                                                                                                                                                                                                                              |  |
| Omkopplingstid från nätspän<br>ning till batteridrift | När batterier är i vilocykel: <5 mikrosekunder. När batterier är i laddningscykel: 0 (ingen). Batterier vilar i 20<br>dygns cykler varefter en laddningscykel tar vid och laddar batterierna i 72 h. Sker nätavbrott när batterier är i<br>vilocykel kopplas batterier in på <5 mikrosekunder. Sker nätavbrott när batterier är i laddningscykel existerar ingen<br>omkopplingstid. |  |
| Inkommande elnät                                      | 230 V AC -240 V AC, 47-63 Hz.                                                                                                                                                                                                                                                                                                                                                       |  |
| Säkring på elnät                                      | Se tabell: Säkringar.                                                                                                                                                                                                                                                                                                                                                               |  |
| Indikering                                            | Lysdiod på kretskort/skåpslucka.                                                                                                                                                                                                                                                                                                                                                    |  |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                     |  |

#### <span id="page-25-0"></span>**Larm**

Larm som visas på indikeringsdiod på skåpets framsida.

- Cellfel i batteri eller ej anslutet batteri.
- Laddarfel, underspänning.
- Laddarfel, överspänning.
- Låg systemspänning, systemspänning under 24,0 V i nätdrift.
- Låg batterispänning, under 24,0 V DC vid nätavbrott.
- Nätavbrottslarm.
- Sabotagebrytare.
- Säkringsfel.
- Åldrat batteri

Utökande larmfunktioner går att få över kommunikation eller med larmkort.

#### Tabell 13. Säkringar

| Säkringar                                   | Typ                   |
|---------------------------------------------|-----------------------|
| 5 A                                         | T5A                   |
| 10 A                                        | T10A                  |
| Elnätssäkring på 24 V enheter upp till 15 A | T2,5AH250V. Keramisk. |

#### Tabell 14. Skydd

|                      | Info | Förklaring |
|----------------------|------|------------|
| Djupurladdningsskydd | Ja.  |            |
| Överspänningsskydd   | Ja   |            |
| Övertemperatursskydd | Ja   |            |
| Kortslutningskyddad  | Ja   |            |

### **Tekniska data, PRO3 I2C-kort**

| Info                          | Förklaring                                                                                                                                                                                                                                                                            |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kortnamn:                     | PRO3 I2C-kort                                                                                                                                                                                                                                                                         |
| Version:                      | 1.6                                                                                                                                                                                                                                                                                   |
| Produktbeskrivning            | Kort som gör det möjligt att kommunicera med UC via i2C.                                                                                                                                                                                                                              |
| Rekommenderad miljö           | Inomhus, klass 1. Omgivningstemperatur: +5°C – 40°C.                                                                                                                                                                                                                                  |
| Skyddsklass                   | IPX0                                                                                                                                                                                                                                                                                  |
| Rekommenderad montering       | Batteribackup med PRO3-moderkort.                                                                                                                                                                                                                                                     |
| Ingångsspänning               | 27,3 VDC                                                                                                                                                                                                                                                                              |
| Egenförbrukning               | 10 mA                                                                                                                                                                                                                                                                                 |
| Larm via                      | 2C<br>I                                                                                                                                                                                                                                                                               |
| Antal larmutgångar            | 1 st, I2C. Tillval 2 relä, kan endast specialbeställas.                                                                                                                                                                                                                               |
| Produkten möter kraven enligt | CE direktivet enligt: 765/2008, EMC Direktiv 2014/30EU, Emission: EN61000-6-:2001, EN55022:1998:-A1:2000,<br>A2:2003 Klass B, EN61000-3-2:2001, Immunity: EN61000-6-2:2005, EN61000-4-2, -3, 4, -5, -6, -11. SS-EN 50<br>130-4:2011 Edition 2 & SSF1014 Larmklass 1-4 (Inbrottslarm). |

Tillverkad i Milletekniks fabrik i Partille, Sverige.

Bruksanvisning/produktblad i original: Svenska.

#### <span id="page-26-0"></span>Tabell 15. Larmöversikt

| Larmöversikt i bokstavsordning                                | Larm som kan skickas via I2C. | Indikeringsdiod på huvudkort och LED på dörr. |
|---------------------------------------------------------------|-------------------------------|-----------------------------------------------|
| Nätavbrott                                                    | X                             | X                                             |
| Säkringsfel                                                   | X                             | X                                             |
| Sabotagebrytare                                               | X                             | X                                             |
| Fläktfel                                                      | X                             | -                                             |
| Laddarfel, överspänning                                       | X                             | X                                             |
| Laddarfel, underspänning                                      | X                             | X                                             |
| Cellfel eller ej anslutet batteri                             | X                             | X                                             |
| Låg systemspänning, (systemspänning under 24,0 V i nätdrift). | X                             | X                                             |
| Låg batterispänning (<24,0 V DC) eller nätavbrott             | X                             | X                                             |
| Övertemperatur                                                | X                             | -                                             |
| Undertemperatur                                               | X                             | -                                             |
| Undertemperatur                                               | X                             | -                                             |
| Kort batteritid kvar                                          | X                             | -                                             |
| Åldrat batteri                                                | X                             | X                                             |
| Överström 80 %, dygnsmedelvärde                               | X                             | -                                             |
| Överström 100 %, minutmedelvärde                              | X                             | -                                             |
| Överström 175 %, sekundmedelvärde                             | X                             | -                                             |

### **Nätaggregat**

#### **Nätaggregat - Tekniska Data LRS-150-24**

BT-5 FLX Small COM Gen 2

| Info                                                | Förklaring                       |
|-----------------------------------------------------|----------------------------------|
| Utspänning                                          | 27,3 V                           |
| Utström:                                            | 0 A - 6,5 A                      |
| Utspänning, ripple                                  | 200 mVp-p                        |
| Överspänning                                        | 28,8 V - 33,6 V                  |
| Utspänning återuppladdning, ripple/strömbegränsning | Mindre än 0,6 Vp-p               |
| Verkningsgrad                                       | 89 %                             |
| Strömbegränsning                                    | 110 % - 140 %                    |
| Konstantspänning                                    | +/- 0,5 %                        |
| Reglernoggrannhet                                   | + / - 1,0 %                      |
| Ingångsström (230 V)                                | 1,7 A                            |
| Nätspänningsfrekvens                                | 47 Hz- 63 Hz                     |
| Nätspänning                                         | 230 V AC - 240 V AC              |
| Märkeffekt                                          | 156 W                            |
| Temperaturområde                                    | -30°C - +70°C                    |
| Luftfuktighetsområde                                | 20 % - 90 % RH icke kondenserade |
|                                                     |                                  |

Sitter i:

Nätaggregatet är anpassat och kalibrerat med batteribackupens hård-/mjukvara. Endast nätaggregat som är anpassade och kalibrerade får användas. Kontakta support vid byte av nätaggregat. Användning av nätaggregat som kommer från annan källa kan orsaka skador som inte täcks av garantin. Garanti upphävs om nätaggregat (från annan källa än support/anvisat från support) som ej är korrekt kalibrerat används.

#### <span id="page-27-0"></span>**Nätaggregat - Tekniska Data RSP-320-24**

| Sitter i:                 |
|---------------------------|
| BT-10 FLX Small COM Gen 2 |

| Info                                                | Förklaring                       |
|-----------------------------------------------------|----------------------------------|
| Utspänning                                          | 27,3 V                           |
| Utström                                             | 0 A - 13,4 A                     |
| Utspänning, ripple                                  | 150 mVp-p                        |
| Överspänning                                        | 27,6 V - 32,4 V                  |
| Utspänning återuppladdning, ripple/strömbegränsning | Mindre än 1,2 Vp-p               |
| Verkningsgrad                                       | 89 %                             |
| Strömbegränsning                                    | 105 % - 135 %                    |
| Konstantspänning                                    | +/- 0,5 %                        |
| Reglernoggrannhet                                   | +/- 1,0 %                        |
| Ingångsström (230 V)                                | 2 A                              |
| Nätspänningsfrekvens                                | 47 Hz- 63 Hz                     |
| Nätspänning                                         | 230 V AC - 240 V AC              |
| Märkeffekt                                          | 321,6 W                          |
| Temperaturområde                                    | -30°C - +70°C                    |
| Luftfuktighetsområde                                | 20 % - 90 % RH icke kondenserade |

Nätaggregatet är anpassat och kalibrerat med batteribackupens hård-/mjukvara. Endast nätaggregat som är anpassade och kalibrerade får användas. Kontakta support vid byte av nätaggregat. Användning av nätaggregat som kommer från annan källa kan orsaka skador som inte täcks av garantin. Garanti upphävs om nätaggregat (från annan källa än support/anvisat från support) som ej är korrekt kalibrerat används.

## **Tekniska data kapsling**

### **Kapslingar - Tekniska Data FLX S**

| Info                      | Förklaring                                                       |
|---------------------------|------------------------------------------------------------------|
| Namn                      | FLX S                                                            |
| Kapslingsklass            | IP 32                                                            |
| Mått                      | Höjd: 222 mm, bred 437 mm, djup 145 mm                           |
| Höjdenheter               | 5 HE                                                             |
| Montering                 | Vägg eller 19" rack                                              |
| Omgivningstemperatur      | +5 °C - +40 °C. För bästa batteri-livslängd: +15 °C till +25 °C. |
| Omgivning                 | Miljöklass 1, inomhus. 20% ~ 90% relativ fuktighet               |
| Material                  | Pulverlackerad plåt                                              |
| Färg                      | Svart                                                            |
| Kabelgenomföringar, antal | 4                                                                |
| Batterier som får plats   |                                                                  |
|                           | 2 stycken 14 Ah.                                                 |
| Fläkt                     | Ja                                                               |

## **Garanti, support, tillverkningsland och ursprungsland**

#### **Garanti 5 år**

Produkten har fem års garanti, från inköpsdatum (om inget annat avtalats). Kostnadsfri support under garantitiden nås på [support@milleteknik.se](mailto:support@milleteknik.se) eller telefon, 031-34 00 230. Ersättning för res- och eller arbetstid <span id="page-28-0"></span>i samband med lokalisering av fel, installerande av reparerad eller utbytt vara ingår ej i garantin. Kontakta Milleteknik för mer information. Milleteknik ger support under produktens livslängd, dock som längst 10 år efter inköpsdatum. Byte till likvärdig produkt kan förekomma om Milleteknik bedömer att reparation inte är möjlig. Kostnader för support tillkommer efter det att garantitiden har gått ut.

### **Support**

Behöver du hjälp med installation eller inkoppling?

Du hittar svar på många frågor på: [www.milleteknik.se/support](https://www.milleteknik.se/support/)

Telefon: 031- 340 02 30, e-post: [support@milleteknik.se.](mailto:support@milleteknik.se)

Support har öppet: måndag-torsdag 08:00-16:00, fredagar 08:00-15:00. Stängt 11:30-13:15.

#### **Reservdelar**

Kontakta support för frågor om reservdelar.

#### **Support efter garantitiden**

Milleteknik ger support under produktens livslängd, dock som längst 10 år efter inköpsdatum. Byte till likvärdig produkt kan förekomma om tillverkare bedömer att reparation inte är möjlig. Kostnader för support tillkommer efter det att garantitiden har gått ut.

#### **Tillverkningsland**

Sverige

#### **Tillverkare**

Designad och producerad av Milleteknik AB

## **Batterier**

#### **Batterier ingår ej**

Batterier säljs separat.

#### **Batterikombinationer BT FLX Small COM Gen2 med Battery box 24V FLX S (14 Ah batterier)**

| Batterikapacitet (Ah) | Batterityp | Antal batterier | Batterier i enhet |
|-----------------------|------------|-----------------|-------------------|
| 14 Ah                 | 14 Ah      | 2 st.           | 2 i batteribackup |
| 42 Ah                 | 14 Ah      | 6 st.           | 2 i batteribackup |
|                       |            |                 | 4 i batteribox 1  |
| 70 Ah                 | 14 Ah      | 10 st.          | 2 i Batteribackup |
|                       |            |                 | 4 i batteribox 1  |
|                       |            |                 | 4 i batteribox 2  |

#### <span id="page-29-0"></span>**14 Ah, 12 V AGM-batteri**

| Passar i                              | Antal batterier |       |
|---------------------------------------|-----------------|-------|
| BT-5 FLX Small COM Gen 2              | 2               |       |
| BT-10 FLX Small COM Gen 2             | 2               |       |
|                                       |                 |       |
| Batterityp                            | V               | Ah    |
| Underhållsfritt AGM, blysyra-batteri. | 12 V            | 14 Ah |

#### Tabell 16. 10+ Design life* batteri

| Artikelnummer  | E-nummer | Artikelnamn                               | Terminal            | Mått. Höjd, bredd,<br>djup | Vikt per<br>styck | Fabrikat |
|----------------|----------|-------------------------------------------|---------------------|----------------------------|-------------------|----------|
| MT113-12V14-01 | 5230537  | UPLUS 12V 14Ah 10+<br>Design life batteri | Flatstift 6,3<br>mm | 151x98x101 mm              | 4,2 kg            | UPLUS    |

*Design life är hållbarheten i år för ej använt batteri. Omgivningsfaktorer som värme och last påverkar livslängden. Batterier som har en hållbarhet (+10 Design Life) på 10+ år brukar behöva bytas efter 5-6 år.

## **Anslutning av batteribox**

## **Montering Battery box 24V FLX S till batteribackup i FLX Skapsling**

Batteriboxen monteras på vägg eller i 19" rack under batteribackup.

Kabelgenomföringar finns i kapslingens överkant och i mitten på dess baksida.

![](_page_29_Figure_10.jpeg)

### <span id="page-30-0"></span>**Inkoppling batteribox Batteribox 24V FLX S med batteribackup BT FLX COM Gen2**

![](_page_30_Figure_2.jpeg)

Bilden visar en batteribackup med en batteribox.

Bilden ger även en översikt över kopplingar för batterikablar och batterisäkringar.

| Batterikablage | Förklaring                                |
|----------------|-------------------------------------------|
| B1+            | Kopplas till säkring                      |
| B1-            | Kabel från moderkort kopplas till batteri |
| B2+            | Kabel från moderkort kopplas till batteri |
| B2-            | Kopplas till säkring                      |
| B3+            | Kopplas till säkring                      |
| B3-            | Kopplas till B6-                          |
| B4+            | Kopplas B5+                               |
| B4-            | Kopplas till säkring                      |
| B5+            | Se B4+                                    |
| B5-            | Kopplas till säkring                      |
| B6+            | Kopplas till säkring                      |
| B6-            | Se B3-                                    |

#### <span id="page-31-0"></span>Tabell 17. Inkoppling

| Nummer | Förklaring                                                 |
|--------|------------------------------------------------------------|
| 1      | Kablage från batteribackup på dubbelstift i batteribackup. |

### **Sabotagekontakt vid extra batteribox**

Har en eller flera batteriboxar kopplats till enheten skall sabotagekontakterna seriekopplas för att larm från alla enheter skall ges. Det är viktigt att seriekopplingen har slutning vid den sista sabotagekontakten. Seriekopplingen skall börja i enheten och vända tillbaka i den sista batteriboxen.

## **Adress och kontaktuppgifter**

RCO Security AB Box 3130 169 03 Solna Sverige Växel: 08-546 560 00 info@rco.se www.rco.se