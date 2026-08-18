# Consulte y elabore un sistema coordenado X, Y y Z donde se dibuje un vector con coordenadas 
#ingresadas por el usuario.
import numpy as np
import matplotlib.pyplot as plt

print("\nVECTOR EN EL ESPACIO 3D")

try:
    x = float(input("Ingrese la componente X: "))
    y = float(input("Ingrese la componente Y: "))
    z = float(input("Ingrese la componente Z: "))
except ValueError:
    print("Debe ingresar valores numéricos.")
    exit()

# Crear la figura 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

# Vector desde el origen hasta (x, y, z)
ax.quiver(
    0, 0, 0,
    x, y, z,
    color="crimson",
    linewidth=2,
    arrow_length_ratio=0.1
)

# Límites simétricos para que se vea bien el sistema de ejes
limite = max(abs(x), abs(y), abs(z), 1) * 1.3

ax.set_xlim([-limite, limite])
ax.set_ylim([-limite, limite])
ax.set_zlim([-limite, limite])

# Ejes de referencia
ax.plot(
    [-limite, limite],
    [0, 0],
    [0, 0],
    color="black",
    linewidth=0.6
)

ax.plot(
    [0, 0],
    [-limite, limite],
    [0, 0],
    color="black",
    linewidth=0.6
)

ax.plot(
    [0, 0],
    [0, 0],
    [-limite, limite],
    color="black",
    linewidth=0.6
)

# Nombres de los ejes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Título
ax.set_title(f"Vector V = ({x}, {y}, {z})")

# Calcular magnitud del vector
magnitud = np.sqrt(x**2 + y**2 + z**2)

print(f"\nMagnitud del vector: {magnitud:.4f}")

# Mostrar y guardar la gráfica
plt.tight_layout()
plt.savefig("vector_3D.png", dpi=150)
plt.show()