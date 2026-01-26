# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 20:03:31 2026

"""


# ---------------------------------------------------------
# NEURONA CON REGLA DE OJA
# Implementación de la regla de Oja en Python
# ---------------------------------------------------------

# Importar los módulos necesarios
import numpy as np
import matplotlib.pyplot as plt
import pickle

# Cargar los datos
# Objetivo: Abrir el archivo pickle que contiene los puntos (x,y)
with open('_7bfd5defa66c4d019fdb4bd6af2a62b5_c10p1.pickle', 'rb') as f:
    data = pickle.load(f)

# Ver qué contiene data
print(type(data))  # data es un diccionario
print(data.keys())  # muestra las claves disponibles

# Acceder a la clave que contiene los puntos (normalmente 'X' o 'c10p1')
# Ajusta esta línea según la clave exacta en tu pickle
X = np.array(data['c10p1'], dtype=float)  # ahora X es un array numpy 2D

# Centrar los datos en la media
# Objetivo: Sustraer la media de cada columna para que los datos tengan media cero
X = X - np.mean(X, axis=0)

# Visualizar los datos centrados
# Objetivo: Comprobar que la nube de datos está centrada alrededor de (0,0)
plt.figure(figsize=(6,6))
plt.scatter(X[:,0], X[:,1], alpha=0.6)
plt.title("Datos centrados en la media (0,0)")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.show()

# Inicializar parámetros de la regla de Oja
# eta: tasa de aprendizaje
# alpha: parámetro de Oja
# dt: paso de tiempo discreto
# n_iter: número de iteraciones para aprendizaje en línea
# w: vector de pesos inicial aleatorio (2D)
eta = 1.0
alpha = 1.0
dt = 0.01
n_iter = 100000
w = np.random.rand(2)  # vector columna inicial aleatorio 2x1

# Aprendizaje en línea con la regla de Oja
# Objetivo: actualizar w usando cada punto de datos uno a uno, en bucle
for t in range(n_iter):
    # Seleccionar punto de datos de forma cíclica
    i = t % X.shape[0]  # recorrer de 0 a 99 y luego volver a empezar
    u = X[i]  # punto de datos actual (vector 2D)

    # Calcular la salida de la neurona
    v = np.dot(w, u)  # producto punto entre pesos y entrada

    # Actualizar vector de pesos usando la versión discreta de Oja
    w += dt * eta * (v * u - alpha * v**2 * w)

# 7️⃣ Mostrar vector de pesos final
print("Vector de pesos final (w):")
print(w)

# Visualizar vector de pesos sobre los datos
# Objetivo: ver hacia dónde converge w en relación a la nube de datos
plt.figure(figsize=(6,6))
plt.scatter(X[:,0], X[:,1], alpha=0.6)
# Dibujar vector w desde el origen
plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='r', width=0.01)
plt.title("Datos centrados y vector de pesos final")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.show()


