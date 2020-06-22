#---CONFIGURACION LOG MEDIANTE ARCHIVO

from time import time#Importa modulo time de la clase time
import logging
from logging.config import fileConfig

def decorador_TiempoEjecucion(funcion_Test):
    """
    Ejecuta la funcion test y calcula el tiempo de ejecucion
    Print the result to the standard output.
    """
    def wrapper(*args, **kwargs):
        # Iniciamos Cuenta.
        start_time = time()
        # Ejecutamos la funcion_Test
        ret = funcion_Test(*args, **kwargs)
        # Calcula tiempo transcurrido => Tiempo actual menos tiempo de inicio.
        tiempo_Ejecucion = time() - start_time
        logger.debug(tiempo_Ejecucion)
        return ret
    
    return wrapper

def dec_class(cls):
    """El decorador de clase recibe como primer argumento el objeto clase."""

    class NewCls:
        """Creamos una nueva clase que reemplazará a la original."""
    
        def __init__(self, *args, **kwargs):
            self.original_instance = cls(*args, **kwargs)
        
        def __getattribute__(self, name):
            """Este método se llama siempre que se accede a un método de un objeto NewCls. Esté método 
            primero intenta acceder a los atributos de NewCls, si falla, entonces accede a los de 
            self.original_instance, y si el atributo es un metodo, entonces se aplica el decorador.
            """
            try:    
                result = super().__getattribute__(name)
            except AttributeError:      
                pass
            # El else se ejecuta cuando no se lanza ninguna excepción
            else:
                return result
            result = self.original_instance.__getattribute__(name)
            if type(result) == type(self.__init__):
                return decorador_TiempoEjecucion(result)
            else:
                return result
    return NewCls

@dec_class
class MyClase():

    
    def test(self):
        for i in range(10000):
            "Hola, mundo!".replace("Hola", "Adios")

    def test2(self):
        for i in range(10000):
            "Hola, mundo!".replace("Hola", "Adios")       

fileConfig('logging_config.ini')
logger=logging.getLogger()

clase=MyClase()
clase.test()
clase.test2()