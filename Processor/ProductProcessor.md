Nu ska vi implementera ProductProcessor-klassen som är huvudklassen för att bearbeta produktdokumentation och extrahera strukturerad information.



Detta är en robust och omfattande `ProductProcessor`-klass som kan:

1. Bearbeta produktdokumentation och extrahera strukturerad information
2. Hantera stora filer genom att dela upp dem i mindre bitar
3. Validera extraherad information
4. Spara resultat till fil i olika format
5. Cachehantering för att spara och ladda tidigare resultat
6. Generera FAQ-svar baserat på extraherad information
7. Visa sammanfattningar av resultat i terminalen

Den hanterar också felhantering och felåterställning, samt spårning av framsteg och prestandastatistik.

I nästa meddelande ska vi implementera arbetsflödeshantering med arbetarklasser och köhantering för att möjliggöra parallell bearbetning av produkter.