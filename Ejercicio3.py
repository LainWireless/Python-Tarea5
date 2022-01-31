temperaturas='''Utrera,29,12
Dos Hermanas,32,14
Sevilla,30,15
Alcalá de Guadaíra,31,14
Madrid,35,0
Palencia,33,4
Murcia,25,7
Teruel,20,0
'''
lista1 = []
lista2 = []
lista1 = temperaturas.splitlines()
nombrelista = False
for elem in lista1:
    temp = elem.split(",")
    lista2.append(temp)
for elemento in lista2:
    elemento[1] = int(elemento[1])
    elemento[2] = int(elemento[2])
for elementos in lista2:
    print("%s tiene una temperatura media al año de %.2f ºC"%(elementos[0],(elementos[1]+elementos[2])/2))
nombre = input("Escriba uno de los lugares de la lista: ")
for elementos in lista2:
    if elementos[0]==nombre:
        print("La temperatura máxima en %s es de %d ºC y la mínima de %d ºC"%(elementos[0],elementos[1],elementos[2]))
        nombrelista = True
if not nombrelista:
    print("Error, el nombre no estaba en la lista.")