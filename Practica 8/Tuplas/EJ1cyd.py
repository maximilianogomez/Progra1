# c. Ingresar un horario desde teclado, verificando que sea correcto.
# d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
# segundo se considerará que el primero corresponde al día anterior. En ningún
# caso la diferencia en horas puede superar las 24 horas.

import datetime

#FUNCIONES:
def validacion(h,m,s):
    tupla = ()
    if h < 0 or h > 23:
        raise ValueError("hour must be in 0..23")
    elif m < 0 or m > 60:
        raise ValueError("minute must be in 0..59")
    elif s < 0 or s > 60:
        raise ValueError("second must be in 0..59")
    else:
        tupla += (h,m,s)
    return tupla

def diferencia_horarios(t1,t2):
    h1, m1 , s1 = t1
    h2, m2, s2 = t2
    while s2 - s1 < 0:
        s2 += 60
        m2 -= 1
    dif_seg = s2 - s1
    while m2 - m1 < 0:
        m2 += 60
        h2 -= 1
    dif_min = m2 - m1
    dif_hora = h2 - h1
    if h1 > h2:
        dif_hora += 24
        if dif_hora > 24:
            raise ValueError("Error, la diferencia horaria es mayor a 24 horas")
    t_dif = (dif_hora,dif_min,dif_seg)
    return t_dif
        

#PROGRAMA PRINCIPAL:
def main():
    try:
        h = int(input("Ingrese una hora(0 a 23): "))
        m = int(input("Ingrese los minutos (0 a 59): "))
        s = int(input("Ingrese los segundos (0 a 59): "))
        t1 = validacion(h,m,s)
        h2 = int(input("Ingrese una hora(0 a 23): "))
        m2 = int(input("Ingrese los minutos (0 a 59): "))
        s2 = int(input("Ingrese los segundos (0 a 59): "))
        t2 = validacion(h2,m2,s2)
        print(t1)
        print(t2)
        t_diferencia = diferencia_horarios(t1,t2)
        print(t_diferencia)

    except ValueError as mensaje:
        print(mensaje)
    
main()