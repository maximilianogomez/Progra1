# Desarrollar una función que reciba tres números enteros positivos y verifique si
# corresponden a una fecha gregoriana válida (día, mes, año). Devolver True o False
# según la fecha sea correcta o no. Realizar también un programa para verificar el
# comportamiento de la función.

#Funciones:
def IngresarPositivo(mensaje):
    """Ingresa un numero y te lo hace validar """
    numero = int(input(mensaje))
    while numero < 1:
        print("El numero ingresado es menor que 1")
        numero = int(input(mensaje))
    return numero


def EsBisiesto(anio):
    """True si el año es bisiesto, False si no lo es"""
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0
    
def Validarfecha(dia,mes,anio):
    """Supongo que la fecha es valida """
    fechavalida = True
    if dia < 1 or mes < 1 or anio < 1:
        #algun valor es negativo
        fechavalida = False
    elif mes > 12:
        #mes es mayor a 12
        fechavalida = False
    elif dia > 31:
        #dia es mayor a 31
        fechavalida = False
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
        #mes de 30 dias y dia mayor a 30
        fechavalida = False
    elif mes == 2 and EsBisiesto(anio) and dia > 29:
        #anio bisiesto y el dia de febrero mayor a 29
        fechavalida = False
    elif mes == 2 and (not EsBisiesto(anio)) and dia > 28:
        #anio bisiesto y el dia de febrero mayor a 28
        fechavalida = False
    return fechavalida


def main():
    print("Ejercicio 1.2 validar una fecha")
    print("Ingrese una fecha")
    dia = IngresarPositivo("Ingrese un dia: ")
    mes = IngresarPositivo("Ingrese un mes: ")
    anio = IngresarPositivo("Ingrese un anio: ")
    
    esfechavalida = Validarfecha(dia,mes,anio)
    
    if esfechavalida:
        print("La fecha ingresada es valida ")
    else:
        print("La fecha ingresada no es valida")

#Programa Principal:
if __name__ == "__main__":
    main()