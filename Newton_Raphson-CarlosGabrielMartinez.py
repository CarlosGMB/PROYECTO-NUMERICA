# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 23:02:14 2025

@author: Carlos
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 8 * x * np.sin(x) * np.exp(-x) - 1

def df(x):
    return 8 * np.exp(-x) * (np.sin(x) - x * np.cos(x) - x * np.sin(x))

def newton_raphson(x0, tol=1e-4, max_iter=5):
    iterations = []
    xr = x0
    for i in range(max_iter):
        x_new = xr - f(xr) / df(xr)
        error = abs((x_new - xr) / x_new) * 100 if x_new != 0 else 0
        iterations.append((i+1, round(x_new, 4), round(error, 4)))
        xr = x_new
        if error < tol:
            break
    return iterations, xr

x0 = 0.3
iterations, root = newton_raphson(x0)

print("i\t x_i\t ε_r")
for i, xi, er in iterations:
    print(f"{i}\t{xi}\t{er}")

x_vals = np.linspace(0, 1, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x) = 8x sin(x) e^(-x) - 1')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.scatter(root, f(root), color='red', zorder=3, label=f'Raíz estimada: {round(root, 4)}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Método de Newton-Raphson')
plt.show()