---HUNDIR LA FLOTA---

-----------------------------------------------------------------------------------------------------------------------------


Juego hundir la flota programado en python. 3 archivos:
  - variables
  - funciones
  - main

-----------------------------------------------------------------------------------------------------------------------------
VARIABLES

  ASIGNACION DE LONGITUDES DE LOS BARCOS
    barco_1 = 1
    barco_2 = 2
    barco_3 = 3
    barco_4 = 4
    
  ITERABLE PARA ACCEDER TANTO A LA LONGITUD , COMO A LOS ESPACIOS LIBRES QUE SE NECESITARÁN PARA PODER COLOCAR EL BARCO
    barcos_largos = [barco_4,barco_3,barco_3,barco_2,barco_2,barco_2,barco_1,barco_1,barco_1,barco_1]
    
  DICCIONARIO CON LOS ESPACIOS LIBRES QUE NECESITA CADA BARCO
    espacios_libres = {
        barco_4 : [' ',' ',' ',' '],
        barco_3 : [' ',' ',' '],
        barco_2 : [' ',' '],
        barco_1 : [' ']
     
    }

    
-----------------------------------------------------------------------------------------------------------------------------

FUNCIONES

  def  init_tablero():
    - Crea 3 tableros de 10x10. Usando una matriz de numpy. Los tableros se asignarán a los nombres:
    
      1) tablero_jugador --> Tablero donde se guardarán los barcos pertenecientes al jugador
      2) tablero_oculto --> Tablero donde se guardarán los barcos pertenecientes a la máquina
      3) tablero_maquina --> Tablero donde el jugador visualizará dónde ha disparado.

  
  def limpiar_pantalla ():
    - Limpia la terminal.
    - Se llamará a esta función siempre antes de mostrar un tablero nuevo.


  def chequear_alrededor(tablero,barco,coordenada_init_x,coordenada_init_y):
    - Devuelve una matriz con las posiciones donde en x e y con +-1 de distancia en todas las direcciones donde se intentará 
      colocar el barco. 
    - Se llamatá a esta función al colocar un nueo barco:
    
    ARGUMENTOS:
      - tablero --> tablero sobre el que se están colocando los barcos. Dos opciones: (tablero_oculto,tablero_jugador)
      - barco --> indica qué barco se está colocando. COn ello puede acceder a la longitud del barco
      - coordenada_init_x --> coordenada en x, donde se empieza a colocar el barco
      - coordenada_init_y) --> coordenada en y, donde se empieza a colocar el barco
      
  
  def colocar_barco(tablero):
    - Función que coloca aleatoriamente los barcos de la lista barcos_largos en tablero que entra como argumento.
    
    FUNCIONAMIENTO:
    - Entra en un bucle que itera sobre la lista de barcos, para cada barco:
      - Crea aleatoriamente las coordenadas x, y. 
      - Elige aleatoriamente la orientación S o E 
      - Dependiendo de la orientación y de la longitud del barco que se está colocando, comprueba dos cosas:
        1º Que las psiciones que ocupará elbarco son todas ' '.(espacio en blanco.
        2º Que en las posiciones que me devuelve la funcion chequear_alrededor no hay ningún O que representaría otro barco.

    ARGUMENTOS:
      - tablero --> tablero sobre el que se están colocando los barcos. Dos opciones: (tablero_oculto,tablero_jugador)
    
  
  def mostrar_estado(tablero):
    - Función que muestra en pantalla un tablero
    
    FUNCIONAMIENTO:
    - Limpia la pantalla
    - Muestra en pantalla el estado actual del tablero.
  
    ARGUMENTOS:
      - tablero --> tablero que se quiere mostrar.


  def menu_inicio():
    - Función que muestra en pantalla un menú con dos opciones. 
      1- Jugar  --> Entra en el juego
      2- Salir --> Mensaje de despedida y fin del programa.

  def introducir_coordenadas():
    - Función que solicita al usuario que introduzca 2 coordenadas x e y. Valores del 1 al 10.
    - Comprueba que los valores introducidos son numeros y que están entre 1 y 10, en caso contrario vuelve a solicitar la entrada de coordenadas.
    - devuelve el valor de las coordenadas.

  def comprobar_disparo(coor_X,coor_Y,tablero):
    - Función que recibe las coordenadas de disparo, y un tablero e imprime un mensaje en pantalla indicando si se ha acertado, si no, o si ya habías     disparado en ese lugar. También devuelve una variable llamado disparo con el valor que correspondería posicionar. 3 opciones ('X','O','*')

  def disparo_jugador (tablero_oculto,tablero_maquina):
    - Función que llama a las funciones introducir_coordenadas() , comprobar_coordendas() y mostrar_tablero ().
    - Además el valor disparo que venía de comprobar_coordenadas () en las coordendas que venian de introducir_coordenadas().

  def disparo_maquina (tablero_jugador):
    - Función que genera unas coordendas aleatorias.
    - también llama a la función comprobar_coordenadas() y recibe la variable disparo.
    - Asigna el valor disparo a laposición del tablero de las coordenadas generadas.

  def quedan_barcos(tablero):
    - Función que comprueba si queda algún barco en el tablero.
    - Devuelve un booleano que servirá para finalizar el juego o seguir en el bucle del juego.



  
