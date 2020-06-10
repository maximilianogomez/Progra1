#Notas tuplas
#tuplas: sus elementos son inmutables
#        se arman con () y , . Los () son opc
        
dias = () # tupla vacia

dias2 = ("Lunes",) #para crear una tupla con elem se debe poner una coma

print(dias)
print(dias2)

#se puede usar el operador: *

binario = (0,1)*3
print(binario)

#se puede hacer tupla de tuplas

primavera = (21, "septiembre")

invierno = (21, "junio")

estaciones = (primavera, invierno)
print(estaciones)

#operador +
fecha = ()
fecha = fecha + (25,)
fecha += ("Enero",)
fecha += (2009,)
print(fecha)

alumno = "Jose",
alumno = alumno + (fecha,)
print(alumno)
print(alumno[0])
print(alumno[1])
print(alumno[1][0])
print(alumno[1][1])
print(alumno[1][2])

#nota si hago alumno = alumno + fecha me desempaqueta la fecha
print("empaquetado")
alumno = ()
alumno = "Jose",
alumno = alumno + (fecha)
print(alumno)

#se puede iterar con un ciclo
semana = ("Lunes","Martes","Miercoles","Jueves","Viernes")

for dia in semana:
    print(dia)
    
#admite rebanadas 
findelargo = semana[len(semana)-1:] + ("Sabado", "Domingo")
print(findelargo)

#Funciones: len() , max (), min(), sum()
#operador : * + in
#metodos : index(), count()

#Empaquetado: se añade muchos valores a una variable
print("Ejemplo 2 de empaquetado: ")
dia = 22
mes = 10
año = 2019
fecha = (dia,mes, año)

#Desempaquetado: a una tupla se le añade una serie de valores simples
fecha = (25,'Enero',2009)
dia,mes,año = fecha

#