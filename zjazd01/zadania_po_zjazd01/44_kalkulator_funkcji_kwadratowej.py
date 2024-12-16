# Kalkulator funkcji kwadratowej. Napisz program, który pobierze współczynniki a, b, c funkcji kwadratowej
# i obliczy jej miejsca zerowe.

import math

# Pobierz współczynniki od użytkownika
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

# Sprawdź, czy a jest równe 0
if a == 0:
    print("To nie jest funkcja kwadratowa, ponieważ a = 0.")
else:
    # Oblicz deltę
    delta = b ** 2 - 4 * a * c
    print(f"Delta wynosi: {delta}")

    # Sprawdź wartość delty
    if delta > 0:
        # Dwa różne miejsca zerowe
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Funkcja ma dwa miejsca zerowe: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        # Jedno miejsce zerowe
        x0 = -b / (2 * a)
        print(f"Funkcja ma jedno miejsce zerowe: x0 = {x0}")
    else:
        # Brak miejsc zerowych w liczbach rzeczywistych
        print("Funkcja nie ma miejsc zerowych w liczbach rzeczywistych.")