"""El objetivo de este ejercicio es crear un decorador que capture cualquier excepción de una función y muestre por el log la traza de la excepción."""
import traceback, sys, logging

#Configuracion del log
logger=logging.getLogger()
logger.handlers=[]

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-6s %(levelname)-6s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def decorador_Funcion_Ejemplo(func_Ejemplo):

    def funcion_Interna_Decorador(*args, **kwargs):
        try:
            resultado=func_Ejemplo(*args, **kwargs)
            return resultado
        except:
            logger.info("\nDATOS A MOSTRAR POR EL LOG CUANDO SE PRODUCE UNA EXCEPCION:")
            exc_info = sys.exc_info()
            logger.error(exc_info[0])
            logger.error(exc_info[1])
            logger.info("TRAZA:")
            traceback.print_tb(exc_info[2])

    return funcion_Interna_Decorador


@decorador_Funcion_Ejemplo
def funcion_Ejemplo(valor):
    result=valor+1
    print(result)

#Funcionamiento correcto
print("Funcionamiento correcto:")
funcion_Ejemplo(5)

#Causa excepcion
print("Funcionamiento con fallo:")
funcion_Ejemplo("Hola")