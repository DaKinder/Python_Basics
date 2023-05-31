# Задача №17.
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

myList1 = [1, 1, 2, 0, -1, 3, 4, 4]
print(type(myList1))
print(myList1)
# пробразовали список в множество
mySet = set(myList1)
print(type(mySet))
print(mySet)


# Задача №19.
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

myList2 = [1, 2, 3, 4, 5]
k = int(input('Введите величину сдвига: ')) % len(myList2)
for item in range(k):
    n = myList2.pop()
    myList2.insert(0, n)

print(myList2)

# Задача №21.
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

myListDic = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

listKeys = []
listValues = []
for item in myListDic:
    listKeys.append(list(item.keys())[0]) # преобразовали в список
    listValues.append(list(item.values())[0]) 
print(set(listKeys)) # преобразовали в множество
print(set(listValues))

# Задача №23.
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# Вариант 1
myList3 = [0, -1, 5, 2, 3]
print(myList3)
count = 0

for i in range(1, len(myList3)):
    if(myList3[i] > myList3[i - 1]):
        count += 1
print(f'Кол-во элементов: {count}')

# Вариант 2
result = [myList3[i] for i in range(1, len(myList3)) if myList3[i] > myList3[i - 1]]
print(f'Элементы: {result}')
result = [i for i in range(1, len(myList3)) if myList3[i] > myList3[i - 1]]
print(f'Индексы: {result}')
