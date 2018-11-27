import random                       #Importo librerias y declaro mis variables.
import sys
Arreglo = []
eleccion=0

def Revolver():                 #Metodo para para crear el arreglo aleatorio del 0 al 100 de 99 valores.
    for x in range(0,100,1):
        Arreglo.insert(x,random.randint(0,100))     #Inserto en el arreglo un valor aleatorio del 0 al 100, 99 veces.
        
def Ordenar(distancia):             #Metodo para ordenar los valores del arreglo.
    if distancia >= 1:              #El programa funciona con recursividad asi que recibe una distancia que es la longitud del arreglo entre 2.
        for cont in range(len(Arreglo)-distancia):    #Con dicha distancia entra a 2 ciclos donde el primero se encarga de saber cuantas veces
            for cont2 in range(cont,(len(Arreglo)-distancia),distancia):#va a hacer los saltos en el arreglo y el segundo es para comparar
                if (Arreglo[cont2] > Arreglo[distancia+cont2]):         #un valor en cuestion con el que esta al salto de la distancia.
                    copia = Arreglo[distancia+cont2]                    #Si el valor es mayor al valor que esta en el salto de la distancia
                    Arreglo[distancia+cont2] = Arreglo[cont2]           #creo un copia del segundo valor, el nuevo valor del segundo sera el
                    Arreglo[cont2] = copia                              #primero, y el nuevo valor del primero sera la copia en cuestion.
        else:
            return Ordenar(distancia//2)                                #Despues vuelve a entrar al metodo enviandole una nueva distancia que es
    else:                                                               #la anterior dividida entre 2.
        return Arreglo                                                  #Cuando el tamanio de la distancia sea igual a 1, termina el proceso y 
                                                                        #returna el arreglo ordenado.
    
def BusquedaBinaria(Arreglo):                               #Metodo para ordenar mediante el procedimiento binario.
    global eleccion
    ArregloNuevo = []                                       #Creo un arreglo nuevo vacio cada vez.
    pivote = Arreglo[len(Arreglo)//2]                       #Tomo un valor pivote que sera el valor centrar del arreglo en cuestion.
    if eleccion == pivote:                                  #SI el valor buscado es igual al valor central, regreso la posicion en la este esta.
        return len(Arreglo)//2
    elif len(Arreglo)<=1:                                   #Si no, comparo que si el valor del arreglo es menor o igual a 1 significa que ya
        return-1                                            #dividio y dividio el arreglo y no encontro el valor deseado.
    elif eleccion < pivote:                                 #Si el valor es menor al pivote significa que se encuentra a la izquierda del pivote
        for cont in range(len(Arreglo)//2):                 #el valor buscado, entonces en el arreglo nuevo meto todos los valores inferiores
            ArregloNuevo.append(Arreglo[cont])              #al pivote y vuelvo a llamar al metodo enviandole este arreglo reducido.
        print(ArregloNuevo)
        return BusquedaBinaria(ArregloNuevo)
    elif eleccion > pivote:                                 #SI el valor es mayor al pivote significa que se encuentra a la derecha del pivote
        for cont in range(len(Arreglo)//2,len(Arreglo),1):  #el valor buscado, entonces en el arreglo nuevo meto todos los valores superiores
            ArregloNuevo.append(Arreglo[cont])              #al pivote y vuelvo a llamar al metodo enviandole este arreglo reducido.
        print(ArregloNuevo)
        return BusquedaBinaria(ArregloNuevo)                #Todo esto se repite hasta que se encuentre el valor o la longitud del arreglo sea 1.
    
def Menu():                                     #Menu...
    global eleccion
    eleccion = str(input("\nIngrese el numero a buscar en el arreglo, "
           "\no teclee 'X' para salir del programa: "))
    if eleccion == "X" or eleccion =="x":           #SI presiona X el usuario cierro el programa.
        sys.exit()                                  #Metodo reservado del programa para cerrar el programa.
    else:
        print("\nComportamiento de la busqueda...")
        eleccion = int(eleccion)                    #El valor que ingresa el usuario me aseguro que sea entero asi que lo convierto.
        posicion = BusquedaBinaria(Arreglo)         #Llamo al metodo para buscar y le envio el Arreglo, y recibo la posicion en que se
        if posicion == -1:                          #encontro el valor. Si retorna -1 significa que no se encontro en el arreglo.
            print("\nValor no encontrado en el arreglo...")
        else:
            print("\nEl valor "+str(eleccion)+""
                  " se encuentra en la posicion "+str(posicion)+""  #Imprimo la posicion en que se encontro el valor.
                  " del ultimo sub-arreglo.")
        print()
        Menu()
        
print("Arreglo de 100 elementos con un intervalo de 0 a 100 creado aleatoriamente, ordenado...\n")
Revolver()                                      #Llamo al metodo para crear el arreglo aleatorio.
Arreglo = Ordenar(len(Arreglo)//2)              #Llamo a este metodo que es el SHELLSORT para ordenar el arreglo ya que se requiere.
Arreglo = Ordenar(1)
print(Arreglo)                                  #Imprimo el arreglo para que el usuario pueda ver que valores puede buscar.
Menu()
    
