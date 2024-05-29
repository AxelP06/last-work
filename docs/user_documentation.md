# Användardokumentation för Kakburkar Beställningssystem

## Översikt

Detta system är utformat för att hantera beställningar av kakburkar. Du kan lägga till beställningar för olika typer av kakburkar och systemet kommer att hålla reda på alla beställningar.

## Användning

För att köra programmet, kör `main.py` med Python 3.

När programmet startas kommer du att se en lista över aktuella beställningar. Om det inte finns några beställningar kommer det att säga "Inga beställningar än."

Du kommer sedan att bli ombedd att ange ditt namn. Om du vill avsluta programmet, skriv 'q' och tryck på Enter.

Nästa steg är att välja en kaksort. Du kan välja mellan "Chokladbollar", "Kolabollar", "Dammsugare" och "Godis". Om du skriver något annat än dessa alternativ kommer du att få ett felmeddelande och bli ombedd att försöka igen.

Efter att du har valt en kaksort kommer du att bli ombedd att ange antalet kakburkar du vill beställa. Skriv in antalet och tryck på Enter.

Din beställning kommer sedan att läggas till i listan över aktuella beställningar. Om du redan har beställt samma kaksort tidigare kommer antalet kakburkar att ökas med det nya antalet.

När du avslutar programmet kommer alla beställningar att skrivas ut och sparas i en textfil.

## Felhantering

Om du skriver in ett ogiltigt namn, kaksort eller antal kakburkar kommer programmet att ge dig ett felmeddelande och be dig att försöka igen. Se till att du följer instruktionerna noggrant för att undvika fel.