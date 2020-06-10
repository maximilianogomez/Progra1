# Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
# 20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.

#PROGRAMA PRINCIPAL:
def main():
    dic = {}
    for i in range(1,21):
        dic[i] = i**2
    for claves in dic:
        print("clave: ", claves, "valor: ", dic[claves])

main()