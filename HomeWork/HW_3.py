import random as rnd

# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai
# Последняя строка содержит число X
# input 5
# 1 2 3 4 5
# Сколько раз встречается число 3
# output -> 1

listLen = int(input('Введите длину списка: '))

myList = []
for item in range(listLen) :
    myList.append(rnd.randint(0,10))
print(*myList)

userInput = int(input('Введите число, узнаем сколько раз оно встречается в списке: '))

count = 0

for item in myList:
    if item == userInput:
        count +=1

print(f'Число {userInput} встречается {count} раз') 


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# input 5
# 1 2 3 4 5
# 6
# output -> 5


myList2 = [rnd.randint(0,100) for item in range(int(input('Введите длину списка: ')))]

print(*myList2)

userInput = int(input('Введите число, найдём ближайшее по значению: '))

nearest = myList2[0]

minDiff = abs(userInput - myList2[0])

for i in range(1, len(myList2)):

    diff = abs(myList2[i] - userInput) 
    
    if diff <= minDiff: 
        nearest = myList2[i]
        minDiff = diff
        
print(f'Ближайшее к числу {userInput} по значению будет {nearest}')

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12


word = input('введите слово, подсчитаем его ценность: ').upper()

dict = {'AEIOULNSTRАВЕИНОРСТ':1,
        'DGДКЛМПУ':2,
        'BCMPБГЁЬЯ':3,
        'FHVWYЙЫ':4,
        'KЖЗХЦЧ':5,
        'JXШЭЮ':8,
        'QZФЩЪ':10}

result = 0

for letter in word:
    for key,value in dict.items():
        if letter in key:
            result += value

print(f'Ваш результат = {result}')
