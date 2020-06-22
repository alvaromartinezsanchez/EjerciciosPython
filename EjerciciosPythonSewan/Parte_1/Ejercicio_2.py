"""Listas superpuestas¶
Escribe una función que tome como parámetros dos listas 
y devuelva True si tienen al menos un miembro en común, 
y False en caso contrario. """

Lista_1=[1,2,3,4,5]
Lista_2=[6,7,8,9,10]
Lista_3=[1,3,5,7,9]#Lista_3 Coincide con ambas

def compruebaListas( lista1, lista2):
    coincidencia=False
    for letra in lista1:
        if(letra in lista2):
            coincidencia=True
    
    return coincidencia
            
print("Coinciden Lista_1 y Lista_2: ")
print(compruebaListas(Lista_1,Lista_2))
print("---------------------------")
print("Coinciden Lista_1 y Lista_3: ")
print(compruebaListas(Lista_1,Lista_3))
print("---------------------------")
print("Coinciden Lista_2 y Lista_3: ")
print(compruebaListas(Lista_2,Lista_3))
print("---------------------------")