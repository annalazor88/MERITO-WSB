# Anagramy. Napisz program, który sprawdzi, czy dwa podane przez użytkownika słowa są anagramami.

def czy_anagram(słowo1, słowo2):
    # Usuwamy spacje i zamieniamy wszystkie litery na małe, by sprawdzić niezależnie od wielkości liter
    słowo1 = słowo1.replace(" ", "").lower()
    słowo2 = słowo2.replace(" ", "").lower()

    # Sprawdzamy, czy posortowane litery obu słów są takie same
    return sorted(słowo1) == sorted(słowo2)


# Wprowadzenie danych przez użytkownika
pierwsze_słowo = input("Podaj pierwsze słowo: ")
drugie_słowo = input("Podaj drugie słowo: ")

# Sprawdzamy, czy słowa są anagramami
if czy_anagram(pierwsze_słowo, drugie_słowo):
    print("Tak, te słowa są anagramami!")
else:
    print("Nie, te słowa nie są anagramami.")