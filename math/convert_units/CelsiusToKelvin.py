kelvin_konstante = 273.15

while True:
    grad_auswahl = int(input("Wählen Sie aus was sie machen möchten:\n1: Celsius zu Kelvin\n2: Kelvin zu Celsius\nAuswahl:"))
    if int(grad_auswahl)==1:
        C = float(input("Geben Sie einen Temperaturwert in °C ein: "))
        Kelvin = C+kelvin_konstante
        print(f"{C}°C in Kelvin beträgt: {Kelvin}°F")
    elif int(grad_auswahl)==2:
        K = float(input("Geben Sie einen Temperaturwert in K(Kelvin) ein: "))
        Celsius = K - kelvin_konstante
        print(f"{K}K(Kelvin) in Celsius beträgt: {Celsius}°C")
    else:
        print("Eingabe ungültig bitte erneut eingeben.")
    entscheidung = input("Möchten Sie einen weiteren Wert umwandeln (Y/N)?: ").lower()
    if entscheidung == "y":
        continue
    else:
        break
