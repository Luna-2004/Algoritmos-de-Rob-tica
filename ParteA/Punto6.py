#Realice un programa que calcule la fuerza de avance y retroceso de un cilindro neumático de doble
#efecto. Debe establecer previamente los valores de presión, así como las dimensiones físicas del
#cilindro para realizar el cálculo.
import math

def fuerza_cilindro(presion, diametro_piston, diametro_vastago):
    """
    Calcula la fuerza de avance y retroceso de un cilindro
    neumático de doble efecto.

    presion: en Pa (o kPa, según unidades consistentes)
    diametro_piston: diámetro del pistón en metros
    diametro_vastago: diámetro del vástago en metros
    """
    area_piston = math.pi * (diametro_piston ** 2) / 4
    area_vastago = math.pi * (diametro_vastago ** 2) / 4
    area_anular = area_piston - area_vastago  # área efectiva en el retroceso

    fuerza_avance = presion * area_piston
    fuerza_retroceso = presion * area_anular

    return fuerza_avance, fuerza_retroceso, area_piston, area_anular

# Datos de ejemplo
presion = 600000          # 600 kPa = 6 bar, en Pascales
diametro_piston = 0.05    # 50 mm
diametro_vastago = 0.02   # 20 mm

f_avance, f_retroceso, a_piston, a_anular = fuerza_cilindro(
    presion, diametro_piston, diametro_vastago
)

print(f"Área del pistón: {a_piston:.6f} m²")
print(f"Área anular (retroceso): {a_anular:.6f} m²")
print(f"Fuerza de avance: {f_avance:.2f} N")
print(f"Fuerza de retroceso: {f_retroceso:.2f} N")