"""
дано натуральное число, требуется понять является ли год с данным номером весокосным
год является весокосным, если  его номер кратен 4
но не кратен 100, а также если он кратен 400
"""
year = int(input("введите год для проверки: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("год кратен!")
else:
    print("не кратен!")
