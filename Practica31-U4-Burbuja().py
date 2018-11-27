import random               #Importo la libreria y declaro mis variables.
Burbuja = []

def Revolver():                                     #Metodo para para crear el arreglo aleatorio del 0 al 100 de 99 valores.
    for x in range(0,100,1):                
        Burbuja.insert(x,random.randint(0,100))     #Inserto en el arreglo un valor aleatorio del 0 al 100, 99 veces.

def Ordenar():                                              #Metodo para ordenar el arreglo mediante la burbuja.
    for pivote in range(1,len(Burbuja),1):                  #Son dos ciclos anidados porque se evalua un valor con todos los del arreglo.
        for indice in range(0,len(Burbuja)-1,1):            #EL primer ciclo inicia en la posicion 0 y el segundo en el sig valor.
            if (Burbuja[pivote] <= Burbuja[indice]):        #SI el valor es menor al siguiente, creo una copia del menor, en la posicion del menor
                copia = Burbuja[pivote]                     #coloco el otro valor y por ultimo en la posicion del otro valor coloco la copia.
                Burbuja[pivote] = Burbuja[indice]
                Burbuja[indice] = copia
print ("Arreglo de 100 elementos creado aleatoriamente revuelto...\n")
Revolver()                                                  #LLamo al metodo para crear el arreglo primero.
print (Burbuja)
print ("\nArreglo anterior ordenado por el metodo de la burbuja...\n")
Ordenar()                                                   #LLamo al metodo para ordenar el arreglo.
print(Burbuja)
        
