Bicola = [0,0,0,0,0,0,0,0,0,0]              #Inicializo mis variables, la bicola tendra 10 valores como maximo.
indFRONTi = 0
indREARi = 0                            #Mis indices que manipulan la izquierda inician en 0 y los de la derecha en 9 (ultima posicion).
indFRONTd = 9
indREARd = 9
import sys                              #Utilizo esta libreria para salir del programa.
    
def pushDerecha(indREARd,valor):        #Metodo push por la derecha solamente. Inserta el valor enviado en el indice deseado.
    Bicola[indREARd] = valor
    if indREARd <= 0:                   #Si el indice llega a 0 se regresa a 10 que es el otro extremo. retorno el indice disminuido en 1
        indREARd = 10                   #para la sig insercion.
    return indREARd-1

def pushIzquier(indREARi,valor):        #Metodo push por la izquierda solamente. Inserta el valor enviado en el indice deseado.
    Bicola[indREARi] = valor
    if indREARi >=9:                    #Si el indice llega a 9 se regresa a 0 que es el otro extremo. retorno el indice disminuido en 1
        indREARi = -1                   #para la sig insercion.
    return indREARi+1

def Menu():                             #Menu donde manejo todos mis indices para no perder sus valores durante el programa.
    global indFRONTi
    global indREARi
    global indFRONTd
    global indREARd
    print("1.- Insertar elemento en la bicola circular.\n"
          "2.- Salir.")
    eleccion = int(input("Que desea realizar?: "))
    lugaresdisponibles = len([cont for cont,x in enumerate(Bicola) if x==0])    #Utilizo este arreglo con un for para saber cuantos 0 hay en la bicola y asi
    if eleccion ==1:                                                            #saber cuantos lugares disponibles tiene.
        if (lugaresdisponibles!=0):                                                     #Si los lugares disponibles son diferentes de 0 significa que 
            valor = int(input("Ingrese un valor entero("+str(lugaresdisponibles)+       #hay lugares disponibles.
                              " lugares disponibles): "))
            eleccion = str(input("Teclee\t'I' si por la izquierda, o\n"                 #Le pregunto al usuario que si quiere ingresar por la izquierda
                                 "\t'D' si por la derecha: "))                          #o si por la derecha de la bicola.
            if eleccion == 'I':
                indREARi = pushIzquier(indREARi,valor)                                  #Mando a llamar al metodo correspondiente con sus parametros.
            elif eleccion == 'D':
                indREARd = pushDerecha(indREARd,valor)                                  #Mando a llamar al metodo correspondiente con sus parametros.
            else:
                print("\nOpcion incorrecta...\n")                                       #Si los lugares disponibles es 0, es que no hay lugares.
            print("\nIngresado...\n")
        else:
            print("\nLa bicola circular esta llena...\n")
        print(Bicola)
        Menu()
    elif eleccion ==2:                                                                  #Utilizo esta libreria para cerrar el programa.
        sys.exit()
    else:
        print("\nOpcion incorrecta...\n")
        Menu()
Menu()                                                                      #LLamo al Menu por primera vez para iniciar la recursividad.
            
        
    
