""" Lanzador de dados 
Existen diferentes tipos de dados, según el número de caras de estos.
 De 4, de 6, de 8, de 10, de 12 y de 20 caras. 
 En juegos que utilizan estos dados, se usa una notación concreta para 
 decir cuandos datos hay que lanzar y de que tipo:

-"1d6" para indicar un dado de 6 caras
-"3d4" para lanzar 3 dados de 4 caras
-y en general "ndm" para indicar que se lanzan n dados de m caras

El objetivo de este ejercicio es crear una función que reciba como argumento 
una cadena de texto, y que devuelva una lista con cada uno de los resultados 
que se hayan obtenido en los lanzamientos de dados. """

#Parto de la suposición de que no podemos lanzar mas de 9 dados y de que cada cara posee un valor único y progresivamente ascendente.

import random #Importamos clase random 

#Obtenemos valores del usuario
numDados=input("Introduce cuantos dados vas a lanzar: ")
tipoDados=input("Indica cuantas caras poseen los dados a lanzar: ")
ordenTirada=numDados,"d",tipoDados

#Funcion que recibe cadena y devuelve lista de resultados
def realizarLanzamientoDados(cadena):

    numeroDadosLanzados=int(cadena[0]) 
    
    #Compruebo si el valor para el tipo de dado(caras) es de uno o dos digitos
    if len(cadena)==3:
        tipoDadoLanzado=cadena[2]
    elif len(cadena)==4:
        tipoDadoLanzado=cadena[2]+cadena[3]
    
        
    print("Numero de dados: ",numeroDadosLanzados)
    print("Caras del dado: ",tipoDadoLanzado)

    lanzamientos=0 #Nº de dados a lanzar
    resultados=[] #Lista con Resultado de las tiradas
    while lanzamientos<numeroDadosLanzados:
        lanzamientos+=1

        resultados+=[random.randint(1,int(tipoDadoLanzado))]# Genero numero aleatorio dependiendo del numero de caras
        
    return resultados



print("Resultados: ",realizarLanzamientoDados(ordenTirada))

