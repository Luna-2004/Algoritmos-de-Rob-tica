#Obtenga las coordenadas X y Y de los contornos de dos logos de automóviles (Chevrolet, Hyundai, 
#Mazda, etc.), a través de Python.


import cv2
import numpy as np
import matplotlib.pyplot as plt

def obtener_contorno(ruta_imagen, umbral=None):
    # 1. Leer la imagen en escala de grises
    img = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"No se encontró la imagen: {ruta_imagen}")

    # 1b. Suavizar un poco para reducir ruido típico de fotos JPEG
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # 2. Binarizar (blanco/negro) para resaltar la figura del logo.
    #    Si no se indica un umbral fijo, se usa Otsu para calcularlo
    #    automáticamente (más robusto con fotos reales).
    if umbral is None:
        _, binaria = cv2.threshold(
            img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )
    else:
        _, binaria = cv2.threshold(img, umbral, 255, cv2.THRESH_BINARY_INV)

    # 3. Detectar contornos externos
    contornos, _ = cv2.findContours(
        binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if not contornos:
        raise ValueError("No se detectaron contornos. Ajusta el umbral o revisa la imagen.")

    # 4. Tomar el contorno más grande (el logo principal)
    contorno_principal = max(contornos, key=cv2.contourArea)

    # 5. Extraer coordenadas X, Y
    xs = contorno_principal[:, 0, 0]
    ys = contorno_principal[:, 0, 1]

    # Invertir Y porque en imágenes el eje Y crece hacia abajo
    ys = img.shape[0] - ys

    return xs, ys

def graficar_contorno(xs, ys, titulo):
    plt.figure(figsize=(6, 6))
    plt.plot(xs, ys, color="black", linewidth=1.5)
    plt.gca().set_aspect("equal")
    plt.title(titulo)
    plt.xlabel("X (px)")
    plt.ylabel("Y (px)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"contorno_{titulo}.png", dpi=150)
    plt.show()

def main():
    # IMPORTANTE: estos archivos deben estar en la MISMA carpeta que este
    # script, o debes escribir la ruta completa (ver ejemplo con r"..." al
    # final de este archivo).
    logos = {
        "Logo1": "Chevrolet-Logo.png",
        "Logo2": "images.png",
    }

    for nombre, archivo in logos.items():
        try:
            xs, ys = obtener_contorno(archivo)
            print(f"\n{nombre}: se extrajeron {len(xs)} puntos del contorno")
            print("Primeros 5 puntos (X, Y):")
            for x, y in list(zip(xs, ys))[:5]:
                print(f"  ({x}, {y})")
            graficar_contorno(xs, ys, nombre)

            # Guardar las coordenadas en un archivo de texto
            np.savetxt(f"coordenadas_{nombre}.csv",
                       np.column_stack((xs, ys)),
                       delimiter=",", header="X,Y", comments="")
        except FileNotFoundError as e:
            print(f"\n{e}")
            print(f"Coloca el archivo '{archivo}' en esta carpeta para procesarlo.")

if __name__ == "__main__":
    main()
