

import pprint
import random 
import time
import os


#Lo primero del todo es crear el tablero con esta definición PARA TI, para colocar tus barcos 

def crear_tablero():
    tablero = []
    columnas = ["   a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    tablero.append(columnas)
    filas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(0, 10):
        linea = []
        linea.append(i + 1)
        for j in range(0, 10):
            linea.append(" ")
        tablero.append(linea)
    return tablero



#al inicializarse el juego, se da el mensaje de bienvenida y se presenta el tablero vacío 


def mensaje_bienvenida():
    #TAMANO = 10
    # tablero_usuario = crear_tablero(TAMANO) #crear tablero con el tamaño deseado
    print("Bienvenido al juego de HLF. Aquí tienes tu tablero:\n")
    

#se llama a la funcion para que se coloquen los barcos fijos en el TABLERO DEL ORDENADOR 

def posicionar_barcos_fijos(tablero_computer):
    # Colocando barco1
    tablero_computer[3][3] = "B"
    tablero_computer[4][3] = "B"
    tablero_computer[5][3] = "B"
    tablero_computer[6][3] = "B"
    
    #Colocando barco2
    tablero_computer[3][4] = "B"
    tablero_computer[4][4] = "B" 
    tablero_computer[5][4] = "B"
    #barco3
    tablero_computer[3][8] = "B"
    #barc4
    tablero_computer[2][6] = "B"
    #barco5
    tablero_computer[6][2] = "B"
    #barco6
    tablero_computer[4][1] = "B"
    #barco7
    tablero_computer[10][3] = "B"
    tablero_computer[10][4] = "B"
    #barco8
    tablero_computer[8][5] = "B"
    tablero_computer[8][6] = "B"
    #barco9
    tablero_computer[9][8] = "B"
    tablero_computer[9][9] = "B"
    #barco10
    tablero_computer[5][9] = "B"
    tablero_computer[6][9] = "B"
    tablero_computer[7][9] = "B"
    
    return tablero_computer


#ahora vamos a intentar conseguir que el usuario pueda añadir sus propios barcos!
    

def colocar_barcos_usuario(tablero):
    print("Vamos a añadir tus barcos")
    os.system("cls")
    barcos_size = [4,3]
                   # 3,2,2,2,1,1,1,1]
    for z in range(len(barcos_size)):
        os.system("cls")
        
        if barcos_size[z] == 4:
            print("Primero añadiremos el porta-aviones de 4 posiciones")
        elif barcos_size[z] == 3:
            print("Luego un barco de 3 posiciones")    
  #      elif barcos_size[z] == 2:
 #           print("Ahora toca un barco de 2 posiciones")
 #       else:
  #          print("Por último los barcs de una posición")
        
        pprint.pprint(tablero) 
        while True:
            
            try:
                # Entrada de la fila
                fila1 = int(input("Dame el número de fila donde quieres colocarlo (1-10): "))
                if fila1 < 1 or fila1 > 10:
                    raise ValueError("El número de fila debe estar entre 1 y 10.")
                
                # Entrada de la columna
                columna1 = input("Ahora dame la letra de la columna donde lo quieres (a-j): ").lower()
                if columna1 not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
                    raise ValueError("La letra de la columna debe ser entre 'a' y 'j'.")
                
                # Entrada de la orientación
                orientacion = input("Dime hacia donde lo quieres crear: Escribe uno: N, S, E, O: ").upper()
                if orientacion not in ['N', 'S', 'E', 'O']:
                    raise ValueError("La orientación debe ser N, S, E, o O.")

                # Si todas las entradas son correctas, salimos del bucle
                break
            except ValueError as ve:
                print(f"Error: {ve}. Intenta de nuevo.")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}. Intenta de nuevo.")    
                
                
        # Convertimos la letra de la columna a índice
        columna1 = ord(columna1) - ord('a')  # Convierte de letra a índice (1-10)
        
        
        # Verificamos si las coordenadas están dentro de los límites del tablero
        if not (0 <= fila1 < 11 and 0 <= columna1 < 11):
            print("Coordenadas fuera de los límites. Intentalo de nuevo.")
            return tablero
        
        # Ahora comprobamos si hay suficiente espacio para colocar el barco
        
        if orientacion == "S":
            if 11 < fila1 <= 0:
                print("No hay suficiente espacio.")
                #Como puedo hacer para mandarlo de nuevo a introducir coordenadas???
            else:
                for i in range(barcos_size[z]):
                    #print(range(barcos_size[z]))
                    #print(barcos_size[z])
                    tablero[fila1 + i][columna1 + 1] = "B"
        elif orientacion == "N":
            if 10 < fila1 < 0:
                print("No hay suficiente espacio.")
            else:
                for i in range(barcos_size[z]):
                    tablero[fila1 - i][columna1 + 1] = "B"
        elif orientacion == "E":
            if 10 < fila1 < 0:
                print("No hay suficiente espacio.")
            else:
                for i in range(barcos_size[z]):
                    tablero [fila1][columna1 + i + 1] = "B"
        elif orientacion == "O":
            if 10 < fila1 < 0:
                print("No hay suficiente espacio.")
            else:
                for i in range(barcos_size[z]):
                    tablero [fila1][columna1 - i + 1] = "B"
        time.sleep(1)
    return tablero
   
       
        
 #Una vez terminado la colocación de los barcos, se visualizan 2 tableros: 
 #TABLERO CON BARCOS. del jugador para que vea sus barcos y los disparos que recibe
 # TABLERO VACÍO: la representación del tablero del ordenador, para que sepa donde ha disparado ya y si ha acertado o no
    
def visualizar(tablero, tablero_computer_visualizar):
    print("Aquí tienes tu tablero con todos tus barcos \n")
    pprint.pprint(tablero)
    
    
    print("\n Aquí tienes el tablero de tu contrincante para que puedas ver tus disparos \n")
    pprint.pprint(tablero_computer_visualizar)  
    
    
    
    #se configura el disparo pidiendo dos imputs de posición al usuario y viendo los 3 posibles impactos:

def disparo_jugador(tablero_computer, tablero_computer_visualizar):
    ganador1 = False
    continuar = True
    while continuar == True:
        os.system("cls")
        print("disparemos")
        pprint.pprint(tablero_computer_visualizar)
        i = int(input("Dame el número de fila donde quieres disparar (1-10):")) 
        j = input("Ahora dame la letra de la columna (a-j):").lower()
        # Convertimos la l3
        # etra de la columna a índice
        j = ord(j) - ord('a') # Convierte de letra a índice (1-10)
        
        j = j + 1
        if not (0 <= i < 11 and 0 <= j < 11):
            print("Coordenadas fuera de los límites. Intentalo de nuevo.")
            
        
        elif tablero_computer[i][j] == "B":
            print("Tocado!")   #si la coordenada proporcionada da a una B, es un barco por tanto será TOCADO el mensaje y se sigue jugando
            time.sleep(1)
            tablero_computer[i][j] = "X"
            tablero_computer_visualizar[i][j] = "X"
            pprint.pprint(tablero_computer_visualizar)
            ganador1 = False
            ganador1 = ganador(tablero_computer)
            if ganador1 == True:
                print("GANASTE!! ZORIONAK!!")
                break
            else:
                print("sigue jugando!")
                time.sleep(2)
        
        
        elif tablero_computer[i][j] == " ":  # Si la coordenada da un espacio vacío, se pasa el mensaje AGUA y acaba su turno
            print("Agua")
            time.sleep(1)
            tablero_computer[i][j] = "O"
            tablero_computer_visualizar[i][j] = "O"
            pprint.pprint(tablero_computer_visualizar)

            print("Turno de tu oponente")
            continuar = False
            time.sleep(2)
        else:    #Otra opción es que el usuario repita coordenada y entonces saltará este mensaje y perderá turno
            print("Ya habías disparado allí")
            
    return ganador1     
        # ahora la función que usará el ordenador para disparar 
        
def disparo_computer(tablero):
    ganador1 = False
    continuar = True
    while continuar == True:   
        i = random.randint(1, 10)
        j = random.choice("abcdefghij")
        #random.randrange
        j = ord(j) - ord('a')
        j = j + 1
        print(i, j)
        
        if tablero[i][j] in ["O", "X"]:
        # Si ya se ha disparado ahí, probar de nuevo
            time.sleep(1)
            continue
        
        
        if tablero[i][j] == "B":
            print("Tocado!")   #si la coordenada proporcionada da a una B, es un barco por tanto será TOCADO el mensaje y se sigue jugando
            tablero[i][j] = "X"
            pprint.pprint(tablero)
            time.sleep(2)
            
            ganador1 = ganador(tablero)
            if ganador1 == True:
                print("Perdiste mierdecilla!! Más suerte la próxima vez!")
                break
            else:
                print("El contrincante sigue jugando!")
                time.sleep(2)
                continue 
        
        elif tablero[i][j] == " ":  # Si la coordenada da un espacio vacío, se pasa el mensaje AGUA y acaba su turno
            print("Agua")
            tablero[i][j] = "O"
            pprint.pprint(tablero)
            time.sleep(2)
            print("Te toca!")
            continuar = False
            time.sleep(2)  
        
    return continuar
        
        #else:    #Otra opción es que el usuario repita coordenada y entonces saltará este mensaje y perderá turno
           # print("Ya ha disparado allí, volverá a probar")
           # return True
        
    return ganador1
   
   # funcion de ganador!!!     
   
def ganador(tablero):
    
    for fila in tablero:
        for z in fila:
            if z == "B":
                ganador1 = False
                return ganador1
        
     
    return True