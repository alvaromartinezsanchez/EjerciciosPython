""" El objetivo de este ejercicio es crear un script que dada la ruta de un fichero de entrada y uno de 
salida, siendo el fichero de entrada un log de una aplicación web de Python, escriba en el fichero de 
salida un CSV con las siguietes columnas: """

import csv,sys,os

class Metodo():

    def __init__(self,nombreMetodo,ruta,tiempo):
        self.Nombre_Metodo=nombreMetodo
        self.Ruta=ruta
        self.Tiempo=tiempo
        self.SumaTiempos=int(tiempo)
        self.Peticiones=1
        self.TiemposMedia=0

    
    def sumarTiempo(self,time):
        self.SumaTiempos+=int(time)
    
    def sumarPeticion(self):
        self.Peticiones=self.Peticiones+1

    def calcular_Media_Tiempo(self):
        return self.SumaTiempos/self.Peticiones
    
    def mostrarDatos(self):
        print("Metodo",self.Nombre_Metodo," Ruta: ",self.Ruta," Tiempo: ",self.Tiempo," Tiempo Media: ",self.calcular_Media_Tiempo()," Peticiones: ",self.Peticiones)

#---- RUTA DEL ARCHIVO DE ENTRADA SERVER.LOG ----------------------

#   ./Parte_4/server.log

ruta=input("Introduce la ruta del directorio a examinar")#Introducir Ruta a server.log
sys.path.append(ruta)
path_Ruta=sys.path[len(sys.path)-1]#Obtiene posicion de la "ruta" situada en ultima posicion

if os.path.exists(path_Ruta):#Comprueba si existe la ruta

    with open('./Parte_4/server.log', newline='') as csvfile:#Guarda en csvfile la apertura del archivo
        rutas=[]#Almacena las direcciones de ruta, para luego comprovar si se repiten y controlar las peticiones
        lista_Metodos=[]#Almacena los objetos Metodo que se van creando
        spamreader=csv.reader(csvfile,delimiter=' ',quotechar='|')
        for row in spamreader:
            nombreMetodo=row[17]
            ruta=row[18]#Direccion de ruta
            
            if ruta in rutas:#Comprueba si la ruta es nueva o repetida
                for i in lista_Metodos:
                    if i.Ruta==ruta and i.Nombre_Metodo==nombreMetodo:#Si coinciden direccion de ruta y nombre del metodo se suma peticion e incremeta tiempototal y calcula media
                        i.sumarPeticion()
                        i.sumarTiempo(row[24])
                        i.calcular_Media_Tiempo
                    
            else:
                tiempo=row[24]
                rutas.append(ruta)#Añade alista de rutas aparecidas
                lista_Metodos.append(Metodo(nombreMetodo,ruta,tiempo))#Crea objeto metodo y añade a la lista
        
        with open('archivo_Salida.csv', 'w', newline='') as csvArchivo:
            spamwriter = csv.writer(csvArchivo, delimiter=',',dialect='excel', quotechar=',', quoting=csv.QUOTE_MINIMAL)#Crea archivo y especifica formato "excel"
            fieldnames=['Método','Ruta','Tiempo Medio','N. de Peticiones']#Crea lista para cabecera
            writer=csv.DictWriter(csvArchivo,fieldnames=fieldnames)
            writer.writeheader()
            for metodo in lista_Metodos:
                spamwriter.writerow([metodo.Nombre_Metodo,metodo.Ruta,str(metodo.calcular_Media_Tiempo())+" "+"ms",str(metodo.Peticiones)+" "+"pet"])#Accede a los metodos del objeto "Metodo()"