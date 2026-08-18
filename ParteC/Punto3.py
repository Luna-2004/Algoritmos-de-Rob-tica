#Implemente la ecuación de carga y descarga para un circuito RC.
# El usuario ingresa por teclado el #valor de voltaje (V), capacitancia (𝜇𝐹) y resistencia (Ω). Posteriormente realice en Python la gráfica.

import matplotlib.pyplot as plt
import numpy as np

print("\nCIRCUITO RC: CARGA Y DESCARGA")


try:
    V = float(input("Ingrese el voltaje de la fuente V (voltios): "))
    C_uF = float(input("Ingrese la capacitancia C (microfaradios, µF): "))
    R = float(input("Ingrese la resistencia R (ohmios): "))
except ValueError:
    print("Debe ingresar valores numéricos.")
    exit()

# Conversión de microfaradios a faradios
C = C_uF * 1e-6

# Constante de tiempo
tau = R * C

# Vector de tiempo: hasta 5 constantes de tiempo
t = np.linspace(0, 5 * tau, 1000)

# Ecuaciones de carga y descarga
Vc_carga = V * (1 - np.exp(-t / tau))
Vc_descarga = V * np.exp(-t / tau)


print(f"\nConstante de tiempo tau = R*C = {tau:.6f} s")

fig, axs = plt.subplots(1, 2, figsize=(13, 5.5))

# Gráfica de carga
axs[0].plot(t, Vc_carga, color="green", linewidth=2)
axs[0].axhline(V, color="gray", linestyle="--",
               linewidth=0.8, label=f"V = {V} V")

axs[0].set_title("Carga del capacitor")
axs[0].set_xlabel("Tiempo (s)")
axs[0].set_ylabel("Voltaje Vc(t) (V)")
axs[0].grid(True, alpha=0.4)
axs[0].legend()

# Gráfica de descarga
axs[1].plot(t, Vc_descarga, color="darkorange", linewidth=2)
axs[1].axhline(0, color="gray", linestyle="--", linewidth=0.8)

axs[1].set_title("Descarga del capacitor")
axs[1].set_xlabel("Tiempo (s)")
axs[1].set_ylabel("Voltaje Vc(t) (V)")
axs[1].grid(True, alpha=0.4)


plt.suptitle(
    f"Circuito RC | V={V} V, C={C_uF} µF, "
    f"R={R} Ω, tau={tau:.4f} s"
)

plt.tight_layout()


plt.savefig("circuito_RC.png", dpi=150)
plt.show()