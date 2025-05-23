"""
Created on Apr 10 19:37:27 2025

@author: Carlos Gabriel Martínez Bravo 346307
"""

# rutinas_integracion

import numpy as np

def trapecio_simple(f, a, b):
    return (b - a) / 2 * (f(a) + f(b))

def trapecio_multiple(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h / 2 * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpson_1_3(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n debe ser par para Simpson 1/3")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

def simpson_3_8(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("n debe ser múltiplo de 3 para Simpson 3/8")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return 3 * h / 8 * (y[0] + 3 * np.sum(y[1:-1][(np.arange(1, n) % 3 != 0)]) +
                        2 * np.sum(y[1:-1][(np.arange(1, n) % 3 == 0)]) + y[-1])