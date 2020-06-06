# 3.Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los próximos Juegos Panamericanos.
# Para eso encargó la realización de un programa que incluya las siguientes funciones:

# FUNCIONES
# Graba en un archivo las alturas de los atletas de distintas disciplinas, los que se ingresan desde el teclado.
# Cada dato se debe grabar en una línea distinta.
def GrabarRangoAlturas():
    try:
        archivo = open("RangoAlturas.txt","w")
        print("Se abrió el archivo")
    except IOError:
        print("No se pudo crear el archivo")
    else:
        while True:
            deporte = input("Ingrese el deporte: (-1 para terminar): ")
            if deporte == "-1":
                break
            archivo.write(deporte+"\n")
            while True:
                try:
                    altura = float(input("Ingrese la altura: (-1 para terminar): "))
                    if altura == -1:
                        break
                except ValueError:
                    print("Error, se esperaba un numero")
                else:
                    archivo.write(str(altura)+"\n")
        print("Se modificó el archivo")
    finally:
        archivo.close()
        print("Se cerró el archivo")

# Graba en un archivo los promedios de las alturas de los atletas presentes en el archivo generado en el paso anterior.
# La disciplina y el promedio deben grabarse en líneas diferentes.
def GrabarPromedio():
    try:
        alturas = open("RangoAlturas.txt","r")
        promedio = open("PromedioAlturas.txt","w")
    except IOError:
        print("No se pudo abrir/crear los archivos")
    else:
        cont = 0
        suma = 0
        registro = alturas.readline()
        while registro != "":
            registro = registro.replace("\n","")
            while not registro.isalpha() and registro != "":
                suma += float(registro)
                cont += 1
                registro = alturas.readline()
                registro = registro.replace("\n","")
            if cont != 0:
                prom = str(round((suma / cont),2)) 
                promedio.write(prom + "\n")
                cont = 0
                suma = 0
            if registro.isalpha():
                registro += "\n"
                promedio.write(registro)
            registro = alturas.readline()
            
    finally:
        alturas.close()
        promedio.close()
            
def main():
    GrabarRangoAlturas()
    GrabarPromedio()

main()
                