#Konwersja temperatury. Napisz funkcję, która konwertuje temperaturę
# ze stopni Celsjusza na Fahrenheita.

def celsius_na_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Przykładowe użycie
celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
fahrenheit = celsius_na_fahrenheit(celsius)
print(f"{celsius:.2f}°C to {fahrenheit:.2f}°F")