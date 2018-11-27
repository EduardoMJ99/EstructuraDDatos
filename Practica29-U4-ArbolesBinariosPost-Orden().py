import sys                          #Importo y declaro mis variables.
q = None

class Hoja():                       #Clase que crea los nodos con 3 atributos, el que guarda el valor y sus dos enlaces(izq y der).
    def __init__(self,datos):      
        self.datos = datos
        self.der = None
        self.izq = None

def Unir():                     #Metodo para enlazar los nodos que se vayan creando.
    global raiz                 #Declaro e inicializo mis variables.
    global q
    bandera = True
    p=Hoja(str(input("Ingrese el elemento a enlazar: ")))   #Creo el nuevo nodo enviandole el valor que ingreso el usuario.
    if (q == None):                     #Si la variables es Nula significa que es la primera vez que entra a crear Nodos, por lo tanto
        raiz = p                        #el primer nodo se convierte en la raiz y q lo igualo a este para no entrar mas aqui.
        print("\nRaiz creada...\n")
        q=raiz
    else:                               #Si no, entro a un ciclo que se encarga de moverve en los nodos segun el usuario vaya
        while bandera:                  #eligiendo izquierda o derecha para posicionar el nodo que acaba de crear.
            print("\t\t\tIngrese 'I' para izquierda o,\n"
                    "\t\t\tIngrese 'D' para derecha: ")
            if q.izq ==None:                                                    #Esta parte la utilizo para mostrarle al usuario
                print("Nodo izquierda vacio, terminar aqui.",end='\t\t')        #que hay en la parte izquierda y la parte derecha
            else:                                                               #del nodo en el que esta.
                print("Nodo ocupado por "+q.izq.datos+", continua...",end='\t\t')
            if q.der ==None:
                print("Nodo derecha vacio, terminar aqui.")
            else:
                print("Nodo ocupado por "+q.der.datos+", continua...")
            eleccion = str(input(": "))                                 
            if (eleccion == "I") and (q.izq ==None):        #Si eligio IZQUIERDA y esta vacio el lugar, inserto ahi el Nodo nuevo,
                q.izq = p                                   #lo enlazo con el anterior y termino el ciclo.
                print("\nNodo creado y enlazado...\n")
                bandera = False
            elif (eleccion == "I") and (q.izq !=None):      #Si eligio IZQUIERD y esta ocupado, me muevo al nodo siguiente y continuo.
                q = q.izq
            elif (eleccion == "D") and (q.der == None):     #Si eligio DERECHA y esta vacio el lugar, inserto ahi el Nodo nuevo,
                q.der = p                                   #lo enlazo con el anterior y termino el ciclo.
                print("\nNodo creado y enlazado...\n")
                bandera = False
            elif (eleccion == "D") and (q.der != None):     #Si eligio DERECHA y esta ocupado, me muevo al nodo siguiente y continuo.
                q=q.der
            else:
                print("\nOpcion incorrecta...\n")
        q=raiz                                              #Al final posiciono este puntero en la raiz para no crear mas raices
                                                            #al volver a entrar a este metodo.

def InOrden(NodoAImprimir):                     #Metodo para recorrer el arbol en InOrden...
  if NodoAImprimir != None:                     #SI el nodo en el que estoy no es Nulo entonces sigue con el recorrido.
      InOrden(NodoAImprimir.izq)                #Primero la recursividad llega a los nodos de la izquierda hasta que uno sea Nulo,
      print(NodoAImprimir.datos)                #Se imprimen, luego la raiz, y luego lo mismo con los de la derecha.
      InOrden(NodoAImprimir.der)

def PreOrden(NodoAImprimir):                    #Metodo para recorrer el arbol en pre orden...
  if NodoAImprimir != None:                     #Si el nodo en el que estoy no es nulo entonces sigue con el recorrido.
      print(NodoAImprimir.datos)                #Primero imprime el nodo en el que esta, luego se mueve mediante recursividad a
      PreOrden(NodoAImprimir.izq)               #los nodos de la izquierda hasta que alguno sea nulo, se imprimen y luego lo mismo
      PreOrden(NodoAImprimir.der)               #con los de la derecha.

def PostOrden(NodoAImprimir):                   #Metodo para recorrer el arbol en post orden
  if NodoAImprimir != None:                     #Si el nodo en el que estoy no es nulo entonces sigue con el recorrido.
      PostOrden(NodoAImprimir.izq)              #Primero se profundiza en los nodos de la izquierda del arbol hasta llegar a uno
      PostOrden(NodoAImprimir.der)              #nulo, despues se profundiza en los derechos y al final en la raiz.
      print(NodoAImprimir.datos)
      
def Menu():                                 #Menu...
    print ("1.- Crear y enlazar hoja.\n"
           "2.- Recorrido In Orden.\n"
           "3.- Recorrido Pre Orden.\n"
           "4.- Recorrido Post Orden\n"
           "5.- Salir.")
    eleccion = int(input("Que desea realizar?: "))
    if eleccion ==1:
        Unir()                          #Si eligio esta opcion llamo al metodo Unir y llamo al Menu para seguir.
        Menu()
    elif eleccion ==2:
        if q != None:                   #SI eligio esta opcion llamo al metodo In-Orden si es que existe raiz en el arbol.
            print()
            InOrden(raiz)
        else:
            print("\nNo existe el arbol...")
        print()
        Menu()
    elif eleccion ==3:                  #Si eligio esta opcion llamo al metodo pre orden si es que existe raiz en el arbol.
        if q != None:
            print()
            PreOrden(raiz)
        else:
            print("\nNo existe el arbol...")
        print()
        Menu()
    elif eleccion ==4:                  #SI eligio esta opcion llamo al metodo post orden si es que existe raiz en el arbol.
        if q != None:
            print()
            PostOrden(raiz)
        else:
            print("\nNo existe el arbol...")
        print()
        Menu()
    elif eleccion ==5:
        sys.exit()                      #SI eligio esta opcion llamo al metodo reservado para salir del programa.
    else:
        print("\nValor ingresado invalido...\n")
        Menu()
Menu()                                   #Inicio el programa llamando al Menu para iniciar la recursividad.
