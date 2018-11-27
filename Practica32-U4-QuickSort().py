import random               #Importo la libreria y declaro mis variables.
QuickSort = []

def Revolver():                                 #Metodo para para crear el arreglo aleatorio del 0 al 100 de 99 valores.
    for x in range(0,100,1):
        QuickSort.insert(x,random.randint(0,100))   #Inserto en el arreglo un valor aleatorio del 0 al 100, 99 veces.

def Ordenar(Arreglo):                           #Metodo para ordenar los valores del arreglo.
    arreglomenores = []
    arreglomayores = []                         #Declaro e inicializo mis variables.
    arreglopivotes = []
    
    if len(Arreglo) > 1:                        #Si la longitud del arreglo es mayor a 1 va a hacer el procedimiento,
        pivote = Arreglo[0]                     #que es tomar un valor pivote, en este caso el primer valor del arreglo.
        for valor in Arreglo:                   #En este ciclo, por cada valor del Arreglo...
            if valor == pivote:                 #Compara si el valor pivote es igual al valor del arreglo,
                arreglopivotes.append(valor)    #Si lo es agrega a un nuevo arreglo dicho valor.
            if valor < pivote:                  #Compara si el valor pivote es menor al valor del arreglo,
                arreglomenores.append(valor)    #Si lo es, agrega a un nuevo arreglo dicho valor.
            if valor > pivote:                  #Compara si el valor pivote es mayor al valor del arreglo,
                arreglomayores.append(valor)    #SI lo es, agrega a un nuevo arreglo dicho valor.
        return Ordenar(arreglomenores)+arreglopivotes+Ordenar(arreglomayores)   #Al terminar, vuelvo a llamar al metodo
    else:                                                                       #enviandole un arreglo anidado de los
        return Arreglo                                                          #anteriores en orden, y asi hasta
                                                                                #que la longitud del arreglo sea 1.
Revolver()                                      #LLamo al metodo para crear el arreglo primero.
print("Arreglo de 100 elementos creado aleatoriamente...\n"+str(QuickSort))
QuickSort = Ordenar(QuickSort)                  #LLamo al metodo para ordenar el arreglo y se lo mando
print("\nArreglo anterior ordenado por el metodo de QuickSort..\n"+str(QuickSort))  #y lo recibo ya ordenado.


