# La función de Ackermann A(m,n) se define de la siguiente forma:
# n+1 si m = 0
# A(m-1,1) si n = 0
# A(m-1,A(m,n-1)) de otro modo
# Imprimir un cuadro con los valores que adopta la función para valores de m entre
# 0 y 3 y de n entre 0 y 7.

#FUNCIONES:
def acker(m,n):
    if m == 0:
        return n+1
    elif n == 0:
        return acker(m-1,1)
    else:
        return acker(m-1,acker(m,n-1))
        
    
#PROGRAMA PRINCIPAL:
def main():
    try:
        x = int(input("Ingrese un numero: "))
        y = int(input("Ingrese otro numero: "))
        print(acker(x,y))
    except ValueError:
        print("Se esperaba un numero entero")

if __name__ == "__main__":
    main()