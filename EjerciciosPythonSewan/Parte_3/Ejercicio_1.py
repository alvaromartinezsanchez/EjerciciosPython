"""El objetivo de este ejercicio es desarrollar un decorador que permita medir el tiempo que 
tarda en ejecutarse los métodos de una clase y que el resultado se pueda mostrar o por pantalla 
o pueda ser guardado en un fichero. """

from time import time#Importa modulo time de la clase time
from io import *

def decorador_TiempoEjecucion(funcion_Test):
    """
    Ejecuta la funcion test y calcula el tiempo de ejecucion
    Print the result to the standard output.
    """
    def wrapper(self=None, *args, **kwargs):
        # Iniciamos Cuenta.
        start_time = time()
        # Ejecutamos la funcion_Test
        ret = funcion_Test(self, *args, **kwargs)
        # Calcula tiempo transcurrido => Tiempo actual menos tiempo de inicio.
        tiempo_Ejecucion = time() - start_time
        print("¿Que deseas hacer con el resultado?")
        opcion=input("Pulsa 1 para imprimir en consola y 2 para guardar en archivo")
        if opcion=="1":
            print("Tiempo de ejecucion: %0.10f seconds." % tiempo_Ejecucion)
        elif opcion=="2":
            archivo=open("archivo.txt", "w")
            contenido="Tiempo de Ejecucion: "+str(tiempo_Ejecucion)
            #Añadimos contenido 
            archivo.write(contenido)
            archivo.close()
        return ret
    
    return wrapper

class MyClase():

    @decorador_TiempoEjecucion
    def test(self):
        for i in range(10000):
            "Hola, mundo!".replace("Hola", "Adios")

clase=MyClase()
clase.test()