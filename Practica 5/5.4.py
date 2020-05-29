# Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
# las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
# un programa para imprimir los números enteros entre 1 y 100000, y que solicite
# confirmación al usuario antes de detenerse cuando se presione Ctrl-C.


#PROGRAMA PRINCIPAL:
def main():
    for i in range(1,100001):
        try:
            print(i)
        except KeyboardInterrupt:
            resp = input("Desea finalizar: (s/n) ")
            if resp.lower() == "s" or resp.lower() == "si":
                print("Fin")
                break
    
main()