class Mensaje():

    def __init__(self,contenido):
        
        self.Contenido=contenido
        self.Enviados=[]
        self.Recibidos=[]
        self.Abiertos=[]
        self.Abierto=False
    
    #Añade a la lista enviados el id de usuario
    def añadirEnviado(self,id_Us):
        self.Enviados.append(id_Us)
    
    #Añade a la lista Recibidos el id de usuario
    def añadirRecibido(self,id_Us):
        self.Recibidos.append(id_Us)
    #Devuelve la lista de eviados que contiene el identificador de mensaje y el id de todos los usuarios a los que se ha enviado
    def mostrarEnviados(self):
        return self.Enviados
    #Devuelve la lista de Recibidos que contiene el identificador de mensaje y el id de todos los usuarios a los que se ha enviado
    def mostrarRecibidos(self):
        return self.Recibidos