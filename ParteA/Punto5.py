#Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo)
#y un parámetro de salida (matriz).

import numpy as np

def rotacion_x(angulo_grados):
    a = np.radians(angulo_grados)
    return np.array([
        [1, 0, 0],
        [0, np.cos(a), -np.sin(a)],
        [0, np.sin(a),  np.cos(a)]
    ])

def rotacion_y(angulo_grados):
    a = np.radians(angulo_grados)
    return np.array([
        [ np.cos(a), 0, np.sin(a)],
        [ 0, 1, 0],
        [-np.sin(a), 0, np.cos(a)]
    ])

def rotacion_z(angulo_grados):
    a = np.radians(angulo_grados)
    return np.array([
        [np.cos(a), -np.sin(a), 0],
        [np.sin(a),  np.cos(a), 0],
        [0, 0, 1]
    ])

# Ejemplo de uso
angulo = 45  # grados

print("Rotación en X:\n", rotacion_x(angulo))
print("\nRotación en Y:\n", rotacion_y(angulo))
print("\nRotación en Z:\n", rotacion_z(angulo))