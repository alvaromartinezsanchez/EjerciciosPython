#importamos el modulo io y metodo open para abrirlo
from io import open
import re
import collections

#Abre el archivo en modo lectura y almacena el contenido
archivo_texto=open("../Parte_2/Isla.txt", "r")
texto=str(re.findall('\w+',archivo_texto.read()))
archivo_texto.close()
counter = collections.Counter(texto.split())#convertimos texto en coleccion
ordenadas=counter.most_common(30)##Almacena lista de parejas ordenada


resultado=iter(ordenadas)
print("Palabra  Repeticiones")
print(ordenadas)