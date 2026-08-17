#Realice un programa que le permita al usuario ingresar los coeficientes de una función de 
#transferencia de segundo orden y graficar su comportamiento, además se debe mostrar que tipo 
#de sistema es: subamortiguado, criticamente amortiguado y sobreamortiguado.


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def clasificar_sistema(zeta):
    if zeta < 1:
        return "Subamortiguado (0 < zeta < 1): respuesta oscilatoria decreciente"
    elif zeta == 1:
        return "Críticamente amortiguado (zeta = 1): retorno más rápido sin oscilar"
    else:
        return "Sobreamortiguado (zeta > 1): retorno lento sin oscilar"

def main():
    print("\n FUNSIÓN DE TRASFERENCIA DE SEGUNDO ORDEN")
    print("G(s) = wn^2 / (s^2 + 2*zeta*wn*s + wn^2)\n")

    try:
        wn = float(input("Ingrese la frecuencia natural wn (rad/s): "))
        zeta = float(input("Ingrese el factor de amortiguamiento zeta: "))
    except ValueError:
        print("Debe ingresar valores numéricos.")
        return

    # Coeficientes del sistema: numerador y denominador
    num = [wn**2]
    den = [1, 2 * zeta * wn, wn**2]

    sistema = signal.TransferFunction(num, den)

    # Respuesta al escalón
    t, y = signal.step(sistema)

    tipo = clasificar_sistema(zeta)
    print(f"\nTipo de sistema: {tipo}")

    plt.figure(figsize=(9, 6))
    plt.plot(t, y, color="navy", linewidth=2)
    plt.axhline(1, color="gray", linestyle="--", linewidth=0.8, label="Valor final")
    plt.title(f"Respuesta al escalón | wn={wn} rad/s, zeta={zeta}\n{tipo}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Salida y(t)")
    plt.grid(True, alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig("respuesta_2do_orden.png", dpi=150)
    plt.show()

if __name__ == "__main__":
    main()
