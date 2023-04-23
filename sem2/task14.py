"""
Задача 14: Требуется вывести все целые степени двойки
(т.е. числа вида 2k), не превосходящие числа N
"""
num = int(input("введите число N  "))
first_digit= 1
i=1
for i in range (num):
    first_digit*= 2
    print(first_digit)