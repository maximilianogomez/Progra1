def nombreMes(nroMes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    try:
        if nroMes < 1:
            raise ValueError
        mes = meses[nroMes - 1]
    except (IndexError,ValueError):
        mes = ""
    
    return mes

def main():
    nroMes = int(input("Ingrese el numero del mes: "))
    print(f"Mes: {nombreMes(nroMes)}")
    
main()