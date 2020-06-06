# Escribir un programa que permita grabar un archivo los datos de lluvia caída durante
# un año. Cada línea del archivo se grabará con el siguiente formato:
# <dia>;<mes>;<lluvia caída en mm> por ejemplo 25;5;319
# Los datos se generarán mediante números al azar, asegurándose que las fechas
# sean válidas. La cantidad de registros también será un número al azar entre 50 y
# 200. Por último se solicita leer el archivo generado e imprimir un informe en formato
# matricial donde cada columna represente a un mes y cada fila corresponda a
# los días del mes. Imprimir además el total de lluvia caída en todo el año.

from random import randint as r

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

def CrearMatriz(n = 31, m = 12):
    filas = n+1                                       
    col = m                                                    
    matriz = []                                                 
    for _ in range(filas):
        matriz.append([0] * col)
    return matriz

def imprimirMatriz(matriz):
    'muestra una matriz por pantalla'
    meses = ["Enero","Febre","Marzo","Abril","Mayo","Junio","Julio","Agost","Septi","Octub","Novie","Dicie"]
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        if f == 0:
            print("\t" + "Enero","Febre","Marzo","Abril","Mayo","Junio","Julio","Agost","Septi","Octub","Novie","Dicie")
        for c in range(columnas):
            if c == 0:
                print(f"Día {f}: ", "%6d" %matriz[f][c], end = "")
            else:
                print("%6d" %matriz[f][c], end = "")
        print()

#PROGRAMA PRINCIPAL:
def main():
    try:
        arch = open("Lluvia.txt",'w')
    except IOError:
        print("Error, no se pudo crear el archivo")
    else:
        registros = r(50,200)
        for _ in range(registros):
            dia = r(1,31)
            mes = r(1,12)
            anio = r(1900,2020)
            while not Validarfecha(dia , mes , anio):
                dia = r(1,31)
                mes = r(1,12)
                anio = r(1900,2020)
            arch.write(str(dia)+";"+str(mes)+";"+str(r(1,500))+"\n")
        arch.close()
        print("Su archivo Lluvia.txt se creó exitosamente")
    try:
        arch = open("Lluvia.txt")
    except IOError:
        print("Error, no se pudo abrir el archivo")
    else:
        matriz = CrearMatriz()
        linea = arch.readline()
        while linea != "":
            linea = linea.replace("\n","")
            lista = linea.split(";")
            matriz[int(lista[0])-1][int(lista[1])-1] = int(lista[2])
            linea = ";".join(lista)
            linea = linea + "\n"
            linea = arch.readline()
        imprimirMatriz(matriz)
        arch.close()

if __name__ == "__main__":
    main()