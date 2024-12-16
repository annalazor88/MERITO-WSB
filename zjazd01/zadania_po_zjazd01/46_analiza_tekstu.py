# Analiza tekstu Napisz program, który pobierze od użytkownika tekst i wyświetli:
#
# Liczbę znaków w tekście
# Liczbę słów
# Liczbę zdań (przyjmij, że zdania kończą się kropką, wykrzyknikiem lub znakiem zapytania)

# Pobierz tekst od użytkownika
tekst = input("Podaj tekst: ")

# Liczba znaków w tekście (wliczając spacje)
liczba_znakow = len(tekst)

# Liczba słów w tekście
liczba_slow = len(tekst.split())

# Liczba zdań w tekście (zdania kończą się ., ! lub ?)
liczba_zdan = sum(1 for znak in tekst if znak in ".!?")

# Wyświetlenie wyników
print("Liczba znaków:", liczba_znakow)
print("Liczba słów:", liczba_slow)
print("Liczba zdań:", liczba_zdan)