# Escribir un programa que permita ingresar una cadena de caracteres y coloque en
# mayúscula la primera letra posterior a un espacio, eliminando todos los espacios
# que contenga. Imprimir por pantalla la cadena obtenida.
# Ejemplo:
# Cadena original:
# Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos.
# Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
# Cadena final:
# PlateroEsPequeño,Peludo,Suave;TanBlandoPorFuera,QueSeDiríaTodoDeAlgodón,QueNoLlevaHuesos.Sólo
# LosEspejosDeAzabacheDeSusOjosSonDurosCualDosEscarabajosDeCristalNegro.

#Funciones:
def mayusc_espacio(cad):
    cad = cad.title().replace(" ","")
    return cad

#Programa Principal:
def main():
    cadena = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos.Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro"
    cadena = mayusc_espacio(cadena)
    print(cadena)
    
main()