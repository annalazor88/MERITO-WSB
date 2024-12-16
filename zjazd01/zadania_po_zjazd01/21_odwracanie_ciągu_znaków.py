# Odwracanie ciągu znaków. Napisz funkcję, która przyjmuje ciąg znaków i
# zwraca go w odwróconej kolejności.

def odwracanie_ciagu(ciag):
    return ciag[::-1]

# Przykładowe użycie
ciag_znakow = input("Podaj ciąg znaków: ")
odwrocony_ciag = odwracanie_ciagu(ciag_znakow)
print(f"Odwrócony ciąg: {odwrocony_ciag}")