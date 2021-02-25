numero = 0                                                              #Declaro e inicializo variables.
indice = 0                                                              
                                                                        
def Factorial(numero,indice):                                           #El metodo recibe 2 parametros, si 'indice' es igual a 0, termina el metodo,
    if indice ==0:                                                      #si no,
        return
    else:                                                               #imprime la conversion de las variables a tipo string (str()) y utilizo el
        print ("{0} x {1} = ".format(str(numero),str(indice)), end = '')#end='' para indicar que no brinque renglon al momento de imprimir.
        numero = numero * indice                                        #el valor de 'numero' cambia a la multiplicacion de su valor con el indice
        print (numero)                                                  #Imprimo el valor de numero y llamo a este metodo enviandole el nuevo valor
        return (Factorial(numero,indice-1))                             #de 'numero' y el valor de 'indice' decrementado en uno.



numero = int(input("Factorial de: "))                                   #Recibo el valor que desea el usuario hacer factorial.
print ("----------------------Recursividad------------------")
Factorial(numero,numero-1)                                              #Llamo al metodo con los valores de las variables.
print ("----------------------Iteracion---------------------")
for indice in range(numero-1,0,-1):                                     #Iteracion que inicia en el valor que el usuario ingreso menos uno, termina
    print ("{0} x {1} = ".format(str(numero),str(indice)), end = '')    #hasta que llega a cero y decrementa en uno. 
    numero = numero * indice                                            #En el cuerpo del ciclo hace lo mismo que el metodo 'Factorial'
    print (numero)                                                      #Imprimo el valor de numero ya multiplicado por indice.
