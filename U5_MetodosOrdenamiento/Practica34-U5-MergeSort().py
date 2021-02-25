import random                   #Importo la libreria y declaro mis variables.
MergeSort = []

def Revolver():                                         #Metodo para para crear el arreglo aleatorio del 0 al 100 de 99 valores.
    for x in range(0,100,1):
        MergeSort.insert(x,random.randint(0,100))       #Inserto en el arreglo un valor aleatorio del 0 al 100, 99 veces.
        
def Ordenar(distancia):                                     #Metodo para ordenar los valores del arreglo.
    global MergeSort                                        #El arreglo lo declaro global para usar su valor dentro del metodo.
    if distancia//2<=len(MergeSort)+1:                      #Si la distancia entre 2 es menor o igual a la longitud del arreglo hara el proceso.
        bandera = True                                      #La distancia es la longitud de los mini arreglos que se forman durante el programa.
        Arreglo = MergeSort[:]                              #Creo un clon del arreglo a ordenar pero sin dejar referencias para no editar este.
        for cont in range(0,len(MergeSort)-1,distancia):    #Este ciclo se hara tantas veces la distancia quepa en el tamanio del arreglo.
            bandera = True
            bandera2 = True                                 #Declaro e inicializo mis variables necesarias.
            bandera3 = True
            indleft = cont                                  #Utilizo 2 punteros para comparar los valores, uno inicia donde inicia el ciclo y el
            indright = cont + distancia//2                  #otro inicia donde inicie el anterior puntero mas la distancia entre 2.
            if indright >=len(MergeSort):                   #Si el puntero de la derecha llega al tope del arreglo, no inicia el ciclo que sigue.
                bandera = False
            dondempezoleft = indleft                        #Estas dos variables las utilizo como banderas para saber donde inicio a compararse
            dondempezoright = indright                      #los valores y de esta manera cuando el indleft llegue al tope donde inicio el indleft
            while bandera:                                  #significa que se deja de comparar y termina el ciclo.
                if (MergeSort[indleft] >= MergeSort[indright]): #Si el valor de la izquierda es mayor o igual que el de la derecha,
                    Arreglo[cont] = MergeSort[indright]         #en un nuevo arreglo agrego el valor que es menor y el indice donde estaba y lo
                    indright = indright + 1                     #aumento en 1.
                    if indright>=len(MergeSort):                #Si el puntero derecho llega al tope del arreglo, lo posiciono donde debe terminar
                        indright = dondempezoright+distancia//2 #para terminar el ciclo.
                elif (MergeSort[indleft] < MergeSort[indright]):#SI el valor de la izquierda es menor que el de la derecha,
                    Arreglo[cont] = MergeSort[indleft]          #en un nuevo arreglo agrego el valor que es menor y el indice donde estaba y lo
                    indleft = indleft + 1                       #aumento en 1.
                if (indright>=dondempezoright+distancia//2):    #Si el puntero derecho llega a donde debe terminar que es donde empezo mas la   
                    while(bandera2):                            #distancia entre 2, entro a un ciclo que se encarga de meter en el nuevo arreglo
                        cont=cont+1                             #todos los valores faltantes de la izquierda ya que la derecha llego al tope.
                        Arreglo[cont] = MergeSort[indleft]
                        indleft = indleft+1
                        if(indleft>=dondempezoleft+distancia//2):   #Si el puntero izquierdo llega a donde debe terminar que es donde empezo el 
                            bandera2 = False                        #puntero de la derecha basicamente, termino el este ciclo y el otro tambien.
                            bandera = False
                elif(indleft>=dondempezoleft+distancia//2):     #Si el puntero izquierdo llega a donde debe terminar que es donde emepzo mas la 
                    while(bandera3):                            #distancia entre 2, entro a un ciclo que se encarga de meter en el nuevo arreglo
                        cont=cont+1                             #todos los valores faltantes de la derecha ya que la izquierda llego al tope.
                        Arreglo[cont] = MergeSort[indright]
                        indright = indright+1
                        if(indright>=dondempezoright+distancia//2) or (indright>=len(MergeSort)):   #Si el puntero derecho llega a donde debe
                            bandera3 = False                                    #de terminar que es cuando llega a donde empezo mas la distancia
                            bandera = False                                     #entre 2 O cuando el indice derecho llega al tope del arreglo
                cont=cont+1                                                     #termino el ciclo y el otro tambien.
        MergeSort = Arreglo[:]                  #Al final de las comparaciones el arreglo lo igualo al que acabo de ordenar sin dejar referencia,
        return Ordenar(distancia*2)             #para eso el [:].  Posterirmente vuelvo a llamar al metodo con la distancia duplicada.
    else:                                       #Todo esto lo hara hasta que la distancia entre 2 sea mas grande que el tamanio del arreglo.
        return -1
            
        
Revolver()                                      #Llamo al metodo para crear el arreglo aleatorio.
print("Arreglo de 100 elementos creado aleatoriamente...\n"+str(MergeSort))
Ordenar(2)                                      #Llamo al metodo para ordenar enviandole por primera vez una distancia de 2.
print("\nArreglo anterior ordenado por el metodo de MergeSort..\n"+str(MergeSort))
