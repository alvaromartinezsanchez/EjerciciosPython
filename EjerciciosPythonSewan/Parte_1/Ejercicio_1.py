nombreUsuario=input("Introduce el nombre de usuario: ")

if (len(nombreUsuario)<=12 and len(nombreUsuario)>=6 and str.isalnum(nombreUsuario)):
    print("El nombre de Usuario ",nombreUsuario," es correcto")
else:
    print("El nombre de Usuario ",nombreUsuario," NO es correcto")
    print("El nombre de Usuario debe contener entre 6 y 12 caracteres alfanumericos")
