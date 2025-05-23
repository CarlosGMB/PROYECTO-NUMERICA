# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 20:49:17 2025

@author: Carlos Gavriel Martinez Bravo
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 8 * x * np.sin(x) * np.exp(-x) - 1

def secant_method(x0, x1, tol=1e-4, max_iter=5):
    print(f"{'Iteración':<10}{'xi':<15}{'xi+1':<15}{'Error (%)':<15}")
    print("-" * 50)
    
    for i in range(max_iter):
        f_x0, f_x1 = f(x0), f(x1)
        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        error = abs((x2 - x1) / x2) * 100 if x2 != 0 else 0
        
        print(f"{i:<10}{x0:<15.4f}{x1:<15.4f}{error:<15.4f}")
        
        if error < tol:
            break
        
        x0, x1 = x1, x2
    
    return x2

x0, x1 = 0.5, -0.3
raiz = secant_method(x0, x1)


x_vals = np.linspace(-1, 1, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8,6))
plt.plot(x_vals, y_vals, label='f(x) = 8x sin(x) e^(-x) - 1', color='blue')
plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.axvline(raiz, color='red', linestyle='--', label=f'Raíz estimada: {raiz:.4f}')
plt.scatter(raiz, f(raiz), color='red', zorder=3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Método de la Secante')
plt.grid()
plt.show()