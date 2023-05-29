import random
print(list_1 := [random.randint(1,9) for _ in range(5)])
print(list_2 := [random.randint(1,9) for _ in range(5)])
list_3 = zip(list_1,list_2)
print(list_3)
def find_farthst_orbit(list_of_orbits: list)-> list[tuple[int,int]]:map