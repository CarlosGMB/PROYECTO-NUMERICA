# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 20:58:10 2025

@author: Carlos Gabriel Martínez Bravo
"""
#Método de bisección 
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2 * x * np.cos(2 * x) - (x + 1)**2

def biseccion(a, b, iteraciones):
    xr_prev = None
    print(f"{'Iteración':<10}{'x_i':<10}{'a':<10}{'b':<10}{'Error (%)':<10}")
    print("-" * 50)

    for i in range(1, iteraciones + 1):
        xr = (a + b) / 2  # Punto medio
        f_xr = f(xr)

        error_rel = abs((xr - xr_prev) / xr) * 100 if xr_prev is not None else None
        print(f"{i:<10}{xr:<10.5f}{a:<10.5f}{b:<10.5f}{error_rel if error_rel is not None else '-':<10}")

        if f(a) * f_xr < 0:
            b = xr  
        else:
            a = xr  

        xr_prev = xr 

    return xr


a, b = -3, -2
iteraciones = 5

raiz_estimada = biseccion(a, b, iteraciones)

x_vals = np.linspace(-3.5, -1.5, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)', color='b')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(raiz_estimada, color='r', linestyle='--', label=f'Raíz estimada ({raiz_estimada:.5f})')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Bisección')
plt.legend()
plt.grid()
plt.show()