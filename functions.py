import numpy as np  
import pandas as pd  

def is_lower_triangle(matrix):
    # Esta funcion retorna False si no es una matriz cuadrada; True si lo es
    (filas, columnas) = matrix.shape
    # Verifiquemos que es una matriz cuadrada
    if filas != columnas:
        return False
    
    # variable que facilita ver si la matriz es vacia:
    sum = 0

    for i in range(filas):
        for j in range(filas):
            sum += matrix[i,j]
            if matrix[i,j] != 0 and matrix[i,j] != 1: # Vemos que solo haya 1s o 0s
                return False
            if i < j and matrix[i,j] == 1: # si nos salimos del triangulo, tiene que ser un 0.
                return False
    
    # aqui confirmamos que no sea vacia
    if sum == 0:
        return False

    return True

def n_per_file(matrix):
    # Esta funcion entregara el numero de valores en cada fila
    
    filas = matrix.shape[0]
    n = 0
    diccionario = {}
    for i in range(filas):

        return

    return

def delete_n(matrix, n):
    return