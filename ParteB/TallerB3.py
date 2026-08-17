import math


print("1. Prisma\n2. Pirámide\n3. Cono truncado\n4. Cilindro")
opcion = input("Porfavor seleccione una de las siguientes opciones: ")

if opcion == '1':
    area_base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura: "))
    print(f"Volumen del Prisma: {area_base * altura:.2f}")

elif opcion == '2':
    area_base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura: "))
    print(f"Volumen de la Pirámide: {(area_base * altura) / 3:.2f}")

elif opcion == '3':
    r_mayor = float(input("Ingrese el radio mayor: "))
    r_menor = float(input("Ingrese el radio menor: "))
    altura = float(input("Ingrese la altura: "))
    volumen = (math.pi * altura / 3) * (r_mayor**2 + r_menor**2 + r_mayor * r_menor)
    print(f"Volumen del Cono Truncado: {volumen:.2f}")

elif opcion == '4':
    radio = float(input("Ingrese el radio de la base: "))
    altura = float(input("Ingrese la altura: "))
    print(f"Volumen del Cilindro: {math.pi * (radio**2) * altura:.2f}")

else:
    print("Opción no válida. Por favor ejecute el programa de nuevo.")