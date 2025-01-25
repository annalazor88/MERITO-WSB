# Zadanie 3: Zarządzanie magazynem
# Stwórz program do zarządzania magazynem produktów.
# Specyfikacja:
# 1. Magazyn przechowuje produkty w postaci słownika: {produkt: ilość}.
# 2. Stwórz funkcje:
# - Dodawania produktu do magazynu.
# - Usuwania produktu z magazynu.
# - Sprawdzenia dostępnych produktów (używając zbiorów).
# 3. Dodaj możliwość raportowania brakujących produktów.
# Magazyn przechowywany jako słownik
# Definiujemy magazyn jako słownik
# Magazyn przechowywany jako słownik

magazyn = {}

def dodaj_produkt(nazwa, ilosc):
    if ilosc <= 0:
        print("Ilość musi być większa od 0.")
        return
    if nazwa in magazyn:
        magazyn[nazwa] += ilosc
        print(f"Zwiększono ilość produktu '{nazwa}' o '{ilosc}'.")
    else:
        magazyn[nazwa] = ilosc
        print(f"Dodano nowy produkt '{nazwa}' w ilości '{ilosc}'.")

def usun_produkt(nazwa, ilosc):
    if ilosc <= 0:
        print("Ilość musi być większa od 0.")
        return
    if nazwa in magazyn:
        if magazyn[nazwa] > ilosc:
            magazyn[nazwa] -= ilosc
            print(f"Zmniejszono ilość produktu '{nazwa}' o {ilosc}.")
        elif magazyn[nazwa] == ilosc:
            del magazyn[nazwa]
            print(f"Usunięto produkt '{nazwa}' z magazynu.")
        else:  # Jeśli próbujemy usunąć więcej, niż jest dostępne
            print(f"Nie można usunąć {ilosc}, ponieważ dostępne jest tylko {magazyn[nazwa]}.")
    else:
        print(f"Produkt '{nazwa}' nie istnieje w magazynie.")

def sprawdz_produkty():
    if magazyn:
        print("Dostępne produkty w magazynie:")
        for produkt, ilosc in magazyn.items():
            print(f"- {produkt}: {ilosc}")
    else:  # Jeśli magazyn jest pusty
        print("Magazyn jest pusty.")

def raport_brakow():
    brakujace = [produkt for produkt, ilosc in magazyn.items() if ilosc == 0]  # Szukamy produktów o ilości 0
    if brakujace:
        print("Brakujące produkty:")
        for produkt in brakujace:
            print(f"- {produkt}")
    else:
        print("Brak brakujących produktów.")

# Główna funkcja do testowania
def main():
    print("Witaj w systemie zarządzania magazynem!")
    dodaj_produkt("jabłka", 10)  # Dodajemy 10 jabłek
    dodaj_produkt("banany", 5)   # Dodajemy 5 bananów
    usun_produkt("jabłka", 3)    # Usuwamy 3 jabłka
    sprawdz_produkty()           # Sprawdzamy produkty
    usun_produkt("jabłka", 7)    # Próbujemy usunąć więcej jabłek niż jest
    raport_brakow()              # Raportujemy braki
    usun_produkt("banany", 5)    # Usuwamy wszystkie banany
    sprawdz_produkty()           # Sprawdzamy produkty po usunięciu bananów

if __name__ == "__main__":
    main()