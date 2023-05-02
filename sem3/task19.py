"""
дана последовательность из n целых чисел и число K, необходимо сдвинуть
всю последовательность, (сдвиг циклический) на К элементов вправо.
К - положительное число
"""
k = int(input("Введите К: "))
my_list = [1,2,3,4,5]
# n = len(my_list)
# new_my_list = my_list[-k:]+ my_list[:-k]
# print(new_my_list)
for _ in range (k):
    my_list.insert(0,my_list.pop()) # .pop - последний элемент
print(my_list)


