# Escribir una función que reciba como parámetro un número entero entre 0 y 3999
# y lo convierta en un número romano, devolviéndolo en una cadena de caracteres.
# ¿En qué cambiaría la función si el rango de valores fuese diferente?

#Funciones:
def convertir_romano(num):
    simbolos = ["M", "CM", "D", "CD", "C","XC", "L","XL" , "X", "IX", "V","IV", "I"]
    valores = [1000, 900, 500,400, 100, 90, 50, 40,10, 9, 5,4,1]
    romano = ""
    i = 0
    while num > 0:
        for x in range(num//valores[i]):
            romano += simbolos[i]
            num -= valores[i]
        i += 1
    return romano

def convertir_romano2(num):
    simbolos = ["M", "CM", "D", "CD", "C","XC", "L","XL" , "X", "IX", "V","IV", "I"]
    valores = [1000, 900, 500,400, 100, 90, 50, 40,10, 9, 5,4,1]
    romano = ""
    i = 0
    while num > 0:
        sim = num // valores[i]
        romano += (simbolos[i]*sim)
        num -= (valores[i]*sim)
        i +=  1
    return romano
            
def validarNum(mensaje):
    num = int(input(mensaje))
    while num < 0 or num > 3999:
        print("Numero invalido")
        num = int(input(mensaje))
    return num

#Programa Principal:
def main():
    numero = validarNum("Escriba un numero entre 0 y 3999: ")
    numRomano = convertir_romano2(numero)
    print(f"El numero {numero} en romano es: {numRomano}")

if __name__ == "__main__":
    main()