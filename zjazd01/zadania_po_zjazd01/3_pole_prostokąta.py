# Obliczanie pola prostokąta. Napisz program, który pobierze od użytkownika długość i szerokość prostokąta, a następnie obliczy i wyświetli jego pole.
# Prosimy użytkownika o podanie długości prostokąta i zapisujemy ją w zmiennej 'dlugosc'
dlugosc = float(input("Podaj długość prostokąta: "))

# Prosimy użytkownika o podanie szerokości prostokąta i zapisujemy ją w zmiennej 'szerokosc'
szerokosc = float(input("Podaj szerokość prostokąta: "))

# Obliczamy pole prostokąta jako iloczyn długości i szerokości
pole = dlugosc * szerokosc

# Wyświetlamy wynik
print("Pole prostokąta wynosi:", pole)