# Задача 30.
# Заполните массив элементами арифметической прогрессии. Её первый 
# элемент, разность (ШАГ) и количество элементов нужно ввести с клавиатуры. Формула 
# для получения n-го члена прогрессии: a(n) = a(1) + (n - 1) * d. 
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

firstElem = int(input("Введите 1й элемент прогрессии: "))
step = int(input("Введите шаг прогрессии: "))
length = int(input("Введите длину прогрессии: "))

arifmProgression = [firstElem + (i - 1) * step for i in range(1, length + 1)]
print("Ряд арифметической прогрессии будет таким:")
print(arifmProgression)
print()

# Задача 32.
# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#         ^  ^  ^  ^   ^   ^  ^  ^   ^   ^  ^  ^   ^  ^   ^   ^  ^   ^   ^  ^
#         0  1  2  3   4   5  6  7   8   9 10 11  12 13  14  15 16  17  18 19  
# Вывод: [1, 9, 13, 14, 19]

import random as rnd

myArray = [rnd.randint(10,50) for index in range(20)]

print("Дан массив чисел:")
print(*myArray)
print(*["%02d" % i for i in range(20)])

myRangeMin = int(input("Введите диапазон сравнения: от... "))
myRangeMax = int(input("                            до... "))

desirableArray = [index for index in range(len(myArray)) if myArray[index] >= myRangeMin and myArray[index] <= myRangeMax]

print("Индексы элементов из заданного диапазона следующие:")
print(desirableArray)
