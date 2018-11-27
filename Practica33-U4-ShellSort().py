import random                       #Importo la libreria y declaro mis variables.
ShellSort = []

def Revolver():                             #Metodo para para crear el arreglo aleatorio del 0 al 100 de 99 valores.
    for x in range(0,100,1):
        ShellSort.insert(x,random.randint(0,100))   #Inserto en el arreglo un valor aleatorio del 0 al 100, 99 veces.

def Ordenar(distancia):             #Metodo para ordenar los valores del arreglo.
    if distancia >= 1:              #El programa funciona con recursividad asi que recibe una distancia que es la longitud del arreglo entre 2.
        for cont in range(len(ShellSort)-distancia):    #Con dicha distancia entra a 2 ciclos donde el primero se encarga de saber cuantas veces
            for cont2 in range(cont,(len(ShellSort)-distancia),distancia):  #va a hacer los saltos en el arreglo y el segundo es para comparar
                if (ShellSort[cont2] > ShellSort[distancia+cont2]):         #un valor en cuestion con el que esta al salto de la distancia.
                    copia = ShellSort[distancia+cont2]                      #Si el valor es mayor al valor que esta en el salto de la distancia
                    ShellSort[distancia+cont2] = ShellSort[cont2]           #creo un copia del segundo valor, el nuevo valor del segundo sera el
                    ShellSort[cont2] = copia                                #primero, y el nuevo valor del primero sera la copia en cuestion.
        else:
            return Ordenar(distancia//2)                                    #Despues vuelve a entrar al metodo enviandole una nueva distancia que es
    else:                                                                   #la anterior dividida entre 2.
        return ShellSort                                                    #Cuando el tamanio de la distancia sea igual a 1, termina el proceso y 
                                                                            #returna el arreglo ordenado.

Revolver()                                                  #Llamo al metodo para crear el arreglo aleatorio.
print("Arreglo de 100 elementos creado aleatoriamente...\n"+str(ShellSort))
ShellSort = Ordenar(len(ShellSort)//2)                      #LLamo al metodo enviandole la distancia del arreglo entre 2 y recibo el arreglo.
ShellSort = Ordenar(1)                                      #Al final se le vuelve a hacer una pasada al arreglo con la distancia en 1, ya que el 
print("\nArreglo anterior ordenado por el metodo de ShellSort..\n"+str(ShellSort))  #metodo lo necesita para asegurar que quedo ordenado.
