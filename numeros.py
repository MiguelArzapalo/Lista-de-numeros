numeros = []

n = int(input("¿Cuántos números desea ingresar? "))

for i in range(n):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

orden = input("¿En qué orden desea ordenar los números? (ascendente/descendente) ")

if orden == "ascendente":
    numeros.sort()
elif orden == "descendente":
    numeros.sort(reverse=True)
else:
    print("No se reconoce el orden ingresado.")

print("Los números ordenados son:", numeros)
