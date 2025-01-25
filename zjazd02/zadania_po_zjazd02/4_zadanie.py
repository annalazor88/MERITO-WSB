# Zadanie 4: Analiza tekstu
# Stwórz program, który analizuje podany tekst.
# Specyfikacja:
# 1. Oblicz częstotliwość występowania każdego słowa.
# 2. Znajdź unikalne słowa (pomijając wielkość liter).
# 3. Znajdź słowa wspólne dla kilku tekstów.

import re  # Biblioteka do pracy z wyrażeniami regularnymi

def analiza_tekstu(tekst):
    # 1. Oczyszczanie tekstu z interpunkcji i zmiana na małe litery
    tekst = tekst.lower()  # Zamieniamy tekst na małe litery
    tekst = re.sub(r'[^\w\s]', '', tekst)  # Usuwamy znaki interpunkcyjne (\w oznacza litery i cyfry, \s - białe znaki)

    # 2. Tworzenie listy słów
    slowa = tekst.split()  # Dzielimy tekst na listę słów, np. "Ala ma kota" -> ["ala", "ma", "kota"]

    # 3. Liczenie częstotliwości słów
    czestotliwosc = {}  # Słownik do przechowywania wyników
    for slowo in slowa:  # Iterujemy po liście słów
        if slowo in czestotliwosc:  # Jeśli słowo już istnieje w słowniku
            czestotliwosc[slowo] += 1  # Zwiększamy wartość
        else:  # Jeśli słowo jeszcze nie istnieje
            czestotliwosc[slowo] = 1  # Dodajemy je do słownika z wartością 1

    # 4. Znajdowanie unikalnych słów
    unikalne_slowa = {slowo for slowo, liczba in czestotliwosc.items() if liczba == 1}
    # Używamy zrozumienia zbiorów (set comprehension), aby zebrać słowa, które występują tylko raz.

    return czestotliwosc, unikalne_slowa

def wspolne_slowa(tekst1, tekst2):
    # Oczyszczanie i podział na listy słów
    tekst1 = re.sub(r'[^\w\s]', '', tekst1.lower()).split()
    tekst2 = re.sub(r'[^\w\s]', '', tekst2.lower()).split()

    # Tworzymy zbiory słów
    zbior1 = set(tekst1)  # Zbiór unikalnych słów z tekstu 1
    zbior2 = set(tekst2)  # Zbiór unikalnych słów z tekstu 2

    # Znajdowanie wspólnych słów za pomocą przecięcia zbiorów
    wspolne = zbior1 & zbior2  # Operator & znajduje wspólne elementy między zbiorami

    return wspolne

# Funkcja główna do demonstracji
def main():
    tekst1 = "Ala ma kota. Ala bardzo lubi swojego kota."
    tekst2 = "Kot Ali jest bardzo zabawny. Ala ma dwa koty."

    print("Analiza pierwszego tekstu:")
    czestotliwosc1, unikalne1 = analiza_tekstu(tekst1)
    print("Częstotliwość słów:", czestotliwosc1)
    print("Unikalne słowa:", unikalne1)

    print("\nAnaliza drugiego tekstu:")
    czestotliwosc2, unikalne2 = analiza_tekstu(tekst2)
    print("Częstotliwość słów:", czestotliwosc2)
    print("Unikalne słowa:", unikalne2)

    print("\nWspólne słowa:")
    print(wspolne_slowa(tekst1, tekst2))

if __name__ == "__main__":
    main()
