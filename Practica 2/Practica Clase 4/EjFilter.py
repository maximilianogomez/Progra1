import random

def esPar(num):
    return num % 2 == 0


lista = [random.randint(1,100) for i in range(50)]
print(lista)

pares = filter(esPar,lista)
multiplos3 = filter(lambda x : x % 3 == 0,lista)
listaPares = list(pares)
print(listaPares)

for x in multiplos3:
    print(x, end=" ")