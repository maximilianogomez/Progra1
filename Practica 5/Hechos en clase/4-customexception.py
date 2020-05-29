class LoginError(Exception):
    pass

def login(usuario, passwd):
    """Recibe un nombre de usuario y una contraseña,
    devuelve verdadero si la combinacion es correcta.
    Sino genera una excepcion LoginError
    """
    pwdUsr = buscarPwdUsr(usuario)
    if pwdUsr == None:
        raise LoginError("El usuario no existe")
    elif pwdUsr != passwd:
        raise LoginError("La contraseña es incorrecta")
    
    return True

def buscarPwdUsr(usr):
    usuarios = ["fer", "vero", "eli", "fede", "rama"]
    passwds = ["1234", "pa$$w0rd", "12345679", "", "rama"]
    if usr not in usuarios:
        pwd = None
    else:
        pwd = passwds[usuarios.index(usr)]
    
    return pwd
    
def main():
    usr = input("Ingrese nombre de usuario: ")
    pwd = input("Ingrese su contraseña: ")
    try:
        if login(usr, pwd):
            print("Se autentico correctamente")
    except LoginError as msg:
        print(msg)
        
if __name__ == "__main__":
    main()