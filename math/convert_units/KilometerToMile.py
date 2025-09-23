while True:
    auswahl = int(input("Wählen Sie aus was sie machen möchten:\n1: Kilometer zu Meilen\n2: Meilen zu Kilometer\nAuswahl: "))
    if int(auswahl)==1:
        km = float(input("Geben Sie eine Kilometer-Anzahl ein: "))
        mi = km * 0.621371
        print(f"{km} km sind {mi} mi")
    elif int(auswahl)==2:
        mi = float(input("Geben Sie eine Meilen-Anzahl ein: "))
        km = mi * 1.60934
        print(f"{mi} mi sind {km} km")
    else:
        print("Eingabe ungültig bitte erneut eingeben.")
    entscheidung = input("Möchten Sie einen weiteren Wert umwandeln (Y/N)?: ").lower()
    if entscheidung == "y":
        continue
    else:
        break
