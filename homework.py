import math
import random

# Домашнее задание по четвертому семинару
# 1. ДЗ	Вычислить число c заданной точностью d

# from math import pi
# d = input('Enter number: ').split('.')
# num = str(pi).split('.')
# print(num[0] + '.' + num[1][:len(d[1])])

# 2. ДЗ	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# def find_lst_simple(n):
#     min_simple = 2  # минимальное натуральное число
#     lst = []
#     while n >= min_simple:
#         while n % min_simple == 0:
#             lst.append(min_simple)
#             n /= min_simple
#         min_simple += 1
#     return lst


# n = int(input('Введите натуральное число: '))
# lst = find_lst_simple(n)
# print(f'{lst} - список простых множителей числа {n}')

# 3. ДЗ	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 2, 2, 3, 4]  -> [1, 3, 4]

# def random_sp(n):
#     sp = []
#     for i in range(n):
#         sp.append(random.randrange(n))
#     return sp


# sp = random_sp(6)
# print(f'{sp} - заданная последовательность чисел')
# sp_new = []
# for i in sp:
#     if sp.count(i) == 1:
#         sp_new.append(i)

# print(f'{sp_new} - список неповторяющихся элементов исходной последовательности')

# 4. ДЗ	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# data = open('002.txt', 'w')
# k = 3


# def random_sp(n):
#     sp = []
#     for i in range(n + 1):
#         sp.append(random.randrange(100))
#     return sp


# sp = random_sp(k)
# # print(sp)
# st = ''
# for i in range(len(sp)):
#     if sp[0] == 0:
#         break
#     elif k > 1 and sp[i] > 1:
#         st += ' + ' + str(sp[i]) + 'x^' + str(k)
#         k -= 1
#     elif k > 1 and sp[i] == 1:
#         st += ' + x^' + str(k)
#         k -= 1
#     elif k > 1 and sp[i] == 0:
#         st += ''
#         k -= 1
#     elif k == 1 and sp[i] > 1:
#         st += ' + ' + str(sp[i]) + 'x'
#         k -= 1
#     elif k == 1 and sp[i] == 1:
#         st += ' + x'
#         k -= 1
#     elif k == 1 and sp[i] == 0:
#         k -= 1
#     elif k == 0 and sp[i] != 0:
#         st += ' + ' + str(sp[i])

# if st:
#     print(st[3:] + ' = 0')
#     data.writelines(st[3:] + ' = 0')

# data.close()
# 5. ДЗ	Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

path = '001.txt'
data = open(path, 'r')
for line in data:
    pn1 = line
data.close()

path = '002.txt'
data = open(path, 'r')
for line in data:
    pn2 = line
data.close()

# f = '3x^2 + 5x + -9 = 0'
pn1 = pn1[: -4]
pn1 = pn1.split(' + ')
# print(pn1)
sp1 = []
for i in pn1:
    sp1.append(int(i.split('x')[0]))
# print(sp1)
a1, b1, c1, d1 = sp1

pn2 = pn2[: -4]
pn2 = pn2.split(' + ')
# print(pn2)
sp2 = []
for i in pn2:
    sp2.append(int(i.split('x')[0]))
# print(sp2)
a2, b2, c2, d2 = sp2
a3, b3, c3, d3 = a1 + a2, b1 + b2, c1 + c2, d1 + d2

print(f'{a3}x^3 + {b3}x^2 + {c3}x + {d3} = 0')

data = open('003.txt', 'w')
# запись суммы многочленов в новый файл 003.txt
data.writelines(f'{a3}x^3 + {b3}x^2 + {c3}x + {d3} = 0')
