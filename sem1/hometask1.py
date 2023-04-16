"""
найдите сумму чисел трехзначного числа
"""
num = int(input("введите трехзначное число: "))
firstdigit = int(num//100)
thirddigit = int(num%10)
seconddigit = int((num/10)%10)
sum = firstdigit+thirddigit+seconddigit
print (f"сумма цифр трехзначного числа = {sum}")
