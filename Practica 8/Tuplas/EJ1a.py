# Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios,
# y luego escribir un programa para verificar su comportamiento:
# a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
# válida.

#FUNCIONES:
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

def IngresarPositivo(mensaje):
    """Ingresa un numero y te lo hace validar """
    try:
        numero = int(input(mensaje))
        while numero < 1 and numero != -1:
            print("El numero ingresado es menor que 1")
            numero = int(input(mensaje))
        return numero
    except ValueError:
        raise

#PROGRAMA PRINCIPAL:
def main():
    while True:
        try:
            print("Ejercicio 8.1a validar una fecha ingresada desde el teclado")
            print("Ingrese una fecha")
            dia = IngresarPositivo("Ingrese un dia(-1 para terminar): ")
            if dia == -1:
                break
            mes = IngresarPositivo("Ingrese un mes(-1 para terminar): ")
            if mes == -1:
                break
            anio = IngresarPositivo("Ingrese un anio(-1 para terminar): ")
            if anio == -1:
                break
                
            esfechavalida = Validarfecha(dia,mes,anio)
            
            if Validarfecha(dia,mes,anio):
                fecha = ()
                fecha += (dia,mes,anio)
                print(fecha)
            else:
                print("La fecha ingresada no es valida ")
        except ValueError:
            print("Se esperaba un numero entero")
    
    
    
if __name__ == "__main__":
    main()