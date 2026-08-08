#. Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
#matrices previamente inicializadas.

import numpy as np

# Matrices inicializadas (cuadradas 3x3 para poder multiplicar entre sí)
m1 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

m2 = np.array([[9, 8, 7],
               [6, 5, 4],
               [3, 2, 1]])

suma = m1 + m2
resta = m1 - m2
producto_punto = np.dot(m1, m2)          # multiplicación matricial real
producto_elemento = m1 * m2              # "producto cruz" -> elemento a elemento
division = m1 / m2                        # división elemento a elemento

print("Matriz 1:\n", m1)
print("Matriz 2:\n", m2)
print("Suma:\n", suma)
print("Resta:\n", resta)
print("Producto punto (matricial):\n", producto_punto)
print("Producto elemento a elemento:\n", producto_elemento)
print("División elemento a elemento:\n", division)