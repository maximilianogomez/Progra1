x = "hola mundo"
type(x)
#como abrir un archivo
#variable = open(file,mode = "r") #open retorna un objeto de tipo archivo

#file va el nombre del archivo o la ruta donde se encuentra poner un r adelante para no comerme las secuencias de escape.
#puedo obviarlas con otra "\"
arch = open("datos.txt")
arch = open("c:\\nuevo\\datos.txt")
arch = open(r"c:\nuevo\datos.txt")

#mode indica el modo de apertura de archivo, por default es el modo lectura de un archivo de texto
#primer caracter:
# w: escritura. Crea el archivo para escribir en blanco
# a: añadir al final información(escribis al final del archivo)
# r: lectura
#segundo caracter:
# t: texto
# b: binario

#si no se abre produce un error del tipo IO Error (input/output error).

#antes de probarlo poner la variable de cierre. #variable.close().
#nosotros no vamos a actualizar archivos, creamos o leemos.
#readlines lee cuantos registros tiene el archivo

print(len(arch.readlines()))

#variable.write(cadena) para escribir en donde guardo el archivo alguna cadena por ejemplo. arch.write(cadena)
# #se debe agregar el salto de linea con un cad = cad + "\n" o en el print

#el for se encarga de ir haciendo una lectura de los registros

#cuando utilizo el while tengo que trbajar con el metodo readline. Ej :
#linea = arch.readline()
#while linea != "":


