"""
Created on Apr 11 21:48:21 2025

@author: Carlos Gabriel Martinez Bravo 346307
"""

# main_aplicacion.py

import numpy as np
from rutinas_integracion import (
    trapecio_simple,
    trapecio_multiple,
    simpson_1_3,
    simpson_3_8
)

def f(x):
    return 2 * np.cos(2 * x)

a = 0
b = np.pi / 4

valor_analitico = 1.0

print("Resultados para f(x) = 2cos(2x) en [0, π/4]:\n")

ts = trapecio_simple(f, a, b)
error_ts = abs((valor_analitico - ts) / valor_analitico) * 100
print(f"Trapecio simple: {ts:.6f} | Error relativo: {error_ts:.2f}%")

for n in [2, 4, 6]:
    tm = trapecio_multiple(f, a, b, n)
    error_tm = abs((valor_analitico - tm) / valor_analitico) * 100
    print(f"Trapecio múltiple (n={n}): {tm:.6f} | Error relativo: {error_tm:.2f}%")

n_s13 = 6
try:
    s13 = simpson_1_3(f, a, b, n_s13)
    error_s13 = abs((valor_analitico - s13) / valor_analitico) * 100
    print(f"Simpson 1/3 (n={n_s13}): {s13:.6f} | Error relativo: {error_s13:.2f}%")
except ValueError as e:
    print(f"Error en Simpson 1/3: {e}")

n_s38 = 6
try:
    s38 = simpson_3_8(f, a, b, n_s38)
    error_s38 = abs((valor_analitico - s38) / valor_analitico) * 100
    print(f"Simpson 3/8 (n={n_s38}): {s38:.6f} | Error relativo: {error_s38:.2f}%")
except ValueError as 
    print(f"Error en Simpson 3/8: {e}")