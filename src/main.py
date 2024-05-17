bestallningar = {}  # Lagrar alla beställningar

while True:
    namn = input("Ange ditt namn (eller 'q' för att avsluta): ")
    if namn == 'q':
        break

    kaksort = input("Ange kaksorten du vill beställa: ")
    antal = int(input("Ange antal kakor du vill beställa: "))

    # Skapa en ny post för namnet om det inte redan finns
    if namn not in bestallningar:
        bestallningar[namn] = {}

    # Lägg till eller uppdatera antalet kakor för den givna kaksorten
    bestallningar[namn][kaksort] = bestallningar[namn].get(kaksort, 0) + antal

    print(f"{namn} har lagt till en beställning för {antal} {kaksort} kakor.")

print("Alla beställningar:")
for namn, orders in bestallningar.items():
    print(f"{namn}s beställningar:")
    for kaksort, antal in orders.items():
        print(f"  {kaksort}: {antal} st")
