cola = []           #Declaro mis variables
import sys          #Importo esta libreria para poder salir del programa.

def Crear():                                            #Metodo que inicializa la cola a ceros.
    cola = [0,0,0,0,0]                                  #Regreso la cola inicializada.
    return cola
    
def push(valor,indice):                                 #Metodo que ingresa valores a la cola.
    cola[indice] = valor                                #Se ingresa el valor en el indice.
    return indice+1                                     #Regreso el indice aumentado en uno.

def pop():
    if cola[0] == 0:                                                
        print ("La cola esta vacia.\n")                             #Si la primera posicion tiene 0 es porque la cola esta vacia.
    else:
        for indicecola in range(0,4,1):                             #Cada vez que se quiere eliminar un elemento hay que recorrer los valores de la pila.
            cola[indicecola] = cola[indicecola+1]
        cola[4] = 0                                                 #A la ultima posicion de la cola le asigno un 0.
        print ("Elemento eliminado.\n")

def peek(eleccion):
    if eleccion == "T":                             #Si 'eleccion' es igual a 'T' muestra todos los valores de la cola.
        print (cola)
        print ("\n")
    else:
        if eleccion == "U":                                                 #SI 'eleccion' es igual a 'U' muestro el ultimo valor de la pila.
            print ("El ultimo valor de la cola es "+str(cola[len(cola)-1])) #Obtengo su longitud e imprimo la ultima posicion.
            print ("\n")                                                                                    
        else:                                                               #Si no es porque decidio mostrar el indice del valor ingresado.
            if eleccion == "P":
                print ("El primer valor de la cola es "+str(cola[0]))
                print ("\n")
            else:
                eleccion = int(eleccion)                                        #Convierto el valor a entero para poder manejarlo.
                indices = [cont for cont,x in enumerate(cola) if x == eleccion] #Mediante un ciclo ingreso a un arreglo los indices en donde 
                                                                                #se encuentra el valor, para eso uso "enumerate" que lo que
                                                                                #hace es evaluar cada posicion de la pila en busca de 'x'.
                if len(indices) == 0:                   
                    print ("Valor no encontrado en la pila.\n")                 #Si el arreglo no aumenta es porque no encontro el valor en la pila.
                else:
                    indices = str(indices)                                      #Si si, convierto el arreglo y el valor a cadena para poder imprimirlos.
                    eleccion = str(eleccion)
                    print("\nEl valor "+eleccion+" se encuentra en la/s posiciones "+indices+" de la pila.")
                    print()


def Menu():                                             #Metodo que muestra la interfaz del programa al usuario.
    global cola                                         #LLamo a mi variable global cola.
    print ("1 - Crear la cola.\n"                        #Interfaz...
           "2 - Insertar valores a la cola.\n"
           "3 - Eliminar valores de cola.\n"
           "4 - Mostrar valores de la cola.\n"
           "5 - Salir.")
    eleccion = int(input("Que desea realizar?: "))
    print()
    if eleccion == 1:                                   #Si el usuario elige esta opcion llama al metodo Crear() y regresa la cola 
        cola = Crear()                                  #inicializada en ceros.
        print("Cola creada...\n")
        Menu()                                          #LLamo a Menu() para seguir con recursividad.
    else:
        if eleccion == 2:                                                           #Si el usuario elige esta opcion...
            if len(cola) > 0:                                                       #Averiguo si la cola tiene valores para saber si ha sido creada.
                lugaresdisponibles = [cont for cont,x in enumerate(cola) if x == 0] #Ingreso a una variable todos los ceros que tenga la cola ya que
                indicecola = len(lugaresdisponibles)                                #estos me indican cuantos lugares disponibles hay en la cola.
                indiceciclo = 0                                                     #Cuento los ceros y asi determinar cuantos valores puedo ingresar.

                try:                                                                #Para saber donde iniciar a ingresar valores a la cola busco el primer cero,
                    dondeiniciar = cola.index(0)                                    #de esta manera me regresa el indice del primer cero y de ahi inicio.
                except:                                                             #Si no hay ningun valor con 0 significa que esta llena, para corregir este error
                    pass                                                            #utiliza un catch - except.
                
                while (indiceciclo) < len(lugaresdisponibles):                      #Mientras que el indice sea menor a los lugares disponibles...
                    valor = int(input("Ingrese valores enteros (Espacios disponibles: "+str(indicecola)+") : "))    #Le pido un valor entero y le muestro
                    dondeiniciar = push(valor,dondeiniciar)                                                         #cuantos lugares disponibles hay.
                    indicecola = indicecola -1                                      #Llamo al metodo push() e ingreso el valor que ingreso al usuario
                    indiceciclo = indiceciclo +1                                    #en la posicion donde se debe iniciar segun los lugares disponibles.
                                                                                    #Me regresa el indice aumentado y resto los lugares disponibles.

                print("La cola esta llena.\n")                                      
                Menu()                                                              #LLamo a Menu() para seguir con recursividad.
            else:
                print("La cola no ha sido creada, favor de crearla...\n")           #Si la cola no tiene indices es porque no ha sido creada.
                Menu()                                                              #LLamo a Menu() para seguir con recursividad.
        else:
            if eleccion == 3:                                                       #Si el usuario eligio esta opcion quiere eliminar un valor de la cola...                        
                if len(cola) > 0:                                                   #Si la cola tiene valores...
                    pop()
                else:
                    print("La cola no ha sido creada, favor de crearla...\n")       #Si la cola no tiene indices es porque no ha sido creada.
                Menu()
            else:
                if eleccion == 4:                                                    #Si el usuario eligio esta opcion salgo del programa llamando a este metodo reservado.
                    if len(cola) >0:                            #Se compara si la pila tiene valores, si si se le pregunta el indice del valor que desea ver, o
                        eleccion = str(input("Teclee 'T' para mostrar TODOS los valores de la cola,\nteclee 'U' para mostrar el ULTIMO valor de la cola,\nteclee 'P'"
                                             "para mostrar el PRIMER valor de la cola,\no ingrese el valor que desea buscar en la cola: "))
                        print()
                        peek(eleccion)                          #Si desea ver todos los valores y se llama al metodo. 
                    else:
                        print ("La cola esta vacia.\n")         #Si no, se sabe que la pila esta vacia y no hay valores para mostrar.
                    Menu()
                else:
                    if eleccion == 5:
                        sys.exit()
                    else:
                        print ("Opcion incorrecta...\n")        #SI no es ninguna de las opciones le muestro opcion incorrecta.
                        Menu()                                  #LLamo a Menu() para seguir con recursividad.

Menu()                                                  #LLamo a Menu() para empezar la recursividad.
