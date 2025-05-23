# -*- coding: utf-8 -*-
"""
Created on May 19 17:26:54 2025

@author: Carlos Gabriel Martinez Bravo
"""

import numpy as np
import matplotlib.pyplot as plt

xq = np.array([2, 3, 5], dtype=float)
yq = np.array([6, 19, 99], dtype=float)

def lagrange_quad(x_val):
    x0, x1, x2 = xq
    y0, y1, y2 = yq

    L0 = ((x_val - x1)*(x_val - x2))/((x0 - x1)*(x0 - x2))
    L1 = ((x_val - x0)*(x_val - x2))/((x1 - x0)*(x1 - x2))
    L2 = ((x_val - x0)*(x_val - x1))/((x2 - x0)*(x2 - x1))

    return y0 * L0 + y1 * L1 + y2 * L2

x_plot = np.linspace(2, 5, 100)
y_plot = [lagrange_quad(x) for x in x_plot]

plt.figure()
plt.plot(x_plot, y_plot, label="Interpolación cuadrática")
plt.scatter(xq, yq, color='red', label='Puntos usados')
plt.title("Interpolación cuadrática (Lagrange)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

print(f"f(4) ≈ {lagrange_quad(4):.4f}")
