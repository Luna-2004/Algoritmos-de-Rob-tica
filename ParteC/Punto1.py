# Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C.

import numpy as np
import matplotlib.pyplot as plt

def resistencia_pt100(T):
    """
    Calcula la resistencia de una PT100 para un arreglo de temperaturas T (°C).
    Ecuación de Callendar-Van Dusen.
    """
    R0 = 100.0
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12  # solo aplica para T < 0

    R = np.where(
        T >= 0,
        R0 * (1 + A * T + B * T**2),
        R0 * (1 + A * T + B * T**2 + C * (T - 100) * T**3)
    )
    return R

# Rango de temperaturas solicitado
temperaturas = np.linspace(-200, 200, 1000)
resistencias = resistencia_pt100(temperaturas)

# Gráfica
plt.figure(figsize=(9, 6))
plt.plot(temperaturas, resistencias, color="firebrick", linewidth=2)
plt.axhline(100, color="gray", linestyle="--", linewidth=0.8, label="R = 100 Ω (0°C)")
plt.axvline(0, color="gray", linestyle="--", linewidth=0.8)
plt.title("Curva característica del sensor PT100")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ω)")
plt.grid(True, alpha=0.4)
plt.legend()
plt.tight_layout()
plt.savefig("pt100_curva.png", dpi=150)
plt.show()

print(f"Resistencia a -200°C: {resistencia_pt100(np.array([-200]))[0]:.4f} Ω")
print(f"Resistencia a 0°C:    {resistencia_pt100(np.array([0]))[0]:.4f} Ω")
print(f"Resistencia a 200°C:  {resistencia_pt100(np.array([200]))[0]:.4f} Ω")
