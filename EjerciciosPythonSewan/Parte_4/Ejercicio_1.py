"""El objetivo de este ejercicio es crear un script de Python que tome como argumento 
una ruta y que muestre por pantalla cual es el fichero más grande de esa ruta."""

import sys
import os
from pathlib import Path

# DIRECCION---> /home/alvaro/Desktop/Python/Modulos

ruta=input("Introduce la ruta del directorio a examinar")
sys.path.append(ruta)
path=sys.path[len(sys.path)-1]#Obtiene posicion de la "ruta" situada en ultima posicion



def listarArchivosdeCarpeta(path):
    return [obj.name for obj in Path(path).iterdir() if obj.is_file()]

lista_Archivos=listarArchivosdeCarpeta(path)
arvhivo_Mayor=""
tamaño_Mayor=0
for archivo in lista_Archivos:
    tamaño_Archivo=os.path.getsize(path+"/"+archivo)
    print("El archivo ",archivo," es un archivo",os.path.isfile(path+"/"+archivo))
    print("Tamaño: ",os.path.getsize(path+"/"+archivo))
    if tamaño_Archivo>tamaño_Mayor:#Obtiene el archivo de mayor tamaño
        tamaño_Mayor=tamaño_Archivo#Tamaño
        arvhivo_Mayor=archivo#Nombre
print("El archivo mayor es ",arvhivo_Mayor," con un tamaño de ",tamaño_Mayor)

