"""Distancia de Hamming¶
El objetivo de este ejercicio es escribir una función que calcule la 
distancia de Hamming entre dos cadenas de la misma longitud. 
La distancia de Hamming es el número de carácteres diferentes entre 
dos cadenas. """

Cadena_1=""
Cadena_2=""
Repetir=True #Almacena resultado de comparar longitud entre ambas cadenas introducidas



#Funcion que recibe dos cadenas y compara las letras que tienen diferentes
def distanciaHamming(cad_1, cad_2):
    hamming=0

    #Tengo en cuenta que si una letrea o caracte se repite solo lo cuento una vez.
    comprobadas=""#Almacena las letras que ya se han comprobado para no aumentar el hamming
    letrasRepetidas="no"#Almacena las letras que se han repetido para mostrarlas

    for letra in cad_1:
        if(letra not in cad_2 and letra not in comprobadas):
            comprobadas+=letra
            hamming+=1
        elif (letra not in cad_2 and letra in comprobadas):
            letrasRepetidas+=letra

    print("Letras diferentes en la primera cadena: ")
    print(comprobadas)
    print("Letras repetidas: ",letrasRepetidas)

    #Reiniciamos los valores
    comprobadas=""
    letrasRepetidas="no"

    for letra in cad_2:
        if(letra not in cad_1 and letra not in comprobadas):
            comprobadas+=letra
            hamming+=1
        elif (letra not in cad_1 and letra in comprobadas):
            letrasRepetidas+=letra


    print("Letras diferentes en la segunda cadena:")
    print(comprobadas)
    print("Letras repetidas: ",letrasRepetidas)         
    return hamming



Cadena_1=input("Introduce la primera cadena: ")
while Repetir:
    print("La primera cadena tiene ",len(Cadena_1)," caracteres")
    Cadena_2=input("Intoduce una segunda cadena con la misma longitud : ")

    if(len(Cadena_1)==len(Cadena_2)):
        Repetir=False



print("La longitud Total de las dos cadenas es de ",len(Cadena_1)+len(Cadena_2)," caracteres \nY su haming es de : ",distanciaHamming(Cadena_1,Cadena_2))