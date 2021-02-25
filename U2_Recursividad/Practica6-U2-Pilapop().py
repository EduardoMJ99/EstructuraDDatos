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
    if eleccion == "T" or eleccion == "t":          #Si 'eleccion' es igual a 'T' o 't' muestra todos los valores de la pila.
        print (pila)
        print ("\n")
    else:
        if type(eleccion) == int:                   #Si 'eleccion' es de tipo entero continua, si no, imprime 'valor ingresado invalido'.
            eleccion = int(eleccion)
            if eleccion>=0 and eleccion<5:          #si 'eleccion' esta en el rango, muestra el valor del indice que el usuario eligio.
                print (pila[eleccion])
                print ("\n")
            else:                                   
                print ("Indice fuera de rango.\n")
        else:
            print ("Valor ingresado invalido.\n")
            
def pop():                                          #Al ser llamado este metodo, elimina el ultimo valor de la pila,
    del pila[-1]                                    #para eso el [-1]
    
def Menu():                                         
    print ("1 - Mostrar valores de la pila.\n2 - Eliminar valor superior de la pila.\n3 - Salir")
    eleccion = int(input("Que desea realizar?: "))
    if eleccion == 1:                               #SI el usuario eligio mostrar los valores de la pila...
        if len(pila) >0:                            #Se compara si la pila tiene valores, si si se le pregunta el indice del valor que desea ver, o
            eleccion = str(input("Teclee 'T' para mostrar toda la pila o ingrese el indice del valor que desea ver (0 a 4): "))
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
        else:                                       #Si el usuario eligio esta opcion es porque quiere salir, llamo al metodo reservado
            if eleccion == 3:                       #sys.exit() para salir del programa.
                sys.exit()                          
            else:                                   #Si no ante todas las condiciones, es porque escribio un digito incorrecto.
                print ("Opcion incorrecta\n")
                Menu()

while indice>=0 and indice<5:                                                   #Ciclo para llamar al metodo push() e ingresar los valores a la pila.
    valor = int(input("Ingrese un valor entero ("+str(indice+1)+"/5): "))
    indice = push(indice,valor)

Menu()                                              #Llamo al Menu por primera vez para iniciar la recursividad.
