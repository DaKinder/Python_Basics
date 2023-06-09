# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

from HW5Functions import involve

print("\n======== ВОЗВЕДЕНИЕ В СТЕПЕНЬ ========")
userNumber = int(input("Введите число  ... "))
userDegree  = int(input("Введите степень... "))

print(f"{userNumber} в степени {userDegree} (рекурсия) = ", end="")
print('{:,}'.format(involve(userNumber, userDegree)).replace(',', ' '))
print(f"Проверка встроенной функцией:", end="")
print('{:,}'.format(userNumber**userDegree).replace(',', ' ') + "\n")

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций допускаются только 
# +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

from HW5Functions import sum

print("\n===== СЛОЖЕНИЕ ЦЕЛЫХ НЕОТРИЦАТАЛЬНЫХ ЧИСЕЛ (рекурсия) =====")
number1 = int(input("Введите ПЕРВОЕ число ... "))
number2 = int(input("Введите ВТОРОЕ число ... "))

print(f"Сумма указанных чисел {number1} + {number2} = {sum(number1, number2)}\n")