# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print("...Программа поиска сцммы цифр трехзначного числа...")
inputNum = int(input('Введите число:'))
flag = True
while (flag):
    if inputNum < 100 or inputNum >= 1000:
        inputNum = int(input('Попробуйте ещё разок: '))
    else:
        flag = False

tempNum = inputNum
summ = 0
while (inputNum > 0):
    summ += inputNum % 10
    inputNum //= 10

print(f"{summ} -> {summ} ({tempNum // 100} + {tempNum //10%10} + {tempNum %10})")


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10


# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить ровно k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no
