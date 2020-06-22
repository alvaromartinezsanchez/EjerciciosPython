"""Soporte para envíos individualizados en simulador de notificaciones
En el escenario planteado anteriormente sólo se da soporte para simular envíos en broadcast. 
Añade una nueva clase de mensaje y modifica el servidor para permitir el envío de mensajes individualizados."""

import uuid#Importa clase para generar id de usuario
import random #Importamos clase random para numero aleatorio de simulador de error de entrega

Usuarios={}#Almacena registro de usuarios en diccionario key=uid  contenido=objeto usuario
Mensajes=[]#Almacena los mensajes creados en lista
Enviados=[]#Almacena uid de los usuarios a los que se ha enviado un mensaje
Recibidos=[]#Almacena uid de los usuarios que han recibido un mensaje
Abiertos=[]#Almacena uid de los usuarios que han abierto el mensaje

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

#----MENSAJE

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


#---SIMULADOR DE NOTIFICACIONES

#Crea usuarios y añade nombre e id
def crearUsuario():
    for i in range(1,1001):
        nombre="Usuario"+str(i)#Genera nombre de usuario
        id_U=str(uuid.uuid1())#Genera Id de usuario
        Usuarios[id_U]=Usuario(nombre,id_U)#Almacena en diccionario usuarios key=id:U contenido objeto usuario


#ENVIO DIFUSION

def enviarMensaje(contenido):
    cod_Mensaje=Mensaje(contenido)#Creamos objeto mensaje
    Mensajes.append(cod_Mensaje)#Añade a lista mensajes
    
    for usuario in Usuarios:
        cod_Mensaje.añadirEnviado(usuario)#Añadimos a lista de Enviados
        Usuarios[usuario].añadir_A_BandejaEntrada(cod_Mensaje)#Añadimos a diccionario BandejaEntrada de cada usuario de la lista


#ENVIO UNICO

def enviarMensajeUnico(contenidoMensaje,nombreUsuario):
    cod_Mensaje=Mensaje(contenidoMensaje)#Creamos objeto mensaje
    Mensajes.append(cod_Mensaje)#Añade a lista mensajes
    for usuario in Usuarios:
        if Usuarios[usuario].Nombre==nombreUsuario:
            cod_Mensaje.añadirEnviado(usuario)#Añadimos a lista de Enviados
            Usuarios[usuario].añadir_A_BandejaEntrada(cod_Mensaje)#Añadimos a lista BandejaEntrada del usuario


#LEER MENSAJE DIFUSION

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


#LEER MENSAJE UNICO

def leerMensajeUnico(nombreUsuario,pos_mensaje):
    print("Lectura de mensaje con id ",pos_mensaje," para el usuario ",nombreUsuario)
    for usuario in Usuarios:
        if Usuarios[usuario].Nombre==nombreUsuario:
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


#MUESTRA BANDEJA ENTRADA USUARIO

def mostrarBandejaEntradaUsuario(nombre_Usuario):
    for usuario in Usuarios:
        if Usuarios[usuario].Nombre==nombre_Usuario:
            print("Bandeja de entrada de usuario:",nombre_Usuario)
            Usuarios[usuario].mostrarBandejaEntrada()

#LLAMADAS A FUNCIONES

crearUsuario()

#enviarMensaje("Hola")

enviarMensajeUnico("Hola, Esto es un mensaje unico","Usuario5")

mostrarBandejaEntradaUsuario("Usuario5")

leerMensajeUnico("Usuario5",0)