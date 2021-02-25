import sys

class Nodo():
    def __init__(self,datos):                   #Esta clase crea los Nodos de la lista con 3 atributos, el valor y los enlaces vacios.
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
   
def Menu():                                         #Menu...
    print ("1.- Crear y enlazar nodo.\n"   
           "2.- Salir.")
    eleccion = int(input("Que desea realizar?: "))
    if eleccion ==1:
        Enlazar()                                               #Si eligio esta opcion llamo al metodo enlazar.
        print("\nNodo creado y doblemente enlazado...\n")
        Menu()
    elif eleccion ==2:
        sys.exit()                                               #Utilizo esta libreria para cerrar el programa.
    else:
        print("\nValor ingresado invalido...\n")
        Menu()

raiz = Nodo("Raiz")                                                     #AL inicio del programa creo la Raiz con el valor Raiz como unico.
p=raiz
q=raiz                                                                  #Y mi puntero lo igualo a la raiz para de ahi comenzar la lista.
Menu()                                                                  #LLamo al metodo Menu para iniciar la recursividad...

