"""Bandeja de entrada
En este ejercicio vamos a crear una bandeja de entrada de mensajes 
enviados a usuarios, así como tres funciones, una para enviar mensajes,
 otra obtener los pendientes de leer y otra para leer un mensaje.

-Cada mensaje tendrá tres campos, origen (nombre del usuarios que lo envió),
 contenido, y si se ha leído o no
-Los usuarios se crean de forma dinámica al enviar un mensaje
-La función para enviar mensajes recibe el nombre del usuario que lo 
envía y el contenido
-La función para leer un mensaje muestra el contenido, quien lo envía 
lo marca como leído.
-La función para obtener el listado de los mensajes pendientes por 
leer para un usuario dado, sólo muestra los que no están leídos, 
un resumen del contenido del mensaje, y un identificador de este. """

bandejaEntrada=[]
bandejaEntradaUsuario=[]
Num_Mensaje=0

def enviarMensaje(origen, contenido):
    global Num_Mensaje
    Mensaje={"Id": Num_Mensaje, "Origen": origen, "Contenido": contenido, "Leido" : False}
    bandejaEntrada.append(Mensaje)
    Num_Mensaje+=1
    return bandejaEntrada

def leerMensaje(id):
    mensaje=""
    for i in range(len(bandejaEntrada)):
        if bandejaEntrada[i]["Id"]==id:
            mensaje+="ID    Origen     Contenido         Leido  \n \n"
            mensaje+= str(bandejaEntrada[i]["Id"])+"     "
            mensaje+= bandejaEntrada[i]["Origen"]+"     "
            mensaje+= bandejaEntrada[i]["Contenido"]+"     "
            bandejaEntrada[i]["Leido"]="True"+"            "
            mensaje+= bandejaEntrada[i]["Leido"]
    
    return mensaje

def verMensajesNoLeidos(usuario):
    Resumen=""
    for i in range(len(bandejaEntrada)):
        if bandejaEntrada[i]["Origen"]==usuario and bandejaEntrada[i]["Leido"]==False:
            Resumen=bandejaEntrada[i]["Contenido"][0:15]
            Mensaje={"Id": bandejaEntrada[i]["Id"],"Origen": bandejaEntrada[i]["Origen"],"Resumen":Resumen }
            bandejaEntradaUsuario.append(Mensaje)
    verTodosLosMensajes(bandejaEntradaUsuario)

def verTodosLosMensajes(bandeja):
    mensaje=iter(bandeja)
    for c in range(len(bandeja)):
        print(next(mensaje))
    print("                                         ")

enviarMensaje("Alvaro","Este es el contenido del mensaje")
enviarMensaje("Manolo","Parece que funciona....")
enviarMensaje("Alvaro","No lo dudaba en ningun momento..!!")
enviarMensaje("Luis","Si eso parece, ahora faltan las demas funciones")
enviarMensaje("Maria","Y a mi queeeeeeeeeeeeeeeeeeeeeee...")
print("----------BANDEJA ENTRADA--TODOS LOS MENSAJES----------\n")
verTodosLosMensajes(bandejaEntrada)
print("--------------LEER MENSAJE- Por Id Mensaje---------------")
print(leerMensaje(1))
print()
print("-------VER MENSAJES NO LEIDOS--Por Nombre Origen--------\n")
verMensajesNoLeidos("Alvaro")