# Kakburkar Beställningssystem

Detta är ett enkelt beställningssystem för kakburkar. Användaren kan lägga till beställningar för olika typer av kakburkar och systemet kommer att hålla reda på alla beställningar.

## Funktioner

- Användaren kan lägga till beställningar för olika typer av kakburkar.
- Systemet visar alla aktuella beställningar.
- Användaren kan avsluta programmet när som helst genom att skriva 'q'.
- Vid programmets avslut sparar systemet alla beställningar i en textfil.

## Användning

När programmet startas kommer det att visa en lista över aktuella beställningar. Om det inte finns några beställningar kommer det att säga "Inga beställningar än."

Användaren kommer sedan att bli ombedd att ange sitt namn. Om användaren skriver 'q' kommer programmet att avslutas.

Användaren kommer sedan att bli ombedd att välja en kaksort från följande: Chokladbollar, Kolabollar, Dammsugare, Godis. Om användaren skriver något annat än dessa kommer de att få ett felmeddelande och bli ombedd att försöka igen.

Användaren kommer sedan att bli ombedd att ange antalet kakburkar de vill beställa.

När en beställning har lagts till kommer systemet att bekräfta detta genom att säga "[Användarens namn] har lagt till en beställning för [antal] [kaksort] kakburkar."

När programmet avslutas kommer det att skriva ut alla beställningar och spara dem i en textfil.

## Installation

För att köra detta program, klona bara detta repo och kör `main.py` med Python 3.

## Licens

Detta projekt är licensierat under The Unlicense.