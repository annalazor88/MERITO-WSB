# Zadanie 2: Analiza ankiety
# Stwórz program, który zbiera odpowiedzi ankietowe od użytkowników i analizuje wyniki.
# Specyfikacja:
# 1. Każdy użytkownik wybiera kilka kategorii, które mu się podobają (np. sport, muzyka,
# technologia).
# 2. Program powinien:
# - Policzyć, ile razy każda kategoria została wybrana.
# - Znaleźć kategorie wspólne dla wszystkich użytkowników.
# - Wyświetlić unikalne kategorie wybrane przez każdego użytkownika.
# Przykładowe dane wejściowe:
# responses = { "Anna": {"sport", "muzyka", "podróże"}, "Jan": {"technologia", "sport",
# "muzyka"}, "Maria": {"muzyka", "sztuka", "sport"} }

# Dane wejściowe - przykładowe odpowiedzi ankietowe

responses = {
    "Anna": {"sport", "muzyka", "podróże"},
    "Jan": {"technologia", "sport", "muzyka"},
    "Maria": {"muzyka", "sztuka", "sport"}
}

# Analiza wyników ankiety
def analyze_survey(responses):
    # Liczba wystąpień każdej kategorii
    category_count = {}
    for user_categories in responses.values():
        for category in user_categories:
            category_count[category] = category_count.get(category, 0) + 1

    print("1. Liczba wystąpień każdej kategorii:")
    for category, count in category_count.items():
        print(f"{category}: {count}")

    # Kategorie wspólne dla wszystkich
    common = set.intersection(*responses.values())
    print("\n2. Kategorie wspólne dla wszystkich:")
    print(common if common else "Brak wspólnych kategorii.")

    # Unikalne kategorie dla każdego użytkownika
    print("\n3. Unikalne kategorie dla każdego użytkownika:")
    for user, categories in responses.items():
        unique = categories - set.union(*(resp for u, resp in responses.items() if u != user))
        print(f"{user}: {unique}")

# Uruchomienie analizy
def main():
    analyze_survey(responses)

if __name__ == "__main__":
    main()