#----USUARIO

class Usuario():

    def __init__(self,nombre,cod_Usuario):
        self.Nombre=nombre
        self.cod_U=cod_Usuario
        self.BandejaEntrada=[]

    def añadir_A_BandejaEntrada(self,id_Men):
        self.BandejaEntrada.append(id_Men)#Añade a bandeja de entrada de usuario que hace la llamada
        id_Men.Recibidos.append(self.cod_U)#Añade a lista recibidos
    
    def mostrarBandejaEntrada(self):
        for i in range(len(self.BandejaEntrada)):
            print("Id: ",i,"Contenido: ",self.BandejaEntrada[i].Contenido," Leido: ",self.BandejaEntrada[i].Abierto)

    def leerMens(self,mensaje,usuario):
        
        self.BandejaEntrada[mensaje].Abierto=True
        self.BandejaEntrada[mensaje].Abiertos.append(usuario.cod_U)
