import sys                          #Importo y declaro mis variables.
q = None

class Hoja():                       #Clase que crea los nodos con 3 atributos, el que guarda el valor y sus dos enlaces(izq y der).
    def __init__(self,datos):      
        self.datos = datos
        self.der = None
        self.izq = None

def Unir():                         #Metodo para enlazar los nodos que se vayan creando.
    global raiz                     #Declaro e inicializo mis variables.
    global q
    bandera = True
    p=Hoja(str(input("Ingrese el elemento a enlazar: ")))   #Creo el nuevo nodo enviandole el valor que ingreso el usuario.
    if (q == None):                 #Si la variables es Nula significa que es la primera vez que entra a crear Nodos, por lo tanto
        raiz = p                    #el primer nodo se convierte en la raiz y q lo igualo a este para no entrar mas aqui.
        print("\nRaiz creada, los elementos menores al nodo seran \npuestos a la izquierda y los mayores a la derecha...\n")
    else:                           #Si no ya creo nodos diferentes a la raiz, para esto utilizo el sig ciclo para ir comparando
        while(bandera):             #nodo por nodo con el nodo que se desea ingresar.
            if (int(p.datos)<=int(q.datos)):    #Si es menor o igual al nodo en el que estamos, lo coloca a su izquierda si es
                if (q.izq==None):               #que esta desocupado.
                    q.izq=p
                    bandera = False
                else:                           #Si no esta desocupado, se mueve al nodo de la izquierda y se repite la instruccion.
                    q = q.izq
            elif (int(p.datos)>int(q.datos)):   #Si es mayor al nodo en el que estamos, lo coloca a su derecha si es que esta
                if (q.der==None):               #desocupado.
                    q.der=p
                    bandera = False
                else:                           #Si no esta desocupado, se mueve al nodo de la derecha y se repite la instruccion.
                    q = q.der
        print("\nNodo creado y enlazado...\n")
    q=raiz
        
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
