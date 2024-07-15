# Tarea 3: DCCachos 🎲🃏

## Consideraciones generales :octocat:

Los archivos principales son <cliente/main_cliente.py> y <servidor/main_servidor.py> lso cuales simulan un juego de cachos, generando una interacción servidor-cliente (en el cual se pueden conectar varios clientes). En este, el objetivo principal es llegar al final de la partido con vidas restantes. Esto se logra a través de las opciones posibles por turno, incluyendo PASAR, ANUNCIAR TURNO, USAR PODER, TIRAR DADOS y DUDAR. El juego funciona en base a turnos, escogidos aleatoriamente, en el cual el numero de jugadores es 4, y si no se logra llenar la sala se rellena con BOTS, que tienen una determinada forma de jugar. El juego cuenta con dos interfaz gráficas, una que corresponde a la SALA DE ESPERA en el cual se muestra los 4 jugadores, sus nombres e iconos, y si se une mas que 4, le avisa al jugador 5 (y en adelante) que está llena la sala y debe esperar. En adición, si un jugador dentro de los 4 que van a jugar, se desconecta, se une uno de los que está en la lista de espera. Luego, si cualquier jugador (dentro de los que van a jugar) presiona el botón COMENZAR, empieza el juego, y se le muestra a todos los jugadores la interfaz gráfica del juego. Si el turno es del bot, comienza inmediatamente y sigue al siguiente jugador. Finalmente, si un jugador pierde (se le acaban las vidas), o se desconecta, se actualiza la interfaz grafica y los turnos. Cuando solo queda un jugador se le avisa que gano el juego, y que debe salir del programa, a los jugadores que perdieron se les avisa que deben salir del programa (como dice el enunciado).


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

* Networking: 18 pts (16%):

    **Protocolo: 2 pts**
    * Correcto uso de TCP/IP. (2pts): Hecha completa ✅
    
    **Correcto uso de sockets: 5 pts**
    * Instancia y conecta los sockets de manera correcta. (2pts): Hecha completa ✅
    * Las aplicaciones pueden trabajar concurrentemente sin bloquearse por escuchar un socket. (3pts): Hecha completa ✅

    **Conexión: 3 pts**
    * La conexión es sostenida en el tiempo y de propósito general para todos los tipos de mensajes que pueden intercambiar. (3pts): Hecha completa ✅
    
    **Manejo de Clientes: 2 pts**
    * Se pueden conectar múltiples clientes sin afectar el funcionamiento del programa. (2pts): Hecha completa ✅

    **Desconexión Repentina 6pts**
    * Si el servidor se desconecta, se le advierte a los clientes con un mensaje y se les permite cerrar el programa. (3pts): Hecha completa ✅
    * Si algún cliente se desconecta, se descarta su conexión sin afectar al resto de clientes. Si se desconecta en una partida, entonces seguirán jugando los que queden en la sala. (3pts): Hecha completa ✅

* Arquitectura Cliente - Servidor: 18 pts (16%):

    **Roles: 9 pts**
    * Correcta separación de recursos entre Cliente y Servidor. (3pts): Hecha completa ✅
    * Las responsabilidades de cada cliente son consistentes al enunciado. (3pts): Hecha completa ✅
    * Las responsabilidades del servidor son consistentes al enunciado. (3pts): Hecha completa ✅
    
    **Consistencia: 5 pts**
    * Se mantiene coordinada y actualizada la información en todos los clientes y en el servidor. (2pts): Hecha completa ✅
    * Se utilizan locks cuando es necesario. (3pts): Hecha completa ✅
    
    **Logs: 4 pts**
    * Se implementan logs del servidor, que permiten visualizar la información indicada en el enunciado. (4pts): Hecha completa ✅

* Manejo de Bytes: 26 pts (22%):

    **Codificación: 5 pts**
    * Se utiliza little endian para codificar los primeros 4 bytes que contienen el largo del contenido. (1pt): Hecha completa ✅
    * Se utiliza big endian para codificar el número identificador de cada bloque a bytes. (1pt): Hecha completa ✅
    * El mensaje se separa en bloques de 128 bytes, donde los primeros 4 corresponden al largo del contenido del mensaje ya encriptado. Si el mensaje restante del último bloque no es múltiplo de 128, se rellena con ceros. (3pts): Hecha completa ✅
    
    **Decodificación: 5 pts**
    * Se utiliza little endian para decodificar los primeros 4 bytes que contiene el largo del contenido. (1pt): Hecha completa ✅
    * Se utiliza big endian para decodificar el número identificador de cada bloque a bytes. (1pt): Hecha completa ✅
    * El mensaje se separa en bloques de 128 bytes, donde los primeros 4 corresponden al largo del contenido del mensaje ya encriptado. Si el mensaje restante del último bloque no es múltiplo de 128, se quitan los ceros. (3pts): Hecha completa ✅

    **Encriptación: 6 pts**
    * Se logra mover el mensaje una cantidad n de espacios a la derecha. Este n es generado aleatoriamente dado la seed del id del jugador. Se intercambia el byte de la posición 0 por el de la posición n. (6pts): Hecha completa ✅

    **Desencriptación: 6 pts**
    * Se logra desencriptar el mensaje, separando correctamente cada componente y sin perdida de información. (6pts): Hecha completa ✅

    **Integración: 4 pts**
    * Utiliza correctamente el protocolo para el envío de mensajes. (4pts): Hecha completa ✅

* Interfaz Gráfica: 22pts (19%):

    **Ventana de Inicio: 6 pts**
    * Se visualiza correctamente la ventana. Se muestran todos los elementos solicitados, incluyendo jugadores y botones. La información se actualiza correctamente. (2pts): Hecha completa ✅
    * Cuando un jugador selecciona la opción de comenzar partida, se redirige a la ventana de juego. En caso de que no se encuentren 4 jugadores, los restantes son rellenados con bots. (2pts): Hecha completa ✅
    * Si la sala se encuentra llena o bien hay una partida en curso, el nuevo jugador que ingrese no accederá a la partida y se le informará que espere la próxima partida. (2pts): Hecha completa ✅
    
    **Ventana de Juego: 16 pts**
    * Se visualiza correctamente la ventana del juego con todos los elementos solicitados en el enunciado. La información se actualiza correctamente para todos los clientes (2pts): Hecha completa ✅
    * Se visualizan los nombres y dados de todos los jugadores. Solo es visible los dados del jugador. Para los contrincantes, estos dados permantecen ocultos. (2pts): Hecha completa ✅
    * Existe una forma para anunciar el dado en el turno del jugador. (1pt): Hecha completa ✅
    * Existe la forma de pasar en el turno. Al momento de pasar, se salta el turno del siguiente jugador. (2pts): Hecha completa ✅
    * Existe la forma de cambiar los dados. Al momento de cambiarlos, se actualizan los dados del jugador con unos nuevos. (1pt): Hecha completa ✅
    * Existe la forma de dudar. Al momento de dudar, se verifican las condiciones del enunciado y comienza una nueva ronda. (2pts): Hecha completa ✅
    * Existe la forma de usar un poder. El jugador es capaz de seleccionar al rival afectado. (2pts): Hecha completa ✅
    * Se actualizan correctamente las vidas de los jugadores al finalizar cada ronda. (1pt): Hecha completa ✅
    * La partida termina cuando solo queda un jugador con vidas restantes. Una vez que se termina la partida, se le informa a cada jugador si gana o pierde. (3pts): Hecha completa ✅

* Reglas de DCCachos: 22pts (19%):

    **Inicio del juego: 5pts**
    * Se asigna un partidor de la primera ronda de forma aleatoria. (1pt): Hecha completa ✅
    * Se define un orden de los turnos de los jugadores. El orden se respeta durante todo el juego. (2pts): Hecha completa ✅
    * Se asignan aleatoriamente todas los dados de los jugadores. (2pts): Hecha completa ✅

    **Bots: 3 pts**
    * Los Bots que juegan siguen las instrucciones indicadas en el enunciado. (3pts): Hecha completa ✅

    **Ronda: 12 pts**
    * Al anunciar un valor, se respeta la condición de que sea estrictamente mayor al último valor anunciado. (2pts): Hecha completa ✅
    * Se puede pasar conservando el valor anunciado más alto por un jugador anterior. (2pts): Hecha completa ✅
    * Al momento de dudar se verifica que el jugador anterior tenga al menos un valor más alto del que anuncio. El jugador que se equivoca pierde una vida. Lo mismo sucede si se duda el paso. (3pts): Hecha completa ✅
    * Se pueden cambiar los dados solo una vez por turno. Si se cambian los dados, no se puede dudar. (1pt): Hecha completa ✅
    * Se puede usar un poder únicamente si se tiene el valor de los dados para hacerlo. (4pts): Hecha completa ✅

    **Termino del juego: 2 pts**
    * Se asigna correctamente el jugador ganador al último jugador con vidas restantes. (2pts): Hecha completa ✅

* Archivos: 10 pts (9%):

    **Parámetros (JSON): 4 pts**
    * Todos los parametros se encuentran en alguno de los parametros.json. (2pts): Hecha completa ✅
    * Se utiliza y carga correctamente parametros.json. (2pts): Hecha completa ✅

    **main.py: 4 pts**
    * Para ejecutar tanto el cliente como el servidor se pasa como argumento el puerto mediante la consola. (4pts): Hecha completa ✅

    **Cripto.py**
    *Se implementa y utiliza correctamente cripto.py. (2pts): Hecha completa ✅


* Bonus: 4 décimas máximo

    **Cheatcodes: 1 décima**
    * Cumple con todos los requisitos de este bonus. (1 décima): No hecho ❌

    **Turno con tiempo: 3 décimas**
    * Cumple con todos los requisitos de este bonus. (3 décimas): No hecho ❌

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main_servidor.py``` y ```main_cliente.py```. Además se debe crear los siguientes archivos y directorios adicionales:

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint(), choices()```
2. ```sys```: ```sys.exit(), sys.argv / sys``` 
3. ```socket```: ```socket() / socket```
4. ```PyQt5.QtCore```: ```pyqtSignal, QObject/ PyQt5```
5. ```PyQt5.QtWidgets```: ```QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QMessageBox, QComboBox / PyQt5```
6. ```PyQt5.QtGui```: ```QPixmap, QFont/ PyQt5```
7. ```json```: ```json```
8. ```pickle```: ```loads(), dumps() / pickle```
9. ```time```: ```sleep() / time```
10. ```threading```: ```Thread(), Lock() / threading```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```cripto.py```: Contiene las funciones: ``` encriptar()``` y ```desencriptar()```. Principales funciones para recibir y mandar mensajes de parte del cliente al servidor.
2. ```backend.py```: Hecha para conectar el cliente con la interfaz gráfica de inicio y de juego, a través de señales. Esta tiene la clase ```Cliente_Ventana```, que le avisa a las diferentes ventanas del juego información del cliente y el juego de DCCachos.
3. ```ventana_inicio.py```: Hecha para modelar la parte inicial del codigo e interfaz gráfica que interactúa con el usuario, como jugadores en espera y comenzar el juego. Esta tiene la clase ```Ventana_Inicio```, que a su vez interactua con el backend con señales.
4. ```ventana_juego.py```: Hecha para modelar la parte donde se muestra,y se juega DCCachos. La clase ```Ventana_Juego```, es donde ocurre todo el juego, y se va actualizando.
5. ```funciones.py```: Archivo que tiene funciones generales, como de codificar y decodificar los mensajes, para la lógica del cliente.
6. ```parametros.json```: Archivo que contiene todos los parametros utilizados a lo largo de la interfaz grafica y por parte del cliente.
7. ```cripto_servidor.py```: Contiene las funciones: ``` encriptar()``` y ```desencriptar()```. Principales funciones para recibir y mandar mensajes de parte del servidor al cliente.
8. ```DCCachos.py```: Hecha para modelar y revisar los turnos del juego, tanto para los clientes como para los bots. Esta tiene la clase ```DCCachos``` y ```Bots```, que modelan la logica del juego.
9. ```funciones_servidors.py```: Archivo que tiene funciones generales, como de codificar y decodificar los mensajes, prints para los logs del servidor y cargar los parametros.
10. ```parametros_servidor.json```: Archivo que contiene todos los parametros utilizados a lo largo del juego para el servidor y su lógica.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Sea el servidor o el cliente, el juego (i.e. el main.py) se correra parado desde la carpeta T3.

2. Otro supuesto que hice fue que el tamaño de las ventanas de inicio siempre será 500, 500, y las de juego 800, 700. Esto por que ese es tamaño optimo para los sprites y otros elementos del juego, y en general esto tipos de juegos tienen un tamaño predeterminado, que en este caso son mas chicos que la pantalla completa. 

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>

** Cuando un jugador utiliza un poder se empieza el nuevo turno con la persona que se vio afectado por el poder**

** Al momento de mandar el mensaje mando el largo del contenido en little endian, para hacer la codificación (en la funcion codificar), pero también mando el largo el largo de todo la codificacion en formato big endian. Entonces, si cumplí con las reglas para mandar el mensaje y además, le mande el largo de todo el mensaje en big endian, pues se me acomodaba para el funcionamiento de mi codigo. ** 

-------