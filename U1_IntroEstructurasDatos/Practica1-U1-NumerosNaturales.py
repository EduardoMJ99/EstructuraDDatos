resultado = 1                           #Declaro e inicializo variable.

def Operacion(resultado):               #Metodo que recibe el valor 'resultado' y primero compara
    if resultado <= 100:                #si el valor es menor a 100, si si, lo imprime, si no, 
        print (resultado)               #llama a este metodo con el valor aumentado a uno y asi
        return (Operacion(resultado+1)) #recursivamente hasta que imprime el numero.

Operacion(resultado)                    #Llamo al metodo y le envio un parametro.
