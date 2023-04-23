"""
жители решили узнать, действительно ли это самая длинная оттепель за все время
оттепель = температура >0
пользователь вводит количество дней от 1 до 100
температуры - целые числа в диапазоне от -50 до 50
input: 6 -> -20 30 -40 10 25 -2
output: 2
"""
import random
days = int(input("введите количество дней "))
today = 0
i=1
count = 0
max = 0
while i<=days:
    today+= random.randint(-1,5)
    print (today, end=" ")
    if today > 0:
        count+=1
    if max < count:
        max = count
    else:
        count = 0
    i+=1

print (f"\n количество дней с положительной температурой подряд = {count}")        

