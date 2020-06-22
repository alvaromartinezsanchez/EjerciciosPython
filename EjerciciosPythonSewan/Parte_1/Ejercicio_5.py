"""Problema chino¶
Crea una función que resuelva el siguiente problema:

Contamos 35 cabezas y 94 patas entre gallinas y conejos en una 
granja, ¿cuántos conejos y cuantas gallinas tenemos? """



cabezasTotal=35
patasTotal=94

numeroGallinas=lambda cabezas, patas:((4*cabezas)-patas)//2
numeroConejos=lambda cabezas, gallinas:cabezas-gallinas
print(numeroGallinas(cabezasTotal,patasTotal))
print(numeroConejos(cabezasTotal,numeroGallinas(cabezasTotal,patasTotal)))

