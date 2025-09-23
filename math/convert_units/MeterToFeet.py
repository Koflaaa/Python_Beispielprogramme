while True:
    auswahl = int(input("Wählen Sie aus was sie machen möchten:\n1: Meter zu Feet (Fuß)\n2: Feet (Fuß) zu Meter\nAuswahl: "))
    if int(auswahl)==1:
        meter = float(input("Geben Sie eine Meter-Anzahl ein: "))
        feet = meter * 3.28084
        print(f"{meter} m sind {feet} ft.")
    elif int(auswahl)==2:
        feet = float(input("Geben Sie eine Feet-Anzahl ein: "))
        meter = feet * 0.3048
        print(f"{feet} ft sind {meter} m.")
    else:
        print("Eingabe ungültig bitte erneut eingeben.")
    entscheidung = input("Möchten Sie einen weiteren Wert umwandeln (Y/N)?: ").lower()
    if entscheidung == "y":
        continue
    else:
        break
