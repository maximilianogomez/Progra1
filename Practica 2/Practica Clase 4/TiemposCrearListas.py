from time import time_ns as t

cant = 10000000
inicio = t()
lista = [x*2 if x%2==0 else x*3 for x in range(cant)]
fin = t()
print("Tiempo por comprension:",(fin-inicio)/1000000000,"segundos")
inicio = t()
lista2 = []
for x in range(cant):
    if x%2 == 0:
        lista2.append(x*2)
    else:
        lista2.append(x*3)
fin = t()
print("Tiempo por ciclos:",(fin-inicio)/1000000000,"segundos")