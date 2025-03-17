from HLFfunciones import * #de funciones importame todo lo que haya
import pprint
import time
import os

def main():
    
    mensaje_bienvenida()
    #paso 1: creamos el tablero del usuario
    tablero = crear_tablero()
    pprint.pprint(tablero)
    time.sleep(1)
    #paso 2, tablero del ordenador
    tablero_computer = crear_tablero()

    #paso 3, 
    tablero_computer_visualizar = crear_tablero() 
    time.sleep(2)
    #paso 4, se llama a la funcion para que se coloquen los barcos fijos en el TABLERO DEL ORDENADOR
    tablero_computer = posicionar_barcos_fijos(tablero_computer)
    print("Los barcos de tu oponente, ya están listos. Vamos a colocar tus barcos:")
    time.sleep(2)
    #paso 5.ahora vamos a intentar conseguir que el usuario pueda añadir sus propios barcos!
    tablero = colocar_barcos_usuario(tablero)
   
    time.sleep(2)
    os.system("cls")
    #paso 6. Una vez terminado la colocación de los barcos, se visualizan 2 tableros: 
    #TABLERO CON BARCOS. del jugador para que vea sus barcos y los disparos que recibe
    # TABLERO VACÍO: la representación del tablero del ordenador, para que sepa donde ha disparado ya
    visualizar(tablero, tablero_computer_visualizar)
    time.sleep(6)
    
    ganador1 = False
    
    while ganador1 == False: 
        
        #se configura el disparo pidiendo dos imputs de posición al usuario y viendo los 3 posibles impactos:
        ganador1 = disparo_jugador(tablero_computer, tablero_computer_visualizar)
        time.sleep(2)
        if ganador1 == True:
            break

        time.sleep(1)   
        # ahora la función que usará el ordenador para disparar 
    
        ganador1 = disparo_computer(tablero)   
        time.sleep(2)



main()