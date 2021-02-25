colacircular = [0,0,0,0,0]           #Declaro e inicializo variables 
indicePUSH = 0
indicePOP = 0
import sys                          #Importo esta libreria para poder salir del programa.


def push(indicePUSH,valor):             #Metodo para ingresar valores a la cola.
    colacircular[indicePUSH] = valor    #Ingrese el valor envidado en el indice deseado.
    if indicePUSH >=4:                  #SI el indice llega a 4 se regresa al inicio de la cola (0).
        indicePUSH = -1
    return indicePUSH+1                 #Retorno el indice aumentado en 1 para la sig insercion.

def pop(indicePOP):                     #Metodo para eliminar valores de la cola.
    colacircular[indicePOP] = 0         #Cambio el valor que habia por 0 para interpretar que se ha eliminado.
    if indicePOP>=4:                    #Si el indice llega a 4 se regresa al inicio de la cola (0).
        indicePOP=-1
    return indicePOP+1                  #Retorno el indice aumentado en 1 para la sig eliminacion.

def Menu(indicePUSH,indicePOP):                                       #Menu...
    print ("1.- Insertar elemento en la cola circular.\n"             #Siempre mando los indices para mantener
           "2.- Eliminar elemento en la cola circular.\n"             #sus mismos valores en todo el programa.
           "3.- Salir.")
    eleccion = int(input("Que desea realizar?: "))

    lugaresdisponibles = len([cont for cont,x in enumerate(colacircular) if x==0])  #Esto lo utilizo para saber
                                                                                    #cuantos ceros tiene la cola.
    if eleccion == 1:
        if ((indicePOP!=indicePUSH) or (colacircular[indicePUSH]+colacircular[indicePUSH]==0)):             #Si los indices estan en distintos lugares
            indicePUSH = push(indicePUSH,int(input("\nIngrese un valor entero("+str(lugaresdisponibles)+    #o la suma de los valores en las posiciones
                                                   " lugares disponibles): ")))                             #en las que estan es cero, significa que hay
            print("Ingresado...\n")                                                                         #lugares disponibles en la cola.
        else:
            print ("\nLa cola circular esta llena...\n")
        Menu(indicePUSH,indicePOP)                                  #Mando los indices siempre para no perder sus valores en todo el programa.
    else:
        if eleccion == 2:                                           #Si eligio esta opcion es para eliminar,
            if colacircular[indicePOP]!=0:                          #Si el valor en el que esta el indice es distinto de cero significa que tiene
                indicePOP = pop(indicePOP)                          #valores para poder eliminar, si no es que la cola esta vacia.
                print("Eliminado...\n")
            else:
                print ("\nLa cola esta vacia...\n")             
            Menu(indicePUSH,indicePOP)                              #Mando los indices siempre para no perder sus valores en todo el programa.
        else:
            if eleccion ==3:                                        #SI eligio esta opcion sale del programa.
                sys.exit()
            else:
                print ("\nOpcion incorrecta\n")
                Menu(indicePUSH,indicePOP)
                
Menu(indicePUSH,indicePOP)                                          #Llamo por primera vez al programa para iniciar la recursividad.
