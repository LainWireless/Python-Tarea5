lista = []
numero = int(input("¿Cuántas palabras tiene la lista?: "))
while numero == 0:
        print("¡Una lista no puede tener 0 palabras!")
        numero = int(input("¿Cuántas palabras tiene la lista?: "))
if numero == 1:
    palabra= input("Dime la palabra: ")
    lista.append(palabra)
else:
    for i in range(0,numero):
        palabra = input("Dime la palabra %d: "%(i+1))
        lista.append(palabra)
print()
print("La lista creada es: ",end="")
for elemento in lista:
    print(elemento,end=" ")
print()
menu = "1. Contar\n2. Modificar\n3. Eliminar\n0. Salir\n"
print(menu)
opcion = int(input("Introduce el número de la opción que quieres ejecutar: "))
while opcion != 0:
    if opcion == 1:
        buscar = input("¿Qué palabra quieres buscar?: ")
        print()
        print("La palabra %s aparece %d veces"%(buscar,lista.count(buscar)))
        print()
    elif opcion == 2:
        buscar = input("¿Qué palabra quieres sustituir?: ")
        while buscar not in lista:
            buscar = input("Error. Palabra no encontrada. ¿Qué palabra quieres sustituir?: ")
        sustituir = input("¿Por qué palabra quieres sustituir la anterior?: ")
        while buscar in lista:
            lista[lista.index(buscar)] = sustituir
        print()
        print("¡Esta es tu lista ahora!: ",end="")
        for elemento in lista:
            print(elemento,end=" ")
        print()
    elif opcion == 3:
        eliminar = input("¿Qué palabra deseas eliminar?: ")
        while eliminar not in lista:
            eliminar = input("Error. Palabra no encontrada. ¿Qué palabra deseas eliminar?: ")
        while eliminar in lista:
            lista.remove(eliminar)
        print()
        print("¡Esta es tu lista ahora!: ",end="")
        for elemento in lista:
            print(elemento,end=" ")
        print()
    else:
        print()
        print("Error. Opción inválida.")
        print()
    print()
    print(menu)
    opcion = int(input("Introduce el número de la opción que quieres ejecutar: "))
    print()
if opcion == 0:
    print()
    print("¡Hasta luego!")