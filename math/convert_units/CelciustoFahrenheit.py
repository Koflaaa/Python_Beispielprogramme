while True:
    grad_auswahl = int(input("Wählen Sie aus was sie machen möchten:\n1: Celsius zu Fahrenheit\n2: Fahrenheit zu Celsius\nAuswahl:"))
    if int(grad_auswahl)==1:
        C = int(input("Geben Sie einen Temperaturwert in °C ein: "))
        Fahrenheit = (C * (9/5) + 32)
        print(f"{C}°C in Fahrenheit beträgt: {Fahrenheit}°F")
    elif int(grad_auswahl)==2:
        F = float(input("Geben Sie einen Temperaturwert in °F ein: "))
        Celsius = 5/9 * (F-32)
        print(f"{F}°F zu Celsius beträgt: {Celsius}°C")
    else:
        print("Eingabe ungültig bitte erneut eingeben.")
    entscheidung = input("Möchten Sie einen weiteren Wert umwandeln (Y/N)?: ").lower()
    if entscheidung == "y":
        continue
    else:
        break
