# Intercalar los elementos de una lista entre los elementos de otra.
# La intercalación deberá realizarse exclusivamente mediante la técnica
# de rebanadas y no se creará una lista nueva sino que se modificará la
# primera. Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7],
# lista1 deberá quedar como [8, 5, 1, 9, 3, 7].
import random

def Intercalar(lista1, lista2):
    largo = len(lista2)
    for i in range(1,largo*2,2):
        lista1[i:i] = [lista2[i//2]]
        
lista1 = [random.randint(1,50) for i in range(random.randint(5,10))]
lista2 = [random.randint(1,50) for i in range(random.randint(5,10))]
print(lista1)
print(lista2)
Intercalar(lista1, lista2)
print(lista1)    
    
    
def main():
    lista1 = [random.randint(1,50) for i in range(random.randint(5,10))]
    lista2 = [random.randint(1,50) for i in range(random.randint(5,10))]
    print(lista1)
    print(lista2)
    Intercalar(lista1, lista2)
    print(lista1)  
        

main()
