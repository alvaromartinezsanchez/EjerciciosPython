#importa el modulo io y metodo open para abrirlo
from io import open
import re
import collections
import os

#Abre el archivo en modo lectura y almacena el contenido
archivo_texto=open("./Isla.txt", "r")
texto=str(re.findall('\\w+',archivo_texto.read()))
archivo_texto.close()
counter = collections.Counter(texto.split())#convertimos texto en coleccion
ordenadas=counter.most_common()##Almacena lista de parejas ordenada


resultado=iter(ordenadas)
print("Palabra  Repeticiones")
for i in range(30):
    print(ordenadas[i])