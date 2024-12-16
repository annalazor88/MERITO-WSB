#Szyfr Cezara. Napisz funkcję, która zaszyfruje podany przez użytkownika tekst za pomocą szyfru Cezara z
# przesunięciem o określoną liczbę znaków.

def szyfr_cezara(tekst, przesuniecie):
    zaszyfrowany_tekst = ""

    for znak in tekst:
        if znak.isalpha():
            # Sprawdzamy, czy znak jest literą
            start = ord('A') if znak.isupper() else ord('a')
            zaszyfrowany_tekst += chr((ord(znak) - start + przesuniecie) % 26 + start)
        else:
            # Jeśli znak nie jest literą (np. spacja, przecinek), zostaje niezmieniony
            zaszyfrowany_tekst += znak

    return zaszyfrowany_tekst


# Przykładowe użycie
tekst = input("Podaj tekst do zaszyfrowania: ")
przesuniecie = int(input("Podaj przesunięcie (liczba całkowita): "))

wynik = szyfr_cezara(tekst, przesuniecie)
print(f"Zaszyfrowany tekst: {wynik}")