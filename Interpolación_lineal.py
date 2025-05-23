# -*- coding: utf-8 -*-
"""
Created on May 19 17:25:52 2025

@author: Carlos Gabriel Martinez Bravo
"""

import numpy as np

x = np.array([1, 2, 3, 5, 7, 8])
y = np.array([3, 6, 19, 99, 291, 444])

x0, x1 = 3, 5
y0, y1 = 19, 99
x_interp = 4
y_interp = y0 + ((y1 - y0)/(x1 - x0)) * (x_interp - x0)

print(f"Interpolación lineal en x = {x_interp} -> f(x) ≈ {y_interp}")
