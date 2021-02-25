cola = []                   #Declaro e inicializo mis variables
contador = 0
import sys                  #Importo esta libreria para salir del programa.

def push(elemento):                                                                 #Metodo que recibe el elemento a ingresar a la cola,
    cola.append(elemento)                                                           #esta funcion ingresa el elemento en la ultima posicion de la cola.
    print ("\nCliente ingresado("+str(5-len(cola))+" lugares disponibles)...\n")    #Imprime la cantidad de lugares disponibles para el usuario,
    
def pop():                                                                          #Metodo que elimina el proximo valor a salir de la cola...
    for indice in range(0,len(cola)-1,1):                                           #Este ciclo recorre los elementos de la cola pasando el valor
        cola[indice] = cola[indice+1]                                               #de la sig posicion en la actual, lo hara segun la cantidad de valores en la cola.
    del cola[-1]                                                                    #Ya que recorri todos los valores, elimino el ultimo para que este disponible,
    print ("\nEl cliente ha pasado...\n")                                           #para esto utilizo 'del cola[-1]', elimina el valor de la ultima posicion.
    
def peek():                                                                         #Metodo que muestra los clientes que hay en la cola...
    print("\nHay "+str(len(cola))+" cliente/s en la fila...")                       #Imprime la cantidad de valores que hay en la cola y cuales hay en ella.
    print(cola)
    print()
          
def Menu():
    global contador                                                                 #Llamo a la variable global contador para utilizarla dentro de este modulo.
    print("1.- Ingresar cliente en la fila.\n"
          "2.- Pasar el cliente que sigue a caja.\n"
          "3.- Mirar los clientes.\n"
          "4.- Terminar...")
    eleccion = int(input("Que desea realizar?: "))
    if eleccion ==1:                                                                #Si eligio esta opcion es para ingresar valores a la cola,
        if len(cola)>=5:                                                            #Si la cola tiene 5 o mas valores...
            print("\nLa fila esta llena, esperar a que se libere un espacio...\n")  #La cola esta llena.
        else:                                                                       #Si no...
            contador = contador+1                                                   #Hago un contador para ingresarlo a la cola y tomarlos como "numero de cliente".
            push(contador)                                                          #Llamo al metodo push y le envio el valor del contador.
        Menu()                              #Llamo a Menu para seguir recursividad.
    else:
        if eleccion ==2:                                                            #SI elgio esta opcion es para eliminar el sig valor de la cola.
            if len(cola)<=0:                                                        #Si la cola no tiene elementos significa que esta vacia.
                print("\nLa fila esta vacia...\n")
            else:                                                                   #Si no, llamo al metodo pop().
                pop()
            Menu()                          #Llamo a Menu para seguir recursividad.
        else:
            if eleccion ==3:                                                        #SI eligio esta opcion es para mostrar los valores de la cola.
                if len(cola)<=0:                                                    #Si la cola no tiene elementos significa que esta vacia.
                    print("\nLa fila esta vacia...\n")
                else:                                                               #Si no, llamo al metodo peek().
                    peek()
                Menu()                      #Llamo a Menu para seguir recursividad.
            else:
                if eleccion ==4:                                                    #Es para salir del programa, llamo al metodo reservado exit()
                    sys.exit()
                else:
                    print ("\nOpcion incorrecta...\n")                              #Opcion incorrecta si no es ninguna de las anteriores

Menu()                                  #Llamo al Menu pro primera vez para iniciar la recursividad.
