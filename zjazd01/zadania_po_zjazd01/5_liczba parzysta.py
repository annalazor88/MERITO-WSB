# Sprawdzanie liczby parzystej. Napisz funkcję, która przyjmuje liczbę i zwraca
# informację, czy jest ona parzysta czy nieparzysta.

# Definiujemy funkcję o nazwie 'sprawdz_parzystosc'
def sprawdz_parzystosc(liczba):
    # Sprawdzamy, czy liczba podzielona przez 2 daje resztę 0
    if liczba % 2 == 0:
        return "Liczba jest parzysta"
    else:
        return "Liczba jest nieparzysta"

# Przykład użycia funkcji
liczba = int(input("Podaj liczbę: "))
wynik = sprawdz_parzystosc(liczba)
print(wynik)