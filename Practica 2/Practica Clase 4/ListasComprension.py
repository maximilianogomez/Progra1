import random

lista = [random.randint(1,100) for i in range(50)]
print(lista)

lista2 = [x * 2 if x % 2 == 0 or x % 3 == 0 else x * 3 for x in range(1,51)]
print(lista2)

lista3 = []
for x in range(1,51):
    if x % 2 == 0 or x % 3 == 0:
        lista3.append(x * 2)
    else:
        lista3.append(x * 3)

print(lista3)

lista4 = [random.randrange(2,101,2) for i in range(50)]

print(lista4)