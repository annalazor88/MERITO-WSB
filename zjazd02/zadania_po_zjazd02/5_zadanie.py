# Zadanie 5: Ranking studentów
# Stwórz system, który przechowuje i analizuje oceny studentów.
# Specyfikacja:
# 1. Każdy student ma listę ocen przechowywaną w słowniku {student: [oceny]}.
# 2. Funkcje:
# - Dodawanie oceny dla studenta.
# - Obliczanie średniej oceny dla każdego studenta.
# - Znalezienie najlepszych i najgorszych studentów.

# Słownik przechowujący dane studentów i ich oceny
students = {}

# 1. Funkcja do dodawania oceny dla studenta
def dodaj_ocene(student, ocena):
    if student not in students:  # Sprawdzamy, czy student już istnieje w słowniku
        students[student] = []  # Jeśli nie, tworzymy nową listę ocen dla tego studenta
        print(f"Dodano nowego studenta: {student}")
    if 1 <= ocena <= 6:  # Sprawdzamy, czy ocena jest w poprawnym zakresie (1-6)
        students[student].append(ocena)  # Dodajemy ocenę do listy ocen studenta
        print(f"Dodano ocenę {ocena} dla studenta {student}.")
    else:  # Jeśli ocena nie jest poprawna
        print("Ocena musi być liczbą w zakresie 1-6.")  # Komunikat o błędzie

# 2. Funkcja do obliczania średniej oceny dla każdego studenta
def oblicz_srednie():
    if not students:  # Sprawdzamy, czy słownik studentów nie jest pusty
        print("Brak danych o studentach.")  # Jeśli pusty, komunikat dla użytkownika
        return
    srednie = {}  # Tworzymy nowy słownik na średnie oceny
    print("Średnie oceny studentów:")
    for student, oceny in students.items():  # Iterujemy po każdym studencie i jego ocenach
        if oceny:  # Sprawdzamy, czy lista ocen nie jest pusta
            srednia = sum(oceny) / len(oceny)  # Obliczamy średnią ocen
            srednie[student] = srednia  # Dodajemy wynik do słownika
            print(f"- {student}: {srednia:.2f}")  # Wyświetlamy średnią z 2 miejscami po przecinku
        else:  # Jeśli student nie ma ocen
            print(f"- {student} nie ma ocen.")  # Informacja o braku ocen
    return srednie  # Zwracamy słownik średnich ocen

# 3. Funkcja do znalezienia najlepszych i najgorszych studentów
def znajdz_najlepszych_najgorszych():
    srednie = oblicz_srednie()  # Obliczamy średnie oceny (wykorzystujemy poprzednią funkcję)
    if not srednie:  # Jeśli brak danych, kończymy funkcję
        return
    max_srednia = max(srednie.values())  # Znajdujemy najwyższą średnią
    min_srednia = min(srednie.values())  # Znajdujemy najniższą średnią

    # Znajdujemy studentów z najwyższą średnią
    najlepsi = [student for student, srednia in srednie.items() if srednia == max_srednia]
    # Znajdujemy studentów z najniższą średnią
    najgorsi = [student for student, srednia in srednie.items() if srednia == min_srednia]

    print(f"Najlepszy(e) student(ci) ({max_srednia:.2f}): {', '.join(najlepsi)}")
    print(f"Najgorszy(e) student(ci) ({min_srednia:.2f}): {', '.join(najgorsi)}")

# 4. Funkcja główna do testowania programu
def main():
    dodaj_ocene("Jan", 5)  # Dodajemy ocenę dla Jana
    dodaj_ocene("Anna", 6)  # Dodajemy ocenę dla Anny
    dodaj_ocene("Jan", 4)  # Dodajemy kolejną ocenę dla Jana
    dodaj_ocene("Anna", 5)  # Dodajemy kolejną ocenę dla Anny
    dodaj_ocene("Kasia", 3)  # Dodajemy ocenę dla Kasi
    dodaj_ocene("Kasia", 2)  # Dodajemy kolejną ocenę dla Kasi
    dodaj_ocene("Adam", 6)  # Dodajemy ocenę dla Adama

    print("\nObliczanie średnich:")
    oblicz_srednie()  # Wywołujemy funkcję do obliczania średnich ocen

    print("\nRanking studentów:")
    znajdz_najlepszych_najgorszych()  # Wywołujemy funkcję do analizy najlepszych i najgorszych

if __name__ == "__main__":
    main()
