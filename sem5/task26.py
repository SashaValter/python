def degree(a,b):
    res = 1
    for i in range(0,b):
        res *=a
    return res
a = int(input("введите число А: "))
b = int(input("введите число B: "))
print(degree(a,b))