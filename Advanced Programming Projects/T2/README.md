# Tarea 2: DCCazafantasmas 👻🧱🔥

## Consideraciones generales :octocat:

El archivo principal, <main.py> simula un juego del tipo arcade, donde el personaje a manejar es Luigi, y el objetivo principal es llegar a la posicion de la estrella final y agarrarla. Sin embargo, Luigi tiene una cierta cantidad de vidas, y tiempo, para lograr este objetivo. Este juego cuenta con otras entidades como fantasmas, diferenciados pos su movimiento (vertical, horizontal y "follower"), que tienen como objetivo quitarle vidas a Luigi, pues cuando chocan con Luigi este pierde una vida. Adicionalmente, existen otros tipos de bloques, como la pared, que no se puede mover, el fuego, que tambien le puede quitar una vida a Luigi y la roca que solo puede ser movida por Luigi. Este programa cuenta con 4 ventanas de juego: Ventana_Inicial, Ventana_Juego, Ventana_Juego_Timer, y Ventana_Final. 

Por otra parte, en cuanto al mapa de juego, este se crea en base a la informacion guardada en la carpeta "mapas", o en base a la creacion del modo constructor donde el usuario puede colocar las entidades en el mapa, utilizando el metodo de "Drag and Drop".

Finalmente, se le avisará al usuario si perdio, por que perdio, sea por falta de tiempo o vidas, o si ganó, el puntaje final basado en lo explicitado en el enunciado.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

* Ventanas: 27 pts (27%)

    **Ventana de Inicio: 8 pts (7%)**
    * La ventana de inicio se visualiza correctamente. Se visualizan los elementos mínimos y estos no se superponen entre sí. (2pts): Hecha completa ✅
    * Se verifica que el nombre sea alfanumérico, esté en el rango de caracteres y que no sea vacío. En caso contrario, se debe notificar el error mediante un mensaje o pop-up. (3pts): Hecha completa ✅
    * Se puede seleccionar cualquier mapa de la carpeta "Mapa" o bien indicar que no se quiere cargar uno predefinido. Luego se ingresar a la Ventana de Juego. (2pts): Hecha completa ✅
    * El botón de salir cierra la ventana y termina el programa. (1pt): Hecha completa ✅
    
    **Ventana de Juego: 22 pts (18%)**
    * Se visualiza correctamente el mapa del juego y todos los elementos mínimos requeridos.
    Los elementos no se superponen entre sí. (4pts): Hecha completa ✅
    * Las estadísticas se actualizan a medida que progresa el juego. (4pts): Hecha completa ✅
    * La ventana carga el mapa si se ha seleccionado uno, o comienza en un mapa vacío si está en modo constructor. (2pts): Hecha completa ✅
    * El panel de construcción contiene todas las entidades que se pueden poner en el mapa. (2pts): Hecha completa ✅
    * El panel de construcción señala cuántos elementos de cada entidad quedan disponibles para poner en el mapa. (2pts): Hecha completa ✅
    * El juego inicia cuando el botón para jugar el mapa es presionado. (4pts): Hecha completa ✅
    * El botón de salir cierra la ventana actual y sale del programa. (1 pt): Hecha completa ✅

* Mecanicas de juegos: 47 pts (47%):

    **Luigi: 9 pts**
    * Al detectar la colisión entre Luigi y los Fantasmas o el Fuego, Luigi pierde una vida y vuelve al punto donde inició el nivel. (2pts): Hecha completa ✅
    * Al colisionar con una Pared, Luigi no puede seguir avanzando en esa dirección. Si colisiona con una Roca, debe poder arrastrarla. (3pts): Hecha completa ✅
    * Se muestra consistencia con las teclas de movimiento que se presionan, y la dirección hacia donde Luigi avanza. (4pts): Hecha completa ✅
    
    **Fantasmas: 14 pts**
    * Cada fantasma se mueve de manera independiente de los demás, respetando su propia velocidad y dirección. (4pts): Hecha completa ✅
    * La velocidad con la cual cada fantasma se mueve se decide de manera aleatoria. (1 pt): Hecha completa ✅
    * Se implementan correctamente el Fantasma horizontal y el Fantasma vertical, con sus respectivas características. (6 pts): Hecha completa ✅
    * Cuando un fantasma colisiona con un Fuego, el fantasma desaparece. Si colisiona con una Pared o Roca, invierte su sentido de dirección y sigue avanzando, respetando su propio movimiento. (3pts): Hecha completa ✅
    
    **Modo constructor: 14 pts**
    * No se puede superponer un bloque en una casilla que ya está ocupada. (2pts): Hecha completa ✅
    * El panel de construcción tiene un máximo de elementos por entidad que se pueden poner en el mapa. (4pts): Hecha completa ✅
    * Ninguna sprite tiene movimiento al no haber iniciado el juego. (2 pts): Hecha completa ✅
    * Al apretar el botón de Jugar, se verifica que exista un sólo Luigi y una sóla Estrella en el mapa. Si se cumple, el modo constructor queda deshabilitado, impidiendo la modificación del mapa, y el juego comienza junto a la cuenta regresiva. (6 pts): Hecha completa ✅
    
    **Fin de ronda: 10 pts**
    * Se calculan correctamente el puntaje al terminar la ronda. (2 pts): Hecha completa ✅
    * Se implementan las tres formas de terminar la ronda: cuando Luigi se queda sin vidas, cuando libera a Aossa de la Estrella, o cuando la cuenta regresiva llega a cero. (4 pts): Hecha completa ✅
    * En caso de victoria o derrota, se notifica al usuario indicando el resultado, nombre del usuario y puntaje. Además suena el sonido correspondiente del caso. (2 pts): Hecha completa ✅
    * Aparece el botón de salir automáticamente al acabar el juego. Este botón termina el programa. (2 pts): Hecha completa ✅

* Interacción con el usuario: 14 pts (14%):

    **Clicks: 8 pts**
    * El modo constructor es implementado completamente y correctamente con el click izquierdo. (8 pts): Hecha completa ✅
    
    **Animaciones: 6 pts**
    * El movimiento de los personajes en el mapa es fluído y animado, según las sprites correspondientes. (6 pts): Hecha completa ✅

* Archivos: 4pts (4%):

    **Sprites: 2 pts**
    * Trabaja correctamente con todos los archivos entregados. (2 pts): Hecha completa ✅
    
    **Parametros.py: 2 pts**
    * Utiliza e importa correctamente parametros.py. (2 pts): Hecha completa ✅

* Bonus: 8 décimas máximo

    **Volver a Jugar: 2 décimas**
    * Cumple con todos los requisitos de este bonus. (2 décimas): Hecha completa ✅

    **Follower villian: 3 décimas**
    * Cumple con todos los requisitos de este bonus. (3 décimas): Hecha completa ✅

    **Drag and Drop: 3 décimas**
    * Cumple con todos los requisitos de este bonus. (3 décimas): Hecha completa ✅

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint(), uniform() / módulo```
2. ```sys.exit()```: ```sys.exit() / sys``` 
3. ```os```: ```listdir() / os```
4. ```PyQt5.QtCore```: ```pyqtSignal, QObject, QTimer, QPropertyAnimation, QPoint, Qt, QMimeData / PyQt5```
5. ```PyQt5.QtWidgets```: ```QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QMessageBox, QComboBox / PyQt5```
6. ```PyQt5.QtGui```: ```QPixmap, QKeyEvent, QColor, QFont, QIcon, QDrag, QMouseEvent / PyQt5```
7. ```PyQt5.QtMultimedia```: ```QSound / PyQt5```
8. ```copy()```: ```deepcopy() / copy```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```entidades.py```: Contiene a ```Luigi```, ```Ghost_V```, ```Ghost_H```, ```Roca``` y ```Follower_Villain```. Principales entidades del juego, que se pueden mover e interactuar con el usuario.
2. ```backend.py```: Hecha para modelar la parte del código que maneja la lógica y funcionalidad del juego. Esta tiene la clase ```Juego```, que le avisa a las diferentes ventanas del juego información como las posiciones de las entidades y bloques, cuando moverse, si se pueden mover, cuando chocan, etc...
3. ```ventana_inicio.py```: Hecha para modelar la parte inicial del codigo e interfaz gráfica que interactúa con el usuario, como escoger mapa y enviar el nombre. Esta tiene la clase ```Ventana_Inicio```, que a su vez interactua con el backend con señales.
4. ```ventana_juego.py```: Hecha para modelar la parte donde se muestra, o construye el mapa. La clase ```Ventana_Juego```, puede dar inicio al juego y también limpiar el mapa cuando esté en el modo constructor.
5. ```ventana_juego_timer.py```: Archivo de python que modela el juego y movimiento de las entidades, mostrando como disminuye el tiempo y las vidas de Luigi. La clase ```Ventana_Juego_Timer```, interactúa principalmente con el usuario a través del teclado, posibilitando el movimiento, agarrar la estrella, pausar y cheats.
6. ```ventana_final.py```: Archivo que contiene la clase ```Ventana_Final```, está le muestra el resultado final al usuario, y le da la posibilidad de salir del programa
7. ```funciones.py```: Archivo que tiene funciones generales, como de revisar posiciones adyacentes, entregar nuevas posiciones, entregar sprites y entregar el tiempo en forma str.
8. ```parametros.py```: Archivo que contiene todos los parametros utilizados a lo largo del juego.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. El primer supuesto que realicé a la hora de modelar el juego, es que cuando un fantasma muere, y despues Luigi pierde una vida, no se volveran a mostrar o "revivir". Esto por que, primero que todo, en el enunciado se menciona "Si algo le hace daño, Luigi perderá una vida y se reiniciará el nivel, haciendo que todos los BLOQUES vuelvan a su estado original.", y en la parte anterior dicen que los bloques son: piedra, pared, fuego y estrella. Adicionalmente, en cuanto al juego, siento que es mas lógico que no revivan, pues el usuario puede jugar estratégicamente moviendo rocas, y/o aludiendo a los follower villians, al fuego, para que mueran los fantasmas.

2. Otro supuesto o decisión que realicé al momento de hacer el bonus y crear el follower villian, fue que siempre seguiran a Luigi pero que su movimiento, o la manera de llegar a Luigi sera determinada de una manera aleatoria, si es que hay objetos impenetrables en el medio, pero siempre podrá llegar a donde este Luigi. Es decir, van a ser muy "tontos" en su movimiento, pero siempre podrán y querán llegar a la posición de Luigi.

3. Otro supuesto que hice fue que el tamaño de las ventanas de juego siempre será 500, 500. Esto por que ese es tamaño optimo para los sprites y otros elementos del juego, y en general esto tipos de juegos tienen un tamaño predeterminado, que en este caso son mas chicos que la pantalla completa. 

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>

** Para los fantasmas followers, los identifique como Z cuando se guardan como archivos en /mapas **

** Cuando Luigi pierde una vida decidi que se muestre la animación de que Luigi, los fantasmas y las rocas, vuelvan a su posición original. Esto para que el juego se vea fluido, y que el usuario entienda que cuando muere, todos las entidades VIVAS van a volver a su lugar de inicio **

** En el bonus de jugar otra vez, le doy al usuario la oportunidad de guardar el juego, es decir el mapa que ha construido, en la carpeta folders, así puede guardar su creación. Esto también lo puedo hacer porque al momento de crear el mapa, verifico que sea un mapa válido, entonces nunca va a quedar un mapa inválido o injugable en ./mapas/ **
-------