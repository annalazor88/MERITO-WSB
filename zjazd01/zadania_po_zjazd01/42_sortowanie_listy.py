# Sortowanie listy Napisz funkcję, która przyjmuje listę liczb i zwraca ją posortowaną w kolejności malejącej
# bez użycia wbudowanych funkcji sortujących.

def sort_descending(lst):
    # Kopiujemy listę, aby nie zmieniać oryginalnej
    sorted_lst = lst[:]

    # Implementacja sortowania bąbelkowego (Bubble Sort)
    for i in range(len(sorted_lst)):
        for j in range(len(sorted_lst) - 1 - i):
            if sorted_lst[j] < sorted_lst[j + 1]:
                # Zamiana miejscami elementów
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]

    return sorted_lst


# Przykład użycia:
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sort_descending(numbers)
print(sorted_numbers)