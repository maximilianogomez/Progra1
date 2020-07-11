edades = {"Juan": 23, "Maria": 18, "Marcelo": 30, "Pedro": 23 }

valores = list(edades.values())

valores.sort()

claves_ord = []

i = 0


while i < len(valores):
    for clave in edades:
        if edades[clave] == valores[i] and clave not in claves_ord:
            #Uso el break porque se repite y quiero pasar a otra iteraciín
            claves_ord.append(clave)
    i += 1

for clave in claves_ord:
    print("Clave : ", clave, "Valor: ", edades[clave] )