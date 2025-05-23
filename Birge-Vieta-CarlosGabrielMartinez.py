# -*- coding: utf-8 -*-
"""
Created on Sat Feb  27 22:51:03 2025

@author: Carlos Gabriel Martínez Bravo
"""
import numpy as np

def birge_vieta(coeffs, x0, max_iter=10):
    n = len(coeffs) - 1
    x = x0  

    
    print("Iter   x_k         b0 (f(x))    (f'(x))     x_k+1       Error %")
    print("-" * 65)
    
    for i in range(max_iter):
        b = np.zeros(n + 1)
        c = np.zeros(n)
     
        b[0] = coeffs[0]
        for j in range(1, n + 1):
            b[j] = coeffs[j] + x * b[j - 1]
        
        c[0] = b[0]
        for j in range(1, n):
            c[j] = b[j] + x * c[j - 1]

        if c[n-1] == 0:
            print("Error: Derivada cero, posible raíz múltiple o mal comportamiento numérico.")
            break

        x_new = x - (b[-1] / c[n-1])
        error = abs((x_new - x) / x_new) * 100  

        print(f"{i+1:>2}    {x:.6f}    {b[-1]:.6f}    {c[n-1]:.6f}    {x_new:.6f}    {error:.4f}")

        x = x_new  

    return x, b[:-1] 

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        real_part = -b / (2*a)
        imag_part = np.sqrt(abs(discriminant)) / (2*a)
        return (real_part + 1j * imag_part, real_part - 1j * imag_part)
    else:
        sqrt_disc = np.sqrt(discriminant)
        x1 = (-b + sqrt_disc) / (2*a)
        x2 = (-b - sqrt_disc) / (2*a)
        return x1, x2

coefficients = [1, -5, 5, -1]

x0 = 0.8

root, new_coeffs = birge_vieta(coefficients, x0, max_iter=10)

a, b, c = new_coeffs  
x1, x2 = quadratic_formula(a, b, c)

print("\nRaíces encontradas:")
print(f"x1 = {root:.6f} (por Birge-Vieta después de 10 iteraciones)")
print(f"x2 = {x1:.6f}, x3 = {x2:.6f} (por fórmula cuadrática)")

