# -*- coding: utf-8 -*-
"""
Created on Sat Feb  26 15:43:57 2025

@author: Carlos Gabriel Marínez Bravo 346307
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 2*x*np.cos(2*x) - (x+1)**2

def falsa_posicion(a, b, tol=1e-6, max_iter=5):
    if f(a) * f(b) > 0:
        print("Error: La función no cambia de signo en el intervalo dado.")
        return None

    print(f"{'Iter':<6}{'a':<10}{'b':<10}{'x_i':<12}{'f(x_i)':<12}{'Error (%)':<12}")
    print("-" * 65)
    
    x_prev = None  
    for i in range(1, max_iter + 1):
       
        if f(a) == f(b):
            print("Error: División por cero al calcular x_i.")
            return None
        
        xi = b - (f(b) * (a - b)) / (f(a) - f(b))
        f_xi = f(xi)

        error = abs((xi - x_prev) / xi) * 100 if x_prev is not None else np.nan

        print(f"{i:<6}{a:<10.4f}{b:<10.4f}{xi:<12.6f}{f_xi:<12.6f}{error if x_prev is not None else '-':<12}")

        if abs(f_xi) < tol or (x_prev is not None and error < tol):
            break

        if f(a) * f_xi < 0:
            b = xi
        else:
            a = xi

        x_prev = xi  

    return xi

a, b = -3, -2

raiz = falsa_posicion(a, b, max_iter=5)

x_vals = np.linspace(-3.5, -1.5, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="f(x)", color='b')
plt.axhline(0, color='k', linestyle='--', linewidth=0.8)
if raiz is not None:
    plt.scatter(raiz, 0, color='r', zorder=3, label=f"Raíz estimada: {raiz:.6f}")
    plt.axvline(raiz, color='r', linestyle='--', linewidth=0.8, alpha=0.7)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Método de la Falsa Posición")
plt.legend()
plt.grid()
plt.show()
