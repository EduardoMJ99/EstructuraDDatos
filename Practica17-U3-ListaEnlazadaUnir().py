import sys

class Nodo():                               #Esta clase crea los Nodos de la lista con 2 atributos, el valor y el enlace vacio.
    def __init__(self,datos):
        self.datos = datos
        self.siguiente = None

def Enlazar():                                              #Este metodo se encarga de enlazar los nodos que se vayan creando.
    global p
    global q
    p=Nodo(str(input("Ingrese el elemento a enlazar: ")))   #Mando a llamar a la clase y le mando el valor ingresado.
    q.siguiente = p                                         #Despues utilizo 2 punteros, donde q es el Nodo anterior y p el nuevo nodo.
    q=p                                                     #Al nodo que tiene el puntero q lo enlazo con el nuevo nodo(q.siguiente)
   
def Menu():                                             #Menu...
    print ("1.- Crear y enlazar nodo.\n"   
           "2.- Salir.")
    eleccion = int(input("Que desea realizar?: "))
    if eleccion ==1:                                    #Si eligio esta opcion llamo al metodo enlazar.
        Enlazar()
        print("\nNodo creado y enlazado...\n")
        Menu()
    elif eleccion ==2:
        sys.exit()                                      #Utilizo esta libreria para cerrar el programa.
    else:
        print("\nValor ingresado invalido...\n")
        Menu()

raiz = Nodo("Raiz")                                     #AL inicio del programa creo la Raiz con el valor Raiz como unico.
p=raiz                                                  #Y mis punteros los igualo a la raiz para de ahi comenzar la lista.
q=raiz      
Menu()                                                  #LLamo al metodo Menu para iniciar la recursividad...

    
