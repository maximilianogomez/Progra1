# Escribir una función que reciba como parámetro una tupla conteniendo una fecha
# (día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
# en formato extendido. Por ejemplo, para (12,10,17) devuelve "12 de Octubre de
# 2017". Escribir también un programa para verificar su comportamiento

import EJ1a

class Fechainvalida(Exception):
    pass

#FUNCIONES:
def cambiar_formato(tupla):
    dia,mes, anio = tupla
    meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    if mes >= 1 and mes <= 12:
        mes = meses[mes-1]
    else:
        raise Fechainvalida
    cad = (str(dia) + ' de '+ str(mes)+' de '+str(anio))
    return cad


#PROGRAMA PRINCIPAL:
def main():
    while True:
        try:
            dia = int(input("Ingrese un dia(en numeros, -1 para terminar): "))
            if dia == -1:
                break
            mes = int(input("Ingrese un mes(en numeros): "))
            anio = int(input("Ingrese un anio(en numeros): "))
            if EJ1a.Validarfecha(dia,mes,anio):
                tupla = (dia,mes,anio)
                cad = cambiar_formato(tupla)
                print(cad)
            else:
                raise Fechainvalida("La fecha no es valida")
        except Fechainvalida as mensaje:
            print(mensaje)
        except ValueError:
            print("Se esperaba un numero entero")
            
if __name__ == "__main__":
    main()