#Obliczanie średniej z trzech liczb. Napisz program, który pobierze od użytkownika trzy liczby i
# obliczy ich średnią arytmetyczną.

# Pobranie trzech liczb od użytkownika
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))
liczba3 = float(input("Podaj trzecią liczbę: "))

# Obliczanie średniej arytmetycznej
srednia = (liczba1 + liczba2 + liczba3) / 3

# Wyświetlenie wyniku
print(f"Średnia z podanych liczb wynosi: {srednia:.2f}")