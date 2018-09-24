valor = [0,1]               #Inicializo el arreglo con sus 2 primeras posiciones a 0 y 1 ya que la formula del numero de Fibonacci no realiza la
global indicefinal          #operacion para estos 2 primeros numeros. Declaro la variable global para manejarla dentro y fuera del metodo.


def Fibonacci(indice):              #Metodo que recibe el valor 'indice' y compara si es mayor al indice final que es el numero que ingresa el
    if indice > indicefinal:        #usuario, si si significa que termino de calcula y termina.
        print ("...")
        return
    else:                                               #si no, ingresa al arreglo la suma del valor anterior y el valor anteanterior del mismo
        valor.append(valor[indice-1] + valor[indice-2]) #arreglo, para despues imprimirlo convirtiendo los valores a tipo string (str()) 
        print (str(valor[indice])+",", end ='')         #y no brincar renglon. Despues llama al mismo metodo enviandole el valor del 'indice'
        return Fibonacci(indice+1)                      #incrementado en uno.



indicefinal = int(input("Ingrese el numero del fibonacci deseado: "))   #Recibe el valor que el usuario ingresa.


print ("----------------------Recursividad------------------")
print ("0,1,",end ='')                  #Imprimo primero las 2 primeras posiciones del numero de Fibonacci ya que estas no se pueden calcular
Fibonacci(2)                            #con la formula para despues llamar al metodo con el parametro de 2 para que inicie en ese indice.

print ("----------------------Iteracion---------------------")
for indice in range(indicefinal+1):                 #Realiza el ciclo la cantidad de veces que ingreso el usuario el valor de Fibonacci
    valor.append(valor[indice-1] + valor[indice-2]) #Ingresa al arreglo la suma del valor anterior y el valor anteanterior del mismo arreglo, para
    print (str(valor[indice])+",", end ='')         #despues imprimirlo convirtiendo los valores a tipo string (str()) y no brincar renglon.

print ("...")
