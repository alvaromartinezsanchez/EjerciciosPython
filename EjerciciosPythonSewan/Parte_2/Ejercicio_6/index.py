import uuid#Importa clase para generar id de usuario
import Mensaje
import Usuario
Usuarios={}#Almacena registro de usuarios en diccionario key=uid  contenido=objeto usuario
Mensajes=[]#Almacena los mensajes creados en lista
Enviados=[]#Almacena uid de los usuarios a los que se ha enviado un mensaje
Recibidos=[]#Almacena uid de los usuarios que han recibido un mensaje
Abiertos=[]#Almacena uid de los usuarios que han abierto el mensaje

#Crea usuarios y añade nombre e id
def crearUsuario():
    for i in range(1,1001):
        nombre="Usuario"+str(i)#Genera nombre de usuario
        id_U=str(uuid.uuid1())#Genera Id de usuario
        Usuarios[id_U]=Usuario.Usuario(nombre,id_U)#Almacena en diccionario usuarios key=id:U contenido objeto usuario


#ENVIO DIFUSION

def enviarMensaje(contenido):
    cod_Mensaje=Mensaje.Mensaje(contenido)#Creamos objeto mensaje
    Mensajes.append(cod_Mensaje)#Añade a lista mensajes
    
    for usuario in Usuarios:
        cod_Mensaje.añadirEnviado(usuario)#Añadimos a lista de Enviados
        Usuarios[usuario].añadir_A_BandejaEntrada(cod_Mensaje)#Añadimos a diccionario BandejaEntrada de cada usuario de la lista


#ENVIO UNICO

def enviarMensajeUnico(contenidoMensaje,nombreUsuario):
    cod_Mensaje=Mensaje.Mensaje(contenidoMensaje)#Creamos objeto mensaje
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