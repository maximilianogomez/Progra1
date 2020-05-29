# Desarrollar una función que devuelva una cadena de caracteres con el nombre del
# mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
# obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
# Devolver una cadena vacía si el número de mes es inválido. La detección de meses
# inválidos deberá realizarse a través de excepciones.

def meses(num):
    meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    try:
        mes = meses[num-1]
        
    except (IndexError,ValueError):
        mes = []
    return mes

def main():
    nro = int(input("Ingrese el numero de un mes: "))
    print(meses(nro))
    
main()
            