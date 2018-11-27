import random               #Importo librerias y declaro mis variables.
import sys
Arreglo = []

def Revolver():                 #Metodo para para crear el arreglo aleatorio del 0 al 100 de 99 valores.
    for x in range(0,100,1):
        Arreglo.insert(x,random.randint(0,100))     #Inserto en el arreglo un valor aleatorio del 0 al 100, 99 veces.

def Menu():                     #Menu...
    eleccion = str(input("\nIngrese el numero a buscar en el arreglo, "
           "\no teclee 'X' para salir del programa: "))
    if eleccion == "X" or eleccion =="x":   #SI presiona X el usuario cierro el programa.
        sys.exit()                      #Metodo reservado del programa para cerrar el programa.
    else:
        eleccion = int(eleccion)        #el valor que ingresa el usuario me aseguro que sea entero asi que lo convierto,
        encontrado = [cont for cont,x in enumerate(Arreglo) if x == eleccion]   #despues utilizo este ciclo en un arreglo para ver
        if len(encontrado) ==0:                                                 #en que posiciones del arreglo se encuentra el 
            print("\nValor no encontrado en el arreglo...")                     #valor que el usuario ingreso.
        else:
            print("\nEl valor "+str(eleccion)+""                                #Imprimo las posiciones donde se encontro.
                  " se encuentra en la/s posiciones "+str(encontrado)+""
                  " del arreglo.")
        print()
        Menu()
print("Arreglo de 100 elementos con un intervalo de 0 a 99 creado aleatoriamente...\n")
Revolver()                                              #Llamo al metodo para crear el arreglo aleatorio.
print(Arreglo)                                          #Imprimo el arreglo para que el usario vea que valores puede buscar.
Menu()              #Llamo por primera vez al metodo para iniciar la recursividad.
    
