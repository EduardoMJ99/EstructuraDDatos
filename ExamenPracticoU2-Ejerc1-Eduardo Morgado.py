sumar = 0                   #Declaro e inicializo mi variable.

def Suma(sumar,contador):                       #Funcion que recibe 2 parametros, el valor a sumar y un contador
    if contador >=10:                           #Si el contador = 10 significa que termino de sumar 9 numeros, 
        print ("="+str(sumar))                  #imprimo resultado.
    else:                                       #SI no, sigo sumando valores a la variable
        if contador ==9:                        #Este If lo unico que hace es que en lugar de imprimir el contador concatenado con
            print (str(contador),end= '')       #el signo "+", lo imprime sin el ya que es el ultimo valor a sumar.
        else:
            print (str(contador)+"+",end= '')   #Imprimo el contador concatenado con el signo "+", es solo estetico.
        return Suma(sumar+contador,contador+1)  #RECURSIVIDAD, llamo al mismo metodo enviandole la variable que almacena la suma
                                                #aumentado con el contador, y le envio el contador incrementado en 1.
Suma(sumar,1)               #Para iniciar recursividad, inicio del numero uno.
