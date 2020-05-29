# Los números de claves de dos cajas fuertes están intercalados dentro de un número
# entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
# para obtener ambas claves, donde la primera se construye con los dígitos
# impares de la clave maestra y la segunda con los dígitos pares. Los dígitos se
# numeran desde la izquierda. Ejemplo: Si clave maestra = 18293, la clave 1 sería
# 123 y la clave 2 sería 89.

def claves_separadas(maestra):
    num1 = ""
    num2 = ""
    for i in range(len(maestra)):
        if i % 2 == 0:
            num1 = num1 + maestra[i]
        else:
            num2 = num2 + maestra[i]
    return num1,num2

def claves_rebanadas(maestra):
    num1 = maestra[::2]
    num2 = maestra[1::2]
    return num1,num2
    
def main():
    clave_maestra = input("Ingrese una cadena de caracteres: ")
    clave1,clave2 = claves_rebanadas(clave_maestra)
    print(f"La clave maestra es: {clave_maestra}")
    print(f"La clave 1 es: {clave1} y la clave 2 es: {clave2}")

if __name__ == "__main__":
    main()