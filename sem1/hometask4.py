"""
Требуется определить, можно ли от шоколадки размером n × m долек 
отломить k долек, если разрешается сделать один разлом по прямой между 
дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""
n = int(input("введите длину шоколадки "))
m = int(input("введите ширину шоколадки "))
k = int(input("введите, сколько хотите долек получить "))
if k<n*m:
    if k%n==0 or k%m==0: # проверяем условие
        print ("Yes!")
    else:
        print ("No!")
else:
    print ("количество долек, которое вы хотите отломить, превышает общее количество долек")