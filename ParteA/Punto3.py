#Realice un programa que convierta coordenadas rectangulares a cilíndricas y esféricas

import math

# Coordenadas rectangulares
x, y, z = 3, 4, 5

#  A cilíndricas (r, theta, z) 
r_cil = math.sqrt(x**2 + y**2)
theta_cil = math.atan2(y, x)          # en radianes
theta_cil_grados = math.degrees(theta_cil)

print("Coordenadas cilíndricas:")
print(f"r = {r_cil:.4f}")
print(f"theta = {theta_cil_grados:.4f} grados")
print(f"z = {z}")

# A esféricas (rho, theta, phi)
rho = math.sqrt(x**2 + y**2 + z**2)
theta_esf = math.atan2(y, x)                      # ángulo azimutal
phi_esf = math.acos(z / rho) if rho != 0 else 0   # ángulo polar

print("\nCoordenadas esféricas:")
print(f"rho = {rho:.4f}")
print(f"theta = {math.degrees(theta_esf):.4f} grados")
print(f"phi = {math.degrees(phi_esf):.4f} grados")

#TENER EN CUENTA QUE:
#Funciones trigonométricas usadas: math.sqrt, math.atan2 (mejor que atan porque respeta el cuadrante),
# math.acos, y math.degrees para convertir radianes a grados.