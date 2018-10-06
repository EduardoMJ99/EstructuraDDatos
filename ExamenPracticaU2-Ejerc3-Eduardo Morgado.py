pila =[]                    #Declaro e inicializo la pila
import sys                  #Importo esta libreria para poder salir del programa.

def push(version):                                          #Metodo que ingresa en la ultima posicion de la pila el valor ingresado.
    pila.append(version)
    
def pop():                                                  #Metodo que elimina la ultima version ingresada.
    if len(pila)<=0:                                        #Si la pila no tiene elementos...
        print ("\nNo hay versiones por eliminar...\n")      #Imprime que no hay versiones por eliminar.
    else:
        del pila[-1]                                        #Si si, elimina el elemento de la ultima posicion de la pila, para eso el
        print ("\nVersion eliminada...\n")                  #'del pila[-1]'
        
def peek():                                                 #Metodo que muestra valores de la pila.
    if len(pila)<=0:                                        #Si la pila no tiene elementos es que esta vacia.
        print ("\nLa pila de versiones esta vacia...\n")
    else:                                                   #Si si, el usuario tiene varias opciones por elegir...
        print ("\n1- Mostrar todas las versiones.\n"
               "2- Mostrar la ultima version ingresada.\n"
               "3- Mostrar la primer version ingresada.\n"
               "4- Buscar una version en especifico.")
        eleccion = int(input("Que desea realizar?: "))
        if eleccion ==1:                                        #Si eligio esta opcion muestra todos los valores de la pila empezando por el tope(cima).
            print ("\nLas versiones existentes son: ")          #Para esto hago un ciclo que imprima cada uno de los valores de la pila pero empezando de
            for indice in reversed(pila):                       #la cima hasta el final, para eso "reversed".
                print (indice)
            print()
        else:                                                   #SI eligio esta opcion muestra el ultimo valor ingresado a la pila, para esto obtengo la longitud
            if eleccion ==2:                                    #de la pila y le resto 1 para saber el indice del ultimo elemento.
                print (str(pila[len(pila)-1])+"\n")
            else:
                if eleccion ==3:                                #Si eligio esta opcion muestra el primer valor ingresado por el usuario, que siempre esta en
                    print (pila[0])                             #la posicion 0 de la pila.
                    print()
                else:
                    if eleccion == 4:                           #SI eligio esta opcion muestra la posicion del elemento que el usuario esta buscando,
                        buscar = input("Version a buscar: ")
                        try:
                            posicion = pila.index(buscar)           #Con esta funcion, obtengo el indice donde se encuentra el elemento igual al que ingreso.
                            print ("\nLa version "+str(buscar)+" se encuentra en la posicion "+str(posicion+1)+" de la pila de versiones.\n")
                        except:                                     #EN caso de que no lo encuentra, el programa lanza un error, por lo tanto lo salvo 
                            print ("\nNo se encontro la version en la pila de versiones...\n")                                  #haciendo un try-except.
                    else:
                        print ("\nValor incorrecro ingresado...\n")
                        
def Menu():                                                         #Menu interactivo con el usuario.
    print ("1- Insertar nueva version de proyecto.\n"
           "2- Eliminar ultima version ingresada de proyecto.\n"
           "3- Mostrar versiones de proyecto.\n"
           "4- Salir.")
    eleccion = int(input("Que desea realizar?: "))                  
    if eleccion ==1:                                                #SI eligio esta opcion es para ingresar valores a la pila...
        version = input("Ingresar version: ")                       #Le pido el valor a ingresar a la pila y llamo al metodo enviandole el elemento a ingresar.
        push(version)
        print()
        Menu()                              #Llamo a Menu para seguir con la recursividad.
    else:
        if eleccion ==2:                                            #SI eligio esta opcion es para eliminar un valor de la pila.
            pop()                                                   #Llamo al metodo pop().
            Menu()                          #Llamo a Menu para seguir con la recursividad.
        else:                                                       #Si eligio esta opcion es para mostrar los valores de la pila.
            if eleccion == 3:                                       #Llamo al metodo peek()
                peek()
                Menu()                      #Llamo a Menu para seguir con la recursividad.
            else:
                if eleccion ==4:                                    #SI eligio esta opcion, cierro el programa llamando al metodo reservado exit().
                    sys.exit()
                else:
                    print ("\nValor ingresado incorrecto...\n")
                    Menu()                  #Llamo a Menu para seguir con la recursividad.
Menu()                                      #Llamo por primera vez a Menu para iniciar la recursividad.
