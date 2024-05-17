bestallningar = {}  # Lagrar alla beställningar

while True:
    namn = input("Ange ditt namn (eller 'q' för att avsluta): ")
    if namn == 'q':
        break

    # Användare väljer från en lista med kaksorter
    print("Välj en kaksort: Chokladbollar, Kolabollar, Dammsugare, Godis")
    kaksort = input("Ange kaksorten du vill beställa: ")
    if kaksort not in ["Chokladbollar", "Kolabollar", "Dammsugare", "Godis"]:
        print("Felaktig kaksort, försök igen.")
        continue

    antal = int(input("Ange antal kakburkar du vill beställa: "))

    if namn not in bestallningar:
        bestallningar[namn] = {}
    
    if kaksort in bestallningar[namn]:
        bestallningar[namn][kaksort] += antal
    else:
        bestallningar[namn][kaksort] = antal

    print(namn + " har lagt till en beställning för " + str(antal) + " " + kaksort + " kakburkar.")

print("Alla beställningar:")
for namn in bestallningar:
    print(namn + "s beställningar:")
    for kaksort, antal in bestallningar[namn].items():
        print("  " + kaksort + ": " + str(antal) + " st")
