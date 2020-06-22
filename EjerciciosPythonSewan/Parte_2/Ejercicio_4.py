"""Simulador de notificaciones
El objetivo de este ejercicio es desarrollar un simulador de entrega de notificaciones a usuarios. 
El simulador permitirá definir un entorno con varios usuarios a los que se le pueden entregar notificaciones 
y cada una de estas notificaciones tendrá una serie de estadísticas relacionadadas con los mensajes enviados, 
los recibidos y los abiertos."""

import uuid#Importa clase para generar id de usuario
import random #Importamos clase random para numero aleatorio de simulador de error de entrega

Usuarios={}#Almacena registro de usuarios en diccionario key=uid  contenido=objeto usuario
Mensajes=[]#Almacena los mensajes creados en lista
Enviados=[]#Almacena uid de los usuarios a los que se ha enviado un mensaje
Recibidos=[]#Almacena uid de los usuarios que han recibido un mensaje
Abiertos=[]#Almacena uid de los usuarios que han abierto el mensaje

#-----CLASE USUARIO--------------
class Usuario():

    def __init__(self,nombre,cod_Usuario):
        self.Nombre=nombre
        self.cod_U=cod_Usuario
        self.BandejaEntrada=[]

    #---FUNCIONES
    def añadir_A_BandejaEntrada(self,id_Men):
        #Simulador de errores de entrega
        numero=random.randint(1,100)#Genera numero aleatorio
        if numero!=5:#Si el numero aleatorio es 5 no realiza la insercion a recibidos
            self.BandejaEntrada.append(id_Men)#Añade a bandeja de entrada de usuario que hace la llamada
            id_Men.Recibidos.append(self.cod_U)#Añade a lista recibidos
    
    def mostrarBandejaEntrada(self):
        print(self.BandejaEntrada)

    def leerMens(self,mensaje,usuario):
        self.BandejaEntrada[mensaje].Abierto=True#Modifica el valor del atrubuto leido a true
        self.BandejaEntrada[mensaje].Abiertos.append(usuario.cod_U)#Añade id Usuario a lista de mensajes Abiertos

#---------CLASE MENSAJE
class Mensaje():

    def __init__(self,contenido):
        
        self.Contenido=contenido
        self.Enviados=[]
        self.Recibidos=[]
        self.Abiertos=[]
        self.Abierto=False
    
    #----FUNCIONES

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


#----SERVICIO DE NOTIFICACIÓN

#Crea usuarios y añade nombre e id
def crearUsuario():
    for i in range(1,1001):
        nombre="Usuario"+str(i)#Genera nombre de usuario
        id_U=str(uuid.uuid1())#Genera Id de usuario
        Usuarios[id_U]=Usuario(nombre,id_U)#Almacena en diccionario usuarios key=id:U contenido objeto usuario

#Envia mensajes por difusión
def enviarMensaje(contenido):
    
    
    cod_Mensaje=Mensaje(contenido)#Creamos objeto mensaje
    Mensajes.append(cod_Mensaje)#Añade a lista mensajes
    
    for usuario in Usuarios:
        cod_Mensaje.añadirEnviado(usuario)#Añadimos a lista de Enviados
        Usuarios[usuario].añadir_A_BandejaEntrada(cod_Mensaje)#Añadimos a diccionario BandejaEntrada de cada usuario de la lista
        
#Lee mensaje por difusion
def leerMensaje(nombre,pos_mensaje):
    for usuario in Usuarios:
        if Usuarios[usuario].Nombre==nombre:
            Usuarios[usuario].leerMens(pos_mensaje,Usuarios[usuario])#LLama funcion usuario leer_Men que cambia el atrubuto leido a true y añade usuario a lista de apertura de este mensaje
            mensaje="Id_Mensaje: ",pos_mensaje," Contenido: ",Usuarios[usuario].BandejaEntrada[pos_mensaje].Contenido," Abierto: ",Usuarios[usuario].BandejaEntrada[pos_mensaje].Abierto 
            estadistica="Enviados: ",len(Usuarios[usuario].BandejaEntrada[pos_mensaje].Enviados)," Recibidos: ",len(Usuarios[usuario].BandejaEntrada[pos_mensaje].Recibidos)," Abiertos: ",len(Usuarios[usuario].BandejaEntrada[pos_mensaje].Abiertos)
            enviados="Enviados: ",Usuarios[usuario].BandejaEntrada[pos_mensaje].Enviados
            recibidos="Recibidos: ",Usuarios[usuario].BandejaEntrada[pos_mensaje].Recibidos
            abiertos="Abiertos: ",Usuarios[usuario].BandejaEntrada[pos_mensaje].Abiertos
            print("Info Mensaje: ",mensaje)#Imprime datos del mensaje Id,Contenido,Abierto
            print("Estadisticas: ",estadistica)
            print("-------------------------------------------------ENVIADOS----------------------------------------------------------------------")
            print(enviados)#Id usuario al que se ha enviado el mensaje
            print("-------------------------------------------------RECIBIDOS----------------------------------------------------------------------")
            print(recibidos)#Id usuario que han recivido el mensaje
            print("-------------------------------------------------ABIERTOS----------------------------------------------------------------------")
            print(abiertos)#Id usuario que lo han abierto



crearUsuario()

enviarMensaje("Hola")

leerMensaje("Usuario1",0)



