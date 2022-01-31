lista = []
menu = "1. Añadir número a la lista\n2. Añadir número a la lista en una posición\n3. Longitud de la lista\n4. Eliminar el último número\n5. Elimina un número\n6. Contar números\n7. Posiciones de un número\n8. Mostrar números\n9. Salir"
print(menu)
opcion = int(input(("Introduzca un número del menú para elegir una opción: ")))
while opcion != 9:
    if opcion == 1:
        numero = int(input("Dime un número: "))
        lista.append(numero)
    elif opcion == 2:
        numero = int(input("Dime un número: "))
        posicion = int(input("Dime una posición en la cadena para el número(mínimo 1): "))
        while posicion <= 0:
            print("Error. Debe introducir a partir de 1.")
            posicion = int(input("Dime una posición en la cadena para el número(mínimo 1): "))
        if posicion < len(lista):
            lista.insert(posicion-1,numero)
            print()
        else:
            lista.append(numero)
            print()
    elif opcion == 3:
        print("La lista tiene %d elementos."%(len(lista)))
        print()
    elif opcion == 4:
        print("Se ha eliminado el elemento %d."%(lista.pop()))
        print()
    elif opcion == 5:
        posicion = int(input("Dime una posición a borrar de la lista (mínimo 1): "))
        while posicion <= 0:
            print("Error. Debe introducir a partir de 1.")
            posicion = int(input("Dime una posición a borrar de la lista (mínimo 1): "))
        if posicion < len(lista):
            lista.pop(posicion-1)
            print()
    elif opcion == 6:
        numero = int(input("Dime un número: "))
        print("El número %d aparece %d veces."%(numero,lista.count(numero)))
        print()
    elif opcion == 7:
        numero = int(input("Dime un número: "))
        if numero in lista: 
            print("Está en las posiciones: ",end="")
            for posicion in range(0,len(lista)):
                if lista[posicion] == numero:
                    print(posicion+1,end=" ")
            print()
        else:
            print("El número no se encuentra en ninguna posición.")
            print()
    elif opcion == 8:
        print("La lista actualmente es la siguiente:")
        for elemento in lista:
            print(elemento,end=" ")
        print()
    else:
        print("Opción inválida.")
        print()
    print(menu)
    opcion = int(input(("Introduzca un número del menú para elegir una opción: ")))