import math
import random

# Домашнее задание по второму семинару

# 1. ДЗ	Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 	6782 -> 23
# 	0.56 -> 11

# 1 решение задачи
# n = input('Enter number N: ').split('.')
# if len(n) > 1:
#     n = n[0]+n[1]
# else:
#     n = n[0]
# l = len(n)
# sum = 0
# for i in range(l):
#     sum += int(n[i])
# print(sum)

# 2 решение задачи
# n = input('Enter number N: ')
# sum = 0
# for i in range(len(n)):
#     if n[i] != ".":
#         sum += int(n[i])
# print(sum)

# 3 решение задачи
# n = input('Enter number N: ')
# sum = 0
# for i in range(len(n)):
#     if n[i].isdigit():
#         sum += int(n[i])
# print(sum)

# 2. ДЗ	Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# 	пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

# n = int(input('Enter number N: '))
# mult = 1  # результат произведения чисел
# list = []
# for i in range(1, n+1):
#     list.append(mult)
#     mult *= i + 1
# print(list)

# 3 ДЗ Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.

# list = []
# summ = 0
# n = int(input('Enter number N: '))
# for i in range(1, n+1):
#     list.append(round((1+1/i)**i, 2))
#     summ += (1+1/i)**i
# print(
#     f"Cписок из {n} чисел последовательности (1+1/n)^n: {list}, сумма всех чисел списка равна {round(summ, 2)}")

# 4. ДЗ	Задайте числами список из N элементов, заполненных из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

lst = []
# n = int(input('Enter number N: '))
n = 6
for i in range(-n, n+1):
    lst.append(i)
print(f"задаём список от -{n} до {n}: {lst}")

with open("file.txt") as file:
    array = [int(row.strip()) for row in file]
print(f"считываем позиции из файла: {array}")

mult = 1
for i in array:
    if lst[i] != 0:
        mult *= lst[i]
print(f"Получаем произведение элементов на указанных позициях: {mult}")

# 5. ДЗ	Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, другие методы из библиотеки random - можно).

# original_list = list(range(1, 11))
# mixed_list = []
# print(original_list)
# length = len(original_list)
# for i in range(length):
#     n = random.choice(original_list)
#     mixed_list.append(n)
#     original_list.remove(n)
# print(mixed_list)
