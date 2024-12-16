# Sprawdzanie pełnoletności. Napisz program, który zapyta użytkownika o jego wiek i
# wyświetli komunikat, czy jest pełnoletni.

# Pobranie wieku od użytkownika
wiek = int(input("Podaj swój wiek: "))

# Sprawdzenie pełnoletności
if wiek >= 18:
    print("Jesteś pełnoletni.")
else:
    print("Nie jesteś pełnoletni.")