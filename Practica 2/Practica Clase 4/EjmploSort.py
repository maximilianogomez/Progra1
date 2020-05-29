import random
lista = [random.randint(-50,100) for i in range(10)]

print(lista)
print(lista[::-1])
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
lista.sort(key=lambda x : abs(x), reverse=True)
print(lista)