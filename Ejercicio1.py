lista = []
pregunta = int(input("Número de cadenas que quiere introducir: "))
while pregunta < 1:
    print("Error. El número de cadenas debe ser al menos 1.")
    pregunta = int(input("Número de cadenas: "))
while pregunta > 0:
    cadena = (input("Introduce la cadena: "))
    lista.append(cadena)
    pregunta = pregunta -1
subcad = (input("Introduzca la subcadena: "))
while subcad in lista:
    lista.remove(subcad)
    funciona = True
if funciona:
    for cadena in lista:
        print(cadena,end=" ")    
    print()
else:
    print("La subcadena no estaba en la lista.")