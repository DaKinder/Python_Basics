# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N)
# 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

n = int(input('Введите факториал: ')) + 1
product = 1

for i in range(1, n) :
    product = product * i

print(f'Факториал числа {n-1}! = {product}')

# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# 0 1 1 2 3 5 8 13 21 34
num = int(input('Введите число Фибоначи: '))
fib1 = 0
fib2 = 1
count = 2

for i in range(num + 1):
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    count += 1
    if fib3 == num:
        print(f'Число: {num} является {count} числом Фибоначи')
        break    
    elif fib3 > num:
        print(f'Число: {num} не является числом Фибоначи')
        break


# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

count = 0
maxRange = 0

n = int(input('Введите количество дней: '))

for dayCount in range(n):
    day = int(input('Введите температуру дня: '))
    if day > 0:
        count += 1
    elif count >= maxRange:
        maxRange = count
        count = 0
if count > maxRange:
    maxRange = count

print(f'Максимальная длина оттепели = {maxRange}')

# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

n = int(input('Введите кол-во арбузов: '))
maxWeight = 0
minWeight = 0

for i in range(n):
    weight = int(input('Введите вес арбуза: '))
    if maxWeight == 0:
        maxWeight = minWeight = weight
    elif weight > maxWeight:
        maxWeight = weight
    elif weight < minWeight:
        minWeight = weight

print(f'Вес маленького = {minWeight} , большого = {maxWeight}')