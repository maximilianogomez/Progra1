#PROGRAMA PRINCIPAL:
def main():
    try:
        arch = open("RangoAlturas.txt",'w')
    except IOError:
        print("Hubo un error al crear el archivo")
    else:
        print("Se procede a cargar el archivo con alturas")
        deporte = input("Ingrese un deporte(no ingrese nada para terminar): ")
        while deporte != "":
            deporte = deporte.lower()
            deporte = deporte + "\n"
            arch.write(deporte)
            try:
                altura = float(input("Ingrese una altura(-1 para terminar): "))
                while altura != -1:
                    altura = str(altura) + "\n"
                    arch.write(altura)
                    altura = float(input("Ingrese una altura(-1 para terminar): "))
            except ValueError:
                print("Error,se esperaba un valor numerico")
            deporte = input("Ingrese un deporte(no ingrese nada para terminar): ")
        print("Se finalizó la creación del archivo")
        arch.close()

main()