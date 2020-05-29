# Escribir una función diasiguiente(…) que reciba como parámetro una fecha cualquiera
# expresada por tres enteros (correspondientes al día, mes y año) y calcule y
# devuelva tres enteros correspondientes el día siguiente al dado.
# Utilizando esta función, desarrollar programas que permitan:
# a. Sumar N días a una fecha.
# b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.

import funciones.ingreso as f
import EJ2
import EJ9a

#Funciones:
def fecha_menor(dia1,mes1,anio1,dia2,mes2,anio2):
    """
    Determina cual fecha es menor entre dos fechas y la mayor.
    
    Devuelve el dia,mes, año correspondientes a la fecha menor y el dia, mes, año correspondiente a la fecha mayor
    
    Parámetros:
    dia -- numero entero positivo correspondiente al dia del mes
    
    mes -- numero entero positivo correspondiente al mes del año
    
    año -- numero entero positivo correspondiente al año del calendario.
    """
    if anio2 < anio1 :
        diam = dia2
        mesm = mes2
        aniom = anio2
        diaM = dia1
        mesM = mes1
        anioM = anio1
    elif anio1 < anio2:
        diam = dia1
        mesm = mes1
        aniom = anio1
        diaM = dia2
        mesM = mes2
        anioM = anio2
    else:
        aniom = anio1
        anioM = anio1
        if mes1 < mes2:
            diam = dia1
            diaM = dia2
            mesm = mes1
            mesM = mes2
        elif mes2 < mes1:
            diam = dia2
            mesm = mes2
            diaM = dia1
            mesM = mes1
        else:
            mesm = mes1
            mesM = mes1
            if dia2 < dia1:
                diam = dia2
                diaM = dia1
            elif dia1 < dia2:
                diam = dia1
                diaM = dia2
            else:
                diam = dia1
                diaM = dia1
    return diam,diaM , mesm,mesM , aniom,anioM


def main():
    print("Ejercicio 1.9b, Calcular la cantidad de días existentes entre dos fechas cualesquiera")
    print("Ingresar una fecha")
    dia1 = f.IngresarPositivo("Ingrese un dia: ")
    mes1 = f.IngresarPositivo("Ingrese un mes: ")
    anio1 = f.IngresarPositivo("Ingrse un anio: ")
    dia2 = f.IngresarPositivo("Ingrese un dia: ")
    mes2 = f.IngresarPositivo("Ingrese un mes: ")
    anio2 = f.IngresarPositivo("Ingrse un anio: ")
    if (EJ2.Validarfecha(dia1,mes1,anio1)) and (EJ2.Validarfecha(dia2,mes2,anio2)):
        diam,diaM,mesm,mesM, aniom,anioM = fecha_menor(dia1,mes1,anio1,dia2,mes2,anio2)
        print("Desde: ", end = " ")
        print(diam,mesm,aniom ,sep = "/")
        print("Hasta: ", end = " ")
        print(diaM,mesM,anioM ,sep = "/")
        cont = 0
        while (aniom != anioM or mesm != mesM or diam != diaM):
            diam, mesm ,aniom = (EJ9a.dia_siguiente(diam,mesm,aniom))
            cont += 1
        print("pasaron ", end = " ")
        print(cont, "dias")
    else:
        print("Alguna de las fechas ingresadas no es valida")
        
#Programa Pincipal:        
if __name__ == "__main__":
    main()
    