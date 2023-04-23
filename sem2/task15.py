"""
Иван васильевич пришел на рынок, чтобы купить 2 арбуза, один для себя
другой для тещи. Для себя нужно выбрать по тяжелее.
нужно выбрать самый легкий и самый тяжелый арбуз
"""
import random
watermelon = int(input("введите количество арбузов  "))
max = 1
min = 500
for i in range(watermelon):
    weight = random.randint(1, 25)
    print(weight, end=" ")
    if weight > max:
        max = weight
    if weight < min:
        min = weight
print(f"минимальный вес арбуза = {min}")
print(f"максимальный вес арбуза = {max}")
