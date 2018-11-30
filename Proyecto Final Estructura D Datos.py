#PROYECTO FINAL DE ESTRUCTURA DE DATOS          Morgado Jacome Eduardo #17211545
#PROGRAMA QUE EVALUA UN ARREGLO DESORDENADO DE 1000 ELEMENTOS DE UN INTERVALO DE 0 A 1000 Y SE ORDENA CON DIFERENTES METODOS DE
#ORDENAMIENTO LOS CUALES SERAN      burbuja     quicksort   shellsort   y   mergesort.

import random               #Importo las librerias que necesito y declaro mis arreglos que guardaran el arreglo desordeando.
import sys
import time
Burbuja = []
QuickSort = []
ShellSort = []
MergeSort = []

def Revolver():                                     #Metodo para para crear un arreglo aleatorio del 0 al 1000 de 1000 valores.
    ArregloRevuelto = []
    for x in range(0,1000,1):                
        ArregloRevuelto.insert(x,random.randint(0,1000))     #Inserto en el arreglo un valor aleatorio del 0 al 1000, 1000 veces.
    return ArregloRevuelto

def OrdenarBurbuja():                                              #Metodo para ordenar el arreglo mediante la burbuja.
    for pivote in range(1,len(Burbuja),1):                  #Son dos ciclos anidados porque se evalua un valor con todos los del arreglo.
        for indice in range(0,len(Burbuja)-1,1):            #EL primer ciclo inicia en la posicion 0 y el segundo en el sig valor.
            if (Burbuja[pivote] <= Burbuja[indice]):        #SI el valor es menor al siguiente, creo una copia del menor, en la posicion del menor
                copia = Burbuja[pivote]                     #coloco el otro valor y por ultimo en la posicion del otro valor coloco la copia.
                Burbuja[pivote] = Burbuja[indice]
                Burbuja[indice] = copia



def OrdenarQuickSort(Arreglo):                           #Metodo para ordenar los valores del arreglo.
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
        return OrdenarQuickSort(arreglomenores)+arreglopivotes+OrdenarQuickSort(arreglomayores)   #Al terminar, vuelvo a llamar al metodo
    else:                                                                       #enviandole un arreglo anidado de los
        return Arreglo                                                          #anteriores en orden, y asi hasta
                                                                                #que la longitud del arreglo sea 1.



def OrdenarShellSort(distancia):             #Metodo para ordenar los valores del arreglo.
    if distancia >= 1:              #El programa funciona con recursividad asi que recibe una distancia que es la longitud del arreglo entre 2.
        for cont in range(len(ShellSort)-distancia):    #Con dicha distancia entra a 2 ciclos donde el primero se encarga de saber cuantas veces
            for cont2 in range(cont,(len(ShellSort)-distancia),distancia):  #va a hacer los saltos en el arreglo y el segundo es para comparar
                if (ShellSort[cont2] > ShellSort[distancia+cont2]):         #un valor en cuestion con el que esta al salto de la distancia.
                    copia = ShellSort[distancia+cont2]                      #Si el valor es mayor al valor que esta en el salto de la distancia
                    ShellSort[distancia+cont2] = ShellSort[cont2]           #creo un copia del segundo valor, el nuevo valor del segundo sera el
                    ShellSort[cont2] = copia                                #primero, y el nuevo valor del primero sera la copia en cuestion.
        else:
            return OrdenarShellSort(distancia//2)                           #Despues vuelve a entrar al metodo enviandole una nueva distancia que es
    else:                                                                   #la anterior dividida entre 2.
        return ShellSort                                                    #Cuando el tamanio de la distancia sea igual a 1, termina el proceso y 
                                                                            #returna el arreglo ordenado.


        
def OrdenarMergeSort(distancia):                                     #Metodo para ordenar los valores del arreglo.
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
        return OrdenarMergeSort(distancia*2)             #para eso el [:].  Posterirmente vuelvo a llamar al metodo con la distancia duplicada.
    else:                                       #Todo esto lo hara hasta que la distancia entre 2 sea mas grande que el tamanio del arreglo.
        return -1
            
def OrdenamientoTotal():
    global Burbuja                                  #Llamo a los arreglos para utilizarlos dentro del metodo.
    global QuickSort
    global ShellSort
    global MergeSort
    ArregloTiempos =[]
    print ("Arreglo de 1000 elementos creado aleatoriamente...\n")
    Burbuja = Revolver()                #LLamo una sola vez al arreglo que me crea un arreglo de 100 elementos aleatorio.
    print(Burbuja)
    QuickSort = Burbuja[:]              #Lo que hago aqui es una copia del arreglo desordenado en cada arreglo para cada metodo sin dejar referencia 
    ShellSort = Burbuja[:]              #del uno del otro para evitar si edito uno se cambie el otro.
    MergeSort = Burbuja[:]

    
    print ("\nArreglo revuelto ordenado por el metodo de la burbuja...")
    empezartiempo = time.time()                             #Esta variable empieza a contabilizar el tiempo.
    OrdenarBurbuja()                                                   #LLamo al metodo para ordenar el arreglo.
    print(Burbuja)
    tiempoburbuja = time.time() - empezartiempo             #Esta variable guarda la diferencia entre el tiempo transcurrido menos el iniciado.
    print("|-|-|-|-| Este metodo de ordenamiento tardo "+ str(tiempoburbuja)+" segundos. |-|-|-|-|")
    ArregloTiempos.append(tiempoburbuja)                #Agreso a un arreglo el tiempo que hizo el metodo.
    

    empezartiempo = time.time()                             #Esta variable empieza a contabilizar el tiempo.
    QuickSort = OrdenarQuickSort(QuickSort)                  #LLamo al metodo para ordenar el arreglo y se lo mando
    print("\nArreglo revuelto ordenado por el metodo de QuickSort...\n"+str(QuickSort))  #y lo recibo ya ordenado.
    tiempoquicksort = time.time() - empezartiempo           #Esta variable guarda la diferencia entre el tiempo transcurrido menos el iniciado.
    print("|-|-|-|-| Este metodo de ordenamiento tardo "+ str(tiempoquicksort)+" segundos. |-|-|-|-|")
    ArregloTiempos.append(tiempoquicksort)              #Agreso a un arreglo el tiempo que hizo el metodo.

    empezartiempo = time.time()                             #Esta variable empieza a contabilizar el tiempo.
    ShellSort = OrdenarShellSort(len(ShellSort)//2)                      #LLamo al metodo enviandole la distancia del arreglo entre 2 y recibo elarreglo.
    ShellSort = OrdenarShellSort(1)                                      #Al final se le vuelve a hacer una pasada al arreglo con la distancia en 1,  
    print("\nArreglo revuelto ordenado por el metodo de ShellSort...\n"+str(ShellSort))  #ya que el metodo lo necesita para asegurar que quedo ordenado.
    tiemposhellsort = time.time() - empezartiempo           #Esta variable guarda la diferencia entre el tiempo transcurrido menos el iniciado.
    print("|-|-|-|-| Este metodo de ordenamiento tardo "+ str(tiemposhellsort)+" segundos. |-|-|-|-|")
    ArregloTiempos.append(tiemposhellsort)              #Agreso a un arreglo el tiempo que hizo el metodo.

    empezartiempo = time.time()                             #Esta variable empieza a contabilizar el tiempo.
    OrdenarMergeSort(2)                                      #Llamo al metodo para ordenar enviandole por primera vez una distancia de 2.
    print("\nArreglo revuelto ordenado por el metodo de MergeSort...\n"+str(MergeSort)) #EL 2 representa el tamanio de los subarreglos, se empieza en 2
    tiempomergesort = time.time() - empezartiempo                                    #y aumento cuadraticamente para los siguientes subarreglos.
    print("|-|-|-|-| Este metodo de ordenamiento tardo "+ str(tiempomergesort)+" segundos. |-|-|-|-|")
    ArregloTiempos.append(tiempomergesort)              #Agreso a un arreglo el tiempo que hizo el metodo.
    
                                                            

    print("\n|-|-|-|-| Total de tiempo ejecutado: "+str(tiempoburbuja+tiempoquicksort+tiemposhellsort+tiempomergesort)+" segundos. |-|-|-|-|")
    return ArregloTiempos

def Estadistica():                              #Metodo que realiza la estadistica de los ordenamientos.
    ArregloTiempos = []
    ArregloProvisional = []                     #Utilizo un arreglo para guardar todos los tiempos obtenidos y otro para pasarlos de uno a otro,
    cont=0
    Acumtiempoburbuja = 0
    Acumtiempoquicksort = 0
    Acumtiemposhellsort = 0
    Acumtiempomergesort = 0
    for x in range(30):                                 #Este ciclo llamo al ordenamiento 30 veces y me regresa cada vez un arreglo con 4 valores,
        ArregloProvisional = OrdenamientoTotal()        #que son los tiempos de los metodos de ordenamiento.
        for x in range(len(ArregloProvisional)):        #Este ciclo agrega los valores obtenidos en el ciclo anterior a un arreglo general que los tendra.
            ArregloTiempos.append(ArregloProvisional[x])
    print("\nLa siguiente tabla muestra el tiempo que tardo en segundos cada metodo en ordenar un arreglo aleatorio de 1000 elementos...\n")
    print('{:^25}{:^25}{:^25}{:^25}{:^25}'.format('|# Arreglo|','|Burbuja|','|QuickSort|','|ShellSort|','|MergeSort|')) #Utilizo este formato para
    for x in range(0,len(ArregloTiempos),4):                                                #imprimir como un tabla, este es el encabezado.
        cont = cont+1                                   #Este ciclo se encargara de imprimir todos los tiempos del arreglo.
        print('{:^25}{:^25.8f}{:^25.8f}{:^25.8f}{:^25.8f}'.format(cont,ArregloTiempos[x],ArregloTiempos[x+1],ArregloTiempos[x+2],ArregloTiempos[x+3]))
        Acumtiempoburbuja = Acumtiempoburbuja + ArregloTiempos[x]
        Acumtiempoquicksort = Acumtiempoquicksort + ArregloTiempos[x+1]         #Aqui agrego a un acumulador los tiempos para sacar promedio.
        Acumtiemposhellsort = Acumtiemposhellsort + ArregloTiempos[x+2]
        Acumtiempomergesort = Acumtiempomergesort + ArregloTiempos[x+3]

    print("\nPromedio de tiempo que demoran en ejecutar los metodos de ordenamiento en un arreglo de 1000 elementos: ")
    print("Burbuja = "+str(Acumtiempoburbuja/30))
    print("QuickSort = "+str(Acumtiempoquicksort/30))               #Imprimo el promedio de los tiempos de ejecucion de los metodos.
    print("ShellSort = "+str(Acumtiemposhellsort/30))
    print("MergeSort = "+str(Acumtiempomergesort/30))

def Menu():
    print("\n\n1.- Probar denuevo (1 nuevo arreglo desordenado)."         #Menu...
          "\n2.- Probar 30 arreglos y generar estadistica."
          "\n2.- Salir.")
    eleccion = input("Que desea realizar?: ")
    if eleccion.isdigit():                  #Compruebo si esta ingresando un digito como valor.
        if eleccion == "1":                 #Si eligio esta opcion es para hacer una sola vez el ordenamiento del arreglo.
            OrdenamientoTotal()
            Menu()
        elif eleccion =="2":                #Si eligio esta opcion es para hacer 30 veces los ordenamientos y asi hacer una estadistica.
            Estadistica()
            Menu()
        elif eleccion =="3":                #Opcion para salir, llamo al metodo reservado sys.exit()
            sys.exit()
        else:
            print("\nOpcion incorrecta...")
            Menu()
    else:
        print("\nOpcion incorrecta...")
        Menu()

OrdenamientoTotal()                         #Llamo un vez al Ordenamiento para mostrarlo al usuario y luego Menu() para iniciar recursividad.
Menu()
