##33. Все максимальные значения изменить на минимальные
import random # вызываем инструмент рандома
marks = [random.randint(1,5) for _ in range (10)] # генерируем список оценок
print(marks)
max_marks = max(marks) # создаем переменную. которая имеет максимальное значение из списка
min_marks = min(marks) # то же самое, только минимальное
for i in range(len(marks)): # перебираем каждый элемент списка
    if marks[i]== max_marks : marks[i] = min_marks # своп
print(marks)
