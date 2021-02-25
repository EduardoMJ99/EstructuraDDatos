valor = 0                                   #Declaro e inicializo mis variables.
indice = 0
eleccion = ""
pila=[]

def push(indice, valor):                    #Metodo se encarga de ingresar valores a la pila.
    pila.append(valor)                      #Regresa el valor del indice incrementado en 1.
    return indice +1
    
def peek(eleccion):                         #Metodo se encarga de mostrar al usuario lo que hay dentro de la pila.
    if eleccion == "T":                     #Si 'eleccion' es igual a 'T' muestra todos los valores de la pila.
        print (pila)
    else:
        eleccion = int(eleccion)            #si no, muestra el valor del indice que el usuario eligio mientras este se encuentra en el rango
        if eleccion>=0 and eleccion<5:      #permitido (0 a 4). 
            print (pila[eleccion])          #Imprime el valor del indice de la pila.
        else:
            print ("Indice fuera de rango") #Si no, indica que el indice esta fuera de rango.
            
while indice>=0 and indice<5:                                               #Ingresara valores a la pila mientras el indice este en el rango.
    valor = int(input("Ingrese un valor entero ("+str(indice+1)+"/5): "))   #Recibe el valor y concateno el indice para que el usuario sepa cuantos lleva
    indice = push(indice,valor)                                             #Llamo al metodo enviandole 2 parametros y me regresa el valor del indice
                                                                            #aumentado en uno.
eleccion = str(input("Teclee 'T' para mostrar toda la lista o ingrese el indice del valor que desea ver (0 a 4): "))
peek(eleccion)          #Llamo al metodo.
