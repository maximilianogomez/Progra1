#Sin usar Try-Except
def esFloat(string):
    valido = True
    if string[0] == "-":
        string = string[1:]
    if string.count(".") > 1:
        valido = False
    else:
        string = string.replace(".","")
        if not string.isdigit():
            valido = False
    
    return valido

strFloat = input("Ingrese un numero real: ")
while not esFloat(strFloat):
    print("No es un float valido")
    strFloat = input("Ingrese un numero real: ")

numero = float(strFloat)
print(numero)

#Usando Try-Except
valido = False
while not valido:
    try:
        numero = float(input("Ingrese un numero real: "))
    except:
        print("No es un float valido")
    else:
        valido = True
print(numero)

