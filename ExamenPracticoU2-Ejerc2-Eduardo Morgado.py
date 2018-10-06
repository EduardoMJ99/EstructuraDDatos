exponente = 0                       #Declaro e incializo mis variables
resultado = 2                       #Inicio en 2 ya que es base 2.

try:
    def Exponencial(resultado,exponente):                   #Funcion que recibe el resultado que se esta multiplicando y el exponente que ingresa el usuario
        if (exponente<=1):                                  #Si el exponente es igual o menor a 1 termino e imprimo el resultado
            print ("Resultado = "+str(resultado))
        else:                                               #Si no, llamo a la misma funcion enviandole la variable multiplicada por 2 y el
            return Exponencial(resultado*2,exponente-1)     #exponente reducido en 1 para llegar a un momento en que termina la multiplicacion,

    Exponencial(resultado,int(input("Ingrese el numero entero al que desea elevar la base 2... :")))    #Llamo por primera vez a la funcion
                                                                                                        #donde le envio la variable inicial en 2
                                                                                                        #y el exponente que ingresa el usuario.
                                                                                                                                                                   
except ArithmeticError:                                     #Cuido que no haya un error aritmetico,(overflow, flotantes...)
    print ("\nValor demasiado grande...")
except RecursionError:                                      #Phyton tiene un limite de llamadas recursivas, cuido este error.
    print ("\nOperaciones excedidas....")
    
