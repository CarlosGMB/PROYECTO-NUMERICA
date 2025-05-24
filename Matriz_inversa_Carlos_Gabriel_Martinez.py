# -*- coding: utf-8 -*-
"""
Created on Mar 25 19:34:06 2025

@author: Carlos Gabriel Martinez Bravo
"""

import numpy as np

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

def resolver_por_inversa(A, b, n):
    try:
        A_inv = np.linalg.inv(A)
        x = A_inv @ b  
        print(f"\nSistema {n}:")
        print("Matriz inversa A⁻¹ =\n", A_inv)
        print("Solución x = A⁻¹ * b =", x)
    except np.linalg.LinAlgError:
        print(f"\nSistema {n}: La matriz no es invertible (singular).")

resolver_por_inversa(A1, b1, 1)
resolver_por_inversa(A2, b2, 2)
resolver_por_inversa(A3, b3, 3)
