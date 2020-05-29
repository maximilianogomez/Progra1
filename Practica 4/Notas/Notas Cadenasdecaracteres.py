#Cadena de caracteres:

#nota: se pueden crear cadenas vacias, es decir se pueden crear con 0 o más caracteres.

#se puede usar comillas dobles o simples. ex :

frase = 'Dijo "que hermoso día" pero se ' \
        'quedo en casa estudiando'

print(frase)

#la barra invertida se usa para distribuir una cadena extensa

#las cadenas de caracterese se pueden concatenar con el + . Las dos cosas a concatenar deben ser del mismo tipo o sea cadenas o numeros.

#Replicación:

risa = "ja"
carcajada = risa * 5
print(carcajada)

#se pueden comparar, python es case sensitive.

#secuencias de escape: \n (new line) \t (tab), con un r antes de las comillas podes obviar estas secuencias.

#se pueden usar subindices. Las cadenas son inmutables y no se pueden modificar.

#se pueden usar rebanadas.
cad = "Martes"
print(cad[1:5])

#se puede usar len(cadena). Se puede usar in y not in.

#Se puede usar un min y max. Las letras mayusculas son menores, las mas grandes son las minusculas. Se da el mayor valor de acuerdo al codigo ascii

#se puede usar count e index.
cad = "programar"

print(cad.count("a"))          #me cuenta la cantidad de veces que aparece esa letra

print(cad.index("rama"))       # me tira donde aparece por primera vez esa secuencia

#metodo join:

cad = "12345"           # <sep>.join(<secuencia>)
cad = ",".join(cad)       #devuelve una cadena con el separador entre cada caracter
print(cad)

#metodo split:
#divide una cadena en una lista, buscando sep como separador.
# <cadena>.split(<sep>)
cad = "Programar me encanta"
lista = cad.split(' ')           #por defecto separa por espacio
print(lista)

#metodo replacE:
#Reemplaza una cadena por otra hasta un máximo.
#Si se omite max reemplaza Todas las apariciones.

#<cadena>.replace(<viejo>,<nuevo>,<max>)

#invertir por rebanadas:

cad = "Programar me encanta"

cad = cad[::-1]
print(cad)

# <cadena>.isdigit() #devuelve true si todos los caracteres de la cadena son digitos numericos

# <cadena>.isalpha() #devuelve true si todos los caracteres son alfabeticos

#<cadena>.isalnum() #devuelve true si son todos alfabeticos o numericos. Ningun caracter especial como # por ejemplo

#<cadena>.isupper() # devuelve true si todos los caracteres están en mayusculas. Ignora los caracteres no alfabéticos.

#<cadena>.islower() #devuelve true si todos los caracteres estan en minusculas. Ignora los caracteres no alfabéticos.

#<cadena>.upper() #convierte todos los caracteres de una cadena a mayuscula. Se crea una nueva cadena.

#<cadena>.lower() #devuelve una cadena convertida a minúsculas. Se crea una nueva cadena.

#<cadena>.capitalize() #devuelve una cadena convertida a mayúsculas solo el primer caracter de la primer palabra y el resto en minúsculas

#<cadena>.tittle() #devuelve una cadena convertida a mayúsculas solo el primer caracter de cada palabra y el resto en minúsculas

#<cadena>.center(<ancho>,[relleno]) #devuelve una cadena en el ancho especificado, el resto de la cadena se rellena con espacios o con el caracter relleno

cad1 = "Hola"
cad2 = cad1.center(10, '-')
print(cad2)

#<cadena>.ljust(<ancho>,[relleno]) #alineada a la izquierda

#<cadena>.rjust(<ancho>,[relleno]) #alineada a la derecha

#<cadena>.zfill(<ancho>) #devuelve una cadena alineada a la derecha en el ancho especificado. El comienzo de la cadena se rellena con ceros. Es util en contabilidad

n = 3
cad = str(3).zfill(5)
print(cad)

#<cadena>.lstrip(<str>) #devuelve una cadena sin los caracteres indicados en str al inicio de la cadena

cad = "---Hola-Mundo---"
cad = cad.lstrip("-")
print(cad)

#<cadena>.rstrip(<str>) #devuelve una cadena sin los caracteres indicados en str al final de la cadena

#<cadena>.strip(<str>) #devuelve una cadena sin los caracteres indicados en str al inciio y al final de la cadena

#metodo find.
#<cadena>.find(<str>,[[inicio],[fin]]) #Devuelve la posicion donde se encuentra str en la cadena. Si no lo encuentra devuelve -1(index devuelve error)
#se puede indicar los subindices desde y hasta a buscar.

cad = "---Hola-Mundo---"
pos = cad.find("Mundo")
print(f"La posicion donde esta Mundo es: {pos} en {cad}")       #devuelve 8

#<cadena>.rfind(<str>,[[inicio],[fin]])  #la diferencia es que busca desde la derecha buscando la ultima aparición si lo que busco se repite, find busca la primera aparición

#formato f-strings
# f"cadena con formato {variable}" #se define una cadena y adentro se sustituye las variables

#f"cadena con formato {variable:cantidad}" #la cantidad es para indicarle cuantos lugares en pantalla tiene que ocupar esa variable

#f"cadena con formato {variable:cantidad.2f} #dos de los espacios que quiero que ocupe serán los 2 decimales (.2f)

#para mostrar la variable o funcion aritmetica encierro lo que quiero mostrar con {{valor}} o {{suma}}

valor = 10
print(f" {{valor}} tiene el valor {valor}")

#se puede usar tambien para cadenas de multiples lineas.

valor1 = 25
valor2 = 850
suma = valor1+valor2
cadena = f"""
{valor1:5}
{valor2:5}
-----
{suma:5}
"""
print(cadena)

#metodo format:(ya casi ni se usa)
num1 = 4
num2 = 5
suma = num1 + num2
print("La suma de {} y {} es {}".format(num1,num2, suma))

#sin f string. Convierto todo a string y concateno:
num1 = 4
num2 = 5
suma = num1 + num2
print("La suma de " +str(num1)+ " y " +str(num2)+ " es " +str(suma))
