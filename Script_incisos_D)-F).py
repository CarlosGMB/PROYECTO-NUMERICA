# -*- coding: utf-8 -*-
"""
Created on May 20 18:09:35 2025

@author: Carlos Gabriel Martinez Bravo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv'
df = pd.read_csv(url)

x = df['Experience Years'].values
y = df['Salary'].values
n = len(x)

sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x ** 2)

a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
a0 = (sum_y - a1 * sum_x) / n
#----------------------
# Inciso d)
#----------------------
print(f"Recta de regresión: f(x) = {a0:.2f} + {a1:.2f}x")

# ---------------------
# Inciso e)
# ---------------------

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', label='Datos reales')
x_line = np.linspace(min(x), max(x), 200)
y_line = a0 + a1 * x_line
plt.plot(x_line, y_line, color='red', label='Regresión lineal')

plt.xlabel('Experiencia en años')
plt.ylabel('Salario')
plt.title('Regresión lineal - Experiencia vs Salario')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ---------------------
# Inciso f)
# ---------------------
for experiencia in [15, 30, 50]:
    salario = a0 + a1 * experiencia
    print(f"Salario estimado para {experiencia} años: ${salario:,.2f}")
