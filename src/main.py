# main.py

bestallningar = {}  # Lagrar alla beställningar

while True:
    namn = input("Ange ditt namn (eller 'q' för att avsluta): ")
    if namn == 'q':
        break

    kaksort = input("Ange kaksorten du vill beställa: ")
    antal = int(input("Ange antal kakor du vill beställa: "))
    
    if namn not in bestallningar:
        bestallningar[namn] = {}
    
    if kaksort in bestallningar[namn]:
        bestallningar[namn][kaksort] += antal
    else:
        bestallningar[namn][kaksort] = antal

    print(namn + " har lagt till en beställning för " + str(antal) + " " + kaksort + " kakor.")

print("Alla beställningar:")
for namn in bestallningar:
    print(namn + "s beställningar:")
    for kaksort, antal in bestallningar[namn].items():
        print("  " + kaksort + ": " + str(antal) + " st")
