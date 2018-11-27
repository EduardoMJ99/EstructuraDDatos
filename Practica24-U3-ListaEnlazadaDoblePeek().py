import sys

class Nodo():                                                   #Esta clase crea los Nodos de la lista con 3 atributos, el valor y los enlaces vacios.
    def __init__(self,datos):
        self.datos = datos
        self.siguiente = None
        self.anterior = None

def Enlazar():                          #Este metodo se encarga de enlazar los nodos que se vayan creando.
    global raiz
    global p                            #Declaro e inicializo mis variables.
    global q
    p=Nodo(str(input("Ingrese el elemento a enlazar: ")))   #Creo un nuevo noco enviandole el valor ingresado por el ususario.
    q.siguiente = p                     #El nodo anterior al nuevo lo enlazo con el nuevo
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
    
def Menu():                                     #Menu...
    print ("1.- Crear y enlazar nodo.\n"
           "2.- Mostrar la lista.\n"
           "3.- Salir.")
    eleccion = int(input("Que desea realizar?: "))
    if eleccion ==1:
        Enlazar()                                       #Si eligio esta opcion llamo al metodo enlazar.
        print("\nNodo creado y doblemente enlazado...\n")
        Menu()
    elif eleccion ==2:                                                                  #SI eligio esta opcion es para mostrar valores de la lista
        eleccion = str(input("\nTeclee 'T' para mostrar TODA la lista doble,\n"
                                         "teclee 'U' para mostrar el ULTIMO nodo doblemente enlazado,\n"
                                         "teclee 'R' para mostrar la RAIZ,\n"
                                         "o ingrese el valor que desea buscar en la lista doble: "))
        print()
        Peek(eleccion)                                  #LLamo al metodo Peek con la eleccion del usuario.
        Menu()
    elif eleccion ==3:
        sys.exit()                                      #Utilizo esta libreria para cerrar el programa.
    else:
        print("\nValor ingresado invalido...\n")
        Menu()

raiz = Nodo("Raiz")                                                     #AL inicio del programa creo la Raiz con el valor Raiz como unico.
p=raiz
q=raiz                                                                  #Y mi puntero lo igualo a la raiz para de ahi comenzar la lista.
Menu()                                                                  #LLamo al metodo Menu para iniciar la recursividad...

    
