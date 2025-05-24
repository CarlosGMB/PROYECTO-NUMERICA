# -*- coding: utf-8 -*-
"""
Created on Mar 26 12:29:46 2025

@author: Carlos Gabriel Martinez Bravo
"""

import numpy as np

def doolittle(A):
    n = A.shape[0]
    L = np.zeros_like(A, dtype=float)
    U = np.zeros_like(A, dtype=float)

    for i in range(n):
        L[i][i] = 1
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(i))
        for j in range(i+1, n):
            L[j][i] = (A[j][i] - sum(L[j][k]*U[k][i] for k in range(i))) / U[i][i]
    return L, U

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

A2 = np.array([[1, 1, 1],
               [1, 2, 5],
               [1, 4, 25]])
b2 = np.array([6, 12, 36])

A3 = np.array([[1, 2, 1],
               [3, 8, 1],
               [0, 4, 1]])
b3 = np.array([2, 12, 2])

for i, (A, b) in enumerate([(A1, b1), (A2, b2), (A3, b3)], start=1):
    L, U = doolittle(A)
    z = forward_substitution(L, b)
    x = back_substitution(U, z)
    print(f"\nSistema {i}:")
    print("L =\n", L)
    print("U =\n", U)
    print("Solución x =", x)
