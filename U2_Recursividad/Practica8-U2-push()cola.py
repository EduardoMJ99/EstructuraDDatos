cola = []           #Declaro mis variables
import sys          #Importo esta libreria para poder salir del programa.

def Crear():                                            #Metodo que inicializa la cola a ceros.
    cola = [0,0,0,0,0]                                  #Regreso la cola inicializada.
    return cola
    
def push(valor,indice):                                 #Metodo que ingresa valores a la cola.
    cola[indice] = valor                                #Se ingresa el valor en el indice.
    return indice+1                                     #Regreso el indice aumentado en uno.

def Menu():                                             #Metodo que muestra la interfaz del programa al usuario.
    global cola                                         #LLamo a mi variable global cola.
    print ("1- Crear la cola.\n"                        #Interfaz...
           "2- Insertar valores a la cola.\n"
           "3- Salir.")
    eleccion = int(input("Que desea realizar?: "))
    if eleccion == 1:                                   #Si el usuario elige esta opcion llama al metodo Crear() y regresa la cola 
        cola = Crear()                                  #inicializada en ceros.
        print("Cola creada...\n")
        Menu()                                          #LLamo a Menu() para seguir con recursividad.
    else:
        if eleccion == 2:                                                           #Si el usuario elige esta opcion...
            if len(cola) > 0:                                                       #Averiguo si la cola tiene valores para saber si ha sido creada.
                lugaresdisponibles = [cont for cont,x in enumerate(cola) if x == 0] #Ingreso a una variable todos los ceros que tenga la cola ya que
                if len(lugaresdisponibles)!=5:
                    print("La cola esta llena.\n")                                      
                    Menu()
                else:
                    indicecola = len(lugaresdisponibles)                                #estos me indican cuantos lugares disponibles hay en la cola.
                    indiceciclo = 0                                                     #Cuento los ceros y asi determinar cuantos valores puedo ingresar.
                    dondeiniciar = cola.index(0)
                    while (indiceciclo) < (len(lugaresdisponibles)):                      #Mientras que el indice sea menor a los lugares disponibles...
                        valor = int(input("Ingrese valores enteros (Espacios disponibles: "+str(indicecola)+") : "))    #Le pido un valor entero y le muestro
                        dondeiniciar = push(valor,dondeiniciar)                                                           #cuantos lugares disponibles hay.
                        indicecola = indicecola -1                                      #Llamo al metodo push() e ingreso el valor que ingreso al usuario.
                        indiceciclo = indiceciclo+1
                    print("La cola esta llena.\n")                                      #Me regresa el indice aumentado y resto los lugares disponibles.
                    Menu()                                                              #LLamo a Menu() para seguir con recursividad.
            else:
                print("La cola no ha sido creada, favor de crearla...\n")           #Si la cola no tiene indices es porque no ha sido creada.
                Menu()                                                              #LLamo a Menu() para seguir con recursividad.
        else:
            if eleccion == 3:                           #Si el usuario eligio esta opcion salgo del programa llamando a este metodo reservado.
                sys.exit()
            else:
                print("Opcion incorrecta...\n")         #SI no es ninguna de las opciones le muestro opcion incorrecta.
                Menu()                                  #LLamo a Menu() para seguir con recursividad.

Menu()                                                  #LLamo a Menu() para empezar la recursividad.
