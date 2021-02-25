import sys

class Nodo():                           #Esta clase crea los Nodos de la lista con 2 atributos, el valor y el enlace vacio.
    def __init__(self,datos):
        self.datos = datos
        self.siguiente = None

def Enlazar():                              #Este metodo se encarga de enlazar los nodos que se vayan creando.
    global raiz
    bandera = True                          #Declaro e inicializo mis variables.
    q=raiz
    while (bandera):                        #Este ciclo lo utilizo para posiconar los punteros al final de la lista.
        if q.siguiente == None:
            bandera = False
        else:
            p = q.siguiente
            q=p                                             #Ya que llegue al final de la lista, creo el Nodo y lo enzalo con los punteros.
    p=Nodo(str(input("Ingrese el elemento a enlazar: ")))
    q.siguiente = p
    q=p

def Peek(eleccion):                                         #Este metodo se encarga de mostrar nodos de la lista enlazada.
    global raiz
    bandera = True                                          #Declaro e inicializo mis variables.
    q=raiz
    p=raiz
    if eleccion == "T":                                     #Si eligio esta opcion, entro a un ciclo para mostrar cada Nodo de la lista.
        while (bandera):
            print(q.datos)                                  #Imprimo el valor del nodo en el que estoy.
            if q.siguiente == None:                         #Si su atributo de enlaze es Nulo significa que llegue al final de la lista y termino el ciclo.
                bandera = False
            else:                                           #Si no, avanzo al siguiente nodo con ayuda de los punteros.
                p = q.siguiente                             #Muevo un puntero al sig nodo que esta en el enlace y luego muevo el otro puntero a este nodo.
                q=p
    elif eleccion == "U":                                   #Si eligio esta opcion utilizo exactamente el ciclo anterior solo que solo imprimo el ultimo
        while (bandera):                                    #nodo en el que se quedaron los punteros al salir del ciclo.
            if q.siguiente == None:
                bandera = False
            else:
                p = q.siguiente
                q=p
        print("Ultimo valor de la lista: "+ p.datos+"\n")
    elif eleccion == "R":                                   #SI eligio esta opcion es para imprimir la raiz.
        print("La raiz es: "+p.datos+"\n")
    else:                                                   #Si no fue ninguno de los anteriores significa que esta buscando un nodo por su valor.
        contador=0
        while (bandera):                                    #Para esto utilizo el mismo ciclo anterior para moverme a traves de toda la lista y me detengo
            if eleccion == q.datos:                         #hasta que encuentro el valor deseado o hasta que llegue al final de la lista sin encontrarlo.
                print("El dato "+str(eleccion)+" se encuentra en el nodo "+str(contador)+" de la lista...") #Encontro el valor en la lista.
                bandera = False
            if q.siguiente == None:
                print("El dato "+str(eleccion)+" no existe en la lista...")         #NO encontro el valor en la lista.
                bandera = False
            else:
                contador=contador+1
                p = q.siguiente
                q=p
    print()
    
def Pop(eleccion):                                          #Metodo para eliminar Nodos de la lista.
    global raiz
    q=raiz                                                  #Declaro e inicializo mis variables.
    p=raiz
    bandera = True
    if(raiz.siguiente == None):                             #Si la raiz no tiene enlaces significa que esta sola, por lo tanto no puede eliminarse mas.
            print("No puede eliminar mas ya que solo existe la raiz en la lista...")
    elif eleccion == "A":                                   #En caso de que eligio esta opcion, elimina el ultimo nodo creado.
        while (bandera):                                    #Con este ciclo me posiciono al final de la lista.
            if q.siguiente.siguiente == None:               #Si el enlace del sig Nodo en el que estoy es Nulo, significa que llegue al final de la lista.
                p = q.siguiente                             #Muevo un solo puntero al que quiero eliminar.
                q.siguiente = None                          #Termino el enlace que existe con dicho Nodo...            
                print("Nodo con el dato "+p.datos+" eliminado...")
                del p                                       #Y por ultimo elimino el Nodo.
                bandera = False
            else:                                           #En caso contrario avanzo al sig nodo de la lista...
                p = q.siguiente
                q=p
    elif eleccion == "B":                                   #SI eligio esta opcion es para eliminar y recorrer la raiz.
        if(raiz.siguiente == None):
            print("No puede eliminar mas ya que solo existe la raiz en la lista...")
        else:
            p = raiz.siguiente                              #Coloco un puntero al enlace de la raiz actual,
            raiz = p                                        #Muevo la variable raiz a este nodo que le seguia.
            print("Nueva raiz: "+raiz.datos)
            del q                                           #Elimino la raiz que estaba anterior.
    else:                                                   #SI no es ninguna de las anteriores, es porque esta buscando un NOdo en base a su valor.
        while (bandera):                                    #Utilizo este ciclo para moverme en toda la lista, se detiene hasta que encuentre el valor
            if q.siguiente.datos == eleccion:               #o llegue al final de la lista. Si el Nodo sig al que estoy es el que quiero eliminar...
                p= q.siguiente                              #Muevo un solo puntero al que quiero eliminar,
                q.siguiente = p.siguiente                   #Creo un enlace con el nodo en el que esta antes del que quiero eliminar con el sig del que
                del p                                       #quiero eliminar, finalmente elimino el Nodo en el que estoy.
                print("El dato "+str(eleccion)+" se ha eliminado de la lista...")
                bandera = False
            elif q.siguiente == None:                       
                print("El dato "+str(eleccion)+" no existe en la lista...") #Si no encontro al nodo en la lista...
                bandera = False
            else:                                           #En caso contrario avanzo al sig nodo de la lista...
                p = q.siguiente
                q=p
    print() 
        
def Menu():                                                         #Menu...
    print ("1.- Crear y enlazar nodo.\n"
           "2.- Mostrar los nodos.\n"   
           "3.- Eliminar nodo.\n"
           "4.- Salir.")
    eleccion = int(input("Que desea realizar?: "))
    if eleccion ==1:
        Enlazar()                                                   #Si eligio esta opcion llamo al metodo enlazar.
        print("\nElemento creado y enlazado...\n")
        Menu()
    elif eleccion ==2:
        eleccion = str(input("\nTeclee 'T' para mostrar TODA la lista,\n"                   #SI eligio esta opcion es para mostar los valores de la lista.
                                         "teclee 'U' para mostrar el ULTIMO nodo,\n"
                                         "teclee 'R' para mostrar la RAIZ,\n"
                                         "o ingrese el valor que desea buscar en la lista: "))
        print()
        Peek(eleccion)                                              #Mando a llamar al metodo Peek con la opcion elegida por el usuario.
        Menu()
    elif eleccion ==3:                                                          #Si eligio esta opcion es para eliminar nodos de la lista.
        eleccion = str(input("\t'A'- Eliminar el ultimo nodo creado,\n"
                             "\t'B'- Eliminar y recorrer la raiz o \n"
                             "\tingrese el dato a buscar y eliminar: "))
        print()
        Pop(eleccion)                                               #Mando a llamar al metodo Pop con la opcion elegida por el usuario.
        Menu()
    elif eleccion ==4:
        sys.exit()                                                  #Utilizo esta libreria para cerrar el programa.
    else:
        print("\nValor ingresado invalido...\n")
        Menu()

raiz = Nodo("Raiz")                                     #AL inicio del programa creo la Raiz con el valor Raiz como unico.
q=raiz                                                  #Y mi puntero lo igualo a la raiz para de ahi comenzar la lista.
Menu()                                                  #LLamo al metodo Menu para iniciar la recursividad...

    
