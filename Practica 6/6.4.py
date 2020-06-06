# Escribir un programa que lea un archivo de texto conteniendo un conjunto de
# apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
# ARMENIA.TXT los nombres de aquellas personas cuyo apellido terminan con la
# cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en el archivo
# ESPAÑA.TXT los terminados en "EZ". Descartar el resto. Ejemplo:
# Arslanian, Gustavo –> ARMENIA.TXT
# Rossini, Giuseppe –> ITALIA.TXT
# Pérez, Juan –> ESPAÑA.TXT
# Smith, John –> descartar
# El archivo de entrada puede ser creado mediante el Block de Notas o el IDLE. No
# escribir un programa para generarlo.

#FUNCIONES:
def lectura():
    try:
        origen = open("apellidos.txt",'r')
        armenia = open("armenia.txt",'w')
        italia = open("italia.txt",'w')
        espania = open("espania.txt",'w')
    except IOError as mensaje:
        print(mensaje)
    else:
        for registro in origen:
            registro = registro.replace("\n","")
            #Todos los registros estan de la forma Apellido, Nombre por lo tanto uso split
            lista = registro.split(",")
            #Hago una rebanada del appelido para trabajar con los ultimos 3 caracteres
            rebanada = (lista[0])[len(lista[0])-3::]
            rebanada2 = (lista[0])[len(lista[0])-2::]
            registro = ",".join(lista)
            registro += "\n"
            if rebanada == "ian":
                armenia.write(registro)
            elif rebanada == "ini":
                italia.write(registro)
            elif rebanada2 == "ez":
                espania.write(registro)
        print("Se crearon los archivos satisfactoriamente")
        origen.close()
        armenia.close()
        italia.close()
        espania.close()

#PROGRAMA PRINCIPAL:
def main():
    lectura()

main()