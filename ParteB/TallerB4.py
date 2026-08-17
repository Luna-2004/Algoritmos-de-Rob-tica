
print("1. Cilíndrico\n2. Cartesiano\n3. Esférico")
robot = input("Escoja el tipo de robot: ")

if robot == '1':
    print("El robot cilíndrico tiene una(1) articulación rotacional y dos(2) prismáticas (RPP).")
elif robot == '2':
    print("El robot cartesiano tiene tres(3) articulaciones prismáticas (PPP).")
elif robot == '3':
    print("El robot esférico tiene dos(2) articulaciones rotacionales y una(1) prismática (RRP).")
else:
    print("Opción no válida.")