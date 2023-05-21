def sum(a,b):
    for i in range (0,b):
        a = a + 1
    return a
a = int(input("введите число А: "))
b = int(input("введите число B: "))
print(sum(a,b))