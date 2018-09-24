import sys                  #Importo esta libreria para poder usar el metodo   sys.exit()   que es terminar el programa.
valor = [0,1]               #Inicializo el arreglo con sus 2 primeras posiciones a 0 y 1 ya que la formula del numero de Fibonacci no realiza la
                            #operacion para estos 2 primeros numeros.
def Menu():
    print ("\n------------------------------------------------------\n")        #Creo el metodo Menu para que el usuario elija que desea realizar.
    print ("1 - Imprimir los primeros 100 numeros naturales.\
    \n2 - Factorial de un numero.\n3 - Fibonacci de un numero.\
    \n4 - Salir")
    
    opcion = int(input("Que operacion desea realizar?: "))              #Si eligio '1' llamo al metodo Operacion enviandole el valor de 1 ya que 
    if opcion ==1:                                                      #inicia la impresion de los primeros 100 numeros naturales.
        resultado=1
        Operacion(resultado)
        Menu()                                                          #Al terminar llamo al metodo Menu() para continuar con el programa.
    else:
        if opcion ==2:                                                  #SI eligio '2', le pido que ingrese el numero que desea saber factorial, llamo
            numero = int(input("Factorial de: "))                       #al metodo enviandole el parametro de valor que ingreso y el mismo valor -1
            Factorial(numero,numero-1)
            Menu()                                                      #Al terminar llamo al metodo Menu() para continuar con el programa.
        else:
            if opcion ==3:                                              #Si eligio '3' creo la variale global para poder usarla fuera del metodo.
                global indicefinal                                      
                indicefinal = int(input("Ingrese el numero del fibonacci deseado: "))
                print ("0,1,",end ='')          #Imprimo primero las 2 primeras posiciones del numero de Fibonacci ya que estas no se pueden calcular
                Fibonacci(2)                    #con la formula para despues llamar al metodo con el parametro de 2 para que inicie en ese indice.
                Menu()                          #Al terminar llamo al metodo Menu() para continuar con el programa.
            else:
                if opcion ==4:                  #Si eligio esta opcion quiere salir del programa asi que uso este metodo reservado para salir.
                    sys.exit()

                    #La documentacion de los siguientes metodos se encuentran en las practicas anteriores correspondientes.

def Operacion(resultado):
    if resultado <= 100:
        print (resultado)
        return (Operacion(resultado+1))

def Factorial(numero,indice):
    if indice ==0:
        return
    else:
        print ("{} x {} = ".format(str(numero),str(indice)), end = '')
        numero = numero * indice
        print (numero)
        return (Factorial(numero,indice-1))
    
def Fibonacci(indice):
    if indice > indicefinal:
        print ("...")
        return
    else:
        valor.append(valor[indice-1] + valor[indice-2])
        print (str(valor[indice])+",", end ='')
        return Fibonacci(indice+1)
    
Menu()
