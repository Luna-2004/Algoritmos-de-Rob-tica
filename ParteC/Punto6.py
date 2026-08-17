import cv2
import matplotlib.pyplot as plt

# 1. Definimos una lista con las dos imágenes que queremos procesar
rutas_imagenes = ['chevrolet.jpeg', 'citroen.jpeg']

# 2. Preparamos el lienzo para dos gráficas: 1 fila, 2 columnas. 
# figsize=(12, 5) hace la ventana más ancha para que quepan bien.
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# 3. Iteramos sobre nuestra lista de imágenes
for i, ruta in enumerate(rutas_imagenes):
    # Leer la imagen actual en escala de grises
    imagen = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)

    if imagen is None:
        print(f"Error: No se encontró la imagen '{ruta}'. Revisa el nombre y la ubicación.")
        continue # Si no encuentra una imagen, salta a la siguiente
    
    print(f"\nCoordenadas del logo: {ruta}")
    
    # Convertir los bordes a blanco y el fondo a negro
    _, umbral = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY_INV)
    
    # Encontrar los contornos
    contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Asignamos el sub-gráfico correspondiente (izquierdo o derecho)
    ax = axs[i] 
    
    # Extraer y graficar las coordenadas
    for j, contorno in enumerate(contornos):
        x = contorno[:, 0, 0]
        y = contorno[:, 0, 1]
        
        # REQUERIMIENTO 1: Imprimir coordenadas en consola
        # Usamos .tolist() para imprimir el arreglo completo de forma legible
        print(f"\n -> Contorno {j+1}:")
        print(f"Valores X: {x.tolist()}")
        print(f"Valores Y: {y.tolist()}")
        
        # REQUERIMIENTO 2: Graficar en su respectivo lado (ax)
        ax.plot(x, -y, color='black') 
        
    # Configuraciones estéticas para cada sub-gráfico
    ax.set_title(f"Contorno: {ruta}")
    ax.axis('equal') 
    ax.grid(True)

# Ajustar el espacio para que los títulos no se crucen y mostrar
plt.tight_layout()
plt.show()