# -*- coding: utf-8 -*-
"""
Created on Mar 26 22:12:51 2025

@author: Carlos Gabriel Martinez Bravo
"""

import numpy as np

def cholesky(A):
    n = A.shape[0]
    L = np.zeros_like(A)

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                L[i][j] = np.sqrt(A[i][i] - sum(L[i][k]**2 for k in range(j)))
            else:
                L[i][j] = (A[i][j] - sum(L[i][k]*L[j][k] for k in range(j))) / L[j][j]
    return L

def forward_substitution(L, b):
    n = len(b)
    z = np.zeros(n)
    for i in range(n):
        z[i] = (b[i] - np.dot(L[i, :i], z[:i])) / L[i, i]
    return z

def back_substitution(U, z):
    n = len(z)
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (z[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

A1 = np.array([[4, -2, 1],
               [-2, 4, -2],
               [1, -2, 4]])
b1 = np.array([11, -16, 17])

try:
    L = cholesky(A1)
    print("Matriz L (Cholesky):\n", L)
    print("L @ L.T:\n", L @ L.T)

    z = forward_substitution(L, b1)
    x = back_substitution(L.T, z)
    print("Solución x (Cholesky):", x)

except np.linalg.LinAlgError:
    print("La matriz no es definida positiva. No se puede aplicar Cholesky.")
