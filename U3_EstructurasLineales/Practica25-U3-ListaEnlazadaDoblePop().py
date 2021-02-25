import sys

class Nodo():                                       #Esta clase crea los Nodos de la lista con 3 atributos, el valor y los enlaces vacios.
    def __init__(self,datos):
        self.datos = datos
        self.siguiente = None
        self.anterior = None

def Enlazar():                                          #Este metodo se encarga de enlazar los nodos que se vayan creando.
    global raiz
    bandera = True                                      #Declaro e inicializo mis variables.
    q = raiz
    while(bandera):                                     #Utilizo este ciclo para posicionarme en el ultimo nodo de la lista
        if (q.siguiente == None):                       #Se termina el ciclo hasta que el enlaze del nodo sea NUlo.
            bandera=False
        else:
            p=q.siguiente
            q=p
    p=Nodo(str(input("Ingrese el elemento a enlazar: "))) #Creo un nuevo noco enviandole el valor ingresado por el ususario.
    q.siguiente = p                 #El nodo anterior al nuevo lo enlazo con el nuevo
    p.anterior = q                      #y el nuevo lo enlazo con el anteior
    q=p                                 #Al final muevo los dos ultimos punteros al ultimo nodo.
    
def Peek(eleccion):                     #Este metodo muestra valores de la lista.
    global raiz
    bandera = True
    q=raiz                              #Declaro e inicializo mis variables
    p=raiz
    if eleccion == "T":                 #Si eligio esta opcion imprimo todos los nodos de la lista.
        while (bandera):                #Utilizo este ciclo para moverme a travez de todos los nodos hasta llegar al ultimo.
            print(q.datos)              #Imprimo el valor del nodo en el que estoy.
            if q.siguiente == None:     #Si su atributo de enlaze es Nulo significa que llegue al final de la lista y termino el ciclo.
                bandera = False
            else:                       #Si no, avanzo al siguiente nodo con ayuda de los punteros.
                p = q.siguiente         #Muevo un puntero al sig nodo que esta en el enlace y luego muevo el otro puntero a este nodo.
                q=p
    elif eleccion == "U":               #Si eligio esta opcion utilizo exactamente el ciclo anterior solo que solo imprimo el ultimo
        while (bandera):                #nodo en el que se quedaron los punteros al salir del ciclo.
            if q.siguiente == None:     #Si el siguiente Nodo es la raiz, es porque llego al final de las listas.
                bandera = False
            else:
                p = q.siguiente         #SI no, continua al sig Nodo
                q=p
        print("Ultimo valor de la lista: "+ p.datos+"\n")
    elif eleccion == "R":                                   #SI eligio esta opcion es para imprimir la raiz.
        print("La raiz es: "+raiz.datos+"\n")
    else:                                                   #Si no fue ninguno de los anteriores significa que esta buscando un nodo por su valor.
        contador=1
        while (bandera):                                    #Para esto utilizo el mismo ciclo anterior para moverme a traves de toda la lista y me detengo
            if eleccion == q.datos:                         #hasta que encuentro el valor deseado o hasta que llegue al final de la lista sin encontrarlo.
                print("El dato "+str(eleccion)+" se encuentra en el nodo "+str(contador)+" de la lista...")     #Encontro el valor en la lista.
                bandera = False
            elif q.siguiente == None:
                print("El dato "+str(eleccion)+" no existe en la lista...")          #NO encontro el valor en la list
                bandera = False
            else:
                contador=contador+1                         #Me muevo al sig Nodo de la lista con ayuda de los punteros.
                p = q.siguiente
                q=p
    print()

def Pop(eleccion):              #Metodo para eliminar nodos de la lista.
    global raiz
    q=raiz                      #Declaro e inicializo mis variables.
    p=raiz
    bandera = True
    if(raiz.siguiente == None):                             #Si el nodo que le sigue a la raiz es Nulo es porque solo existe la raiz, entonces
            print("No puede eliminar mas ya que solo existe la raiz en la lista...")    #ya no se puede eliminar mas nodos.
    elif eleccion == "A":                                   #Si no y elige esta opcion que es eliminar el ultimo nodo de la lista....
        while (bandera):                                    #Utilizo este ciclo para posicionarme en el ultimo nodo que es el que quiero eliminar
            if q.siguiente.siguiente == None:               #Si el enlace del nodo siguiente en el que estoy es Nulo es porque llegue al ultimo.
                p = q.siguiente                             #Entonces muevo solo un puntero al nodo que quiero eliminar.
                q.siguiente = None                          #Despues elimino los enlaces que existen con este nodo que quiero eliminar
                p.anterior = None
                print("Nodo con el dato "+p.datos+" eliminado...")
                del p                                       #Por ultimo lo elimino.
                bandera = False
            else:                                           #El ciclo continua con el siguiente nodo...
                p = q.siguiente
                q=p
    elif eleccion == "B":                                   #Si eligio esta opcion es para eliminar la raiz actual y cambiarla por el nodo sig.
        p = raiz.siguiente                                  #Coloco un puntero en el nodo sig a la raiz
        raiz = p                                            #Mueve la raiz a ese puntero
        print("Nueva raiz: "+raiz.datos)
        del q                                               #FInalmente elimino la raiz.
    else:
        while (bandera):                                    #SI no fue ninguna de las anteriores es porque esta buscando un valor en especifico.
            if q.siguiente.datos == eleccion:               #Utilizo la misma dinamica del ciclo anterior para ir recorriendo los nodos de la lista.
                p= q.siguiente                              #hasta que encuentre el nodo deseado o hasta que llegue al final de la lista.
                q.siguiente = p.siguiente                   
                p.siguiente.anterior = q
                del p
                print("El dato "+str(eleccion)+" se ha eliminado de la lista...")
                bandera = False
            elif q.siguiente == None:
                print("El dato "+str(eleccion)+" no existe en la lista...")
                bandera = False
            else:
                p = q.siguiente
                q=p
    print()

def Menu():                                                         #Menu...
    print ("1.- Crear y enlazar nodo.\n"
           "2.- Mostrar la lista.\n"
           "3.- Eliminar nodo de la lista.\n"
           "4.- Salir.")
    eleccion = int(input("Que desea realizar?: "))
    if eleccion ==1:
        Enlazar()                                                   #Si eligio esta opcion llamo al metodo enlazar.
        print("\nNodo creado y doblemente enlazado...\n")
        Menu()
    elif eleccion ==2:
        eleccion = str(input("\nTeclee 'T' para mostrar TODA la lista doble,\n"             #Si eligio esta opcion es para mostrar los valores de la
                                         "teclee 'U' para mostrar el ULTIMO nodo doblemente enlazado,\n"    #lista.
                                         "teclee 'R' para mostrar la RAIZ,\n"
                                         "o ingrese el valor que desea buscar en la lista doble: "))
        print()
        Peek(eleccion)                                      #LLamo al metodo Peek con la eleccion del usuario.
        Menu()
    elif eleccion ==3:                                                          #SI eligio esta opcion es para eliminar los valores de la lista.
        eleccion = str(input("\t'A'- Eliminar el ultimo nodo creado,\n"
                             "\t'B'- Eliminar y recorrer la raiz o \n"
                             "\tingrese el dato a buscar y eliminar: "))
        print()
        Pop(eleccion)                                                           #Mando a llamar al metodo pop con la opcion que eligio el usuario.
        Menu()
    elif eleccion ==4:
        sys.exit()                                          #Utilizo esta libreria para cerrar el programa.
    else:
        print("\nValor ingresado invalido...\n")
        Menu()

raiz = Nodo("Raiz")                                                     #AL inicio del programa creo la Raiz con el valor Raiz como unico.
p=raiz
q=raiz                                                                  #Y mi puntero lo igualo a la raiz para de ahi comenzar la lista.
Menu()                                                                  #LLamo al metodo Menu para iniciar la recursividad...

    
