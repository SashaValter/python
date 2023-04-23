"""
дано натуральное число A>1, определите, каким по счету числом фибоначчи оно
является, то есть выведите такое число n, что f(n) = A.
Если А не является числом Фибоначчи выведите (число -1)
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
987, 1597, 2584, 4181, 6765, 10946, 17711...
"""
number_1 = int(input("введите число больше единицы "))
"""
if number_1<=1:
    print ("вы ввели число меньше единицы!")
else:
    count_number = 1
    first_previous_num = 0
    second_previous_num = 1
    current_num = 1
    while current_num <= number_1:
        current_num = first_previous_num+second_previous_num
        first_previous_num = second_previous_num
        second_previous_num = current_num
        count_number += 1
    if count_number == 0:
        print(-1)
    else:
        print(count_number)
"""
first = 0
second = 1
index = 2
while second <number_1:
    first, second = second, first+second
    index +=1
print (index if second == number_1 else -1)