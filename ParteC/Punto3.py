#Implemente la ecuación de carga y descarga para un circuito RC. El usuario ingresa por teclado el 
#valor de voltaje (V), capacitancia (𝜇𝐹) y resistencia (Ω).  Posteriormente realice en Python la gráfica.

import numpy as np
import matplotlib.pyplot as plt

def main():
    print("\n CIRCUITO RC: CARGA Y DESCARGA")
    try:
        V = float(input("Ingrese el voltaje de la fuente V (voltios): "))
        C_uF = float(input("Ingrese la capacitancia C (microfaradios, µF): "))
        R = float(input("Ingrese la resistencia R (ohmios): "))
    except ValueError:
        print("Debe ingresar valores numéricos.")
        return

    C = C_uF * 1e-6  # convertir µF a F
    tau = R * C       # constante de tiempo (segundos)

    # Vector de tiempo: se grafica hasta 5 constantes de tiempo (>99% del proceso)
    t = np.linspace(0, 5 * tau, 1000)

    # Ecuaciones de carga y descarga
    Vc_carga = V * (1 - np.exp(-t / tau))
    Vc_descarga = V * np.exp(-t / tau)

    print(f"\nConstante de tiempo tau = R*C = {tau:.6f} s")

    fig, axs = plt.subplots(1, 2, figsize=(13, 5.5))

    axs[0].plot(t, Vc_carga, color="green", linewidth=2)
    axs[0].axhline(V, color="gray", linestyle="--", linewidth=0.8, label=f"V = {V} V")
    axs[0].set_title("Carga del capacitor")
    axs[0].set_xlabel("Tiempo (s)")
    axs[0].set_ylabel("Voltaje Vc(t) (V)")
    axs[0].grid(True, alpha=0.4)
    axs[0].legend()

    axs[1].plot(t, Vc_descarga, color="darkorange", linewidth=2)
    axs[1].axhline(0, color="gray", linestyle="--", linewidth=0.8)
    axs[1].set_title("Descarga del capacitor")
    axs[1].set_xlabel("Tiempo (s)")
    axs[1].set_ylabel("Voltaje Vc(t) (V)")
    axs[1].grid(True, alpha=0.4)

    plt.suptitle(f"Circuito RC | V={V} V, C={C_uF} µF, R={R} Ω, tau={tau:.4f} s")
    plt.tight_layout()
    plt.savefig("circuito_RC.png", dpi=150)
    plt.show()

if __name__ == "__main__":
    main()
