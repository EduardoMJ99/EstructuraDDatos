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
def Menu():
    print ("1.- Crear y enlazar hoja.\n"   
           "2.- Salir.")
    eleccion = int(input("Que desea realizar?: "))
    if eleccion ==1:
        Unir()                                      #Si eligio esta opcion llamo al metodo Unir y llamo al Menu para seguir.
        Menu()
    elif eleccion ==2:
        sys.exit()                                  #SI eligio esta opcion llamo al metodo reservado para salir del programa.
    else:
        print("\nValor ingresado invalido...\n")
        Menu()
Menu()                                              #Inicio el programa llamando al Menu para iniciar la recursividad.
