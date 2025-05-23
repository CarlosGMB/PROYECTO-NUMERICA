# -*- coding: utf-8 -*-
"""
Created on May 19 17:29:15 2025

@author: Carlos Gabriel Martinez Bravo
"""


import numpy as np
import matplotlib.pyplot as plt

xn = np.array([1, 2, 3, 5, 7], dtype=float)
yn = np.array([3, 6, 19, 99, 291], dtype=float)

def diferencias_divididas(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:] = (coef[j:] - coef[j-1:-1]) / (x[j:] - x[:n-j])
    return coef

def newton_eval(x_data, coef, x_val):
    n = len(coef)
    result = coef[0]
    prod = 1.0
    for i in range(1, n):
        prod *= (x_val - x_data[i-1])
        result += coef[i] * prod
    return result

coef = diferencias_divididas(xn, yn)

x_vals = np.linspace(1, 7, 200)
y_vals = [newton_eval(xn, coef, x) for x in x_vals]

plt.figure()
plt.plot(x_vals, y_vals, label="Polinomio de Newton")
plt.scatter(xn, yn, color='red', label='Datos originales')
plt.title("Interpolación de Newton de grado 4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

print(f"f(4) ≈ {newton_eval(xn, coef, 4):.4f}")
