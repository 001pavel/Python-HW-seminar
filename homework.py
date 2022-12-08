import math
import random

# Домашнее задание по третьему семинару

# 1. ДЗ	Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# o	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# import random
# sp1 = [2, 3, 5, 9, 3]
# sp3 = list(range(5))


# def random_sp(n):
#     sp = []
#     for i in range(n):
#         sp.append(random.randrange(1, n))
#     return sp


# def sum_odd_position(sp):
#     count = 0
#     for i in range(len(sp)):
#         if i % 2 != 0:
#             count += sp[i]
#     print(count)


# sp2 = random_sp(5)
# print(sp2)
# sum_odd_position(sp2)

# 2.	Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o	[2, 3, 4, 5, 6] => [12, 15, 16];
# o	[2, 3, 5, 6] => [12, 15]
# sp1 = [2, 3, 4, 5, 6]
# sp3 = [2, 3, 5, 6]


# def random_sp(n):
#     sp = []
#     for i in range(n):
#         sp.append(random.randrange(1, n + 1))
#     return sp


# def mult_sp(sp):
#     mult = 1
#     for i in range(len(sp)//2):
#         mult = sp[i] * sp[-1-i]
#         print(mult, end=' ')
#     if len(sp) % 2 != 0:
#         print(sp[(len(sp) // 2)]**2, end=' ')


# sp2 = random_sp(5)
# print(sp2)
# mult_sp(sp2)

# 3.	Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# o	[1.1, 1.2, 3.1, 5, 10.01] => 0.19
# sp1 = [1.1, 1.2, 3.1, 5, 10.01]
# sp3 = [0.03, 1.17, 9.62, 7.2, 4.86]


# def random_sp(n):
#     sp = []
#     for i in range(n):
#         sp.append(round(random.random()*10, 2))
#     return sp


# def find_dif(sp):
#     max_num = sp[0] % 1
#     min_num = sp[0] % 1
#     for i in range(len(sp)):
#         after_dot = sp[i] % 1
#         # print(f"after dot: {after_dot}")
#         if max_num < after_dot:
#             max_num = after_dot
#             # print(f"max: {max_num}")
#         if min_num > after_dot:
#             min_num = after_dot
#             # print(f"min: {min_num}")
#     print(round(max_num - min_num, 2))


# sp2 = random_sp(5)
# print(sp2)
# find_dif(sp2)

# 4.	Напишите программу, которая будет преобразовывать десятичное число в двоичное (встроенными методами пользоваться нельзя).
# Пример:
# o	45 -> 101101
# o	3 -> 11
# o	2 -> 10

# def conv_to_binary(n):
#     sp = []
#     while n > 0:
#         sp.append(n % 2)
#         n //= 2
#     for i in range(len(sp)):
#         print(sp[-1-i], end=' ')


# conv_to_binary(int(input('Enter number: ')))

# 5.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# o	для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def nfib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return nfib(n+2) - nfib(n+1)


k = 8
sp = []

for i in range(-k, k + 1):
    if i < 2:
        sp.append(nfib(i))
    else:
        sp.append(fib(i))

print(sp)
