"""Eliminar duplicados
Crea una función que dada una lista cualquiera, devuelva una copia de
 esta lista eliminando los elementos duplicados. """

Lista= [1, 2, 3, 4, 3, 2, 5, 6, 6, 7, 9, 9, 7, 5, 4, 3]
Lista_2= ["Rojo","Verde","Marron","Negro","Blanco","Negro","Rojo"]

def mostrarListraSinRepetidos(lista):
    return (list(set(lista))) #list-->muestra lista  set-->elimina repetidos de " Lista "

print("Lista 1 :",mostrarListraSinRepetidos(Lista))
print("Lista 2 :",mostrarListraSinRepetidos(Lista_2))