global valor                #Declaro mi variables globales para poder utilizarlas dentro y fuera de los metodos.
global indice
global eleccion
pila = []
global indicepop
import sys
indice = 0

def push(indice, valor):                            #Metodo se encarga de ingresar valores a la pila.
    pila.append(valor)                              #Regresa el valor del indice incrementado en 1.
    return indice +1
    
def peek(eleccion):                                 #Metodo se encarga de mostrar al usuario lo que hay dentro de la pila.
    if eleccion == "T":                             #Si 'eleccion' es igual a 'T' muestra todos los valores de la pila.
        print (pila)
        print ("\n")
    else:
        if eleccion == "U":                                                 #SI 'eleccion' es igual a 'U' muestro el ultimo valor de la pila.
            print ("El ultimo valor de la pila es "+str(pila[len(pila)-1])) #Obtengo su longitud e imprimo la ultima posicion.
            print ("\n")                                                                                    
        else:                                                               #Si no es porque decidio mostrar el indice del valor ingresado.
            eleccion = int(eleccion)                                        #Convierto el valor a entero para poder manejarlo.
            indices = [cont for cont,x in enumerate(pila) if x == eleccion] #Mediante un ciclo ingreso a un arreglo los indices en donde 
                                                                            #se encuentra el valor, para eso uso "enumerate" que lo que
                                                                            #hace es evaluar cada posicion de la pila en busca de 'x'.
            if len(indices) == 0:                   
                print ("Valor no encontrado en la pila.\n")                 #Si el arreglo no aumenta es porque no encontro el valor en la pila.
            else:
                indices = str(indices)                                      #Si si, convierto el arreglo y el valor a cadena para poder imprimirlos.
                eleccion = str(eleccion)
                print("\nEl valor "+eleccion+" se encuentra en la/s posiciones "+indices+" de la pila.")
                print()
def pop():                                          #Al ser llamado este metodo, elimina el ultimo valor de la pila,
    del pila[-1]                                    #para eso el [-1]
    
def Menu():                                         
    print ("1 - Mostrar valores de la pila.\n2 - Eliminar valor superior de la pila.\n3 - Ingresar valores a la pila.\n4 - Salir.")
    eleccion = int(input("Que desea realizar?: "))
    print()
    if eleccion == 1:                               #SI el usuario eligio mostrar los valores de la pila...
        if len(pila) >0:                            #Se compara si la pila tiene valores, si si se le pregunta el indice del valor que desea ver, o
            eleccion = str(input("Teclee 'T' para mostrar todos los valores de la pila,\nteclee 'U' para mostrar el ultimo valor de la pila,\no ingrese el valor que desea buscar en la pila: "))
            print()
            peek(eleccion)                          #Si desea ver todos los valores y se llama al metodo.
            Menu() 
        else:
            print ("La pila esta vacia.\n")         #Si no, se sabe que la pila esta vacia y no hay valores para mostrar.
            Menu()
    else:                                           #Si el usuario eligio eliminar valores de la pila...
        if eleccion == 2:
            indicepop = len(pila)                   #asigno a una variable el tamanio de la pila y la comparo...
            if indicepop>0:                         #Si es mayor a 0, puede llamar al metodo pop() porque tiene valores la pila.
                pop()
                print ("Elemento eliminado.\n")
                Menu()
            else:                                   #Si no, queire decir que la pila esta vacia.
                print ("La pila esta vacia.\n")
                Menu()
        else:                                       
            if eleccion == 3:                       #Si el usuario eligio ingresar valores a la pila lo hara solamente si hay espacio en la pila
                indice = len(pila)                  #mientras sea cierto ingresara los valores.
                while indice<= 4:                   #Llamo al metodo push() mientras el indice sea menor o igual a 4, que indica que hay cupo.
                    valor = int(input("Ingrese un valor entero ("+str(len(pila)+1)+"/5): "))    
                    indice = push(indice,valor)     #Le envio el indice y el valor a ingresar a la pila.
                print ("La pila esta llena")        #Si no indicara que la pila esta llena
                print()
                Menu()
            else:                                   
                if eleccion ==4:                    #Si el usuario eligio esta opcion es porque quiere salir, llamo al metodo reservado
                    sys.exit()                      #sys.exit() para salir del programa.
                else:
                    print ("Opcion incorrecta\n")   #Si no ante todas las condiciones, es porque escribio un digito incorrecto.
                    Menu()
                
while indice>=0 and indice<5:                       #Ciclo para llamar al metodo push() e ingresar los valores a la pila por primera vez.
    valor = int(input("Ingrese un valor entero ("+str(indice+1)+"/5): "))
    indice = push(indice,valor)

Menu()                                              #Llamo al Menu por primera vez para iniciar la recursividad.
