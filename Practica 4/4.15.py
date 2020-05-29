# Muchas aplicaciones financieras requieren que los números sean expresados también
# en letras. Por ejemplo, el número 2153 puede escribirse como "dos mil ciento
# cincuenta y tres". Escribir un programa que utilice una función para convertir un
# número entero entre 0 y 1 billón (1.000.000.000.000) a letras. ¿En qué cambiaría
# la función si también aceptara números negativos? ¿Y números con decimales?

#FUNCIONES:
def validarNumero(mensaje):
    nro = int(input(mensaje))
    while nro < 0 and nro > 1000000000000:
        print("Numero invalido")
        nro = int(input(mensaje))
    return nro

def convertir_letras(nro):
    valores = [1000000000000 ,9000000,8000000,7000000,6000000,5000000,4000000,3000000,2000000,1000000,900000,800000,700000,600000,500000,400000,300000,200000,100000, 90000,80000,70000,60000,50000,40000,30000,20000,10000,9000,8000,7000,6000,5000,4000,3000,2000,1000,900,800,700,600,500,400,300,200,100,90,80,70,60,50,40,30,20,10,9,8,7,6,5,4,3,2,1,0]
    palabras = ["un billón", "nueve millones","ocho millones","siete millones", "seis millones", "cinco millones", "cuatro millones","tres millones", "dos millones","un millon","novecientos mil", "ochocientos mil", "setecientos mil", "seicientos mil", "quinientos mil","cuatrocientos mil", "trecientos mil", "docientos mil", "cien mil","noventa mil", "ochenta mil", "setenta mil", "sesenta mil", "cincuenta mil", "cuarenta mil","treinta mil", "veinte mil", "diez mil", "nueve mil", "ocho mil", "siete mil", "seis mil", "cinco mil", "cuatro mil", "tres mil", "dos mil", "mil", "novesientos", "ochocientos", "setecientos", "seiscientos","quinientos","cuatrocientos","trescientos","doscientos","cien","noventa","ochenta","setenta","sesenta","cincuenta","cuarenta","treinta","veinte","diez","nueve","ocho","siete","seis","cinco","cuatro","tres","dos","uno","cero"]
    pal = ""
    i = 0
    while nro > 0:
        cifra = nro // valores[i]
        x = valores.index(cifra)
        if cifra!= 0:
            nro = nro - (valores[i]*cifra)
            if nro == 0:
                pal = pal + " y "+palabras[i]
            else:
                pal = pal + " "+palabras[i]
        i += 1
        x = 0
    lstPalabras = pal.split()
    for palabra in lstPalabras:
        while lstPalabras.count(palabra) > 1:
            lstPalabras.remove(palabra)
    numero_en_pal = " ".join(lstPalabras)
    return numero_en_pal

#PROGRAMA PRINCIPAL:
def main():
    nro = validarNumero("Ingrese un numero entre 0 y 1 billón: ")
    en_Letras = convertir_letras(nro)
    print(f"La palabra en letras es: {en_Letras}")
    
main()