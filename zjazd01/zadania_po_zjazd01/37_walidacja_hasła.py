# Walidacja hasła. Napisz program, który sprawdzi, czy podane przez użytkownika hasło spełnia następujące warunki:
#
# Ma co najmniej 8 znaków
# Zawiera co najmniej jedną dużą literę
# Zawiera co najmniej jedną cyfrę

def validate_password(password):
    # Sprawdzenie, czy hasło ma co najmniej 8 znaków
    if len(password) < 8:
        return "Hasło musi mieć co najmniej 8 znaków."

    # Sprawdzenie, czy hasło zawiera co najmniej jedną dużą literę
    if not any(c.isupper() for c in password):
        return "Hasło musi zawierać co najmniej jedną dużą literę."

    # Sprawdzenie, czy hasło zawiera co najmniej jedną cyfrę
    if not any(c.isdigit() for c in password):
        return "Hasło musi zawierać co najmniej jedną cyfrę."

    return "Hasło jest poprawne."


# Pętla, która pozwala użytkownikowi na wielokrotne wprowadzenie hasła
while True:
    password = input("Wprowadź hasło: ")
    result = validate_password(password)

    # Jeśli hasło jest poprawne, przerywamy pętlę
    if result == "Hasło jest poprawne.":
        print(result)
        break
    else:
        print(result)
        print("Spróbuj ponownie.")