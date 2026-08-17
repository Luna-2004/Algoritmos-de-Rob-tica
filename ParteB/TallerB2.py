import random


cantidad = int(input("Ingrese la cantidad de números que quiere generar: "))
minimo = int(input("Ingrese el número menor: "))
maximo = int(input("Ingrese el número superior: "))

# Generamos la lista de números aleatorios
numeros = [random.randint(minimo, maximo) for _ in range(cantidad)]
print(f"Los números: {numeros}")