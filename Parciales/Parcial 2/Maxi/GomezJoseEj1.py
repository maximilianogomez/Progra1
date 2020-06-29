'''
Seguimos con contraseñas! En algunos sitios no se permite repetir la contraseña y tampoco tener más de n caracteres iguales,

Se solicita un programa para simular “cambiar una contraseña”.

Como regla general: Las contraseñas no pueden contener espacios y debe tener al menos 8 caracteres,

de los cuales al menos dos deben ser números y al menos un símbolo.

Ingresar por teclado  contraseña actual y contraseña nueva. Ambas deben cumplir la regla general y además

Se debe aceptar la nueva contraseña si ésta tiene el 80% diferente a la contraseña actual.

Permitir simular cambios de contraseña hasta que se ingrese una contraseña vacía en la actual.
'''

#FUNCIONES:
def validacion(cad):
    '''valida que mi contraseña sea correcta'''
    cad = cad.lower()
    val = True
    #espacios
    lst = cad.split(" ")
    if len(lst) > 1:
        #si tuviera mas de 1 elemento la lista significaria que hay algun espacio de por medio
        val = False
    cad = " ".join(lst)
    #numero de caracteres
    if len(cad) < 8:
        val = False
    dig = 0
    simb = 0
    for car in cad:
        if car.isdigit():
            dig += 1
        else:
            if not car.isalnum():
                simb += 1
    #digitos
    if dig < 2:
        val = False
    #simbolos
    if simb < 1:
        val = False
    return val

def similitud(cad1,cad2):
    '''
    Recibe dos cadenas
    Devuelve un error si es que lo hay, en caso contrario no devuelve nada
    La función convierte en conjunto a las cadenas y las interseca para ver la cantidad de letras en común si la cantidad de letras en común es mayor o igual al 80% se levanta error
    '''
    #Asumo que hago la comparación con la contraseña actual, es decir la nueva contraseña debe ser 80% diferente
    conj1 = set(cad1)
    conj2 = set(cad2)
    cien_porc = len(conj1)
    ochenta_porc = (80*len(conj1)/100)
    if len(conj1 & conj2) >= ochenta_porc:
        raise ValueError("La nueva contraseña se parece en más de un 80% con la actual: ")
    
#PROGRAMA PRINCIPAL:
def main():
    while True:
        try:
            contra = input("Ingrese la contraseña actual(vacia para terminar): ")
            if contra == "":
                break
            assert validacion(contra), "Su contraseña actual no cumple alguno de los requisitos generales"
            print()
            nueva_contra = input("Ingrese la nueva contraseña : ")
            assert validacion(nueva_contra), "Su contraseña nueva no cumple alguno de los requisitos generales"
            similitud(contra,nueva_contra)
            print()
            print("Ambas contraseñas son validas")
            print()
        except AssertionError as error:
            print(error)
        except ValueError as error2:
            print(error2)
    
if __name__ == "__main__":
    main()