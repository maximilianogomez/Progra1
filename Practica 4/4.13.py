# Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro
# de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que
# los caracteres de la subcadena no necesariamente deben estar en forma consecutiva
# dentro de la cadena, pero sí respetando el orden de los mismos. Ejemplo:
# Cadena:
# Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos.
# Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
# Sub-cadena: UADE
# Cantidad encontrada: 4 (Las coincidencias están resaltadas en la cadena siguiente)
# Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva
# huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.

#Funcion:
def contador(cad,subcadena):
    cad = cad.lower()
    subcadadena = subcadena.lower()
    inicio = 0
    acum = 0
    i = 0
    pos = 0
    x = 0
    while x != -1:
        while i < len(subcadena) and pos!= -1:
            pos = cad.find(subcadena[i],inicio+1)
            inicio = pos
            i += 1
        if i == len(subcadena):
            acum += 1
        i = 0
        if pos == -1:
            x = -1
    return acum

#Programa Principal:
def main():
    cadena = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos.Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro."
    subcadena = input("Ingrese la subcadena a buscar: ")
    cdad_encontrada = contador(cadena,subcadena)
    print(f"La cantidad de veces que se encontró la subcadena en la cadena fue: {cdad_encontrada}")

main()