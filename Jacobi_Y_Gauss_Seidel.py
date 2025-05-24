# -*- coding: utf-8 -*-
"""
Created on Mar 23 15:38:11 2025

@author: Carlos Gabriel Martinez Bravo
"""

import numpy as np

A = np.array([[1, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, -10]])
b = np.array([7.85, 19.3, 71.4])

x_jacobi = np.zeros(3)
x_gauss = np.zeros(3)

print("=== Método de Jacobi (3 iteraciones) ===")
for it in range(3):
    x_new = np.zeros_like(x_jacobi)
    for i in range(3):
        suma = sum(A[i][j] * x_jacobi[j] for j in range(3) if j != i)
        x_new[i] = (b[i] - suma) / A[i][i]
    x_jacobi = x_new.copy()
    print(f"Iteración {it+1}: {x_jacobi}")

print("\n=== Método de Gauss-Seidel (3 iteraciones) ===")
for it in range(3):
    for i in range(3):
        suma = sum(A[i][j] * x_gauss[j] for j in range(3) if j != i)
        x_gauss[i] = (b[i] - suma) / A[i][i]
    print(f"Iteración {it+1}: {x_gauss}")
