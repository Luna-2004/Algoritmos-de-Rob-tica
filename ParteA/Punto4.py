#4. Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de la temperatura (°C).

#Usando la ecuación de Callendar-Van Dusen.


def resistencia_pt100(temperatura):
    
    R0 = 100.0          # Resistencia a 0°C
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12       # Solo se usa para T < 0

    if temperatura >= 0:
        R = R0 * (1 + A * temperatura + B * temperatura**2)
    else:
        R = R0 * (1 + A * temperatura + B * temperatura**2 +
                   C * (temperatura - 100) * temperatura**3)
    return R

# Ejemplo de uso
for T in [-20, 0, 25, 100, 200]:
    print(f"Temperatura: {T} °C -> Resistencia: {resistencia_pt100(T):.4f} ohms")