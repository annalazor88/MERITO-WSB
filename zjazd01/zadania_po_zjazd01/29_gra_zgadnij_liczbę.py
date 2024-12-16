#Gra "Zgadnij liczbę". Napisz program, w którym komputer losuje liczbę od 1 do 100, a użytkownik ma za zadanie ją odgadnąć. Po każdej próbie program podpowiada, czy
# podana liczba jest za duża czy za mała.

import random  # Importuje moduł, który umożliwia losowanie liczb

# Komputer losuje liczbę od 1 do 100
wylosowana_liczba = random.randint(1, 100)
odgadnieta = False  # Flaga, która śledzi, czy użytkownik odgadł liczbę

print("Witaj w grze 'Zgadnij liczbę'! Komputer wylosował liczbę od 1 do 100.")

# Pętla działa, dopóki użytkownik nie odgadnie liczby
while not odgadnieta:
    # Pobranie liczby od użytkownika i zamiana na typ całkowity
    proba = int(input("Podaj swoją liczbę: "))

    # Sprawdzenie, czy liczba jest za mała, za duża czy trafiona
    if proba < wylosowana_liczba:
        print("Za mało!")
    elif proba > wylosowana_liczba:
        print("Za dużo!")
    else:
        print("Gratulacje! Odgadłeś liczbę!")
        odgadnieta = True  # Zmieniamy flagę, by zakończyć pętlę