# Wyświetlanie liczb nieparzystych. Napisz program, który za pomocą pętli for
# wyświetli liczby nieparzyste od 1 do 20.

for liczba in range(1, 21):
    if liczba % 2 != 0:
        print(liczba)