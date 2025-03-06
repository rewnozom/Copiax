![](_page_0_Picture_0.jpeg)

# **Exempelsamling** R-CARD 5000 och M5

### **FÖRORD 3 1 PRINCIPSKISSER** 1.1 R-CARD 5000 med M5 MEGA och Electrolux 4 1.2 Passersystem 6 1.3 Larmsystem 7 1.4 Fastighetssystem 8 **2 IT-STRUKTUR I R-CARD M5** 2.1 Server-Klient 9 2.2 Server-Klient via brandvägg 10 2.3 Server via tunna klienter 11 2.5 Webbnärvaro 12 2.6 Närvaro/Antipassback 13 2.7 RCO Access 14 2.9 Electrolux WEB/MOBILE 15 2.10 R-CARD M5 BOKA 16 2.11 Integartion med annan datakälla 17 2.12 OPC Server 18 2.13 Driftövervakning 19 **3 TOPOLOGIER (NÄTPRINCIPER)** 3.1 Princip Anknytningar 20 3.2 Lokal anknytning 21 3.3 Anknytning i nätverksmiljö 22 3.4 Virtuell systembuss över nätverk 23 3.5 Systembuss Routing 24 3.6 Princip lokalbuss 25 3.7 Lokalbuss bussnät 26 3.8 Lokalbuss stjärnnät 27 3.9 Lokalbuss stubbar 28 **4 STRÖMFÖRSÖRJNING** 4.1 01-nät 29 4.2 Grupperade UC-50 30 4.3 Separat matning av lås 31 4.4 Aggregat med och utan reservdrift 32 4.5 Aggregat med övervakning 33 **5 LÅSSTYRNING** 5.1 Elslutbleck 34 5.2 Tryckefunktionlås (splitspindel) 35 5.3 Motorlås med styrbox 36 5.4 El-magnet 37 5.5 Dag- och nattlåsning 38 5.6 Dörrbladsläsare för mekaniska regellås 39 5.7 Sluss 40 5.8 NoKey motor 41 5.9 NoKey motor med dag- och nattlåsfunktion 42 5.10 Läsare ansluten till lokalbuss 43 5.11 Virtuella dörrar 44 5.12 Offline-läsare för mekaniska regellås 45 5.13 Låscyliner med inbyggd kodläsare av offline-typ 46 **6 UTRYMNINGSÖPPNING**

| 6.1 | Lås med omvänd funktion och förreglad matning | 47 |
|-----|-----------------------------------------------|----|
| 6.2 | Nödöppning/paniklåsning                       | 48 |

# **7 DÖRRAUTOMATIKSTYRNING** 7.1 Förregling av dörrautomatik 49 **8 IN- OCH UTLÄSNING** 8.1 In- och utpassering via kortläsare 50

- 8.3 In-och utpassering via grind 52 **9 LARMFÖRBIKOPPLING** 9.1 Bonnförbikoppling 53 9.2 Larmpunkt via DB-50 ansluten till externt larmsystem 54 9.3 Larmpunkt i integrerat larmsystem 55 **10 LARMSTYRNING** 10.1 Externt larmsystem från enskild läsare 56
8.2 In- och utpassering via rotationsgrind 51

- 10.2 Extern larmsystem från läsare i larmområde 57 10.3. Integrerat larm från läsare 58 10.4 Integrerat larm från manöverpanel MapR-59 59 10.5 Integrerat larm från manöverpanel R-TOUCH 50 60
### **11 LARMANSLUTNING**

| 11.1 | IO-50xx eller DB-50                                        | 61 |
|------|------------------------------------------------------------|----|
| 11.2 | DIO-5084 med läsare                                        | 62 |
|      | 11.3 DIO-5084 utan läsare                                  | 63 |
|      |                                                            |    |
| 12   | LARMINDIKERING                                             |    |
| 12.1 | Indikering via utgång på enhet                             | 64 |
|      | 12.2 Indikering i R-TOUCH 50 och R-CONTROL                 | 65 |
|      | 12.3 Väsentlig funktion                                    | 66 |
|      |                                                            |    |
| 13   | HISSTYRNING                                                |    |
| 13.1 | En hiss i ett schakt                                       | 67 |
|      | 13.2 Fler parallella hissar och schakt                     | 68 |
|      | 13.3 Våningsläsare för kallelse                            | 69 |
|      |                                                            |    |
| 14   | PORTTELEFON                                                |    |
| 14.1 | Porttelefon för entréer                                    | 70 |
|      |                                                            |    |
| 15   | BOKNING – INFORMATION                                      |    |
| 15.1 | Maskinstyrning via Electrolux Network™                     | 71 |
|      | 15.2 Maskinstyrning Electrolux Network™/Basic interface 72 |    |
|      | 15.3 Maskinstyrning via IO-enhet                           | 73 |
|      | 15.4 Tvättstuga med fler maskingrupper i samma tvättrum 74 |    |

15.5 Bokning med olika förval (bokningsobjekt) 75 15.6 Electrolux Vision™ med Electrolux Network™ 76 15.7 Electrolux Vision™ i trapphus 77

16.1 Elektroniskt styrda postfack 78

Bussar och kommunikation 79 Kabelguide 80 Tekniska krav 81 Anteckningar 84

**16 FASTIGHETSBOX**

**APPENDIX**

# Förord

Den här boken är tänkt att ge idéer och uppslag för dig som projekterar, planerar eller söker information om tekniska lösningar på tillträdesskydd med säkerhetssystemet R-CARD 5000 från RCO Security AB.

Typiska applikationer och installationer är illustrerade som principiella exempel

och förklarande text. Förhoppningsvis kommer du att hitta just de kopplingsexempel du söker med förslag på lämpliga produkter att använda.

Den här utgåvan av Exempelsamling har kompletterats och förändrats något. Som alltid emotser vi tacksamt era förslag till förbättringar.

RCO Security AB info@rco.se

RCO Security AB reserverar sig för allt ansvar för möjliga fel i detta dokument och för alla eventuella konsekvenser av sådana fel, samt förbehåller sig rätten att närhelst ändra innehållet utan föregående underrättelse.

MS Windows™ registrerat varumärke Microsoft Electrolux Boka™ registrerat varumärke Electrolux Electrolux Vision™ registrerat varumärke Electrolux Electrolux Network™ registrerat varumärke Electrolux 1-Wire® registrerat varumärke Dallas Semiconductors iButton® registrerat varumärke Dallas Semiconductors Mifare® registrerat varumärke Philips Semiconductors

![](_page_3_Figure_1.jpeg)

![](_page_4_Figure_0.jpeg)

# **Principskisser**

### 1.2 Passersystem

R-CARD 5000 med M5 som passersystem

![](_page_5_Figure_3.jpeg)

# **Principskisser**

1.3 Larmsystem

R-CARD 5000 med M5 MEGA som inbrottslarmsystem

![](_page_6_Figure_3.jpeg)

Larmöverföring

# **Principskisser** 1.4 Fastighetssystem

R-CARD 5000 med Electrolux Easy™ för integrerade funktioner som tvättstugebokning, information, porttelefon och fastighetsbox

![](_page_7_Figure_2.jpeg)

### **IT-struktur i R-CARD M5** 2.1 Server–Klient

R-CARD M5 Server med R-CARD M5 Klienter i nätverk

![](_page_8_Figure_2.jpeg)

Programvaran R-CARD M5 används för administration av R-CARD 5000-passersystem. R-CARD M5 består av R-CARD M5 Server, R-CARD M5 Klient och en Microsoft SQL-databasserver. De olika delarna installeras i samma dator alternativt som serverinstallation i lokalt nätverk med möjlighet till flera administrationsklienter.

Databashanteraren SQL Server Express Edition medföljer utan kostnad. M5 Server kan även ansluta mot databas installerad på separat SQL-server och beroende på M5-version även nyttja äldre versioner av SQL Server. R-CARD M5 Server sköter kommunikation med passersystemets undercentraler, UC-50 samt databasservern. R-CARD M5 Klient är programmet som operatören använder vid administrationen av systemet. Ansluten till R-CARD M5 Server, antingen direkt i samma dator eller via ett nätverk. Klientens anslutning mot server räknas per samtidig operatör. R-CARD M5 Server kommunicerar med klienten via DCOM.

Vid installation i nätverksmiljö måste serverns inställningar för DCOM anpassas beroende på domäntillhörighet och vald operativssystemsversion. Exempelvis att kommunikation via DCOM tillåts för en i AD definierad grupp av användare.

**Operativsystem som krävs på M5 servern** Se "Tekniska krav" sidan 82

**Licenskrav** R-CARD M5

**Tillägg**

R-CARD M5 KLIENT (per samtidig operatör)

### **IT-struktur i R-CARD M5** 2.2 Server–Klient via brandvägg

R-CARD M5 Server med R-CARD M5 Klient via brandvägg

![](_page_9_Figure_2.jpeg)

En brandvägg kan vara i utförande som hårdvara eller som en programvara. Brandväggen analyserar in- och utgående kommunikation och blockerar, enligt ett regelverk, oönskad trafik.

Om administration och övervakning av passersystemet sker med en klient ansluten via brandvägg måste speciell hänsyn tas. R-CARD M5 Server, klient och brandvägg måste exempelvis konfigureras lika avseende vilket IP-adressområde och över vilka port-nummer datatrafik ska tillåtas.

Brandväggar som använder adresstransformering (NAT) kan inte användas då stöd för detta saknas med DCOM, den teknik som används för kommunikation mellan R-CARD M5 server och klient.

Om behov finns att kunna fjärradministrera R-CARD M5 rekommenderas att en VPN lösning väljs för att säkerställa säkerheten mellan R-CARD M5 Server och Klient.

#### **Systemkrav**

Se "Tekniska krav" sidan 82

**Licenskrav** R-CARD M5

**Tillägg**

R-CARD M5 KLIENT (per samtidig operatör)

# **IT-struktur i R-CARD M5**

2.3 Server via tunna klienter

R-CARD M5 Server med distribuerade klienter

![](_page_10_Figure_3.jpeg)

I större organisationer med arbetsplatser med skilda geografiska placeringar kan en lösning med distribuerade klienter vara ett kostnadseffektivt alternativ.

Support och underhåll av R-CARD M5-programvaran förenklas då exempelvis uppgraderingar endast behöver göras på en dator oavsett hur många administratörer som använder R-CARD M5-klienten.

Istället för att ha programmet installerat på

sin egen dator så ansluter användaren till en central server och använder servern istället för den egna datorn för att köra program och applikationer.

Att exempelvis arbeta i R-CARD M5 klienten via serveranslutningen blir precis som om klienten vore installerad lokalt på den egna datorn.

Exempel på programvaror för hantering av distribuerade klienter är Citrix och Microsoft Remote Desktop.

#### **Systemkrav**

Se "Tekniska krav" sidan 82

**Licenskrav** R-CARD M5

**Tillägg** R-CARD M5 KLIENT (per samtidig operatör)

### **IT-struktur i R-CARD M5** 2.4 Webbnärvaro

R-CARD M5 Server med tilläggsmodul M5 Närvaro web

![](_page_11_Figure_2.jpeg)

Med R-CARD M5 NÄRVARO WEB kan personer som registrerats i en närvarozon visas i en vanlig webbläsare.

Närvarokontroll kräver att både in- och utläsning används vid passage till och från de definierade närvarozonerna. Vilka av anläggningens kortläsare som ska registrera in- respektive utpassage för varje närvarozon är valbart och anges i en inställningsfil.

I webbläsaren visas efter inloggning en lista i realtid med närvarozonerna och antal registrerade i respektive zon. Genom att klicka på zonbenämning erhålls en detaljerad översikt med information som tidpunkt och namn. Vilken information som ska presenteras och i vilken ordning är valbart.

Man kan även begära ut en utskrift på informationen.

Närvaroapplikationen installeras på en dator med Microsoft IIS installerat. Kraven för funktion är även att R-CARD M5 SERVER är i drift och att den är online med anläggningen. Om installation görs på en annan fysisk dator än R-CARD M5 Server användas NÄRVARO WEBtjänst för kommunikation melllan R-CARD M5 och NÄRVARO WEB-applikationen. Om kryptering önskas av webbtrafiken rekommenderas att Microsofts SSL-kryptering används.

Som klient för närvaroapplikationen används webbbläsare av standardtyp som Google Chrome eller Mozilla Firefox med flera.

### **Systemkrav**

Se "Tekniska krav" sidan 82

**Licenskrav** R-CARD M5 R-CARD M5 NÄRVARO WEB R-CARD M5 WEBADMIN (per samtidig operatör)

# **IT-struktur i R-CARD M5**

2.5 Närvaro/Antipassback

R-CARD M5 Server med tilläggsmodul M5 NAP

![](_page_12_Figure_3.jpeg)

Tilläggsmodul för avancerad närvaro- och inpasseringskontroll för anläggningar med höga säkerhetskrav. Med R-CARD M5 NAP utökas R-CARDsystemet med funktioner som entréhänvisning, antipassback-regler, nivå- tid- och antalslarm.

Upp till 255 närvaroområden kan konfigureras per anknytning. Vilka dörrpasseringar som ska registreras som in eller ut i området är fritt definierbart och områdena kan även placeras inuti varandra till ett djup av 8 nivåer. Information om vilka som befinner sig i ett område kan presenteras direkt i en dialog i R-CARD M5-klienten eller som flikar i klientens fönster för visning av realtidshändelser. Via dialogen finns även möjligheter att stoppa och justera räknare samt nollställa området. Med närvarokontrollen ges även möjlighet att använda antalslarm där exempelvis en utgång kan användas för att aktivera ett larm

vid nivå hög, låg, tomt, inte tomt samt närvarande för länge. Närvarokontrollen fungerar helt autonomt och är inte beroende av kommunikation med R-CARD M5-servern.

Med aktiverad antipassback förhindras att samma kort används för inpassering flera gånger i följd utan att en utpassering registrerats däremellan. Antipassbackreglerna kan ställas in för att fungera permanent alternativt som en kortare eller längre tid. Med funktionen Entréhänvisning finns möjlighet att hänvisa användarna till att alltid passera in via utvalda läsare eller områden innan passage medges i andra närvarområden.

M5 NAP interagerar även med M5 MEGA integrerat larmsystem och har även möjlighet att aktivera utskrift av återsamlingslistor sorterade och grupperade till valfria skrivare.

# **Systemkrav** Se "Tekniska krav" sidan 82 **Licenskrav** R-CARD M5 R-CARD M5 NAP

### **IT-struktur i R-CARD M5** 2.6 RCO Access

Dörrstyrning via mobilappen RCO Access

![](_page_13_Figure_2.jpeg)

Med mobilappen RCO Access installerad på en telefon kan användaren ges möjlighet att låsa upp en eller flera dörrar, grindar eller portar. Användaren ges tillgång till systemet genom att ansluta till en webbserver, antigen publikt via internet eller enbart lokalt via det egna trådlösa nätverket. Kommunikationen mellan webbserver och telefon krypteras med SSL Certifikat.

Vilka dörrar som användaren har rättighet att se status för och styra i appen hanteras via en vanlig passerbehörighet kopplad till användarens ordinarie passerkort vilket gör att tillgången till dörrarna även kan schemaläggas, dag och tid.

Uppgifter om anslutningsinställning kan skickas till användare som QR-kod eller länk.

M5UserAPI installeras på en Microsoft IIS-server, antigen som fristående webbserver eller på samma dator som R-CARD M5 är installerat. Om installationen görs på annan fysisk dator än R-CARD M5-server används M5UserAPI tjänst för kommunikation mellan R-CARD M5 och M5UserAPI.

För att använda M5UserAPI krävs en licens per dörr som användaren ska kunna se och styra via mobilappen.

#### **Systemkrav**

Se "Tekniska krav" sidan 82

#### **Licenskrav**

R-CARD M5 ACCESS DÖRR (licens per dörr) R-CARD M5 ACCESS VIRTUELL (licens per dörr)

### **IT-struktur i R-CARD M5** 2.7 Electrolux WEB/MOBILE

Bokning och information i dator och mobiltelefon

![](_page_14_Figure_2.jpeg)

Med Electrolux WEB/MOBILE kan boende ges möjlighet att boka och komma åt information på fastighetens boknings- och informationstavlor direkt från sin dator eller telefon. Via ett webbgränsnitt som efterliknar bokningstavlan eller från en app i telefonen kan användaren boka och avboka tider, se maskinstatus och allmän information samt även se saldo om modulen Electrolux PAYMENT finns installerad.

Electrolux WEB/MOBILE installeras på en dator med Microsoft IIS installerat. Om installation görs på en annan fysisk dator än R-CARD M5 Server användas Electrolux WEB-tjänst för kommunikation mellan R-CARD M5 och Electrolux WEB-applikationen.

internet så bör särskild hänsyn tas till säkerheten. RCARD M5-servern bör därför placeras innanför brandväggen, helt skyddad, på det interna nätverket. Webbservern som publicerar Electrolux WEB direkt mot internet placeras på ett separat nätverk s.k. DMZ. Kommunikationen mellan R-CARD M5 och Electrolux WEB sker via Electrolux WEB-tjänst. Tekniskt kan man installera Electrolux WEB på samma fysiska dator som R-CARD M5 server men av säkerhetsskäl rekommenderas att man delar detta på två fysiska datorer. Om högre säkerhet önskas kan MS IIS-servern förses med SSL-kryptering.

Ett krav för att bokning via Electrolux WEB ska fungera är att kontakten mellan R-CARD M5 Server och undercentralerna med bokningstavlorna är av typen fast uppkoppling.

**Systemkrav** Se "Tekniska krav" sidan 82 **Licenskrav** R-CARD M5 Electrolux BOKA Electrolux WEB/MOBILE Electrolux PAYMENT (option)

Då Electrolux WEB/MOBILE publiceras ut på

### **IT-struktur i R-CARD M5** 2.8 R-CARD M5 BOKA

Aktivering av tidstyrd behörighet via indatafil

![](_page_15_Figure_2.jpeg)

Bokningsprogram för bokning av lokaler som exempelvis idrottsanläggningar och samlingslokaler kan integreras till passersystemet med modulen RCARD M5 BOKA. Bokningen görs i bokningsprogrammet och via en indatafil, som regelbundet kontrolleras av systemprogramvaran, uppdateras persondatabasen med nya eller ändrade bokningar. En bokning tilldelar användarens kort en tidsbestämd behörigt som ger tillträde till lokalen den bokade tiden. I egenskaperna för bokningen anger man om användaren ska kunna passera med antingen kort och pin, enbart kort eller enbart pin. Användaren kan även ges möjlighet att ställa upp dörren eller lägga ut en tillfällig kod. Även belysningen i lokalen kan styras via bokningen, antigen som

en aktivering vid passage i inpasseringsläsaren eller som en tidsbokning i bokningssystemet utan krav på passsering i läsare. Exempel på bokningsprogram är IBGO från Explizit, Rbok från Rbok AB samt Boka Mera.

Även andra program eller lösningar med behov av aktivering av tidsbestämda behörigheter kan använda den här lösningen förutsatt att de finns möjlighet att exportera en indatafil i gällande format. Är bokningsinformationen lagrad på en extern server kompletteras R-CARD M5-installationen med en extra programfil som körs schemalagt för hämtning av bokningsinformation och skapande av indatafil.

### **Systemkrav**

Se "Tekniska krav" sidan 82

**Licenskrav** R-CARD M5 R-CARD M5 BOKA

### **IT-struktur i R-CARD M5** 2.9 Integration med annan datakälla

R-CARD M5 Server med tilläggsmodul R-CARD M5 ADMIN API

![](_page_16_Figure_2.jpeg)

Genom att utbyta data mellan R-CARD M5 och andra datakällor kan behovet av administration minskas. Med R-CARD M5 ADMIN API erhålls en möjlighet att läsa och skriva data till och från persondatabasen i R-CARD M5. Integrationen med andra datakällor hanteras via en tolk eller integrationsmotor som vet var och hur anropen mellan systemen ska utföras och hur det ska översättas så att mottagande system förstår den data som skickas. Integrationsmotorn kommunicerar med R-CARD M5 via R-CARD M5 ADMIN API.

Gränssnittet är ett s.k. REST API för integration

av administrativa funktioner och har stöd för hantering av användare och lägenhetsdata med möjlighet att administrera kort och behörigheter.

Exempel på lämpliga användningsområden är integration mot lönekontorets personalregister eller IT system som Microsofts Active Directory (AD). Uppdateringar av användare i dessa system kan med en integration automatiskt även uppdatera passersystemets uppgifter om användaren. R-CARD M5 Admin API är en licensierad tilläggsmodul till R-CARD M5 och installeras på en Microsoft IIS server.

# **Systemkrav** Se "Tekniska krav" sidan 82 **Licenskrav** R-CARD M5 R-CARD M5 ADMIN API

### **IT-struktur i R-CARD M5** 2.10 OPC Server

R-CARD M5 Server med tilläggsmodul M5 OPC

![](_page_17_Figure_2.jpeg)

R-CARD M5 OPC kan användas som ett generellt integrationsgränssnitt för olika typer av överordnade kontroll- och styrsystem.

Händelser och styrkommandon kan via s.k. OPCtaggar hanteras mellan R-CARD M5 SER-VER och överordnad klient. Exempel på användningsområden är grafisk presentation och som gränssnitt mot styr och regler-system samt för kontroll av kamerasystem.

En fastighetsägare som vill spara energi kan exempelvis via OPC skicka statusinformation till styr och regler-systemet om att larmet är tillkopplat för att då sänka värme och ventilation samt släcka belysningen i fastigheten.

R-CARD M5 OPC stödjer Alarm & events V1.02 samt Data Access V2.05.

#### **Systemkrav**

Se "Tekniska krav" sidan 82

**Licenskrav** R-CARD M5 R-CARD M5 OPC

### **IT-struktur i R-CARD M5** 2.11 Driftövervakning

R-CARD M5 Server med Driftövervakning konfigurerad

![](_page_18_Figure_2.jpeg)

Driftövervakning är en standardfunktion i R-CARD M5 som kan användas för att aktivera s.k. driftlarm i klientens larmfönster alternativt som ett e-postmeddelande eller sms.

Driftövervakningen bygger på att man definierar händelsefilter (triggvillkor) baserat på en eller flera händelser kopplat mot en eller flera enheter och användare. Händelsefiltret kopplas därefter till önskad typ av larmfunktion som exempelvis e-post.

När händelsefiltret "triggar" genereras ett e-postmeddelande till specificerad mottagare. Exempel på användningsområden är larmpåeller avslag, dörrpassager i övervakade dörrar, larm om uppställda dörrar, m.m.

För att skicka driftlarm som e-post krävs kommunikation med en e-post-server via SMTP-protokollet. För sms krävs att e-post-servern har en installerad sms-gateway.

### **Systemkrav**

Se "Tekniska krav" sidan 82

**Licenskrav** R-CARD M5

# **Topologier (nätprinciper)** 3.1 Princip anknytningar

Systembuss för kommunikation mellan R-CARD M5 och UC-50

![](_page_19_Figure_2.jpeg)

### **Anknytning**

En anknytning är en kommunikationsförbindelse mellan R-CARD M5 Server och inkopplad platsutrustning.

Anknytningen etableras mellan R-CARD Server och en undercentral UC-50 och för kommunikationen mellan centralerna används systembuss. Kommunikationen mellan R-CARD server och undercentral samt internt på systembuss sker krypterat. Ett segment av systembuss ansluter upp till 16 (med routing 80) UC-50 per anknytning. Upp till 255 anknytningar kan anslutas till R-CARD M5 Server som ständigt uppkopplade (online). Utöver dessa kan upp till 65 000 anknytningar anslutas för att kopplas upp först vid behov.

### **Systembuss**

Systembussen använder CAN (Controlled Area Network). Välj kabel för CAN-bussen med hänsyn till avstånd och antal enheter. Kabeln skall vara ett par partvinnat och har inget krav på skärm. Längd på kabeln är max 1 000 meter. Se kabelguide sist i detta dokument för rekommenderade kabeltyper.

# **Topologier (nätprinciper)** 3.2 Lokal anknytning

Anslutning av UC-50 via korsad nätverkskabel till R-CARD M5 Server

![](_page_20_Figure_2.jpeg)

ska användas för programmering och därefter kopplas ur kan man med fördel använda en korsad nätverkskabel som kommunikationsförbindelse mellan RCARD M5 Server och undercentralens nätverksmodul IP-50.

Användning av TCP/IP-kommunikation och datorns inbyggda nätverkskort gör att installationen blir enkel och man har fördelen av att vid behov kunna ansluta anläggningen till ett LAN/WAN.

För inläsning av kodmedia kan en USB-ansluten bordsläsare användas.

# **Topologier (nätprinciper)** 3.3 Anknytning i nätverksmiljö

Anslutning av undercentral UC-50 med IP-50 över nätverk till R-CARD M5 Server

![](_page_21_Figure_2.jpeg)

R-CARD M5 Server kan installeras antingen på nätverk som utbreder sig lokalt eller mellan verksamhetens olika arbetsplatser med skilda geografiska placeringar.

Anknytning för TCP/IP förutsätter att undercentral UC-50 med nätverksmodulen IP-50 och R-CARD M5 Server har kommunikationsmöjlighet mellan varandra. Anläggningsdelar kan anslutas till R-CARD M5 Server via LAN, intranet eller via internet. IP-50 använder fast IP-adress alternativt DHCP-adress i kombination med dynamisk DNS-tjänst.

Undercentralen har även möjlighet att göra sin IPadress känd för R-CARD M5-servern via s.k.

MACadressering. En sådan lösning förutsätter att eventuell brandvägg på R-CARD M5-serversidan tillåter kommunikation över vald port. Som standard används UDP-port 1 000. IP-anknytningen tar som mest 200 Kbit/s och normalt 20 Kbit/s av nätverkets kapacitet och kommunikationen är krypterad.

Saknas möjlighet till fast anslutning kan UC-50 med IP-50 anslutas mot 3G/4G-router med abonnemang för datakommunikation.

Användning av TCP/IP-kommunikation för en anknytning gör att man kan nyttja befintlig infrastruktur och enkelt nå avlägsna anläggningsdelar.

![](_page_21_Figure_9.jpeg)

Anslutning av fler IP-anslutna UC-50 på samma IP-anknytning

![](_page_22_Figure_2.jpeg)

Anknytning 1 med Systembuss över IP

Som alternativ till lokalt kabelbunden systembuss kan LAN/WAN användas som virtuell systembuss för kommunikation mellan UC-50. Med systembuss över IP kan upp till 16 nätverksanslutna UC-50 anslutas till samma anknytning. Fördelen med en sådan lösning är exempelvis möjlighet att nyttja logiska funktioner, signaler mellan in- och utgångar, över längre sträckor eller fjärrboka mellan bokningspaneler ansluta till olika fastigheter utan möjlighet till lokal kabelbunden kommunikation. Kravet för den typen av funktioner är att enheterna tillhör samma anknytning vilket systembuss över IP möjliggör.

Beakta att vid användning av systembuss över IP skapas ett beroende av nätverket vilket innebära driftstörningar på anläggningen om nätverket inte fungerar. Man bör därför bl.a. eftersträva att säkerställa strömförsörjning av aktiva nätverkskomponenter som hubbbar, switchar m.m.

Systembuss över IP kan anslutna maximalt 16 UC-50 med IP-50 samt maximalt 16 UC-50 kopplade under dessa med lokalt kabelbunden systembuss som en anknytning. Maximalt antal dörrmiljöer per anknytning är dock alltid 255. Kravet för systembuss över IP är att samtliga ingående UC-50 med IP-50 har kommunikations möjlighet alla till alla. Vid implementation av systembuss över IP adresseras samtliga ingående enheter som om de vore anslutna på en anknytning. UC-50 på kabelbunden systembuss kan utökas med ytterligare segment med systembuss över IP förutsatt att inte antalet systembuss segment överstiger nio nivåer.

Se 3.5 Systembuss-routing.

3.5 Systembuss-routing

Förlängning av systembuss med routing mellan UC-50

![](_page_23_Figure_3.jpeg)

Ett systembussegment kan sträcka sig upp till 1 000 meter och ansluta maximalt 16 undercentraler UC-50. Om detta skulle vara begränsande, kan systembussen förlängas med routing. Genom att koppla samman två IP-50 försedda UC-50 med en nätverkskabel kan den "primära" systembussen routas till en "sekundär" som kommer att erbjuda ytterligare 1 000 meter systembuss med möjlighet att ansluta ytterligare 16 undercentral UC-50. Detta kan upprepas fyra gånger, varför systembussen kan utsträckas till totalt 5 000 meter och totalt 80 UC-50.

De UC-50 som ingår i routing fungerar i övrigt fullt ut för att ansluta enheter på lokalbuss.

Systembussen kan använda kommunikation via CAN- eller TCP/IP och vara uppdelad i flera segment. Vid användning av systembuss över IP och routing räknas varje kommunikationsteknik som ett segment. Mellan två undercentraler UC-50 på en anknytning får det maximalt finnas nio systembusssegment/byten av kommunikationsteknik.

# **Topologier (nätprinciper)** 3.6 Princip lokalbuss

Lokalbuss för kommunikation mellan UC-50 och läsare, dörr och larmanslutningsenheter samt andra terminaler

![](_page_24_Figure_2.jpeg)

Lokalbuss ombesörjer kommunikation och strömförsörjning av olika enheter anslutna till undercentral UC-50. Anslutna enheter kan vara läsare typ Reader-5xx d.v.s. läsare vars första siffra börjar med 5 eller anslutningsenheter för läsare och larmdetektorer som DB-50, IO-50xx och DIO-5084, eller linjekort för telekommunikation TEL-50, eller andra terminaler som manöverpanel MapR 509, portapparat PA-519 och bokningstavla Electrolux Vision Light.

Datakommunikation med RS-485 sträcker sig upp till 1 000 meter från första till sista enhet inkopplad på bussen. Kabel ska vara försedd med ett

par (partvinnat) för kommunikation samt minst två ledare för spänningsmatning vars area dimensioneras efter totala strömuttaget på kabeln. Inget krav på skärm. Se kabelguide sist i detta dokument för rekommenderade kabeltyper.

UC-50 levereras i utförande för 2 (UC-50/2), 4 (UC- 50/4) eller 8 (UC-50/8) dörrplatser. Oavsett ovan nämnda begränsningar kan samtliga även ansluta in-/utenheter (IO-50xx), DIO-5084 (som ren larmanslutningsenhet, ej med läsare) TEL-50 eller Electrolux Network Master™. upp till totalt 16 enheter per UC-50.

# **Topologier (nätprinciper)** 3.7 Lokalbuss bussnät

Normal anslutning av enheter till lokalbuss

![](_page_25_Figure_2.jpeg)

Lokalbussen kommunicerar med anslutna enheter ("multi drop") och levererar matningsspänning. Anslutningar i enheter utgörs av urkopplingsbara skruvplintar varför urkoppling av enhet låter sig göras utan inverkan på övrigt system. Lokalbussen skall termineras med impedans (se röd prick). Termineringen utförs med bygling

i enheterna och UC-50, alternativt i enhetens boot-meny.

**OBS** UC-50 behöver inte vara placerad i änden av lokalbussen, utan kan mycket väl vara placerad "mitt i" för optimering av totala längden för lokalbussen.

### **Topologier (nätprinciper)** 3.8 Lokalbuss stjärnnät

Stjärnkopplat nät via plintbox eller PL-50

![](_page_26_Figure_2.jpeg)

![](_page_26_Figure_3.jpeg)

Befintligt kablage kan vara förlagt som stjärnnät dvs. kablar är dragna från central plats till varje dörr. En inte ovanlig kabelförläggning för äldre system. Genom att ansluta enheter t. ex. DB-50 med ett returpar för kommunikationen, bibehålls RS-485- specifikationens "multi drop"-anslutning. Central koppling av lokalbussen kan utföras som i exempel 1 i en speciell plintbox eller som i exempel 2 med hjälp av PL-50, en plintbox med slitsplintar.

Befintligt kablage kan återanvändas förutsatt att det i övrigt uppfyller kraven. Genom att lokalbussen går tur och retur för varje avgrening, måste man observera att lokalbussens längd blir dubbla längden för kablaget. Används PL-50 termineras anslutna enheter via bygel i PL-50.

Om behov finns kan PL-50 placeras på annan plats än direkt vid UC-50.

# **Topologier (nätprinciper)** 3.9 Lokalbuss stubbar

Lokalbuss förlagd som matarkabel med anslutning via stubbar

![](_page_27_Figure_2.jpeg)

Framförallt för enheter som måste anslutas med karmöverföring som ex 508 rekommenderas flerkardelig kabel för att undvika utmattning i ledarna. Om längden på ledningen mellan plintbox och enheten på dörr ej överstiger 3 meter

kan kommunikation utgöra en s.k. "stubbe" dvs. endast ett par används. Vid längre kabelväg ska lokalbussens datapar dras fram och tillbaka. Färre trådar i mjukkabel kan eventuellt minska kostnaden för både kabel och plint.

NoKey 508

# **Strömförsörjning** 4.1 01-nät

UC-50 spänningsmatas med gemensam strömförsörjning via 01-nät

![](_page_28_Figure_2.jpeg)

Av olika skäl önskas ibland gemensam strömförsörjning av all platsutrustning. Från ett strömförsörjningsaggregat fördelas matningen genom ett s.k. 01-nät. Genom att endast en strömförsörjning nyttjas kan underhåll av batterier förenklas.

Om anläggningen är omfattande, måste spänningsfall i 01-nätet beaktas.

Avsäkringen av 01 nät bestämms av vilken kabeldimension som använts.

# **Strömförsörjning** 4.2 Grupperade UC-50

Grupper om fler UC-50 spänningsmatas med gemensam strömförsörjning

![](_page_29_Figure_2.jpeg)

För en större anläggning kan det av olika skäl t.ex. för att hålla reservdrifttiden eller klara strömuttaget, vara lämpligt att fördela lasten.

Genom placering av ett separat strömförsörjningsaggregat tillsammans med fler UC-50 på samma plats, kan samma aggregat mata alla UC-50 i gruppen.

Om fler strömförsörjningsaggregat används kan dessa vara mindre och matarledningar kortare dvs. eventuella spänningsfall mindre.

Avsäkringen bestämms av vilken kabeldimension som använts.

Separat aggregat för strömförsörjning av elektriska lås

![](_page_30_Figure_2.jpeg)

Vid lång sträckning eller liten area för kabel fram till en dörranslutningsenhet, DB-50 eller IO-50xx, kan spänningsfall förväntas.

Utöver ordinarie matning av DB-50 och IO-50xx, kan separat strömförsörjningsaggregat kopplas in för matning av elektriska lås (lasten).

Denna lösning kan med fördel användas då man har höga krav på gångtid för larmet och strömbelastningen på låsen är svårbedömd.

* Potientiell fri slutning till el-lås

# **Strömförsörjning** 4.4 Aggregat med och utan reservdrift

Matning med 24VDC

![](_page_31_Figure_2.jpeg)

Om inga krav finns på funktion vid nätspänningsbortfall kan enkel likriktare som ger 24 V användas.

Enkla transformatorer med inbyggd likriktare kan användas. Utrustning som UC-50, DB-50 och IO- 50xx har inga krav på stabiliserad spänning. Notera dock att en del elektriska lås kan ha krav på stabiliserad eller glättad matning. Ger lägsta kostnad för strömförsörjning men ingen funktion vid nätspännings bortfall.

Vanligtvis vill man dock att anläggningen ska fungera trots nätspänningsbortfall dvs. dörrar ska fungera som vanligt under en bestämd tid. Strömförsörjningsaggregatet utförs då som likriktande batteriladdare med tillhörande ackumulatorer. Likriktaren ska dels klara maximalt strömuttag för anläggningen, dels att ladda urladdade ackumulatorer. Ackumulatorerna ska dimensioneras efter strömuttag och kraven på reservdrifttid. Strömförsörjning med batteribackup ger full funktion vid dörren vid nätspänningsbortfall, dock under begränsad tid.

Matning med 24 VDC med batteribackup och driftövervakning med larm

![](_page_32_Figure_2.jpeg)

För t. ex. inbrottslarmsystem finns förutom krav på reservdrift med batteribackup, också krav på övervakning av driften. T. ex. ska strömförsörjningsaggregatet avge larm vid vissa driftfel.

Inbrottslarmanläggningar levereras alltid med egen batteribackup. Svenska Stöldskyddsföre - ningen kräver att anläggningar ska ha batteri - backup för 12 timmar (klass 1 och 2). Fel på strömförsörjningen överförs som fellarm till larmcentralen. Följande fel ska detekteras: nätspänningsbortfall, minimalspänningslarm (låg batterispänning). RCO:s aggregat detekterar också; överspän ning, åldrat bat teri och underspänning nätdrift.

RCO:s system har integrerad övervakning av nätaggregat. Om yttre strömförsörjning används, ska detektorer och larmdon tvåpoligt avsäkras separat så att inte centralapparatens funktion äventyras vid fel på dessa apparater. Vidare finns avsäkring per anslutningsenhet grupper in, kontra utgångar för dessa matningar, men man bör alltid betänka hur stor del av skyddet som försvinner vid utlöst säkring och gärna dela upp detektorerna i fler grupper.

För att säkerhetställa gångtid utan påverkan av dörrlås kan dessa matas separat.

Strömförsörjning med övervakning kan även erhållas i ett passagesystem utan larm (MEGA).

# **Låsstyrning** 5.1 Elslutbleck

Styrning av elslutbleck med DIO-5084/DB-50

![](_page_33_Figure_2.jpeg)

Elslutbleck kan användas på dörrar med begränsa de krav på brytskydd, som ska styras av kortläsare.

Vid godkänd identifiering vid kortläsare styr DB öppningssignal, vanligen 24 VDC, till elslutblecket som då låser upp genom att frigöra blecket för fallkolven. Vissa elslutbleck är försedda med kolvkontakt som kan användas för att avkänna låst och stängd dörr. Kolvkontakt kan anslutas (streckad signal) till ingång för dörravkänning på DB för att erhålla nerbrytning av öppningssignal. Dörren blir då åter låst vid stängning. Alternativt kan separat magnetkontakt användas för dörravkänning om elslutblecket saknar kolvkontakt.

Elslutbleck som har relativt låg kostnad, ger låg säkerhet p.g.a. den begränsade mekaniska hållfastheten, speciellt då fallkolv används. Låser och låser upp snabbt.

Styrning av tryckefunktionlås med DB-50

![](_page_34_Figure_2.jpeg)

Tryckefunktionslås ger något bättre brytskydd än elslutbleck och kan användas på dörrar styrda av kortläsare.

Vid godkänd identifiering vid kortläsare styr DB öppningssignal, vanligen 24 VDC, till trycke funktionlåset som då elektromekaniskt kopplar in trycket (handtaget) till regeln. Dörren kan därefter öppnas med trycke på både ut- och insida av dörr.

Med s.k. splitspindelfunktion fungerar alltid inre trycket för utpassage och separat öppnaknapp blir då ej nödvändig. För larmförbikoppling ansluts kontakt för trycke/handtagsläge till DB (streckad signal) med egenskap Trycke/ handtagsläge för låsöppning. Vid utpassage med splitspindel genereras ej olåstindikering i läsaren.

Tryckefunktionslås ger bra och snabb låsning och upplåsning. Med splitspindel blir handhavande för utpassering enkelt. Kabel måste dras på/genom dörrblad och karmöverföring måste användas. Exempel på låskistan är av typen ABLOY EL 580.

### **Låsstyrning** 5.3 Motorlås med styrbox

Styrning av motorlås med DIO-5084/DB-50

![](_page_35_Figure_2.jpeg)

För högsta mekaniska hållfasthet och brytskydd kan motorlås användas på dörrar styrda av kort - läsare.

Vid godkänd identifiering vid kortläsare styr DB-50 öppningssignal, vanligen potentialfri slutning, till styrbox för motorlås som med elektrisk motor drar in regeln. När öppningssignal upphör och dörr är stängd, skjuter motorn ut regeln i stolpen. Styrboxen kan eventuellt ge signal för stängd dörr och låst som kan anslutas (streckad

signal) till ingång för dörravkänning på DB-50/ DIO-5084.

Motorlås ger bästa mekaniska brytskydd. Trots hög strömförbrukning under låsning och upplåsning, drar motorlås liten ström i olåst och låst läge. Låsning och upplåsning tar viss tid vilket kan upp levas besvärande. Kabel måste dras på/genom dörrblad och karmöverföring måste användas.

Styrning av elektromagnet med DIO-5084/DB-50

![](_page_36_Figure_2.jpeg)

För vissa passerpunkter som skjutdörrar, gallergrindar eller rullportar, kan elektriska (drag) magneter vara lämpliga som alternativ till andra elektriska lås.

Vid godkänd identifiering på kortläsare styr DIO/DB öppningssignal genom att bryta 24 VDC till el-magneten som då frigör ankardelen som

monterats på dörrbladet. Då strömförbrukningen kan var hög i låst läge, kan det fordras extern strömförsörjning och hjälprelä för funktionen.

El-magneter kan monteras på dörrar som inte är hängda på vanligt vis, men drar hög ström i låst läge.

# **Låsstyrning** 5.5 Dag- och nattlåsning

Styrning av dag- och nattlås med DIO-5084/DB-50

![](_page_37_Figure_2.jpeg)

Entrédörrar ska vara säkert låsta på natten och under dagtid vill man kunna låsa upp enkelt och snabbt. På natten låses dörr med motorlås (och elslutbleck). Kvällstid vid godkänd identifiering låses natt- och daglås upp. Egenskap Fördröjd dörröppning (daglås) gör att nattlåsets kolv måste vara olåst innan daglås öppnas (inställbar tid). Detta för att skydda

motorlåskolv mot belastning/ryck i dörr innan den blivit olåst.

Under dagtid, definierad via tidkanal eller styrd av larmläge, ska motorlåset vara upplåst medan enbart elslutblecket öppnas vid godkänd identifiering. Kombinerar hög säkerhet med enkelhet.

# **Låsstyrning** 5.6 Dörrbladsläsare för mekaniska regellås

Beröringsfri onlineläsare med integrerad tryckeslåsfunktion

![](_page_38_Figure_2.jpeg)

En läsare med inbyggd elektrisk låsning monterade direkt på dörrbladet är ett enkelt sätt att inkludera fler dörrar i passersystemet till en låg kostnad.

NoKey-508 är både beröringsfri läsare och elektriskt lås som monteras på dörr med befintligt (mekaniskt) regellås. Vid godkänd identifiering på läsaren kopplas yttre trycket (handtaget) till tryckesfallet och dörren kan öppnas. Inre trycket för utpassering är alltid inkopplat.

Läsaren finns i flera utförande beroende på vilka säkerhetskrav som gäller för dörren. Med och utan tangentbord samt med möjlighet till montering av mekanisk låscylinder och vredfunktion

för aktivering av regeln då krav på exempelvis säker låsning nattetid ställs. Vilken låsfunktion som erhålls avgörs av vilken typ av låshus som läsaren kombineras med.

NoKey-508 passar på vanliga inner- och ytterdörrar med modullåshus av nordisk standard och behöver varken DB eller annan elektronik för att ansluta till undercentral UC-50. Kabel för kommunikation och strömförsörjning dras på/ genom dörrblad och karmöverföring krävs.

I Mifare-utförande kan även NoKey-508 fungera som initieringsläsare för NoKey offline.

Slussfunktion i R-CARD 5000

![](_page_39_Figure_2.jpeg)

I miljöer med höga renlighet- eller säkerhetskrav kan två eller flera dörrmiljöer på en UC-50 grupperas för att fungera som en eller flera slussar. Vilken slussgrupp dörrmiljön ska tillhöra samt vilken läsare som ska fungera som in- eller utläsare anges i inställningar för dörrmiljön.

Ställs extra höga säkerhetskrav kan slussen även ställas in för att vara låst för en användare i taget. Då måste den användare som passerat in i slussen även passera ut innan någon annan kan passera in.

Möjlighet finns även att på ledig utgång i exempelvis DB eller IO ansluta en indikering för "upptagen sluss".

Inkluderas ingående dörrar i funktionen "Nödöppning" som ingår vid användning av RCARD M5 MEGA integrerat larm så finns möjlighet att vid nödsituation häva slussfunktionen och låsöppna dörrarna.

Motorstyrning av mekaniska regellås

![](_page_40_Figure_2.jpeg)

I miljöer med höga säkerhetskrav kan en dörrmonteradläsare med inbyggd motorstyrning av dörrens ordinarie regellås vara ett kostnadseffektivt alternativ till en traditionell lösning med motorlåshus.

NoKey-523/524 KG20 är en beröringsfri läsare med inbyggd motor för montering på dörr med befintligt låshus försedd med hak- eller rakregel. Vid godkänd identifiering på läsaren drar motorn in regeln och låset kan öppnas med trycket (handtaget). Från dörrens insida styrs låsmotorn med den i kapslingen för elektronik/mekanik inbyggda öppnaknappen eller via motorvredet. Läsenheten kan även förses med cylinder för att mekaniskt från utsidan kunna låsa ut och in regeln.

NoKey-523/524 KG20 passar för montering på vanliga dörrar med godkända regellås av nordisk standardtyp ASSA 8765, 410 eller DORMA 912

och behöver varken DB-50 eller annan elektronik för att ansluta till undercentral UC-50. Kabel för kommunikation och strömförsörjning dras på/ genom dörrblad och karmöverföring krävs.

 Reglat eller oreglat läge kan förutom att styras av godkänd identifiering i läsaren även definieras av tidkanal eller larmets läge.

I Mifare-utförande fungerar NoKey-523/524 KG20 även som initieringsläsare för NoKey offline.

Modellerna är provade enligt SS-EN15684, 1.6.0.4- F.3.1.

Modellen 523 KG20 uppfyller kraven SSF-3522- 1091 enligt klass 3.

Modellen 524 KG20 uppfyller kraven SSF-3522- 1091 enligt klass 2B

Elektroniskt styrd dag- och nattlåsning av mekaniska regellås

![](_page_41_Figure_2.jpeg)

Dörrar i miljöer med höga säkerhetskrav ska vara säkert låsta nattetid och enkla att låsa upp dagtid.

Traditionellt har lösningen varit att montera ett motorlåshus för nattlåsning och nyttja ett elslutbleck styrt av en passerläsare för daglåsning. En väl fungerande lösning men där kostnaden både för låsenheter och installationen blir relativt hög. Ett kostnadseffektivt alternativ kan istället vara att använda en läsare med inbyggd motor för styrning av dörrens ordinarie mekaniska regellås.

NoKey-523/524 KG21 är en beröringsfri läsare med inbyggd motor för montering på dörr med befintligt låshus försedd med hak- eller rakregel. Vid godkänd identifiering på läsaren drar motorn in regeln och yttre trycket (handtaget) kopplas till tryckesfalllet varvid dörren kan öppnas. Från dörrens insida är tryckesfallet alltid inkopplat och låsmotorn styrs med den i kapslingen för elektronik/mekanik inbyggda öppnaknappen eller via motorvredet. Under dagtid, definierat av

tidkanal eller styrd av larmets läge, kan låshuset vara oreglat och enbart tryckesfallet kopplas in vid godkänd identifiering.

Läsenheten kan även förses med cylinder för mekanisk från utsidan kunna låsa ut och in regeln.

NoKey-523/524 KG21 passar för montering på vanliga dörrar med godkända regellås av nordisk standard typ ASSA 8765, 410 eller DORMA 912,919 och behöver varken DB-50 eller annan elektronik för att ansluta till undercentral UC-50. Kabel för kommunikation och strömförsörjning dras på/genom dörrblad och karmöverföring krävs.

I Mifare-utförande fungerar NoKey-523/524 KG21 även som initieringsläsare för NoKey offline.

Online-läsaren med inbyggd motor i kombination med ett godkänt regellås förenar hög mekanisk hållfasthet och brytskydd med enkel montering och handhavande.

Låsstyrning med lokalbuss-ansluten läsare och IO

![](_page_42_Figure_2.jpeg)

Läsare som ansluts direkt till lokalbuss (Reader-50) har vanligtvis inga egna in- eller utgångar. För dörrstyrning med den typen av läsare krävs att den kombineras med lediga in och utgångar på exempelvis en IO-5044. Då alla in och utgångarna i systemet är programmerbara erhålls samma möjlighet till styrningar med lokalbuss-ansluten läsare som i en dörrmiljö med läsare ansluten till exempelvis en DB-50/DIO-5084. Antalet in- respektive utgångar måste finnas tillgängliga i förhållande till behovet man har för dörrmiljön.

I exemplet ovan visas en enkel dörrstyrning med

knappöppning. Om även dörravkänning eller kolvlägesindikering önskas kompletterar man med en eller flera ingångar. För detta ändamål kan ytterligare en IO5044 eller DIO-5084 anslutas, alternativt nyttjar man lediga ingångar på annan närliggande enhet.

Skillnaden med att bygga en anläggning med lokalbuss- anslutna läsare (Reader-50) och IO enheter jämfört med att ansluta läsare till dörrkontrollenheter typ DB-50/DIO-5084 är att lösningen med IO enheter vanligtvis resulterar i mer kabeldragning då man ofta centraliserar utrustningen till exempelvis ett el-rum.

# **Låsstyrning** 5.11 Virtuella dörrar

Kontroll av dörrar utan kortläsare

![](_page_43_Figure_2.jpeg)

En virtuell enhet (eller virtuell kortläsare) kan enklast beskrivas som en dörrmiljö av typ "Reader-50" utan kortläsare. Den virtuella enheten används exempelvis i passersystemet för att länka ihop en ingång med en utgång eller om man vill tidstyra ett lås eller låta låset följa larmets läge. Ett vanligt användningsområde är för kontroll av utrymningsdörrar.

Virtuella enheter erhålls genom att man i egenskaper för en undercentral, med lediga enhetsplatser för dörrmiljöer, väljer de antal virtuella dörrar man behöver. Efter hämtning av anknytning finns de virtuella dörrmiljöerna sedan tillgängliga i enhetsträdet med motsvarande inställningsegenskaper som för en fysisk läsare.

De virtuella dörrarna kan ingå i en eller flera behörighetsgrupper

# **Låsstyrning** 5.12 Offline-läsare för mekaniska regellås

Beröringsfri offline-läsare med integrerad tryckeslåsfunktion

![](_page_44_Figure_2.jpeg)

Dörrar på svårtillgängliga platser eller innerdörrar som saknar elektronisk låsning kan med läsaren NoKey ingå i passersystemet utan behov av kabeldragning. NoKey är en beröringsfri läsare som utan åverkan monteras på dörr med låskista av nordisk standard. Vid godkänd identifiering i NoKey-läsaren kopplas trycket (handtaget) till fallkolven. Inre trycket för utpassering är alltid inkopplat.

Behörigheten som används för identifiering i läsaren bär användarna med sig på kodmedia (kort/tag) av typ Mifare Classic eller Mifare DESFire EV2. Behörighet laddas på kodmedia vid passering av utvalda Mifare-läsare (initieringsläsare) i det trådbundna online-systemet. Behörighetens giltighetstid är valbar från 1–48 timmar, 1–365 dagar eller oändligt och förnyas vid passering av en initieringsläsare. Via kodmediet överförs händelseloggar och exempelvis batteristatus tillbaka till online-systemet. Kodmediet kan också valbart medföra information om andra kort som ska spärras i NoKey-läsaren.

NoKey-läsaren strömförsörjs normalt med 5st AA-batterier men har även möjlighet att ansluta extern strömmatning via en enkel strömadapter. I händelse av strömbortfall kan ett 9-voltsbatteri användas som reservkraft och anslutas från läsarens utsida.

NoKey offline finns i flera olika utföranden, med och utan tangentbord, med eller utan möjlighet till låscylinder samt med eller utan vred för påverkan av låsregel från insidan. All mekanik för inkoppling av handtaget är placerad på insidan av dörren vilket ger hög säkerhet mot manipulation och sabotage.

Ersätt den mekaniska cylindern med elektronisk cylinder med inbyggd beröringsfri läsare.

![](_page_45_Figure_2.jpeg)

Dörrar på svårtillgängliga platser eller innerdörrar som saknar elektronisk låsning kan med LockR Cylinder inkluderas i passersystemet utan att vara fysiskt ansluten via kabel. LockR är en låscylinder med inbyggd beröringsfri läsare om ersätter en mekanisk låscylindern av typ rundcylinder. Vid godkänd identifiering i LockR Cylinder kopplas enheten in och man kan låsa upp regeln genom att vrida på vredet likt en nyckel. Öppningen av dörren sker med ordinarie trycke.

Behörigheten som används för identifiering i läsaren bär användarna med sig på kodmedia (kort/tag) av typ Mifare Classic eller Mifare DESFire EV2. Behörighet laddas på kodmedia vid passering av utvalda Mifare- läsare (initieringsläsare) i det trådbundna online-systemet. Behörighetens giltighetstid är valbar från 1–48 timmar, 1–365 dagar eller oändligt och förnyas vid passering av en initieringsläsare. Via kodmediet överförs valbart händelseloggar och exempelvis batteristatus tillbaka till online-systemet.

Kodmediet kan också valbart medföra information om andra kort som ska spärras i offline-läsaren. LockR Cylinder finns i flera olika utföranden beroende på krav på låsklass, utseende på cylinderring samt typ av låskista (90 eller 360 graders vridning).

### **Utrymningsöppning** 6.1 Lås med omvänd funktion och förreglad matning

Automatisk upplåsning av utrymningsdörrar direktstyrt från externt system t. ex. brandlarm

![](_page_46_Figure_2.jpeg)

För att underlätta utrymning av lokaler kan dörrar som hanteras av R-CARD 5000 styras till olåst t. ex. vid brandlarm. För att säkerställa öppning även om spänningsmatningen försvinner till system och därmed de elektriska låsen, används elektriska lås med s.k. omvänd funktion dvs. elslutbleck som är olåsta utan arbetsström och låsta vid arbetsström. Elslutbleck med

omvänd funktion matas från DB-50 via separata ledare styrd från externt system (brandlarm) som ger en förreglad matningsspän ning. DB-50 matas i övrigt på vanligt vis från lokalbuss. Även om ledningar brinner av kommer aktuella dörrar att ställas i olåst läge. Genom att lösningen har få kom ponenter mellan styrande system och elektriskt lås, är funktionssäkerheten stor.

# **Utrymningsöppning** 6.2 Nödöppning/paniklåsning

Automatisk upplåsning/låsning av dörrar styrt av R-CARD M5 MEGA

![](_page_47_Figure_2.jpeg)

R-CARD 5000 med M5 MEGA kan programmeras att styra olåst på valda dörrar.

Brandöppningsfunktionen är enkel att installera då brandlarmssignal endast behöver anslutas på ett ställe i systemet. Dock är öppningsfunktionen avhängig att elektroniken fungerar.

Funktionen nödöppning kan även användas för att blockera eller låsa en olåst dörr. Vilken typ av larmhändelse som ska aktivera funktionen styrs av vald larmkaraktär.

### **Dörrautomatikstyrning** 7.1 Förregling av dörrautomatik

Styrning av dörrautomatik och elslutbleck från DB-50 med möjlighet till dag och nattaktivering av motorlås

![](_page_48_Figure_2.jpeg)

Av olika skäl kan det vara praktiskt att dörrar öppnar automatiskt dvs. ingen handkraft fodras från användaren. Det kan vara för att underlätta för funktionshindrade, för in- och utlastning eller av bekvämlighetsskäl.

Vid programmerat, olåst t.ex. under dagtid, ombesörjer DB-50 aktivering av dörrautomatik först vid påverkan av armbågskontakt. Dörrautomatiken på - verkas i detta fall inte av att dörren är programmerad olåst.

Är dörren i normalläge d.v.s. låst, sker upplåsning av elslutbleck vid godkänt kort eller öppnaknapp, utan att dörrautomatiken aktiveras. För användare som även då dörren är i normalläge har behov av att dörren öppnar automatiskt kan funktionen dörröppning för funktionshindrade aktiveras på kort eller behörighetsnivå. DB-50 hanterar då både upplåsning av elslutbleck och aktivering av dörrautomatik vid godkänt kort.

Vid påverkan av armbågskontakt UT i normalläget ombesörjer DB-50 både upplåsning av elslutbleck samt aktivering av dörrautomatik.

Vid behov kan dörren även kompletteras med motorlås för ökad säkerhet (streckade signaler i ritningen). Se även 5.7 Dag- och nattlåsning.

### **In- och utläsning** 8.1 In- och utpassering via kortläsare

Utpassering med läsare av typ Reader-509 tillsammans med inläsare av typ Reader-509

![](_page_49_Figure_2.jpeg)

Särskild läsare för utpassering kan användas som alternativ eller komplement till öppnaknapp då det är viktigt att veta vem som passerat ut och vid vilken tidpunkt. Risken för manipulation av öppna knapp kan också minskas exempelvis nattetid genom att då styra över från öppnaknapp till krav på utpassering med kort. Med kontrollerad in- och utpassering ges även möjlighet till närvarokontroll och användning av anti-passbackregler.

Om inget krav finns för skilda behörigheter för inoch utpassering ansluts utläsare direkt till

samma DB-50/DIO-5084 som används för inläsaren. DB- 50/DIO-5084 kommer att styra samma elektriska lås för både in- och utpassering. Vilken säkerhetsnivå, kort och kod eller enbart kort, som ska gälla för utpassering är en valbar inställning för läsaren. Enbart kort för utpassering går även att kalenderstyra om man har olika krav på säkerhetsnivå olika dagar och tider.

Om krav på skilda behörigheter finns kombineras en läsare ansluten till DB/DIO med lokalbuss-ansluten läsare (Reader-50) kopplad mot relä för dubbel styrning till låset.

### **In- och utläsning** 8.2 In- och utpassering via rotationsgrind

In- och utpassering via rotationsgrind med läsare av typ Reader-60

![](_page_50_Figure_2.jpeg)

För vissa speciella dörrmiljöer som exempelvis rotationsgridar eller speed gates kan det finnas behov för separat styrning för utpassering. DB- 50/DIO-5084 med två anslutna läsare kan valbart ställas in för att fungera med separat lås-styrning för in- respektive utpassering. Signalen för utpasseringen kan förutom att

styras från en utpasseringsläsare även erhållas vi öppnaknapp eller rörelsedetektor.

Om krav finns för skilda behörigheter för in- och utpassering använder man en separat DB/DIO med ansluten läsare för utläsning.

# **In- och utläsning** 8.3 In- och utpassering via grind

Utpassering med läsare av typ Reader-509 tillsammans med inläsare av typ Reader-509

![](_page_51_Figure_2.jpeg)

Separat läsare för utläsning kan användas som alternativ eller komplement till öppna knapp då man vill ha registrering på vem som passerat ut. Detta kan även tidstyras så att man på natten kräver utläsning och inte kan öppna med knappöppningen. Läsare som placeras utanför fasaden på en byggnad exempelvis på en grind måste av elsäkerhetsskäl anslutas till en isolerad variant av DIO-5084. Max tillåten längd på terminalbuss RS-485 är 100m.

# **Larmförbikoppling**

9.1 Bonnförbikoppling

Lokal larmförbikoppling av dörrkontakt som är larmgivare till externt larmsystem

![](_page_52_Figure_3.jpeg)

Dörrar med punktskydd som exempelvis ingår i skalskydd, har ofta magnetkontakt som larmgivare och är alltid tillkopplade. Om man ska kunna passera utan att utlösa larm ska passersystemet vid godkänd passering förbikoppla larmpunkten under den tid det tar att passera.

När larmpunkten är ansluten till externt larmsystem måste själva larmkontakten i givaren kortslutas vid godkänd passering. DB-50 har utgång som sluter under inställd tid, vilket är dörröppningstid inklusive förlarmstid och summertid för dörr uppställd.

Vid godkänd passering, dvs. godkänt kort eller öppnaknapp, kommer larmpunkten förbli förbikopplad tills ovan nämnda tid löper ut eller dörren stängs och låses, varpå förbikopplingen bryts ned.

Öppnas dörren utan att det föregås av läsning av godkänt kort eller öppnaknapp, exempelvis genom uppbrytning eller att nyckel eller vred används, sker ingen förbikoppling av magnetkontakten varför larm utlöses.

S.k. bonnförbikoppling är enkel att utföra men har svagheten att ledningar med den förbikopplande signalen ej är övervakade. Det behövs endast att kabelparen kortsluts, så är larmet förbikopplat utan att systemet känner av det. Dessutom behövs två magnetkontakter, en för dörrstyrning och en som larmgivare.

Lokal larmförbikoppling med DB-50 som "larmgivare" till externt larmsystem

![](_page_53_Figure_2.jpeg)

Dörrar med punktskydd som t. ex. ingår i skalskydd, har ofta magnetkontakt som larmgivare och är alltid tillkopplade. Om man ska kunna passera utan att utlösa larm ska passersystemet vid godkänd passering förbikoppla larmpunkten under den tid det tar att passera.

Larmpunkten dvs. magnetkontakten ansluts till ingång för dörravkänning på DB-50. Ingången har möjlighet för dubbelbalansering så säkerheten bibehålls. Externt larmsystem ansluter istället till utgång på DB-50 som programmeras att ge signal då passerutrustning känner uppbruten dörr och dörruppställd.

Vid godkänd passering, dvs. godkänt kort eller öppna - knapp, kommer larmpunkten att förbikopplas tills programmerad tid löper ut eller dörren stängs och låses, varpå förbikopplingen bryts ned.

Öppnas dörren utan att det föregås av läsning av godkänt kort eller öppnaknapp, t.ex. genom uppbrytning eller att nyckel eller vred används, sker ingen förbikoppling av magnetkontakten varför larm utlöses.

Endast en magnetkontakt behövs för både dörr - styrning och som larmgivare. Kabel mellan magnetkontakt och DB-50 såväl som kabel mellan DB-50 och externt larmsystem, är övervakade med dubbel balansering. Dock är DB-50 ej godkänt larmmaterial så anläggning kan ej godkännas utan dispens.

### **Larmförbikoppling** 9.3 Larmpunkt i integrerat larmsystem

Lokal dörravkänning och larmförbikoppling i integrerat system

![](_page_54_Figure_2.jpeg)

Dörrar med punktskydd som t. ex. ingår i skalskydd, har ofta magnetkontakt som larmgivare och är alltid tillkopplade. Om man ska kunna passera utan att utlösa larm ska passersystemet vid godkänd passering förbikoppla larmpunkten under den tid det tar att passera.

Larmpunkten dvs. magnetkontakten ansluts till ingång för dörrövervakning på DIO-5084. Ingången har möjlighet för dubbelbalansering och är då även övervakad.

Vid godkänd passering, dvs. godkänt kort eller öppna - knapp, kommer larmpunkten att förbikopplas tills programmerad tid löper ut eller dörren stängs och låses, varpå förbikopplingen bryts ned.

Öppnas dörren utan att det föregås av läsning av godkänt kort eller öppnaknapp, t. ex. genom uppbrytning eller att nyckel eller vred används, sker ingen förbikoppling av magnetkontakten varvid larm utlöses.

Endast en magnetkontakt behövs för både dörr - styrning och som larmgivare. Godkänd lösning utan dispens/undantag.

Larmstyrning av externt larmsystem vid dörr med läsare

![](_page_55_Figure_2.jpeg)

Manövrering på kortläsare av larmat utrymme (larmområde) med till- och frånslag av externt larm styrt från DIO/DB-50. Styrning av volymskydd görs direkt från kortläsare.

Används vid dörrar som leder in i larmad zon.

Behörig användare kan med #, kort och PIN via läsarens knappsats eller som menyval i Reader 509, låta styra larmutgången på ansluten DIO/ DB50 ansluten till ingång på centralapparat eller anslutningsenhet för det externa larmsystemet. Genom s.k. pulsstyrning kan flera läsare/DB-

50 anslutas mot samma ingång så att till- och frånslag kan ske från fler dörrar som leder in i det larmade utrymmet (larmområdet). Läsare ska vara i utförande med knappsats.

Krav på signal från centralapparat att larmet är på eller av s.k. återkoppling.

Okomplicerad lösning för en eller få dörrar. Vid stort antal dörrar blir kabelförläggningen mer omfattande och svår vilket gör att en styrning via larmområden är att rekommendera.

Larmstyrning av externt larmsystem med läsare i larmområde

![](_page_56_Figure_2.jpeg)

Manövrering av larmat utrymme (larmområde) med till- och frånslag av externt larmsystem direkt från kortläsare. Styrning av volymskydd görs direkt från kortläsare. Används vid dörrar som leder in i larmad zon.

Behörig användare kan med #, kort och PIN eller via menyval på Reader 509 från alla läsare som ingår i larmområdet, styra larmutgången på en ansluten DB-50/DIO-5084 eller IO-50xx, som ansluts till ingång på centralapparat eller anslutningsenhet för det externa larmsystemet. Läsare ska vara i utförande med knappsats.

Krav på signal från centralapparat att larmet är på eller av s.k. återkoppling.

Då endast en enhets utgång behövs för många läsares styrning av larmet, reduceras kabeldragningen väsentligt. Enheten med larmstyrande utgång kan dessutom placeras i närhet av centralapparat för larmsystemet, vilket ytterligare förenklar utförandet.

### **Larmstyrning** 10.3 Integrerat larm från läsare

Larmstyrning av integrerat larm vid dörr med DIO-5084

![](_page_57_Figure_2.jpeg)

Manövrering av larmat utrymme (larmområde) med till- och frånslag av integrerat larm direkt från kort - läsare. Styrning av volymskydd görs direkt från kort läsare. Används vid dörrar som leder in i larmad zon. Behörig användare kan med #, kort och PIN via alla läsare som ingår i larmområdet, styra larmet.

Möjlighet finns även till s.k. "köpa tid" funktion, både i form av standardtid eller som egen vald tid via manöverkod. Används läsare 509 kan styrning av larmområde och "köpa tid" även utföras via menyval. Läsare ska vara i utförande med knappsats. Inga extra anslutningar krävs, all funktion är inbyggd och integrerad.

### **Larmstyrning** 10.4 Integrerat larm från manöverpanel MapR 509

Larmstyrning av integrerat larm med manöverpanel MapR 509

![](_page_58_Figure_2.jpeg)

Manövrering av fler larmade utrymmen (larmområden) med till- och frånslag av integrerat larm från manöverpanel alternativt direkt från kortläsare. Manöverpanel används centralt placerad exempelvis vid gemensam entré för dörrar in mot olika larmområden. Används kortläsare som förbikopplare för inpasseringsväg,

och frånkoppling av larmområden utförs från MapR 509 placerad i övervakat område, erhålls en fullt SSF130-godkänd styrning. Från manöverpanelens menyval hanteras behörighetsstyrt de integrerade larmsystemet (MEGA) samtliga larmområden, upp till 255st.

### **Larmstyrning** 10.5 Integrerat larm från manöverpanel MapR-Touch 50

Anslutning av MapR-Touch 50 för larmstyrning av integrerat larm

![](_page_59_Figure_2.jpeg)

![](_page_59_Figure_3.jpeg)

Manöverpanel med manövrering via touchskärm. MapR-Touch hanterar integrerade larmsystemets (MEGA) samtliga larmområden (255). Förutom all styrning som finns i övriga manöverpaneler från RCO presenterar även MapR-Touch åtgärdstexter vid avvikelser ifrån normalfunktion. Åtgärdstexterna är fritt definierbara per larmingång.

Panelen anpassar funktion och grafiskt gränssnitt beroende på användare som hanterar larmet. En normalanvändare skall enkelt kunna hantera larmet och vid enkla funktionsfel få tydlig information och åtgärdsinstruktioner.

Manöverpanelen presenterar OR-ritningar i touchskärmen. På ritningen visas och hanteras även de larmområden och larmpunkter som är konfigurerade i MEGA larmsystemet.

MapR-Touch ansluts via Ethernet till IP-50-modul i UC- 50. Anslutningen kan variera beroende på om installationen ska följa krav i SSF130 eller ej.

Bild 1 visualiserar en korrekt anslutning enligt SSF:s norm. Bild 2 visualiserar en anslutning som kräver en avvikelse i anläggarintyget om larmsystemet

### **Larmanslutning** 11.1 IO-50xx eller DB-50

Passiva larmgivare anslutna till IO eller DB

![](_page_60_Figure_2.jpeg)

I befintliga R-CARD 5000-system kan behov uppståför att ansluta larmgivare. Om larmgivarna är passiva i meningen att de inte behöver strömförsörjas som t.ex. magnetkontakter eller andra kontakter, kan lediga ingångar på IO- eller DB- enheter exempelvis en DB-50 användas för anslutning.

Ingångarna kan ställas som dubbelbalanserade (2,2k) och blir därmed övervakade. Om sedan

R-CARD M5 uppgraderas till MEGA får man övrig larmhantering.

Det blir enkelt och billigt att ansluta och hantera larm. Endast larmgivare som inte behöver strömförsörjning kan användas om inte separat matning ordnas.

Ej SSF-godkänt

### **Larmanslutning** 11.2 DIO-5084 med läsare

Larmgivare anslutna till DIO-5084 som DB med ansluten läsare

![](_page_61_Figure_2.jpeg)

I många anläggningar finns ett antal larmpunkter samlade kring dörrar och man önskar ansluta larmgivare av olika typ, t. ex. magnetkontakter men också rörelsedetektorer och glaskrossdetektorer. De sen are ska också strömförsörjas med normalt 12 VDC.

DIO-5084 med ansluten läsare kan, utöver att styra och övervaka dörr och lås, också ansluta upp till 8 larmgivare. I praktiken åtgår en sektionsingång för öppnaknapp och en för magnetkontakt på dörren (vilken i sig också blir larmgivare) så det blir 6 lediga sektionsingångar.

Sektionsingångarna kan vara dubbelbalanse-

rade och har anslutningar för 12 VDC strömförsörjning av detektorer. Sling resis ten sen kan programmeras för dubbelbalanseringen vilket möjliggör anpassning mot och anslutning av befintligt installerade detektorer. Återställning av glaskrossdetektorer kan ske genom brytning av matningsspänning.

Det finns fyra utgångar på DIO-5084 2 st relälämpliga för styrning av ellås samt 2 utgångar (12VDC) för anslutning av siren eller blixtljus och skall ej användas till ellås.

I R-CARD M5 MEGA är DIO-5084 godkänd enligt SSF1014 larmklass 3/4.

### **Larmanslutning** 11.3 DIO-5084 utan läsare

Larmgivare anslutna till DIO-5084 som IO utan läsare

![](_page_62_Figure_2.jpeg)

DIO-5084 utan läsare kan ansluta upp till 8 larmgivare på individuella sektionsingångar. Sektionsingångarna kan användas som dubbel balanserat eller enkelbalanserat (strömslinga). Enkelbalanserat kan användas för glaskross och branddetektorer. Återställning av enkelbalanserat byglas för 4 ingångar åtgången alternativt

kan en separat återställnings/matning nyttjas. Motståndsvärdena på dubbel balanserat kan justeras inviduellt.

I R-CARD M5 MEGA är DIO-5084 godkänd enligt SSF1014 larmklass 4.

# **Larmindikering** 12.1 Indikering via utgång på enhet

Larm indikering när en icke korrekt låsning utförs med motorlås

![](_page_63_Figure_2.jpeg)

Ansluts motorlåsets ankarkontakt/statussignal till RCARD 5000-systemet finns möjlighet att erhålla larm samt indikering när dörren inte reglas korrekt vid aktivering av låsregel.

Funktionen fås vid följande inställningar i systemet: En "Dörrstyrning" från en utgång på DIO-5084 styr motorlåsets elektronik, som i sin tur aktiverar motorlåset. Dörrlägesgivare ansluts till ledig ingång på DIO:n som "Dörravkänning". Motorlåsets regel aktiverar en ankarkontakt vid regelmanöver, denna kontakt ansluts också till en ledig ingång på DIO:n som "Låskolvsläge". För att erhålla larm från dessa givare drar man in dem som virtuella larmpunkter i ett larmområde som "Låskolvsfel" och "Dörravkänning uppbruten".

Indikering för låskolvsfel kan tas ut från valfri ledig utgång, exempelvis från en IO som "Låskolvsläge från dörrmiljö".

# **Larmindikering** 12.2 Indikering i R-TOUCH 50 och R-CONTROL

Varning för öppen larmsektion innan tillkoppling

![](_page_64_Figure_2.jpeg)

En öppen dörr eller fönster kan förhindra att larmet tillkopplas som det är tänkt. I en större anläggning kan det därför vara praktiskt att på ett enkelt sätt, innan tillkoppling av larmet, kunna se om dörrar eller fönster är öppna.

Genom att för den larmpunkt som övervakar dörren eller fönstret komplettera egenskapsfältet "Varning för fel innan tillkoppling" med en beskrivande text erhålls möjligheten att i manöverpanelen R-TOUCH 50 och i det grafiska presentationsprogrammet R-CONTROL varna om att larmpunkten är öppen.

I R-TOUCH 50 visas varningen efter inloggning som en grafisk symbol, gul varningstriangel med utropstecken, placerad över lampunktens ordinarie ikon och som varningstext i samband med att ett larmområde valts för att tillkopplas. Väljer man att en ritningsbild i R-TOUCH 50 ska visas publikt blir varningarna även synligt utan krav på inloggning i manöverpanelen.

I det grafiska presentationsprogrammet R-CON-TROL visas larmpunkten med gul bakgrund om den inte är stängd och klar för tillkoppling.

# **Larmindikering** 12.3 Väsentlig funktion

Upplåsningskontroll av utrymningsväg

![](_page_65_Figure_2.jpeg)

För att säkerställa att exempelvis utrymningsdörrar blir upplåsta innan verksamhet börjar bedrivas i lokalerna kan systemets inbyggda stöd för summering av ingående dörrmiljöers låskolvsläge användas. Funktionen benämns ofta som "Väsentlig funktion". En summastatus från en ledig utgång i system och används för att exempelvis styra aktivering av huvudbelysning eller kassalinje. Förblir någon av låsen reglade vid frånkoppling av larmet förblir således funktioner som är väsentliga för verksamhet inte aktiverade.

Kravet för funktionen är att "Stöd för väsentlig funktion (låskolv summastatus)" aktiveras vid konfiguration av de undercentraler, UC-50, som har anslutna dörrar, utgångar för summa status eller larmområden som kommer att beröras av kontrollfunktionen.

Funktion fås med följande inställningar i systemet: Låsets regelkontakt ansluts till ledig ingång på en DIO-5084 som "Låskolvsläge olåst".

Dörren läggs till i larmområdet och "Ingår i väsentlig funktion (låskolv summastatus)" aktiveras som egenskap för dörrmiljön.

Larmområdet kopplas till en ledig utgång med egenskapen "Väsentlig funktion hållande" alternativt "Väsentlig funktion följande".

**Hållande** innebär att efter frånkoppling av larmområdet så blir utgången aktiv när samtliga kolvlägen i larmområdet är i olåst läge och utgång förblir i detta läge (oavsett om någon blir låst) tills området tillkopplats igen.

**Följande** innebär att utgång blir aktiv när samtliga kolvlägen i larmområdet är i olåst läge och faller så fort någon av valda kolvlägena övergår till låst läge.

För att inkludera övervakning av dörrar som ej har inkopplade läsare i funktionen, exempelvis utrymningsdörrar, skapas virtuella dörrmiljöer. Observera att virtuell dörr tar dörrplats i UC-50.

Kompletteras larmområdet med den virtuella larmpunkten "låskolvsfel" för ingående dörrar så kontrollerar systemet även att låsen regalas vid tillkoppling av larmområdet. Uppstår ett fel larmar systemet för tillkopplingsfel på området och orsaken visas i manöverpanelen.

För utökad kontroll kan även systemets driftövervakning användas för att informera ansvarig personal via e-post eller SMS att samtliga dörrar låst upp alternativt blivit låsta.

### **Hisstyrning** 13.1 En hiss i ett schakt

Läsare i hisskorg för att ge tillträde till förutbestämda våningar

![](_page_66_Figure_2.jpeg)

Som med övrig styrning av tillträde vill man hantera behörigheten i pas sersystemet för att låta köra hissen mellan våningar.

Läsare av typ 509 placeras i hisskorgen för användare att identifiera sig med kort eller nyckelbricka eventuellt tillsam mans med PIN. Beroende på behörighet ger systemet tillträde till en eller flera våningar genom att aktivera utgång(ar) på ansluten IO-5004/08. Utgångarna kopplas till automatik för hiss så att användare genom hissens ordinarie tastatur kan köra hissen till vald våning. För fler än 8 våningar med individuell behörighet, används ytterligare IO-5004/8 upp till maximalt 8 enheter dvs. maximalt 64 våningar.

Hisstyrningsfunktionen kan även användas för behörighetsstyrd dörröppning. Observera att endast dörrstyrning kan åstadkommas. Om exempelvis knappöppning krävs måste en virtuell dörrmiljö skapas samt parallel koppling av låsstyrning, virtuell dörr tar plats i UC:n.

Läsare och IO-enheter ska vid styrning av hiss tillhöra samma UC.

# **Hisstyrning** 13.2 Fler parallella hissar och schakt

Läsare i varje hisskorg för parallella schakt, för att ge tillträde till bestämda våningar

![](_page_67_Figure_2.jpeg)

Våning 0

Olika tillträde kan sträcka sig över en eller flera våningar i en fastighet där fler parallella his sar (batteri) används. Som med övrig styrning av tillträde vill man hantera behörigheten i passer systemet, för att låta köra his sar mellan våningar.

Läsare av typ 509 place ras i varje hisskorg för använ da re att identifiera sig med kort eller nyckelbricka even tuellt tillsammans med PIN. Beroende på behörighet ger systemet tillträde till en eller flera våningar genom att aktivera utgång(ar) på ansluten och för hissen aktuell IO-5004/08. Utgångarna kopplas till hiss automatik så att användare ge nom hissens ordinarie tastatur, kan köra hissen till vald våning. För fler än 8 våningar med individuell behörighet, används ytterligare IO-5004/8 upp till maximalt 8 enheter dvs. maximalt 32 vån ingar för 2 hissar, 16 våningar för 4 hissar och 8 våningar för 5-8 hissar.

**OBS** att aktuell UC-50 ska kunna hantera antalet 509 läsare i hissarna.

# **Hisstyrning** 13.3 Våningsläsare för kallelse

Läsare på våningsplan att användas för att kalla på hiss

![](_page_68_Figure_2.jpeg)

Ibland vill man styra behörigheten för att åka hiss genom att använda kortläsare för att kalla på hiss.

Läsare placeras på varje våningsplan vid hissdörr för att antin gen direkt eller indirekt kalla på hiss en. Direkt i betydelsen att endast godkänd läsning behövs för att kalla, eller indirekt genom att godkänd läsning efterföljs av tryckning på ordinarie knapp för att kalla. Utgångarna kopplas till his s - automatik som kör hissen till kalllande våning. För fler än 8 våningar, måste ytterligare UC-50 och IO-5004/8 användas.

# **Porttelefon** 14.1 Porttelefon för entréer

Porttelefoni med portapparat PA-519 som ringer till besöksmottagare

![](_page_69_Figure_2.jpeg)

I framförallt flerbostadsfastigheter önskar man ge tillträde med beröringsfri läsare för boende och porttelefon för besökare. Besökare ska genom att antingen slå telefonnummer eller kortnummer till den boende, identifiera sig genom samtal med den boende på dennes telefon.

Med portapparat PA-519 får boende kortläsarfunktion och besökare möjlighet för porttelefon. Porttelefonen ringer upp boendes egen telefon varvid denne kan öppna för besökaren under pågående samtal.

PA-519 avläser beröringsfritt kort och nyckelbricka, (ev. med PIN) eller gruppkod.

Som portapparat medgerPA-519 dubbelriktad talkommunikation mellan besökare och boende som använder egen telefon som svarsapparat. Boende kan under pågående samtal via PA-519 låsa upp aktuell port. För samtal till boende kan

besökare använda telefonnummer till boende om det är känt, kortnummer visad på namntavla eller om PA-519 används välja den person man vill ringa upp i portapparatens inbyggda display för boende register. PA- 519 har inbyggd utgång för styrning av lås och ingång för öppnaknapp.

För att uppfylla gällande krav på tillgänglighetsanpassning kan installationen komplettares med IOkort för möjlighet att styra dörrautomatik vi öpning.

Genom att PA-519 nyttjar befintligt telenät blir kostnaden för kabelförläggning liten. Dock får man en löpande kostnad för abonnemang och samtal.

För den som vill slippa investera i särskild portappparat finns mobilappen RCO Access som ett alternativ till traditionell porttelefoni.

### **Bokning - information** 15.1 Maskinstyrning via Electrolux Network™

Bokningspanel Electrolux Vision Light™ för bokning av tvättstuga med Electrolux Network™ anslutna maskiner

![](_page_70_Figure_2.jpeg)

För att hindra obehörigt användande av tvättmaskiner ska endast behörigt bokade användare ges tillträde till tvättrum och möjlighet att starta maskiner. Om moderna maskiner från Electrolux används, kan en förreglande funktion erhållas genom Electrolux Network™ anslutning av maskiner till Electrolux Network Master™.

Dessutom kan då maskinerna styras och övervakas intelligent, t. ex. kan driftlarm skickas ut genom R-CARD M5. Electrolux Vision Light™ används som bokningstavla vid bokning av tvättstuga m.m.

Electrolux Vision Light™ avläser beröringsfria kort och taggar för att identifiera användare vid bokningstillfället och vid nyttjandet av bokningsobjektet, typiskt en tvättstuga, på den bokade tiden.

Electrolux Vision Light™ monteras på vägg, i för användare lämplig höjd att betrakta display och att manövrera med knapparna. Funktionen kan även erhållas med Electrolux Vision™ kompletterad med Electrolux Network Master™ för kommunikation med maskiner via Electrolux Network™.

### **Bokning - information** 15.2 Maskinstyrning via Electrolux Network™ och Basic interface

Med Electrolux Network Master och Basic Interface för relästyrning samt återkoppling

![](_page_71_Figure_2.jpeg)

Med Electrolux Basic interface kan man relästyra samt ta in en återkoppling. Basic interfacet kan användas till att styra andra maskiner än Electrolux samt annan typ av utrustning där man vill förhindra att utrustningen kan nyttjas utan aktiverat pass. Återkopplingen säkerställer att man faktiskt har nyttjat maskinen/utrustningen och används med

fördel i kombination med debitering (extra licens).

Basic interfacet ansluts på Electrolux Network och kan blandas med annan Electrolux utrustning såsom exempelvis Electrolux tvättmaskiner, torktumlare och torkskåp.Funktionen kan även erhållas i kombination med Electrolux Easy™.

### **Bokning - information** 15.3 Maskinstyrning via IO-enhetface

Bokningspanel Electrolux Vision Light™ för bokning av tvättstuga med IOboxanslutna tvättmaskiner

![](_page_72_Figure_2.jpeg)

För att hindra obehörigt användande av tvättmaskiner ska endast bokade användare ges tillträde till tvättrum och möjlighet att starta maskiner.

Förregling av äldre Electrolux eller andra fabrikat av tvättmaskiner styrs med IO-box. Vid styrning av tvättmaskiner ska styrutgångar i IO-box byglas för potential fri slutning eller brytning. Om utrustning med annan manöverspänning ansluts, ska mellanreläer användas. Vid förregling av maskiners matningsspänning skall dessutom lämpliga kontaktorer användas.

Funktionen kan även erhållas med Electrolux Vision™.

### **Bokning - information** 15.4 Tvättstuga med fler maskingrupper i samma tvättrum

Tvättstuga med gemensamt tvättrum och flera maskingrupper

![](_page_73_Figure_2.jpeg)

Reader-509

För att hindra obehörigt användande av tvättmaskiner ska endast bokade användare ges tillträde till tvättrum och till bokad maskingrupp.

På bokad tid vid tvättillfället, läses nyckelbrickan vid Electrolux Boka™ som öppnar dörr samt aktiverar passet. Detta innebär också att maskingruppen aktiveras så tvättmaskin kan startas detta sker via Electrolux Network™.

Andra funktioner som möjliggörs med Electrolux Network™ är kontroll av ledigpasstid i förhållande till tvättprogram, maskinen kan skicka eventuella felkoder, om debitering kan maskinen ge detaljerat underlag. Funktionen kan även erhållas med Electrolux Vision™ kompletterad med Electrolux Network Master™ för kommunikation med maskiner via Electrolux Network™.

### **Bokning - information** 15.5 Bokning med olika förval (bokningsobjekt)

Bokning med maskingrupper fördelade på flera rum

![](_page_74_Figure_2.jpeg)

För att hindra obehörigt användande av olika bokningsobjekt kan endast bokade användare ges tillträde till rummet. Vid aktiveringstillfället, på bokad tid, läses nyckelbricka vid Electrolux Easy™ som styr öppning av rätt tvättrum (med rätt maskingrupp). Easy tavlan kan även användas för spridning av information.

Läsare på yttre dörr styrs på vanligt vis av behö-

righet i R-CARD 5000. Bokningsfunktionen kan även kombineras med maskinstyrning enligt 15.1 och 15.2. För kommunikation med maskiner via Electrolux Network™ krävs Electrolux Network Master™, Interface i maskin och eventuellt Electrolux Basic Interface™ beroende på vald maskinmodell. Motsvarande bokningskontroll kan även utföras med Electrolux Vision Light.

### **Bokning - information** 15.6 Electrolux Easy™ med Electrolux Network™

Electrolux Easy™ som information och boknings tavla med maskinstyrning i tvättstugan

![](_page_75_Figure_2.jpeg)

Electrolux Easy™ monterad i trapphus för visning av trapphusregister, allmän information, personlig information, felanmälan och bokning. Samma trapphusregister kan med fördel publiceras även i PA-519. Vilka funktioner som skall visas/användas i Electrolux Easy™ konfigureras i R-CARD M5 klienten och styrs av användarens behörighetsprofil. PA-519 kan vid passage ge en speciell signal om man har ett personligt meddelande i Electrolux Easy™ panelen. Via tvättbokningen styrs tillträde till tvättstugan samt tillgång av maskinerna

via Electrolux Network™ vilket förhindrar nyttjande på icke bokad tid. Styrning av Easy-tavlans belysning kan antingen aktiveras vid lätt touch på skärmen, efter att passage har utförts alternativt med komplettering av en rörelsedetektor, ingång för detta finns i Electrolux Easy™.

Bokningsfunktionen har en mångfald av möjliga regelverk och begränsningsmöjligheter samt kan även kompletteras med möjlighet till debitering.

### **Bokning - information** 15.7 Electrolux Easy™ i trapphus

Electrolux Easy™ trapphusregister och information i trapphuset

![](_page_76_Figure_2.jpeg)

Electrolux Easy™ monterad i trapphus med PA-519 monterad som skalskydd till entrén. Båda delar informationen avseende trapphusregistret.

Registret administreras centralt och distribueras ut till både Electrolux Easy™ och till PA-519. I exemplet används även allmän information som automatiskt växlar bild med trapphus - registret.

Electrolux Easy™ används även till felanmälan

samt personlig information. Om personlig information erhålits ger PA-519 porttelefon ifrån sig ett ljud vid passage så man blir vars om att ett personlig meddelande finns.

MIF-66 läsaren är i exemplet tänkt som passage ner till källaren.

PA-519 i Mifare-utförande fungerar även som initieringsläsare för NoKey offline.

# **Fastighetsbox** 16.1 Elektroniskt styrda postfack

Fastighetsbox med elektroniskt styrda postfack och beröringsfri läsare

![](_page_77_Figure_2.jpeg)

För att underlätta postutdelning i exempelvis flerbostadshus kan fastighetsboxar användas. Boende låser bekvämt och säkert upp sitt postfack med samma nyckelbricka som används för tillträde i fastigheten. Vid godkänd identifiering i kortläsare monterad på eller i anslutning till postfacken öppnas det personliga facket.

För styrning av fastighetsboxens elektroniska lås kan boxen förses med en läsare från RCO ansluten till UC-50 och där IO-kort används för aktivering av de elektroniska låsen. En lösning som kan kontrollera upp till 64 postfack.

För fastighetsboxar med inbyggd läsare och i vissa fall elektroniska namnskyltar finns möjlighet för integration mot R-CARD M5 via R-CARD M5 Admin API/Easy. Molntjänsten som hanterar fastighetsboxens läsare och i förekommande fall boxens namnskyltar kan via API lösningen uppdateras med identifierare som lägenhetsnummer, namn och kortinformation vilket gör att den boende kan öppna postfacket med sin vanliga nyckelbricka.

### **Systembuss**

Systembuss används för datakommunikation mellan M5 Server och en UC-50 samt mellan UC-50. Kommuni kationen använder CAN (Controlled Area Network). Kabel ska ha ett partvinnat par för kommunikation. Inget krav på skärm. Om kabel med skärm används, var noga med anslutningen av densamma. Datakom muni ka tionen kan sträcka sig max 1 000 meter från första till sista inkopplade enhet på bussen.

### **Lokalbuss**

Datakommunikation med RS-485 och spänningsmatning från UC-50 till DB-50, IO-50XX, Reader-50, TEL-50, DIO-5084 och Electrolux Easy™. Kabel ska vara försedd med minst ett par (partvinnat) för kommunikation samt minst två ledare för spänningsmatning vars area dimensioneras efter totala strömuttaget på kabeln. För att öka arean för ström matande ledare kan fler eventuellt oanslutna par användas (dubbleras eller mer). Inget krav på skärm. Datakommunika tionen sträcker sig max 1 000 meter från första till sista på enhet inkopplad på bussen. Spänningsfall på matningen kan begränsa denna längd.

### **Flexkabel lokalbuss**

För karmöverföring rekommenderas flerkardelig kabel för att undvika utmattning i ledarna. Om ledningslängden mellan plintbox och PROX-508/MIF-508 ej överstiger 3 meter kan kommunikation utgöra en s.k. "stubbe" d.v.s. endast ett par används. Vid längre kabelväg ska lokalbussens datapar dras fram och tillbaka från läsaren, d.v.s. två par åtgår.

### **Terminalbuss**

Datakommunikation med I²C inklusive spänningsmatning mellan DB-50 och Reader-60 samt mellan BT-XX och UC-50. I²C kommunikation använder datasignal och klocksignal på separata ledningar. Signalerna ska aldrig ingå i samma par i en kabel, varför icke-partvinnad (fyrskruv) kabel rekommenderas. Om partvinnad kabel används ska plusmatning (eller minus) kopplas i par med data (eller klocka). Datakommunikationen mellan DB-50 och läsare, samt melllan BT-XX och UC-50 sträcker sig upp till 10 meter.

### **Korsad nätverkskabel**

Korsad nätverkskabel (UTP).

### **Terminalbuss RS-485**

Datakommunikation mellan omvandlarkort TB485 anslutet till terminalbusssplinten på DB-50 eller DIO-5084 och läsare typ 509. Kabel ska vara försedd med minst ett par (partvinnat) för kommunikation och två ledare för spännningsmatning. Datakommunikation mellan DIO/DB och läsare kan sträcka sig upp till 100 meter.

### **Signaler**

Överföring av digitala in- och utsignaler, med eller utan spänningsmatning, mellan DB-50, DIO-5084 och dörrmiljö (elektriskt lås, öppnaknapp, dörrkontakt, summer, etc.), extern larmcentralapparat (styrning larm till/ från), eller mellan IO-50xx och dörrmiljö (elektriskt lås, öppnaknapp, etc.), hissautomatik och hjälpreläer för t. ex. tvättmaskinstyrnig. Vald kabel ska erbjuda tillräcklig area för den ström som eventuell last kan dra. För olika installationer kan kabel med fler eller färre ledare vara aktuella, beroende på ledningsarea och last.

### **Larmsignaler**

Överföring av larmsignal från larmgivare med dubbeleller enkelbalanserad (strömslinga) till DIO-5084. Vissa larmgivare strömförsörjs också med 12 VDC i samma kabel.

### **LAN**

Datakommunikation över nätverk mellan M5 Server (PC serverstation) och M5 Klient (PC arbetsstation) och/eller UC-50 (med nätverksmodul IP-50). Nätverk kommmunicerar med Ethernet 100 Mbit/s (100 Base-TX) och med protokollet TCP/IP. Data - kom muni ka tionen sträcker sig upp till 100 meter punkt till punkt (inkl patchkablar). Nätverk "förlängs" normalt med annan nätverks utrustning som t ex hubbar, switchar, routrar.

### **Tele**

Telekommunikation mellan portapparater och TEL-50 samt anslutning av analog telelinje för TEL-50 och LS-50 PSTN.

### **Electrolux Network™**

Datakommunikation och internström - försörjning av interface för upp till 30 maskiner av fabrikat Electrolux. Sträcker sig max 500 meter med fri koppling.

| Bästa alternativ<br>Bra alternativ<br>Möjlig<br>Tele, halogenfri, oskärmad: | ■<br>▲<br>●                              | Systembuss | Lokalbuss | Flexkabel lokalbuss | Terminalbuss | terminalbuss RS-485 | Signaler | Larmsignaler | LAN | Tele | Electrolux Network |
|-----------------------------------------------------------------------------|------------------------------------------|------------|-----------|---------------------|--------------|---------------------|----------|--------------|-----|------|--------------------|
| ELQXB                                                                       | 2x2x0,5 (0,2 mm²)                        | ▲          | ▲         |                     | ●            | ▲                   |          | ■ ■          |     | ■    |                    |
| ELQXB                                                                       | 4x2x0,5 (0,2 mm²)                        | ▲          | ▲         |                     |              | ▲                   |          | ■ ▲          |     | ■    |                    |
| ELQXB                                                                       | 6x2x0.5 (0,2 mm²)                        | ●          | ●         |                     |              | ●                   | ▲        | ●            |     | ■    |                    |
| ELQXB                                                                       | 10x2x0,5 (0,2 mm²)                       | ●          | ●         |                     |              | ●                   | ●        | ●            |     | ■    |                    |
| ELQXB                                                                       | 2x2x0,5 (0,2 mm²)                        | ▲          | ▲         |                     | ●            | ▲                   |          | ■ ■          |     | ■    |                    |
| ELQXB                                                                       | 4x2x0,5 (0,2 mm²)                        | ▲          | ▲         |                     |              | ▲                   |          | ■ ▲          |     | ■    |                    |
| ELQXB                                                                       | 6x2x0,5 (0,2 mm²)                        | ●          | ●         |                     |              | ●                   | ▲        | ●            |     | ■    |                    |
| ELQXB                                                                       | 10x2x0,5 (0,2 mm²)                       | ●          | ●         |                     |              | ●                   | ●        | ●            |     | ■    |                    |
| FQQXB                                                                       | 6x0,22                                   |            |           |                     |              |                     |          |              |     |      |                    |
| 4-skruv, halogenfri, oskärmad:                                              |                                          |            |           |                     |              |                     |          |              |     |      |                    |
| ELQXB                                                                       | 1x4x0,5 (0,2 mm²)                        |            |           |                     | ■            |                     | ●        | ▲            |     |      |                    |
| EQQXB                                                                       | 1x4x0,5 (0,2 mm²)                        |            |           |                     | ■            |                     | ●        | ▲            |     |      |                    |
| Special, halogenfri, oskärmad:                                              |                                          |            |           |                     |              |                     |          |              |     |      |                    |
| RCO kabel                                                                   | 2x1x1,0 mm²+1x2x0,22mm2 (E-nr 48 866 62) |            | ■ ■       |                     |              | ■                   |          |              |     |      |                    |
| FLQQBR                                                                      | 2x1x1,0 mm²+2x2x0,22 mm²                 |            | ■ ■       |                     |              |                     |          |              |     |      |                    |
| FLAQQBR                                                                     | 4x1x1,0 mm²+1x2x0,22mm2                  |            | ■         |                     |              |                     |          |              |     |      |                    |
| FLAQQLY                                                                     | 2x1x1,0 mm²+1x2x0,22mm2 (inne och ute)   | ▲          | ▲         |                     |              |                     |          |              |     |      |                    |
| Electrolux nätverkskabel CMIS 4x0,22mm2                                     |                                          |            |           |                     |              |                     |          |              |     |      | ■                  |
| CAT, halogenfri, oskärmad:                                                  |                                          |            |           |                     |              |                     |          |              |     |      |                    |
| UTP LSZH                                                                    | (CAT 5e) 4x2x0,5 (0,2 mm²)               | ▲          | ▲         |                     |              | ▲                   | ● ●      |              | ■   |      |                    |
| UTP LSZH                                                                    | (CAT 6) 4x2x0,5 (0,2 mm²)                | ▲          | ▲         |                     |              | ▲                   | ●        | ●            | ■   |      |                    |

Angivna kabeltyper i tabellen ovan är enbart exempel på lämpliga kablar för installationen. Kablarnas beteckning kan avvika beroende på vald tillverkare. Vid kabelförläggning utomhus eller i mark rekommenderas kabel förstärkt med yttre mantel av polyeten. I mark bör kabel förläggas i rör.

Avser R-CARD M5 version 5.49.0 och senare

### **R-CARD M5**

### **R-CARD M5 består av följande huvuddelar:**

- R-CARD M5 Server. Sköter kommunikation med passersystemet och databasservern. Alla transaktioner mot databasen går via R-CARD M5 Server, oavsett om det är operatören som ändrar data eller utifrån kommande data som ska lagras, t. ex. loggdata från en dörr.
- R-CARD M5 Klient (R-CARD M5 Arbetsstation). Programmet som operatören använder vid administrationen av systemet. Ansluten till R-CARD M5 Server, antingen direkt i samma dator eller via ett nätverk.

Klientens anslutning mot server räknas per samtidig användare. För fler samtidiga klienter kompletteras systemet med önskat antal klientlicenser.

- Microsoft SQL Server-databas och -server.
- OPC-kommunikation med överordnat presentationssystem.
- Hårdvarurekommendationer
- PC som uppfyller kraven för valt operativsystem
- Fritt utrymme på hårddisk:
	- **⋅** Serverinstallation: Minst 10 GB utöver operativsystemets krav. Installeras SQL Server Express på samma dator krävs ytterligare minst 16 GB.
	- **⋅** Enbart klientinstallation: Minst 4 GB utöver operativsystemets krav.
- Bildskärm med upplösning 1024 x 768 eller högre
- Tangentbord och mus
- USB-port för ev. anslutning av inläsningsenhet för kodbärare
- Om modem eller bordsläsare Reader-20 används krävs en seriell port (RS-232)
- Nätverkskort

### **Operativsystem**

**R-CARD M5 (både Server och Klient) kan köras på följande Microsoft-operativsystem:**

- Windows 10
- Windows 11
- Windows Server 2016 eller senare

### **Microsoft .NET Framework**

### **R-CARD M5 kräver Microsoft .NET Framework version 2.0 och 4.6.1 eller senare.**

Microsoft .NET Framework 4.6 medföljer operativsystemen Windows 10 samt Windows Server 2016 eller senare. Tidiga versioner av Windows 10 som inte har uppdaterats kan ha version 4.6.0, och behöver då uppdateras med operativsystemets uppdateringsfunktion (dvs. "Windows Update").

Om Microsoft .NET Framework 2.0 saknas så kan installationsprogrammet för R-CARD M5 installera det åt dig. Detta kräver att datorn har en fungerande Internetupp-koppling. Du kan också installera det manuellt före installation av R-CARD M5; se installationsmanualen för detaljer.

# **Tekniska krav**

Avser R-CARD M5 version 5.49.0 och senare

### **Microsoft SQL Server**

### **R-CARD M5 fungerar med Microsoft SQL Server 2012 och senare (alla utgåvor eller** *editions***).**

Vi rekommenderar att endast versioner som fortfarande underhålls av Microsoft används. I skrivande stund är detta SQL Server 2017 samt 2019. Se Microsofts Lifecycle Policy för aktuell information.

Express Edition har följande begränsningar och rekommenderas inte för större system:

- Max. utnyttjat RAM minne: 1,4 GB
- Max. storlek på databasfilen: 10 GB
- Antal processorer 1 st. (upp till 4 kärnor)

Standard Edition eller Enterprise Edition rekommenderas för R-CARD M5 system med:

- Fler än 2–5 anknytningar (300–500 enheter)
- Fler än 2500 kort1
- Fler än 2 samtidigt inloggade operatörer
- R-CONTROL, Electrolux PAYMENT (Debitering) eller någon av webbapplikationerna
- Flera databaser i samma SQL Server-instans
- För högsta driftsäkerhet bör SQL Server och R-CARD M5 använda samma nätverkssegment. En databas som körts i en nyare version av SQL Server går inte att ansluta eller återställa i en tidigare version av SQL Server. Detta gäller även mellan SQL Server 2008 och 2008 R2. Mer information om detta finns hos Microsoft.

Avser R-CARD M5 version 5.49.0 och senare

### **Nätverkskrav**

### **Kommunikation mellan R-CARD M5 Server och R-CARD M5 Klient**

I ett distribuerat system (med R-CARD M5 Server och en eller flera klienter som kommunicerar med servern via nätverk) används DCOM-teknik och webbtjänst (TCP port 8090), som kräver vissa kompletterande inställningar. De flesta görs automatiskt vid serverinstallationen. Vissa görs med hjälp av ett verktyg som följer med R-CARD M5, "Administrera M5-databaser".

Klienten sköter i de flesta fall själv sina inställningar vid första programstart.

Delar i R-CARD M5-klienten, som exempelvis ODM och Planritningsverktyget, nyttjar Windows-tjänsten R-CARD M5 Service Host (RaServiceHost). RaServiceHost använder sig av TCP port 8090 som standard för kommunikation mellan klient och server. Det innebär att RaServiceHost behöver DCOM-rättighet till servern om de nyare programdelarna ska användas.

DCOM kräver även att Windows-tjänsten RPC (Remote Procedure Call) är aktiverad på datorer som ingår i R-CARD M5.

Vid kommunikation mellan server och klient måste ev. brandväggar konfigureras för att tillåta trafik på följande portar:

- TCP 135, Service Control Manager (SCM) anrop från DCOM
- Fritt definierbart portintervall öppet för DCOM-trafik både in och ut (rekommendation TCP 50000 50100)

### Externa brandväggar som använder adresstransformering (NAT) kan inte användas.

I system med många klienter eller komplex nätverksmiljö med exempelvis svarstider påverkade av många routerhopp, tillfälliga avbrott eller hög trafikbelastning kan man med fördel köra R-CARD M5-applikationen via en distribuerad klient, t.ex. Citrix, istället för via standardklienten. Förutom färre avbrott i klientapplikationen och bättre prestanda så förenklas även support och underhåll av R-CARD M5-programmet. Uppgradering behöver exempelvis enbart utföras på en dator, oavsett hur många som använder klienten.

### **Kommunikation mellan R-CARD M5 Server och undercentraler (UC-50)**

För att ansluta UC-50 till ett TCP/IP-nätverk används kommunikationsmodulen IP-50:

- Överföringshastigheten är 10Mbit/s halv duplex
- Bandbredd 20 200 kbit/s
- IP-adressering:
	- **⋅** Fast IP
	- **⋅** DHCP i kombination med t.ex. DYNDNS
	- **⋅** MAC-adressering (undercentralen kommunicerar sin adress till R-CARD M5 Server)

IP-kommunikationen sker via UDP port 1000 som standard (portnummer fritt konfigurerbart).

| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| ______________________________________________________________________________________________________________________________________________________________________________ |  |  |
| ______________________________________________________________________________________________________________________________________________________________________________ |  |  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |  |  |
|                                                                                                                                                                                |  |  |
|                                                                                                                                                                                |  |  |

![](_page_84_Picture_0.jpeg)