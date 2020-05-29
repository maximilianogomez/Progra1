# Escribir un programa para crear una lista por comprensión con los naipes de la baraja
# española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros",
# "2 Oros"... ]. Imprimir la lista por pantalla.

# FUNCIONES
def main():
    lista = [(str(num)+" "+palo) for num in range(1,13) for palo in ("Oros", "Basto","Espada","Copa")]
    print(lista)
    
# PROGRAMA PRINCIPAL
main()