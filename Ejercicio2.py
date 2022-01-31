import random
lista = []
for i in range(0,10):
    aleatorio = random.randint(1,100)
    lista.append(aleatorio)
print("Números generados aleatoriamente del 1 al 100:")
for elemento in lista:
    print(elemento,end=" ")
print()
suma = sum(lista)
media = suma / 10
maximo = max(lista)
menu = "1. Sumar\n2. Máximo\n3. Media\n4. Salir"
print(menu)
opcion = int(input("Introduce el número de la opción que quieres ejecutar: "))
while opcion != 4:
    print(menu)
    if opcion == 1:
        print("La suma de todos los números ha sido: ",suma)
    elif opcion == 2:
        print("El mayot número ha sido: ",maximo)
    elif opcion == 3:
        print("La media de todos los números ha sido: ",media)
    else:
        print("Error. Opción inválida.")
    opcion = int(input("Introduce el número de la opción que quieres ejecutar: "))
if opcion == 4:
    print("Hasta luego.")