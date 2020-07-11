#Notas conjuntos
#no tienen orden y ningun elemento esta duplicado
#no tienen orden interno, no es una secuencia. Pueden contener elementos de distinto tipo

#para crearlo se utiliza un {}

paises = {"Argentina","Brasil","Chile","Uruguay"}
print(paises)

#funciones que admite: len(),max(),min(),sum()
#operadores : in, not in, matematicos
#metodos : add,remove, discard, clear, issubset

# intersecciones: &
A = {1,2,3,4,5,6,7}
B = {2,4,6,8,10}
C = A & B
print(C)

#union: |
A = {1,2,3,4,5,6,7}
B = {2,4,6,8,10}
C = A | B
print(C)

#Resta: tener cuidado que se resta: - 
A = {1,2,3,4,5,6,7}
B = {2,4,6,8,10}
C = A - B
print(C)

#Diferencia SImetrica : ^ (es la union de ambos conjuntos y despues se le resta el de la derecha)
A = {1,2,3,4,5,6,7}
B = {2,4,6,8,10}
C = A ^ B
print(C)

#METODOS:
#add(<elemento>)
paises = {"Argentina","Brasil","Chile","Uruguay"}
paises.add("Paraguay")
print(paises)

#remove(<elemento>), elimina el elemento del conjunto. Provoca (KeyError) si no se encuentra en el conjunto
paises.remove("Brasil")
print(paises)

#discard(<elemento>) elimina el elemento. No provoca error si no se encuentra en el conjunto
#clear(), elimina todos los elementos del conjunto

#issubset(<conjunto>)
#Retorna True si <conjunto> esta incluido en el conjunto
conjunto = {2,3,4}
if conjunto.issubset({1,2,3,4,5,6}):
    print("Incluido")
#Convertir a tipo de datos:
set(<iterable>) : convertir a conjunto
list(<iterable>) : convertir a lista
tuple(<iterable>) : convertir a tupla

