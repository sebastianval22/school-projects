# proyectos-escolares
Este es un repositorio que contiene muchos de los proyectos de código en los que he trabajado para cursos universitarios. Este README también enlaza a repositorios externos para proyectos escolares en los que he trabajado.

# Índice
Los cursos están listados en orden cronológico, con los proyectos más recientes más cerca de la parte superior.
Puedes encontrar más información en el README individual de cada proyecto.

## Ingeniería de Software
Este es un proyecto en el que toda la clase trabajó durante la duración del curso. Es una plataforma web diseñada para facilitar la organización y participación en partidos de fútbol (pickup games). Además, permite la creación de grupos privados, la comunicación de usuarios a través de chats y la gestión de permisos de usuario por parte de administradores. Trabajé tanto en el backend como en el frontend del equipo de desarrollo.
[Ir al repositorio](https://github.com/IIC2143/2024-1-grupo-12)

## Bases de Datos
Este es un proyecto grupal en el que creamos una base de datos que modela las entregas, restaurantes y platos de una empresa de alimentos que gestiona varios clientes. También construimos un sitio web que demuestra algunas de las funcionalidades y consultas que soporta la base de datos.
[Ir al repositorio](https://github.com/ilungenstrass/Proyecto-BD-52)

## Programación Avanzada
En este curso trabajé en varios proyectos programando en Python y utilizando librerias externas. 


### Proyecto T0
Esta entrega, específicamente, el archivo principal: `main.py` logra modelar el plan de defensa de un castillo que involucra tortugas y bombas con cierto alcance, a través del uso de funciones recursivas. El código se caracteriza por seguir las 5 reglas descritas en el enunciado de la tarea 0 para construir y validar las soluciones de los tableros.

Primero que todo, modela dos menús con el cual el usuario interactúa. El primer menú, menú de inicio, le pide al usuario el archivo de tablero a abrir, como también comprueba que este sea un archivo válido. Luego, el segundo menú expone cinco opciones de acciones que puede realizar el código con el archivo introducido, y le da de escoger al usuario.

Finalmente, de acuerdo a la elección escogida el programa realiza la acción con la ayuda de las diferentes funciones en módulos como `functions.py` y `tablero.py`.
[Ir al código](https://github.com/sebastianval22/school-projects/tree/main/Advanced%20Programming%20Projects/T0)

### Proyecto T1
El archivo principal, `main.py` simula un torneo de cavar, DCCavaCava, donde existen varias reglas y restricciones. Este torneo es simulado a través de menús, con los que el usuario puede interactuar. El torneo tiene 3 entidades principales imprescindibles para que este funcione, es por esto también que tienen una relación de composición con el Torneo en el Diagrama de Clases. Estas entidades son Arena, Excavador e Ítems. Para agregar estas entidades a Torneo, se trabajó con Objetos, realizando clases de Torneo, Arena, Ítem y Excavador. En estas, se agregaron las características y funciones principales que hace cada entidad (como son explicitadas en el enunciado), como también subclases necesarias, como fueron las del tipo de excavador y tipo de ítem. Finalmente, se agregaron todas las opciones que tiene el usuario a lo largo del juego, a la clase Torneo, y se llaman estos métodos cuando el usuario pida.

Todo este programa y simulación del DCCavaCava, se realiza a partir de un folder llamado "Partidas". En este, se guardan los torneos, y es donde se pueden cargar estos torneos.
[Ir al código](https://github.com/sebastianval22/school-projects/tree/main/Advanced%20Programming%20Projects/T1)

### Proyecto T2
El archivo principal, `main.py` simula un juego del tipo arcade, donde el personaje a manejar es Luigi, y el objetivo principal es llegar a la posición de la estrella final y agarrarla. Sin embargo, Luigi tiene una cierta cantidad de vidas, y tiempo, para lograr este objetivo. Este juego cuenta con otras entidades como fantasmas, diferenciados por su movimiento (vertical, horizontal y "follower"), que tienen como objetivo quitarle vidas a Luigi, pues cuando chocan con Luigi este pierde una vida. Adicionalmente, existen otros tipos de bloques, como la pared, que no se puede mover, el fuego, que también le puede quitar una vida a Luigi y la roca que solo puede ser movida por Luigi. Este programa cuenta con 4 ventanas de juego: `Ventana_Inicial`, `Ventana_Juego`, `Ventana_Juego_Timer`, y `Ventana_Final`.

Por otra parte, en cuanto al mapa de juego, este se crea en base a la información guardada en la carpeta "mapas", o en base a la creación del modo constructor donde el usuario puede colocar las entidades en el mapa, utilizando el método de "Drag and Drop".

Finalmente, se le avisará al usuario si perdió, por qué perdió, sea por falta de tiempo o vidas, o si ganó, el puntaje final basado en lo explicitado en el enunciado.
[Ir al código](https://github.com/sebastianval22/school-projects/tree/main/Advanced%20Programming%20Projects/T2)

### Proyecto T3
Los archivos principales son `cliente/main_cliente.py` y `servidor/main_servidor.py` los cuales simulan un juego de cachos, generando una interacción servidor-cliente (en el cual se pueden conectar varios clientes). En este, el objetivo principal es llegar al final de la partida con vidas restantes. Esto se logra a través de las opciones posibles por turno, incluyendo PASAR, ANUNCIAR TURNO, USAR PODER, TIRAR DADOS y DUDAR. El juego funciona en base a turnos, escogidos aleatoriamente, en el cual el número de jugadores es 4, y si no se logra llenar la sala se rellena con BOTS, que tienen una determinada forma de jugar. El juego cuenta con dos interfaces gráficas, una que corresponde a la SALA DE ESPERA en el cual se muestra los 4 jugadores, sus nombres e íconos, y si se une más que 4, le avisa al jugador 5 (y en adelante) que está llena la sala y debe esperar. En adición, si un jugador dentro de los 4 que van a jugar, se desconecta, se une uno de los que está en la lista de espera. Luego, si cualquier jugador (dentro de los que van a jugar) presiona el botón COMENZAR, empieza el juego, y se le muestra a todos los jugadores la interfaz gráfica del juego. Si el turno es del bot, comienza inmediatamente y sigue al siguiente jugador. Finalmente, si un jugador pierde (se le acaban las vidas), o se desconecta, se actualiza la interfaz gráfica y los turnos. Cuando solo queda un jugador se le avisa que ganó el juego, y que debe salir del programa, a los jugadores que perdieron se les avisa que deben salir del programa (como dice el enunciado).
[Ir al código](https://github.com/sebastianval22/school-projects/tree/main/Advanced%20Programming%20Projects/T3)
