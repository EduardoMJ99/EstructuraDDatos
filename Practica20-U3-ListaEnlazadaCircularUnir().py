import sys

class Nodo():                                   #Esta clase crea los Nodos de la lista con 2 atributos, el valor y el enlace vacio.
    def __init__(self,datos):
        self.datos = datos
        self.siguiente = None

def Enlazar():                          #Este metodo se encarga de enlazar los nodos que se vayan creando.
    global raiz
    global p                            #Declaro e inicializo mis variables.
    global q
    p=Nodo(str(input("Ingrese el elemento a enlazar: ")))   #Creo un Nodo y le mando el valor ingresado.
    q.siguiente = p                     #Como es lista circular, el nodo que vaya creando necesita estar enlazado con la raiz.
    p.siguiente = raiz                  #Para esto la propiedad de enlace del nodo creado le asigno la raiz.
    q=p                                 #Al final muevo ambos punteros al ultimo nodo.
   
def Menu():                                             #Menu...
    print ("1.- Crear y enlazar nodo.\n"   
           "2.- Salir.")
    eleccion = int(input("Que desea realizar?: "))
    if eleccion ==1:
        Enlazar()                                       #Si eligio esta opcion llamo al metodo enlazar.
        print("\nNodo creado y enlazado...\n")
        Menu()
    elif eleccion ==2:
        sys.exit()                                      #Utilizo esta libreria para cerrar el programa.
    else:
        print("\nValor ingresado invalido...\n")
        Menu()

raiz = Nodo("Raiz")                         #AL inicio del programa creo la Raiz con el valor Raiz como unico.
p=raiz                                      #Y mi puntero lo igualo a la raiz para de ahi comenzar la lista.
q=raiz      
Menu()                                      #LLamo al metodo Menu para iniciar la recursividad...

    
