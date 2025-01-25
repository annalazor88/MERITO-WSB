# Zadanie 1: Rozwinięcie zadanie z funkcjami – program do logowania i rejestracji
# użytkowników.
# - program powinien sprawdzać poiom skomplikowania hasła (akceptować haśło bądź nie)
# - w przypadku próby zarejestrowania użytkownika, którego nazwa jest już zajęta, program
# powinien podpowiedzieć podobną, wolną nazwę
# - po 5ciu nieudanych próbach logowania program powinien się zakończyć

import re
import random

# Baza danych użytkowników
user_database = {}

# Sprawdzanie złożoności hasła
def is_password_strong(password):
    if len(password) < 8 or not re.search(r"[A-Z]", password) or not re.search(r"[0-9]", password) or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

# Rejestracja użytkownika
def register_user():
    username = input("Podaj nazwę użytkownika: ")
    if username in user_database:
        print(f"Nazwa zajęta. Propozycja: {username}{random.randint(1, 9999)}")
        return
    password = input("Podaj hasło: ")
    if not is_password_strong(password):
        print("Hasło musi mieć min. 8 znaków, dużą literę, cyfrę i znak specjalny.")
        return
    user_database[username] = password
    print("Rejestracja zakończona.")

# Logowanie użytkownika
def login_user():
    attempts = 0
    while attempts < 5:
        username = input("Podaj nazwę użytkownika: ")
        password = input("Podaj hasło: ")
        if user_database.get(username) == password:
            print(f"Witaj, {username}!")
            return
        print("Niepoprawne dane.")
        attempts += 1
    print("Zbyt wiele prób. Program zakończony.")
    exit()

# Główna pętla programu
def main():
    while True:
        choice = input("\n1. Rejestracja\n2. Logowanie\n3. Wyjście\nWybierz opcję: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()