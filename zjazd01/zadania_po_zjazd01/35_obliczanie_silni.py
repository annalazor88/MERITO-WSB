# Obliczanie silni. Napisz program, który obliczy silnię dla podanej liczby całkowitej.
def oblicz_silnie(n):
    # Sprawdzenie, czy liczba jest całkowita i nieujemna
    if not isinstance(n, int) or n < 0:
        return "Podaj liczbę całkowitą nieujemną."

    # Silnia 0! i 1! wynosi 1
    if n == 0 or n == 1:
        return 1

    # Obliczanie silni za pomocą pętli
    silnia = 1
    for i in range(2, n + 1):
        silnia *= i

    return silnia


# Pobieranie liczby od użytkownika
try:
    liczba = int(input("Podaj liczbę całkowitą: "))
    wynik = oblicz_silnie(liczba)
    print(f"Silnia z {liczba} wynosi: {wynik}")
except ValueError:
    print("Podana wartość nie jest liczbą całkowitą.")