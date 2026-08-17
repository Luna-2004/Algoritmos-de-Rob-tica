import matplotlib.pyplot as plt
import numpy as np

#Variables para generar las curvas (usando trigonometría para los círculos/arcos)
t_media = np.linspace(-np.pi/2, np.pi/2, 20) # Medio círculo (Para D, P, R)
t_completa = np.linspace(0, 2*np.pi, 30)     # Círculo completo (Para O)
t_u = np.linspace(np.pi, 2*np.pi, 20)        # Curva inferior (Para U, J)

# 2. Diccionario (Las letras tienen Ancho = 1, Alto = 2)
# Cada letra tiene una lista de "trazos". Cada trazo es un par de listas (x_coords, y_coords)
letras = {
    'A': [([0, 0.5, 1], [0, 2, 0]), ([0.25, 0.75], [1, 1])],
    'D': [([0, 0], [0, 2]), (0 + 1*np.cos(t_media), 1 + 1*np.sin(t_media))], # Usa curva
    'E': [([1, 0, 0, 1], [2, 2, 0, 0]), ([0, 0.8], [1, 1])],
    'F': [([1, 0, 0], [2, 2, 0]), ([0, 0.8], [1, 1])],
    'G': [([1, 0, 0, 1, 1, 0.5], [2, 2, 0, 0, 1, 1])],
    'H': [([0, 0], [0, 2]), ([1, 1], [0, 2]), ([0, 1], [1, 1])],
    'I': [([0.5, 0.5], [0, 2]), ([0.2, 0.8], [0, 0]), ([0.2, 0.8], [2, 2])],
    'J': [([1, 1], [2, 0.5]), (0.5 + 0.5*np.cos(t_u), 0.5 + 0.5*np.sin(t_u))], # Usa curva
    'L': [([0, 0, 1], [2, 0, 0])],
    'M': [([0, 0, 0.5, 1, 1], [0, 2, 1, 2, 0])],
    'N': [([0, 0, 1, 1], [0, 2, 0, 2])],
    'O': [(0.5 + 0.5*np.cos(t_completa), 1 + 1*np.sin(t_completa))], # Usa curva completa
    'P': [([0, 0], [0, 2]), (0 + 1*np.cos(t_media), 1.5 + 0.5*np.sin(t_media))], # Usa curva
    'R': [([0, 0], [0, 2]), (0 + 1*np.cos(t_media), 1.5 + 0.5*np.sin(t_media)), ([0.4, 1], [1, 0])],
    'S': [([1, 0, 0, 1, 1, 0], [2, 2, 1, 1, 0, 0])],
    'T': [([0.5, 0.5], [0, 2]), ([0, 1], [2, 2])],
    'U': [([0, 0], [2, 0.5]), ([1, 1], [2, 0.5]), (0.5 + 0.5*np.cos(t_u), 0.5 + 0.5*np.sin(t_u))], # Usa curva
    'Y': [([0, 0.5, 1], [2, 1, 2]), ([0.5, 0.5], [1, 0])]
}

#Nombres (En mayúsculas para coincidir con el diccionario)
nombres = ["SANTIAGO", "FELIPE", "MADELEYNY", "ANDRES", "LUNA", "JULIETH"]
colores = ['blue', 'green', 'red', 'purple', 'orange', 'cyan']

plt.figure(figsize=(12, 9))


y_offset = 0 # Inicia en el renglón 0

for idx, nombre in enumerate(nombres):
    x_offset = 0 # Cada nombre inicia a la izquierda del lienzo
    color_actual = colores[idx % len(colores)] # Asigna un color distinto a cada uno
    
    for char in nombre:
        if char in letras:
            for trazo in letras[char]:
                # Convertimos a numpy array para sumar la posición y mover la letra en el plano
                x_coords = np.array(trazo[0]) + x_offset
                y_coords = np.array(trazo[1]) + y_offset
                plt.plot(x_coords, y_coords, color=color_actual, linewidth=3)
        
        # Espaciado a la derecha para la siguiente letra
        x_offset += 1.5 
    
    # Espaciado hacia abajo para el siguiente nombre
    y_offset -= 3.5 

# 5. Configuraciones de la gráfica
plt.title("Nombres del Grupo construidos con Geometría y Funciones Paramétricas")
plt.axis('equal') # Muy importante: Asegura que los círculos no se vean aplastados
plt.grid(True, linestyle='--', alpha=0.6) # Dejamos la cuadrícula para demostrar que son coordenadas
plt.show()