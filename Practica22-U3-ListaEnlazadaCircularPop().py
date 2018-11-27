import sys

class Nodo():                        #Esta clase crea los Nodos de la lista con 2 atributos, el valor y el enlace vacio.
    def __init__(self,datos):
        self.datos = datos
        self.siguiente = None

def Enlazar():                       #Este metodo se encarga de enlazar los nodos que se vayan creando.
    global raiz
    bandera = True                  #Declaro e inicializo mis variables.
    q=raiz
    while (bandera):                                            #COn este ciclo me posiciono en el ultimo nodo de la lista.
        if (q.siguiente == raiz) or (q.siguiente == None):      #Si el nodo siguiente es Nulo o es la raiz es porque 
            bandera = False                                     #se llego al final de la lista.
        else:
            p = q.siguiente
            q=p
    p=Nodo(str(input("Ingrese el elemento a enlazar: ")))       #Creo un nodo nuevo con el valor ingresado.
    q.siguiente = p                                             #Lo enlazo con el anterior nodo y el nuevo lo enlazo con la raiz.
    p.siguiente = raiz
    q=p                                                         #Al final muevo ambos punteros al final de la lista.

def Peek(eleccion):                                         #Metodo para mostrar nodos de la lista.
    global raiz
    bandera = True
    q=raiz                                                  #Declaro e inicializo mis variables
    p=raiz
    if eleccion == "T":                                     #SI eligio esta opcion es para mostrar todos los valores de la lista.
        while (bandera):
            print(q.datos)                                  #Imprimo el valor del nodo en el que estoy.
            if q.siguiente == raiz:                         #Si su atributo de enlaze es Nulo significa que llegue al final de la lista y termino el ciclo.
                bandera = False
            else:                                           #Si no, avanzo al siguiente nodo con ayuda de los punteros.
                p = q.siguiente                             #Muevo un puntero al sig nodo que esta en el enlace y luego muevo el otro puntero a este nodo.
                q=p
    elif eleccion == "U":                                   #Si eligio esta opcion utilizo exactamente el ciclo anterior solo que solo imprimo el ultimo
        while (bandera):                                    #nodo en el que se quedaron los punteros al salir del ciclo.
            if q.siguiente == raiz:                         #Si el siguiente Nodo es la raiz, es porque llego al final de las listas.
                bandera = False
            else:                                           #SI no, continua al sig Nodo
                p = q.siguiente
                q=p
        print("Ultimo valor de la lista: "+ p.datos+"\n")
    elif eleccion == "R":                                   #SI eligio esta opcion es para imprimir la raiz.
        print("La raiz es: "+raiz.datos+"\n")
    else:                                                   #Si no fue ninguno de los anteriores significa que esta buscando un nodo por su valor.
        contador=1
        while (bandera):                                    #Para esto utilizo el mismo ciclo anterior para moverme a traves de toda la lista y me detengo
            if eleccion == q.datos:                         #hasta que encuentro el valor deseado o hasta que llegue al final de la lista sin encontrarlo.
                print("El dato "+str(eleccion)+" se encuentra en el nodo "+str(contador)+" de la lista...") #Encontro el valor en la lista.
                bandera = False
            elif q.siguiente == raiz:
                print("El dato "+str(eleccion)+" no existe en la lista...")         #NO encontro el valor en la lista.
                bandera = False
            else:
                contador=contador+1
                p = q.siguiente
                q=p
    print()

def Pop(eleccion):                              #Metodo para eliminar Nodos.
    global raiz
    q=raiz                                      #Declaro e inicializo mis variables
    p=raiz
    bandera = True
    if(raiz.siguiente == raiz):                 #Si la raiz esta enlazada con ella misma significa que solo existe la raiz en la lista.
            print("No puede eliminar mas ya que solo existe la raiz en la lista...")
    elif eleccion == "A":                       #SI eligio esta opcion es para eliminar el ultimo nodo de la lista.
        while (bandera):
            if q.siguiente.siguiente == raiz:   #Si el nodo siguiente del que quiero eliminar es la raiz, significa que llegue al final de la lista.
                p = q.siguiente                 #Asigno un puntero al valor que quiero eliminar, lo enlazo con la raiz y elimino el nodo este.
                q.siguiente = raiz
                print("Nodo con el dato "+p.datos+" eliminado...")
                del p
                bandera = False
            else:                               #SI no continuo al siguiente Nodo y asi hasta llegar al ultimo nodo.
                p = q.siguiente
                q=p
    elif eleccion == "B":                       #Si eligio esta opcion es para eliminar y sustituir la raiz.
        while (bandera):                        #Utilizo la misma dinamica del ciclo anterior para posicionarme en el ultimo nodo de la lista.
            if q.siguiente == raiz:
                bandera = False
            else:
                p = q.siguiente
                q=p
        p = q.siguiente                         #Ya que estoy al final, coloco un puntero al nodo siguiente de la raiz, este nodo lo enlazo con el
        raiz = p.siguiente                      #anterior de la raiz y finalmente borro la raiz (el puntero que guardaba la raiz).
        q.siguiente = raiz
        print("Nueva raiz: "+raiz.datos)
        del p
    else:
        while (bandera):                                    #SI no fue ninguna de las anteriores es porque esta buscando un valor en especifico.
            if q.siguiente.datos == eleccion:               #Utilizo la misma dinamica del ciclo anterior para ir recorriendo los nodos de la lista.
                p= q.siguiente                              #hasta que encuentre el nodo deseado o hasta que llegue al final de la lista.
                q.siguiente = p.siguiente
                del p
                print("El dato "+str(eleccion)+" se ha eliminado de la lista...")
                bandera = False
            elif q.siguiente == raiz:
                print("El dato "+str(eleccion)+" no existe en la lista...")
                bandera = False
            else:
                p = q.siguiente
                q=p
    print()

def Menu():                                                         #Menu
    print ("1.- Crear y enlazar nodo.\n"
           "2.- Mostrar los nodos.\n"
           "3.- Eliminar nodo.\n"
           "4.- Salir.")
    eleccion = int(input("Que desea realizar?: "))
    if eleccion ==1:
        Enlazar()                                                   #Si eligio esta opcion llamo al metodo enlazar.
        print("\nNodo creado y enlazado...\n")
        Menu()
    elif eleccion ==2:                                                                          #Si eligio esta opcion es para mostrar los valores de la 
        eleccion = str(input("\nTeclee 'T' para mostrar TODA la lista circular,\n"              #lista.
                                         "teclee 'U' para mostrar el ULTIMO nodo enlazado,\n"
                                         "teclee 'R' para mostrar la RAIZ,\n"
                                         "o ingrese el valor que desea buscar en la lista: "))
        print()
        Peek(eleccion)
        Menu()
    elif eleccion ==3:                                                                          #Si eligio esta opcion despliega un menu de opciones
        eleccion = str(input("\t'A'- Eliminar el ultimo nodo creado,\n"                         #para eliminar valores de la lista.
                             "\t'B'- Eliminar y recorrer la raiz o \n"
                             "\tingrese el dato a buscar y eliminar: "))
        print()
        Pop(eleccion)
        Menu()
    elif eleccion ==4:
        sys.exit()                                                      #Utilizo esta libreria para cerrar el programa.
    else:
        print("\nValor ingresado invalido...\n")
        Menu()

raiz = Nodo("Raiz")                                                     #AL inicio del programa creo la Raiz con el valor Raiz como unico.
q=raiz                                                                  #Y mi puntero lo igualo a la raiz para de ahi comenzar la lista.
Menu()                                                                  #LLamo al metodo Menu para iniciar la recursividad...

    
