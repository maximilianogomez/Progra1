# Desarrollar un programa que utilice una función que reciba como parámetro una
# cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
# una tupla con las distintas partes que componen dicha dirección. Ejemplo:
# alguien@uade.edu.ar -> (alguien, uade, edu, ar).

#FUNCIONES:
def mail(cad):
    cad = cad.lower()
    cad = cad.replace("@",".")
    lista = cad.split(".")
    tupla = ()
    for parte in lista:
        tupla += (parte,)
    return tupla

#PROGRAMA PRINCIPAL:
def main():
    correo = input("Introduzca un correo electronico del tipo alguien@uade.edu.ar: ")
    tupla = mail(correo)
    print(tupla)
    
    
main()