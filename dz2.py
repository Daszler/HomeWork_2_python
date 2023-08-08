#Задача 10.
#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть
# 5 -> 10110
# 2
import random
from random import randint

N = int(input("Число монеток: "))
m = 0
k = 0
coins = [0, 1]
for _ in range(N):
    random.shuffle(coins)
    print(f'все монеты{coins}')
    if int(coins[0]) == 0:
        k += 1
    if int(coins[0]) == 1:
        m += 1
print(f'всего монет {m, k}')

if m > k:
    ans = k
else:
    ans = m 
print(f'минимальное количество монет, которое нужно перевернуть {ans}')

#Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных 
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя 
# делает две подсказки. Он называет сумму этих чисел S и их произведение P.
#  Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3


# Вариант 1
# s = int(input("Сумма двух чисел: "))
# p = int(input("Произведение двух чисел: "))

# x = (s- (s**2-4*p)**0.5) // 2
# y = s - x
# if x <= 1000 and y <= 1000:
#     print(f'числа задуманные Петей{x, y}')


# Вариант 2
x = int(input('Введите сумму чисел : '))
y = int(input('Введите произведение чисел: '))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)


# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

N = int(input("Введи число N:"))
i = 0
while 2 ** i <= N:
    print(f"числа вида 2к {i} равна {2 ** i}")
    i += 1

"""Задача 13
Уставшие от необычно теплой зимы, жители решили узнать, 
действительно ли это самая длинная оттепель за всю историю 
наблюдений за погодой. Они обратились к синоптикам, а те, в 
свою очередь, занялись исследованиями статистики за 
прошлые годы. Их интересует, сколько дней длилась самая 
длинная оттепель. Оттепелью они называют период, в 
который среднесуточная температура ежедневно превышала 
0 градусов Цельсия. Напишите программу, помогающую 
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 5"""
from random import randint

# days = int(input('Введите кол-во дней: '))
days = 10  # зададим для отладки
today_temp = randint(-3, 3)
warm_days_counter = 0
warm_days_max = 0

print(f'Температура: ', end="")

for i in range(0, days):

    today_temp += randint(-3, 3)
    print(today_temp, end=" ")

    if today_temp > 0:
        warm_days_counter += 1
    else:
        warm_days_counter = 0
    if warm_days_counter > warm_days_max:
        warm_days_max = warm_days_counter

print()
print(f'Самая длинная оттепель -> {warm_days_max} д.')