# Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios,
# y luego escribir un programa para verificar su comportamiento
# Sumar N días a una fecha.

import EJ1a 

#FUNCIONES:
def sumarN(fecha,n):
    dia , mes , anio = fecha
    dia += n
    while not EJ1a.Validarfecha(dia,mes,anio):
        if mes == 2 and EJ1a.EsBisiesto(anio) and dia > 29:
            #anio bisiesto y el dia de febrero mayor a 29
            dia -= 29
            mes += 1
        elif mes == 2 and (not EJ1a.EsBisiesto(anio)) and dia > 28:
            #anio no bisiesto y el dia de febrero mayor a 28
            dia -= 28
            mes += 1
        elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
            dia -= 30
            mes += 1
        else:
            if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10) and dia > 31:
                dia -= 31
                mes += 1
            elif mes == 12 and dia > 31:
                dia -= 31
                mes = 1
                anio += 1
    fecha = dia, mes, anio
    return fecha
            
def sumarN2(fecha,n):
    dia , mes , anio = fecha
    for _ in range(n):
        if EJ1a.Validarfecha(dia+1,mes,anio):
            dia += 1
        else:
            dia = 1
            if EJ1a.Validarfecha(dia , mes+1,anio):
                mes += 1
            else:
                mes = 1
                anio += 1
    fecha = dia, mes, anio
    return fecha
                
            
#PROGRAMA PRINCIPAL:
def main():
    while True:
        try:
            print("Ejercicio 8.1b sumar n dias a una fecha")
            print("Ingrese una fecha")
            dia = EJ1a.IngresarPositivo("Ingrese un dia(-1 para terminar): ")
            if dia == -1:
                break
            mes = EJ1a.IngresarPositivo("Ingrese un mes(-1 para terminar): ")
            if mes == -1:
                break
            anio = EJ1a.IngresarPositivo("Ingrese un anio(-1 para terminar): ")
            if anio == -1:
                break
                
            esfechavalida = EJ1a.Validarfecha(dia,mes,anio)
            
            if esfechavalida:
                fecha = ()
                fecha += (dia,mes,anio)
                print(fecha)
                nro = EJ1a.IngresarPositivo("Ingrese la cantidad de dias a sumar(-1 para terminar): ")
                if nro == -1:
                    break
                fecha2 = sumarN2(fecha,nro)
                print("La fecha con los dias agregados es: ")
                print(fecha2)
            else:
                print("La fecha ingresada no es valida ")
        except ValueError:
            print("Se esperaba un numero entero")

if __name__ == "__main__":
    main()