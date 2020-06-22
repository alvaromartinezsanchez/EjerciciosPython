""" Fibonacci como un generador¶
El objetivo de este ejercicio es reescribir la funcíon de Fibonacci para 
que genere de forma infinita todos los números de esta secuencia. """
import itertools

def fib(a=0, b=1):
    
    while True:
        yield a
        a, b = b, a + b



f = fib()

for i in f:
    print(i,", \n")
