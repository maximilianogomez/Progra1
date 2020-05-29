# Escribir una función diasiguiente(…) que reciba como parámetro una fecha cualquiera
# expresada por tres enteros (correspondientes al día, mes y año) y calcule y
# devuelva tres enteros correspondientes el día siguiente al dado.
# Utilizando esta función, desarrollar programas que permitan:
# a. Sumar N días a una fecha.
# b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.

import funciones.ingreso as f
import EJ2

#Funciones:
def dia_siguiente(dia,mes,anio):
    """
    Determina el dia siguiente a una fecha ingresada
    
    Devuelve el dia,mes, año correspondientes al dia siguiente de la fecha ingresada
    
    Parámetros:
    dia -- numero entero positivo correspondiente al dia del mes
    
    mes -- numero entero positivo correspondiente al mes del año
    
    año -- numero entero positivo correspondiente al año del calendario.
    """
    if (EJ2.Validarfecha(dia + 1, mes, anio)):
        dia = dia + 1
    elif (EJ2.Validarfecha(1, mes + 1, anio)):
        dia = 1
        mes = mes + 1
    else:
        dia = 1
        mes = 1
        anio = anio + 1
    return dia, mes , anio


def main():
    print("Ejercicio 1.9a, sumar N dias a una fecha")
    print("Ingresar una fecha")
    dia = f.IngresarPositivo("Ingrese un dia: ")
    mes = f.IngresarPositivo("Ingrese un mes: ")
    anio = f.IngresarPositivo("Ingrse un anio: ")
    if (EJ2.Validarfecha(dia,mes,anio)):
        dias = f.IngresarPositivo("Dias a sumar: ")
        for i in range(dias):
            dia, mes ,anio = dia_siguiente(dia,mes,anio)
        print("La nueva fecha es: ", end = " ")
        print(dia,mes,anio ,sep = "/")
    else:
        print("La fecha ingresada no es valida")
        
#Programa Pincipal:        
if __name__ == "__main__":
    main()
    