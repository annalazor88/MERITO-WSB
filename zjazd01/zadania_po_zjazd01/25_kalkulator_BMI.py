# Kalkulator BMI. Napisz program, który obliczy BMI użytkownika na podstawie podanego wzrostu (w metrach) i wagi (w kilogramach), a następnie wyświetli
# odpowiednią interpretację wyniku.

def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)
    return bmi

def interpretacja_bmi(bmi):
    if bmi < 18.5:
        return "Niedowaga"
    elif 18.5 <= bmi < 24.9:
        return "Waga prawidłowa"
    elif 25 <= bmi < 29.9:
        return "Nadwaga"
    else:
        return "Otyłość"

# Pobieranie danych od użytkownika
waga = float(input("Podaj swoją wagę w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach (np. 1.75): "))

# Obliczanie BMI
bmi = oblicz_bmi(waga, wzrost)

# Wyświetlanie wyniku
print(f"Twoje BMI wynosi: {bmi:.2f}")
print(f"Interpretacja: {interpretacja_bmi(bmi)}")