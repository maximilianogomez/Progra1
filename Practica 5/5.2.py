# Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo
# números reales, sume ambos valores y devuelva el resultado como un
# número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
# utilizando manejo de excepciones para detectar el error.

#FUNCIONES:
def suma_cad(cad1,cad2):
    try:
        suma = int(cad1) + int(cad2)
    except ValueError:
        suma = -1
    return suma

#PROGRAM PRINCIPAL:
def main():
    cad1 = input("Ingrese un numero: ")
    cad2 = input("Ingrese otro numero: ")
    if suma_cad(cad1,cad2) == -1:
        print("Alguna de las cadenas no contiene un número válido")
    else:
        print(f"La suma es: {suma_cad(cad1,cad2)}")
    
    
    
    
main()