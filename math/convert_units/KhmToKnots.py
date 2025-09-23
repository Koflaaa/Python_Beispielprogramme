while True:
    auswahl = int(input("Wählen Sie aus was sie machen möchten:\n1: Kilometer pro Stunde zu Knoten\n2: Knoten zu Kilometer pro Stunde\nAuswahl: "))
    if int(auswahl)==1:
        kmh = float(input("Geben Sie eine Geschwindigkeit in km/h ein: "))
        knots = kmh / 1.852
        print(f"{kmh}km/h sind {knots}kn")
    elif int(auswahl)==2:
        knots = float(input("Geben Sie eine Geschwindigkeit in Meilen ein: "))
        kmh = knots * 1.852
        print(f"{knots}kn sind {kmh}km/h")
    else:
        print("Eingabe ungültig bitte erneut eingeben.")
    entscheidung = input("Möchten Sie einen weiteren Wert umwandeln (Y/N)?: ").lower()
    if entscheidung == "y":
        continue
    else:
        break
