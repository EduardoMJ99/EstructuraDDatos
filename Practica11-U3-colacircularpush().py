colacircular = []           #Declaro e inicializo variables 
indicePUSH = 0
import sys                  #Importo esta libreria para poder salir del programa.

def push(indicePUSH,valor):                 #Metodo para ingresar valores a la cola
    colacircular.insert(indicePUSH,valor)   #Metodo insert propio de los arreglos donde le indico el indice y el valor.
    return indicePUSH+1                     #Regreso el indice aumentado para la sig insercion sea en la sig posicion.

def Menu(indicePUSH):                                       #Menu... (cada vez que llamo a menu le mando el indice que maneja el push
    print ("1.- Insertar elemento en la cola circular.\n"   #para conservar su valor en todo el programa).
           "2.- Salir.")
    eleccion = int(input("Que desea realizar?: ")) 
    if eleccion == 1:                                       #Si eligio esta opcion inserta valores siempre y cuando la cantidad
        if len(colacircular) < 5:                           #de valores sea menores a 5 (maximo que yo decido)
            indicePUSH = push(indicePUSH,int(input("\nIngrese un valor entero("+str(5-len(colacircular))+
                                                   " lugares disponibles): ")))
            print()
            Menu(indicePUSH)
        else:
            print ("\nLa cola esta llena...\n")             #Si no se cumple la condicion, significa que la cola esta llena.
            Menu(indicePUSH)
    else:
        if eleccion == 2:                                   #SI eligio esta opcion sale del programa.
            sys.exit()
        else:
            print ("Opcion incorrecta\n")
            Menu()
Menu(indicePUSH)                                            #Llamo por primera vez al programa para iniciar la recursividad.
