# Prosty kalkulator. Napisz program, który pobierze od użytkownika dwie liczby i wyświetli ich sumę,
# różnicę, iloczyn oraz iloraz.

# Pobranie dwóch liczb od użytkownika
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

# Obliczenia
suma = liczba1 + liczba2
roznica = liczba1 - liczba2
iloczyn = liczba1 * liczba2

# Sprawdzenie, czy druga liczba nie jest zerem, aby uniknąć dzielenia przez zero
if liczba2 != 0:
    iloraz = liczba1 / liczba2
else:
    iloraz = "Dzielenie przez zero jest niemożliwe"

# Wyświetlenie wyników
print(f"Suma: {suma}")
print(f"Różnica: {roznica}")
print(f"Iloczyn: {iloczyn}")
print(f"Iloraz: {iloraz}")