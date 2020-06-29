# Leer las frases del archivo frases.txt y crear un nuevo archivo con las palabras de cada registro sin repetirlas, ordenadas
# según su longitud. No considerar caracteres no alfabéticos para la longitud de la palabra. Al finalizar mostrar por pantalla
# un listado de las palabras en orden alfabético y cuantas veces aparece en todo el archivo.
# Recorda no cargar todo el archivo en memoria para resolver.

# FUNCIONES
def limpiarRegistro(registro):
    nuevo = ""
    for letra in registro:
        if letra.isalnum():
            nuevo += letra
        elif letra == " ":
            nuevo += letra
    return nuevo.lower()

def limpiarRegistro2(registro):
    nuevo = ""
    for letra in registro:
        if letra.isalpha():
            nuevo += letra
        elif letra == " ":
            nuevo += letra
    return nuevo.lower()

def ordenarFrase(registro):
    registro = limpiarRegistro(registro)
    lista = registro.split()
    sinRep = list(set(lista))
    sinRep.sort(key=lambda x:len(x))
    regOrdenado = " ".join(sinRep)
    return regOrdenado
    
def main():
    dic = {}
    try:
        archivo = open("frases.txt")
        arch = open("frasesOrdenadas.txt","w")
    except IOError:
        print("Error al crear/abrir el archivo")
    else:
        while True:
            registro = archivo.readline()
            if registro == "":
                break
            registro = registro.rstrip()
            listado = limpiarRegistro2(registro)
            listado = listado.split()
            for palabra in listado:
                if palabra not in dic:
                    dic[palabra] = 1
                else:
                    dic[palabra] += 1
                
            regisOrdenado = ordenarFrase(registro)
            arch.write(regisOrdenado+"\n")
    finally:
        try:
            print("Se modificó el archivo")
            archivo.close()
            arch.close()
        except:
            pass
    
    palabras = list(dic)
    palabras.sort()
    for palabra in palabras:
        if dic[palabra]>1:
            print(f"{palabra:15s} aparece {dic[palabra]:3d} veces")
        else:
            print(f"{palabra:15s} aparece {dic[palabra]:3d} vez")

main()           