# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:34:21 2025

@author: Carlos Gabriel Martínez Bravo 346307
"""
import numpy as np
import matplotlib.pyplot as plt

def multiples_fila(N):
    if not isinstance(N, int) or N <= 0:
        return "Error: N debe ser un entero positivo."
    
    v = np.random.randint(1, 9, N)
    matriz = np.zeros((N, N))
    
    for i in range(N):
        matriz[i] = v * (i + 1)
    
    return matriz

def multiples_columna(N):
    if not isinstance(N, int) or N <= 0:
        return "Error: N debe ser un entero positivo."
    
    v = np.random.randint(1, 9, N)
    matriz = np.zeros((N, N))
    
    for i in range(N):
        matriz[:, i] = v * (i + 1)
    
    return matriz

N = 3
print("Matriz con múltiplos en filas:")
print(multiples_fila(N))

print("Matriz con múltiplos en columnas:")
print(multiples_columna(N))


def graficar_funciones():
    x = np.linspace(-10, 10, 100)
    y1 = x**2
    y2 = np.sin(x)
    y3 = np.cos(x)
    
    plt.plot(x, y1, label='y = x^2', color='purple', linestyle='-', marker='o')
    plt.plot(x, y2, label='y = sin(x)', color='b', linestyle='--', marker='s')
    plt.plot(x, y3, label='y = cos(x)', color='orange', linestyle=':', marker='x')
    
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Gráfica de Funciones')
    plt.grid(True)
    plt.legend()
    plt.show()
graficar_funciones()