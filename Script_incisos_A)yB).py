# -*- coding: utf-8 -*-
"""
Created on May 20 18:01:20 2025

@author: Carlos Gabriel Martinez Bravo
"""

import pandas as pd

# -------------------------------------------------
# INCISOS A y B: Lectura del CSV desde la URL
# -------------------------------------------------

url = 'https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv'

df = pd.read_csv(url)

print("Primeros registros del archivo leído desde la URL:")
print(df.head())

print("\nColumnas encontradas:", df.columns.tolist())

x = df['Experience Years'].values
y = df['Salary'].values
