import numpy as np

# Vectores (3 componentes para el producto cruz)
v1 = np.array([8, 50, 39])
v2 = np.array([5, 20, 98])

suma = v1 + v2
resta = v1 - v2
producto_punto = np.dot(v1, v2)          # escalar
producto_cruz = np.cross(v1, v2)         # vector perpendicular a ambos
division = v1 / v2                       # división elemento a elemento

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Suma:", suma)
print("Resta:", resta)
print("Producto punto:", producto_punto)
print("Producto cruz:", producto_cruz)
print("División:", division)