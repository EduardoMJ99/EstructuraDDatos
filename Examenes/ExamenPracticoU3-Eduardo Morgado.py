q=None                              #Declaro mi puntero q como vacio para que la primera vez que se crea nodo se haga la raiz.

class Nodo():                       #Creo mi clase Nodo donde creo los nodos con 3 atributos,
    def __init__(self,datos):       #un dato, y dos enlaces, uno para el siguiente nodo y otro
        self.datos = datos          #para el anterior.
        self.siguiente = None   
        self.anterior = None

def Enlazar(cont):                      #Metodo para crear y enlazar los nodos.
    global raiz                         #Tomo y creo mis variables necesarias.
    global q
    bandera = True
    p=Nodo(str(cont))                   #Creo el Nodo p con el dato correspondiente.
    if (q==None):                       #Si es la primera vez que el puntero adquiere un valor, declaro el nodo creado
        raiz = p                        #como la raiz.
        q=raiz                          
    else:                               #Si no, muevo los punteros q y p hasta el ultimo nodo creado para que el siguente
        while(bandera):                 #nodo que cree, se enlace con el ultimo de la lista.
            if (q.siguiente == None):   
                bandera=False          
            else:                       #Para lograr esto, muevo mis punteros de tal forma que un puntero adquiere el valor
                p=q.siguiente           #del nodo siguiente, y despues de moverlo, igualo el otro puntero al que movi.
                q=p
        q.siguiente = p                 #Despues de posicionarme en el ultimo Nodo, lo enlazo con el nuevo nodo, 
        p.anterior = q                  #el nuevo nodo lo enlazo con el anterior por que es lista doble, y por 
        q=p                             #ultimo muevo el puntero al recien creado.
    print(q.datos+"    ",end='')        #Imprimo el Nodo creado sin brincar renglon.

def Pop(eleccion):                      #Metodo para eliminar nodos.
    global raiz                         #Tomo y creo mis variables necesarias.
    q=raiz                              #Esto es para posicionarme en la raiz los punteros.
    p=raiz
    bandera = True
    if(raiz.siguiente == None):                                                     #Si la raiz no tiene nodo siguiente, es porque solo existe la raiz.
            print("No puede eliminar mas ya que solo existe la raiz en la lista...")
    else:                                                                           #Si no, 
        while (bandera):                                                            #Este ciclo es para moverse por cada uno de los Nodos de la lista.
            if q.siguiente == None:                                                 #Si se cumple esta condicion, es porque llego al final de la lista    
                print("El dato "+str(eleccion)+" no existe en la lista...")         #y no se encontro el elemento deseado a eliminar.
                bandera = False
            elif raiz.datos == str(eleccion):                                       #Si se cumple esta condicion que significa que el dato buscado a 
                p = raiz.siguiente                                                  #eliminar es la raiz, coloco un puntero en el siguiente Nodo de la
                raiz = p                                                            #raiz, despues igualo la raiz al nodo siguiente, despues elimino
                p.anterior = None                                                   #el enlace que existia con la raiz anterior.
                print("El dato "+str(eleccion)+" se ha eliminado de la lista...")   #Imprimo...
                print("OJO: Raiz cambiada...")
                bandera = False                                                     #Y por ultimo elimino el Nodo donde tenia un puntero en la raiz.
                del q
            elif q.siguiente.datos == str(eleccion):                                #Si se cumple esta condicion que significa que el nodo siguiente en
                p= q.siguiente                                                      #el que estoy es el que quiero eliminar, muevo un puntero a ese nodo,
                q.siguiente = p.siguiente                                           #enlazo el nodo en el que estoy con el nodo que le sigue al que 
                p.siguiente.anterior = q                                            #quiero eliminar, el nodo delante del que quiero eliminar lo enlazo
                del p                                                               #con en el que estoy y por ultimo elimino el nodo.
                print("El dato "+str(eleccion)+" se ha eliminado de la lista...")
                bandera = False
            else:                                                                   #Si no se cumple ninguna de las anteriores, avanzo al siguiente
                p = q.siguiente                                                     #nodo para evaluarlo.
                q=p                                                             

def Peek(eleccion):                     #Metodo para mostrar nodos.
    global raiz                         #Tomo y creo mis variables necesarias.
    bandera = True
    q=raiz                              #Esto es para posicionarme en la raiz los punteros.
    p=raiz
    if eleccion == "A":                         #Esta opcion es para mostrar los nodos de izquiera a derecha.
        while (bandera):                        #Recorro todos los nodos y voy imprimiendolos hasta que la propiedad SIGUIENTE del nodo 
            print(q.datos+"    ",end='')        #en el que estoy sea nula.
            if q.siguiente == None:
                bandera = False
            else:                               #Para avanzar muevo mis punteros de tal forma que un puntero adquiere el valor
                p = q.siguiente                 #del nodo siguiente, y despues de moverlo, igualo el otro puntero al que movi.            
                q=p                             
    elif eleccion == "B":                       #Esta opcion es para mostrar los nodos de derecha a izquiera
        while (bandera):                        #Recorro todos los nodos hasta que la propiedad SIGUIENTE del nodo 
            if q.siguiente == None:             #en el que estoy sea nula, esto para posicionarme en el ultimo nodo de la lista.
                bandera = False
            else:                               #Para avanzar muevo mis punteros de tal forma que un puntero adquiere el valor
                p = q.siguiente                 #del nodo siguiente, y despues de moverlo, igualo el otro puntero al que movi.
                q=p
        while (bandera == False):               #Como mi variables bandera la use en el anterior ciclo, la puedo usar aqui pero la condicion alrevez.
            print(q.datos+"    ",end='')        #Recorro todos los nodos y voy imprimiendolos hasta que la propiedad ANTERIOR del nodo 
            if q.anterior == None:              #en el que estoy sea nula.
                bandera = True
            else:                               #Para avanzar muevo mis punteros de tal forma que un puntero adquiere el valor
                p = q.anterior                  #del nodo anterior, y despues de moverlo, igualo el otro puntero al que movi.
                q=p
    elif eleccion == "C":                       #Esta opcion es para mostar la raiz, simplemente la imprimo con raiz.datos.
        print("La raiz es: "+raiz.datos)
    elif eleccion =="D":                        #Esta opcion es para mostrar los valores finales de izquierda y derecha de la lista.
        while (bandera):                        
            if q.siguiente == None:
                bandera = False                 #Esto ciclo es lo mismo que los anteriores, sirve para posicionarme en el ultimo nodo.
            else:
                p = q.siguiente
                q=p
        print("Final Derecha: "+q.datos, end='')    #Despues, imprimo el dicho nodo.
        while (bandera==False):
            if q.anterior == None:
                bandera = True                  #Esto ciclo es lo mismo que los anteriores, sirve para posicionarme en el primer nodo, ya que con el
            else:                               #anterior ciclo me quede en el ultimo de la lista.
                p = q.anterior
                q=p
        print("      Final Izquierda: "+q.datos)    #Despues, imprimo dicho nodo.
    else:                                       #Esta opcion es para buscar un nodo en la lista enlazada.
        contador=1                              #El contador lo uso para indicar en que nodo se encontro el valor buscado, lo inicializo a 1.
        while (bandera):
            if str(eleccion) == q.datos:        #Si se encuentra el valor buscado lo imprimo.
                print("El dato "+str(eleccion)+" se encuentra en el nodo "+str(contador)+" de la lista contando la raiz.")
                bandera = False
            elif q.siguiente == None:           #Si la propiedad SIGUIENTE del nodo en el que estoy es Nula, es porque estoy en el ultimo nodo y
                print("El dato "+str(eleccion)+" no existe en la lista...")         #no encontre el dato buscado.
                bandera = False
            else:
                contador=contador+1             #S no se cumplen ningunas de las anteriores, cambio de nodo y aumento el contador.
                p = q.siguiente
                q=p

def Inicio():                                                                                 #Metodo que contiene todas las instrucciones.
    print("La lista doblemente enlazada es: ")
    for cont in range(1,10,1):                                                              #Ciclo para crear y enlazar los nodos del 1 al 9.
        Enlazar(cont)
    print("\n\nPara continuar cada vez a la siguiente instruccion presione  <enter>\n")
    input("Leer la lista de izquierda a derecha.")
    Peek("A")                                                               #Llamo al metodo Peek con el parametro A
    input("\n\nLeer la lista de derecha a izquierda.")
    Peek("B")                                                               #Llamo al metodo Peek con el parametro B
    input("\n\nInsertar 10, 11 y 13.")
    Enlazar(10)
    Enlazar(11)                                                             #Llamo a metodo Enlazar para crear y enlazar estos nodos.
    Enlazar(13)
    input("\n\nEliminar 8 y 1.")
    Pop(8)
    Pop(1)                                                                  #Llamo al metodo Pop para buscar y eliminar estos valores.
    input("\nLeer Raiz.")
    Peek("C")                                                               #Llamo al metodo Peek con el parametro C
    input("\nLeer final de la lista lado derecho y lado izquierdo.")
    Peek("D")                                                               #Llamo al metodo Peek con el parametro D
    input("\nBuscar 0,7,8,1.")
    Peek(0)                                                                 
    Peek(7)                                                                 #Llamo al metodo Peek con los valores a buscar en la lista.
    Peek(8)
    Peek(1)
    print("\nLista final: ")
    Peek("A")                                                               #Muestro la lista final
    
Inicio()
