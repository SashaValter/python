"""
по данному целому неотрицательному числу вычислите
n!, решить задачу используя цикл while
"""

n = int(input("введите положительное число "))
"""
if n < 0:
    print("вы ввели отрицательное число!")
else:
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"факториал числа = {factorial}")
"""
if n < 0:
    print("вы ввели отрицательное число!")
else:
    factorial = 1
    i = 1
    for i in range (1,n+1):
        factorial*=i
print(f"факториал числа = {factorial}")

    
