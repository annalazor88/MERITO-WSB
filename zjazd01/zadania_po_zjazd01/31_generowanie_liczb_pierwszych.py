# Generowanie listy liczb pierwszych. Napisz funkcję, która zwróci listę wszystkich liczb pierwszych
# z zakresu od 2 do podanej liczby n.   a

def znajdz_liczby_pierwsze(n):
    liczby_pierwsze = []  # Tworzymy pustą listę, do której będą dodawane liczby pierwsze
    for liczba in range(2, n + 1):  # Iterujemy po liczbach od 2 do n włącznie
        # Sprawdzamy, czy liczba jest pierwsza
        for dzielnik in range(2, int(liczba ** 0.5) + 1):
            if liczba % dzielnik == 0:
                break  # Przerywamy, jeśli liczba ma dzielnik inny niż 1 i ona sama
        else:
            liczby_pierwsze.append(liczba)  # Dodajemy liczbę do listy, jeśli jest pierwsza
    return liczby_pierwsze  # Zwracamy listę liczb pierwszych

# Przykład użycia funkcji
n = int(input("Podaj górną granicę zakresu: "))
print("Liczby pierwsze od 2 do", n, "to:", znajdz_liczby_pierwsze(n))