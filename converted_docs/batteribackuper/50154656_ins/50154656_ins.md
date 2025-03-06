![](_page_0_Picture_0.jpeg)

**INNEHÅLL**

- **1. Teknisk beskrivning.** 
	- **1.1 Allmän beskrivning**
	- **1.2 Blockschema**
	- **1.3 Beskrivning av komponenter och kontakter**
	- **1.4 Tekniska parametrar**
- **2. Installation.** 
	- **2.1 Krav**

# **2.2 Läge med lång räckvidd**

## **2.3 Installationsförfarande**

### **3. Indikation av enhetens drift**

- **3.1 LED-indikering av driftsstatus**
- **3.2 Synlig indikation av switchens drift**

**4. Drift och användning.** 

- **4.1 Överbelastning eller kortslutning av PSU-utgången (SCP på )**
- **4.2 Frånkoppling av urladdat batteri**
- **4.3 Underhåll**

**1. Teknisk beskrivning.**

# **1.1. Allmän beskrivning.**

APS64 är avsedd för oavbruten strömförsörjning av 4 IP-enheter (52 V DC-försörjning).

Systemets huvudsakliga komponenter inkluderar:

- PoE-switch med 6 portar
- 27,6 V buffertströmförsörjning med två 17 Ah / 12 V-batterier
- en omvandlare (DC/DC52230) som ökar spänningen till 52 V DC (matning till PoE-switchen)

Vid strömavbrott aktiveras omedelbart ett reservbatteri.

 Automatisk upptäckt av enheter som drivs med standarden PoE/PoE+ aktiveras vid portar 1-4 på switchen. UP LINKportarna används för anslutning till en annan nätverksenhet. Lysdioderna på frontpanelen indikerar enhetens driftsstatus (beskrivs i tabell 8).

Switchen sitter inuti ett metallhölje (färg RAL 9003) med rum för två 17 Ah/12 V-batterier. Höljet är utrustat med en mikroswitch som aktiveras om luckan öppnas (frontpanelen).

APS64 är försedd med två lysdioder på frontpanelen (röd lysdiod - indikerar en 230 V matningsspänning, grön lysdiod indikerar likspänning).

PoE-tekniken ansluter till nätverket och minskar installationskostnaderna eftersom den inte kräver en separat strömkabel till varje enhet. Metoden gör det möjligt att försörjs andra nätverksenheter.

## **1.2 Blockschema.**

![](_page_1_Figure_22.jpeg)

Bild 1. Blockschema.

### **1.3 Beskrivning av komponenter och kontakter.**

![](_page_2_Figure_1.jpeg)

#### **Tabell 1. (Se Bild. 2)**

| Komponent nr.<br>(Bild 2) | Beskrivning                                             |
|---------------------------|---------------------------------------------------------|
| [1]                       | PoE-switch                                              |
| [2]                       | Buffertenhet för switchläge                             |
| [3]                       | DC/DC52230-omvandlare                                   |
| [4]                       | Utgångsfilter                                           |
| [5]                       | Sabotageswitch (terminaler) för manipulationsskydd (NC) |
| [6]                       | Batterifack för två 17 Ah/12 V-batterier                |
| [7]                       | Strömförsörjningskontakt till PSU - L, N                |
|                           | Skyddskontakt (elektrisk chock)                         |
| [8]                       | BAT +, BAT - batteriutgång + BAT röd, - BAT svart       |

![](_page_2_Figure_4.jpeg)

## **Tabell 2. (Se bild 3)**

| Beskrivning                           |  |  |
|---------------------------------------|--|--|
| 2 st UPLINK-portar                    |  |  |
| 4 x PoE-portar (1÷ 4)                 |  |  |
| 52 V DC-uttag                         |  |  |
| Ytterligare komponenter för montering |  |  |
| Växla till läget Lång räckvidd        |  |  |
|                                       |  |  |

#### **1.4 Tekniska parametrar**

- switchens parametrar (tab.3)
- elektriska parametrar (tab.4)
- mekaniska parametrar (Tab.5)
- driftssäkerhet (tab.6)
- driftsparametrar (tab.7)

### **Tabell3. Switchens parametrar**

| Portar                  | 6 st 10/100 Mb/s-portar (4 st PoE + 2 st UP LINK) med automatisk hantering av |  |  |
|-------------------------|-------------------------------------------------------------------------------|--|--|
|                         | anslutningshastighet och MDI/MDIX Auto Cross                                  |  |  |
| PoE-strömförsörjning    | IEEE 802.3af/at (1÷4 portar), 52 V DC / 30 W i varje port *                   |  |  |
| Läge med lång räckvidd  | Lång räckvidd, VLAN                                                           |  |  |
| Protokoll, standarder   | IEEE802.3, 802.3u, 802.3x CSMA/CD, TCP/IP                                     |  |  |
| Bandbredd               | 1,6 Gbps                                                                      |  |  |
| Överföringsmetod        | Lagra-och-vidarebefordra                                                      |  |  |
| Synlig driftsindikering | Switchens strömförsörjning;                                                   |  |  |
|                         | Länk/Act;                                                                     |  |  |
|                         | PoE-status                                                                    |  |  |
|                         |                                                                               |  |  |

*Det angivna värdet på 30 W är maximal belastning per port. Total maximal belastning 120W på samtliga portar. För maximal livslängd rekommenderas en kontinuerlig belastning på maximalt 80W.

#### **Tabell 4. Elektriska parametrar**

| Nätförsörjning                                                | ~200-240 V; 50 Hz                                                   |  |
|---------------------------------------------------------------|---------------------------------------------------------------------|--|
| Strömstyrka upp till                                          | 1,4 A                                                               |  |
| Strömförsörjning                                              | 133 W                                                               |  |
| Utgångsström vid PoE-portarna (RJ45)                          | 4 st 0,6 A ΣI=2,3A max.                                             |  |
| Utgångsström vid PoE-portarna (RJ45)                          | 52 V DC                                                             |  |
| Kortslutningsskydd SCP och överbelastningsskydd OLP           | 105% ÷ 150% PSU-effekt, manuell omstart                             |  |
|                                                               | (felet kräver frånkoppling av utgångskretsen för DC)                |  |
| PSU-strömförbrukning                                          | 250 mA/27,6 V DC                                                    |  |
| Batteriets laddningsström                                     | 0,5 A max. /2 st 17 Ah (+/-5%)                                      |  |
| Batterikretsskydd SCP och retur                               | proppsäkring                                                        |  |
| polaritetsanslutning                                          |                                                                     |  |
| Djupurladdningsskydd UVP                                      | U<19 V (± 5%) – frånkoppling av anslutningsbatteri                  |  |
| Sabotageskydd:<br>- MANIPULERINGS-indikator när höljet öppnas | - mikroswitch, NC-kontakter (stängt hölje),<br>0,5 A@50 V DC (max.) |  |
|                                                               |                                                                     |  |

![](_page_3_Figure_13.jpeg)

### **Tabell 5. Mekaniska parametrar**

| Mått                | W=397, H=350, D+D1=92+8 [+/- 2mm]<br>W1=402, H1=355 [+/- 2mm]         |
|---------------------|-----------------------------------------------------------------------|
| Batterifackets mått | 370 x 180 x 80mm (WxHxD) max                                          |
| Brutto- / nettovikt | 4,5 / 4,8 kg                                                          |
| Hölje               | Stålplatta, DC01 1,0mm färg vit RAL 9003                              |
| Förslutning         | Spårskruv x 2 (fram), (låsaggregat möjligt)                           |
| Anslutningar        | Strömförsörjning till enheterna: RJ45-uttag                           |
|                     | Ingång 230 V: Φ 0,63-2,50 (AWG 22-10)                                 |
|                     | Batteriutgång BAT: 6,3F-2,5                                           |
|                     | MANIPULERINGS-utgång: ledningar                                       |
| OBS!                | Höljet ska inte vidröra monteringsytan för att kablar ska kunna dras. |

| Tabell 6. Driftssäkerhet                             |                 |
|------------------------------------------------------|-----------------|
| Skyddsklass PN-EN 609501:2007                        | I (första)      |
| Skyddsgradering PN-EN 60529: 2002 (U)                | IP20            |
| Isoleringens elektriska tålighet:                    |                 |
| - mellan ingångs- och utgångskretsar på PSU          | 3000 V AC min.  |
| - mellan ingångskrets och skyddskrets                | 1500 V AC min.  |
| - mellan utgångskrets och skyddskrets                | 500 V AC min.   |
| Isoleringsresistans:                                 |                 |
| - mellan ingångs- och utgångskrets eller skyddskrets | 100 MΩ, 500V DC |
| Förklaringar                                         | CE              |

## **Tabell 7. Driftsparametrar**

| Driftstemperatur                            | -10ºC+40ºC            |
|---------------------------------------------|-----------------------|
| Förvaringstemperatur                        | -20ºC+60ºC            |
| Relativ luftfuktighet                       | 20%90%, utan kondens  |
| Vibrationer under drift                     | oacceptabelt          |
| Impulsvågor under drift                     | oacceptabelt          |
| Direkt isolering                            | oacceptabelt          |
| Vibrationer och impulsvågor under transport | Enligt PN-83/T-42.106 |

### **2. Installation**

### **2,1. Krav & säkerhet**

### **Endast auktoriserad och erfaren personal får installera och underhålla denna enhet.**

Enheten ska monteras i begränsade utrymmen, enligt miljöklass II, med normal luftfuktighet (RH = 90% max. utan kondens) och en temperatur mellan -10°C och + 40°C.

Switchen ska monteras vertikalt med tillräckligt konvektionsluftflöde genom ventilationshålen i höljet.

Innan du installerar switchen ska du utföra en belastningsutjämning.

### **Det angivna värdet på 30 W är maximal belastning per port**. **Total maximal belastning 120W på samtliga portar. För maximal livslängd rekommenderas en kontinuerlig belastning på maximalt 80W.**

Eftersom enheten är avsedd för löpande drift är den inte utrustad med en strömbrytare och därför måste ett lämpligt överbelastningsskydd tillämpas i strömförsörjningskretsen. Dessutom ska användaren informeras om rätt urkopplingsmetod (exempelvis med en lämplig säkring i säkringsskåpet). Det elektriska systemet ska överensstämma med gällande standarder och föreskrifter.

### **2,2. Läge med lång räckvidd**

Switchen har två diftslägen: standard och utökad räckvidd. När omkopplaren för lång räckvidd är inställd på läget STANDARD (se bild 5), erbjuder PoE-portarna 100Mb/s i upp till 100 meter. I läget EXTEND ökas räckvidden till 250 meter och hastigheten minskar till 10 Mb / s. Dessutom aktiveras VLAN-funktionen som isolerar PoE-portarna mellan varandra (kommunikation sker mellan UpLink-portarna och enskilda PoE). I båda lägena är UpLink-portarnas hastighet 100 Mb / s.

**OBS!** En omstart krävs för att ändra läge!

## **2,3. Installationsförfarande**

![](_page_4_Picture_15.jpeg)

**Stäng av spänningen i 230 V före installationen.**

1. Montera PSU på önskad plats och anslut ledningarna. 2. Anslut strömkablarna (230 V) till LN-klämmorna på PSU .

![](_page_4_Picture_18.jpeg)

**Jordskyddskretsen ska alltid kopplas in, dvs. den gula och gröna tråden på strömkabeln ska fästas på sidan av terminalen - märkt med symbolen '** ' **på PSU-höljet. Det är förbjudet att använda PSU utan en korrekt tillverkad och fullt fungerande chockskyddskrets! Det kan orsaka fel på enheten eller elektriska stötar.**

3. Anslut jordledningen till terminalen markerad med symbolen (strömförsörjningsmodulens kontakt). Anslut jordkabeln till klämman märkt med jordsymbolen . Använd en kabel med tre trådar (med en gul och grön skyddstråd) för anslutningen. Dra kablarna till klämmorna genom anslutningskortets isolerande bussningar. 4. Anslut strömmen (230 V).

5. Anslut batteriet (observera färgerna):

- batteriutgång (+V): BAT+ kabel / röd,
- batteriutgång (0V): BAT - kabel / GND / svart.

6. Anslut kamerans kablar till RJ45-anslutningarna (PoE-anslutningar) och anslut enheten till nätverket (UP LINKanslutningen).

7. Kontrollera synlig indikation av switchens drift

- 8. När installation och korrekt funktion har kontrollerats kan höljet stängas.
### **3. Indikation av enhetens drift**

## **3.1 LED-indikering av driftsstatus.**

PSU är utrustad med två ljusdioder på frontpanelen:

![](_page_5_Figure_9.jpeg)

# **3.2 Synlig indikation av switchens drift (se Tabell 8).**

### **Tabell 8. Indikation av switchens drift**

#### **SYNLIG INDIKATION AV STRÖM TILL SWITCHEN**

#### **OPTISK INDIKATION VID PoE-PORTARNA (1÷4)**

| GRÖNT LED-LJUS (PoE)<br>Indikation av PoE<br>strömförsörjning till RJ45-<br>portarna                      | AV- ingen strömförsörjning till RJ45-porten (enheten är inte ansluten eller<br>överensstämmer inte med IEEE802.3af/ som standard)<br>PÅ - strömförsörjning till RJ45-porten<br>Blinkar - kortslutning eller utgångsöverbelastning |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GULT LED-LJUS (LÄNK)<br>Anslutningsstatus för LAN<br>enheter, 10 M/s eller 100 Mb/s<br>och dataöverföring | AV - ingen anslutning<br>PÅ - enheten är ansluten; 10 Mb/s eller 100 Mb/s<br>Blinkar - dataöverföring                                                                                                                             |

#### **OPTISK INDIKATION VID UP LINK-PORTARNA**

| GRÖNT LED-LJUS                                                                                            | Porten på vänster sida:<br>Lyser inte - ingen spänning<br>Lyser - switchen fungerar som väntat           | Porten på höger sida:<br>Lyser inte - switchen används i normalt<br>läge<br>Lyser - Läget med lång räckvidd är aktivt |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| GULT LED-LJUS (LÄNK)<br>Anslutningsstatus för LAN<br>enheter, 10 M/s eller 100<br>Mb/s och dataöverföring | AV - ingen dataöverföring<br>PÅ - enheten är ansluten 10 Mb/s eller 100 Mb/s<br>Blinkar - dataöverföring |                                                                                                                       |

![](_page_6_Picture_0.jpeg)

(Batteri ingår inte).

### **4. Drift och användning.**

### **4.1 Överbelastning eller kortslutning i PSU-utgången (SCP på).**

Vid överbelastning stängs utgångsspänningen liksom LED-indikatorn av automatiskt. Spänningen återställs omedelbart när felet (överbelastningen) åtgärdas.

#### **4.2 Frånkoppling av urladdat batteri**.

PSU är utrustad med ett frånkopplingssystem för urladdade batterier . Under batteridrift kopplas batteriet ur när spänningen sjunker under 19 V vid batteripolerna.

#### **4.3 Underhåll**.

Allt underhåll ska utföras efter att PSU har kopplats bort från nätaggregatet. PSU kräver inte några specifika underhållsåtgärder, men om den blir mycket dammig rekommenderas inre rengöring med tryckluft. Vid byte av säkring ska den nya ha samma parametrar.

![](_page_6_Picture_9.jpeg)

#### **WEEE-MÄRKNING**

**Elektrisk och elektronisk utrustning får inte bortskaffas tillsammans med vanligt hushållsavfall. I enlighet med EU:s WEEE-direktiv ska avfall från elektrisk och elektronisk utrustning bortskaffas separat från vanligt hushållsavfall** .

*Strömförsörjningsenheten är anpassad för användning med ett tätat blybatteri (SLA). Den får inte kasseras och måste återvinnas enligt tillämplig lag.*

**Pulsar sp. j.**  Siedlec 150, 32-744 Łapczyca, Polen Tel. (+48) 14-610-19-40, Fax. (+48) 14-610-19-50 e-post: biuro@pulsar.pl, sales@pulsar.pl http:// www.pulsar.pl, www.zasilacze.pl