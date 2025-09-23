while True:
    auswahl = int(input("Wählen Sie aus was sie machen möchten:\n1: km/h zu Meilen\n2: Meilen zu km/h\nAuswahl: "))
    if int(auswahl)==1:
        KilometerProStunde = float(input("Geben Sie eine Geschwindigkeit in km/h ein: "))
        mph = KilometerProStunde *  0.6213711922 
        print(f"{KilometerProStunde}km/h sind {mph}mph")
    elif int(auswahl)==2:
        MeilenProStunde = float(input("Geben Sie eine Geschwindigkeit in Meilen ein: "))
        kmh = MeilenProStunde * 1.60934
        print(f"{MeilenProStunde}mph sind {kmh}km/h")
    else:
        print("Eingabe ungültig bitte erneut eingeben.")
    entscheidung = input("Möchten Sie einen weiteren Wert umwandeln (Y/N)?: ").lower()
    if entscheidung == "y":
        continue
    else:
        break
