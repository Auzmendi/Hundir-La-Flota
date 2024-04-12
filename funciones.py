import numpy as np
import random
import time
import variables as var

def  init_tablero():
    tablero = np.full((10,10),' ')
    tablero_oculto = np.full((10,10),' ')
    tablero_maquina =  np.full((10,10),' ')
    # print(tablero)
    return tablero,tablero_oculto,tablero_maquina

def chequear_alrededor(tablero,barco,coordenada_init_x,coordenada_init_y):
    if coordenada_init_x!=0 and coordenada_init_y!=0:
            tab_check = tablero[(coordenada_init_x-1) : (coordenada_init_x + 1 + len(var.espacios_libres[barco])),(coordenada_init_y-1) : (coordenada_init_y+2)]
    elif coordenada_init_x==0 and coordenada_init_y!=0:
            tab_check = tablero[(coordenada_init_x) : (coordenada_init_x + 1 + len(var.espacios_libres[barco])),(coordenada_init_y-1) : (coordenada_init_y+2)]            
    elif coordenada_init_x!=0 and coordenada_init_y==0:
            tab_check = tablero[(coordenada_init_x-1) : (coordenada_init_x + 1 + len(var.espacios_libres[barco])),(coordenada_init_y) : (coordenada_init_y+2)]
    elif coordenada_init_x==0 and coordenada_init_y==0:
            tab_check = tablero[(coordenada_init_x) : (coordenada_init_x + 1 + len(var.espacios_libres[barco])),(coordenada_init_y) : (coordenada_init_y+2)]
            
            
    return tab_check


def colocar_barco(tablero):
    longitud =4

    for barco in  var.barcos_largos:
        # print('-'*100)
        # print(f'Coloco el barco : {barco}')
        colocado = False
        
        while colocado == False:
            coordenada_init_x = np.random.randint (0,10)
            coordenada_init_y = np.random.randint (0,10)
            orien=np.random.choice(['S','E'])
            # print(f'La orientación es: {orien}')
            # print(f'Coordenadas :{(coordenada_init_x,coordenada_init_y)}')
            if orien == 'S':
                coordenada_final_x = coordenada_init_x + len(var.espacios_libres[barco]) 
                coordenada_final_y = coordenada_init_y
                if (coordenada_final_x > 9) or (coordenada_final_x < 0 ) or (coordenada_final_y > 9) or (coordenada_final_y < 0 ) :
                    # print('No se puede colocar el barco')
                    continue
            elif orien == 'E':
                coordenada_final_x = coordenada_init_x 
                coordenada_final_y = coordenada_init_y + len(var.espacios_libres[barco]) 
                if (coordenada_final_x > 9) or (coordenada_final_x < 0 ) or (coordenada_final_y > 9) or (coordenada_final_y < 0 ) :
                    # print('No se puede colocar el barco')
                    continue
            # time.sleep(0.8)
            hay_barco = False
            
            if list(tablero[coordenada_init_x : coordenada_init_x + len(var.espacios_libres[barco]) , coordenada_init_y]) == list(var.espacios_libres[barco]) and (orien =='S') and barco!=var.barco_1 :
                tab_check=chequear_alrededor(tablero,barco,coordenada_init_x,coordenada_init_y)
                
                if 'O' in tab_check:
                    # print('Hay un barco en ese camino')
                    hay_barco = True
                else:
                    tablero[coordenada_init_x : coordenada_init_x + len(var.espacios_libres[barco]) , coordenada_init_y] = 'O'
                    colocado = True
                    # print(tablero)
                
                    
            
            elif list(tablero[coordenada_init_x , coordenada_init_y]) ==list(var.espacios_libres[barco]) and (orien =='S') and barco==var.barco_1 :
                tab_check = chequear_alrededor(tablero,barco,coordenada_init_x,coordenada_init_y)
                if 'O' in tab_check:
                    # print('Hay un barco en ese camino')
                    hay_barco = True
                else:
                    tablero[coordenada_init_x : coordenada_init_x + len(var.espacios_libres[barco]) , coordenada_init_y] = 'O'
                    colocado = True
                    # print(tablero)
            
            elif  list(tablero[coordenada_init_x , coordenada_init_y : coordenada_init_y + len(var.espacios_libres[barco]) ]) == list(var.espacios_libres[barco]) and (orien =='E') and  barco!=var.barco_1:
                tab_check = chequear_alrededor(tablero,barco,coordenada_init_x,coordenada_init_y)
                if 'O' in tab_check:
                    # print('Hay un barco en ese camino')
                    hay_barco = True
                    
                else:
                    tablero[coordenada_init_x , coordenada_init_y : coordenada_init_y + len(var.espacios_libres[barco]) ] = 'O'
                    colocado = True
                    # print(tablero)
            
            elif  list(tablero[coordenada_init_x , coordenada_init_y ]) == list(var.espacios_libres[barco]) and (orien =='E') and  barco==var.barco_1:
                tab_check = chequear_alrededor(tablero,barco,coordenada_init_x,coordenada_init_y)
                if 'O' in tab_check:
                    # print('Hay un barco en ese camino')
                    hay_barco = True
                else:
                    tablero[coordenada_init_x , coordenada_init_y ] = 'O'
                    colocado = True
                    # print(tablero)
            
                
            


    # print('TODOS LOS BARCOS ESTÁN COLOCADOS')
    # print(tablero)
    return tablero

def mostrar_estado(tablero):
    print(f'\n{tablero}')

def menu_inicio():
    print('MENÚ PRINCIPAL')
    print('-'*100)
    time.sleep(0.5)
    print('1. Nuevo Juego.\n2. Salir')
    opcion = int(input())
    return opcion
    

def introducir_coordenadas():
    print('Introduce las coordenadas del disparo.(Números del 1 al 10)')
    datos_correctos=True
    
    while datos_correctos==True:
        try:
            coor_X = int(input('COORDENADA X'))
            coor_X +=-1
            if coor_X in range(10):
                coor_Y = int(input('COORDENADA Y'))
                coor_Y +=-1 
                if coor_Y in range(10):
                    datos_correctos=False
        except:
            datos_correctos = True       
    return coor_X,coor_Y  


def comprobar_disparo(coor_X,coor_Y,tablero):
    if tablero[coor_X,coor_Y] == ' ':
        disparo = '*'
        print('DISPARO AL AGUA')
    elif tablero[coor_X,coor_Y] == 'O':
        disparo = 'X'
        print('ACIERTO!!')
    elif tablero[coor_X,coor_Y] == 'X':
        disparo = 'X'
        print('YA HABIAS DISPARADO AHÍ')
    elif tablero[coor_X,coor_Y] == '*':
        disparo = '*'
        print('YA HABIAS DISPARADO AHÍ')
        
    return disparo


def disparo_jugador (tablero_oculto,tablero_maquina):
    coor_x, coor_y = introducir_coordenadas()
    disparo = comprobar_disparo(coor_x,coor_y,tablero_oculto)
    tablero_oculto[coor_x,coor_y] = disparo 
    tablero_maquina[coor_x,coor_y] = disparo 
    mostrar_estado(tablero_maquina)
    return tablero_oculto,tablero_maquina,disparo



def disparo_maquina (tablero_jugador):
    coor_x = np.random.randint (0,10)
    coor_y = np.random.randint (0,10)
    disparo = comprobar_disparo(coor_x,coor_y,tablero_jugador)
    tablero_jugador[coor_x,coor_y] = disparo
    mostrar_estado(tablero_jugador)
    return tablero_jugador,disparo


def quedan_barcos(tablero):
    lista_filas = [fila_tablero for fila_tablero in tablero[:11]]
    for i in range(len(lista_filas)):
        if 'O' in lista_filas[i]:
            return True
    return False

def main ():
    opcion = menu_inicio()
    if opcion == 1:
        tablero_jugador,tablero_oculto,tablero_maquina = init_tablero()   
        time.sleep(0.5)
        
        tablero_jugador = colocar_barco(tablero_jugador)
        tablero_oculto = colocar_barco(tablero_oculto)
        
        
        print('TABLERO JUGADOR')
        mostrar_estado(tablero_jugador)
        
        print('TABLERO OCULTO')
        mostrar_estado(tablero_oculto)
        
        print('TABLERO MAQUINA')
        mostrar_estado(tablero_maquina)
        
        
        
        while True:
            acierto_jugador = True
            while acierto_jugador == True:
                time.sleep(0.5)
                mostrar_estado(f'TABLERO DEL JUGADOR \n {tablero_maquina}')
                time.sleep(0.5)
                tablero_oculto,tablero_maquina,disparo = disparo_jugador (tablero_oculto,tablero_maquina)
                if disparo == 'X':
                    continue
                
                else:
                    acierto_jugador = False
                    
            acierto_maquina = True
            while acierto_maquina == True:
                time.sleep(0.5)
                
                tablero_jugador,disparo = disparo_maquina(tablero_jugador)
                if disparo == 'X':
                    continue
                else:
                    acierto_maquina = False
            mostrar_estado(f'TABLERO DE la MAQUINA \n {tablero_jugador}')
            time.sleep(0.5)        
            if quedan_barcos(tablero_oculto)==False:
                print('Has ganado!')
                mostrar_estado(tablero_oculto)
                break
                
            elif quedan_barcos(tablero_jugador)==False:
                print('La máquina ha ganado')
                mostrar_estado(tablero_jugador)
                break
            
                
        
        
        
    elif opcion ==2:
        print('HASTA MAÑANA')