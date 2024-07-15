# Tarea 1: DCCavaCava 🏖⛏

## Consideraciones generales :octocat:

El archivo principal, <main.py>  simula un torneo de cavar, DCCavaCava, donde existen varias reglas y restricciones. Este torneo es simulado a través de menús, con los que el usuario puede interactuar. El torneo tiene 3 entidades principales imprescindibles para que este funcionen, es por esto tambiñen que tienen una relación de composicion con el Torneo en el Diagrama de Clases. Estas entidades son Arena, Excavador e Ítems. Para agregar estas entidades a Torneo, se trabajo con Objetos, realizando clases de Torneo, Arena, Ítem y Excavador. En esta, se agregaron las caracteristicas y funciones principales que hace cada entidad (como son explicitadas en el enunciado), como tambien subclases necesarias, como fueron las del tipo de excavador, y tipo de item. Finalmente, se agregaron todas las opciones que tiene el usuario a lo largo del juego, a la clase Torneo, y se llaman estos métodos cuando el usuario pida. 

Todo este programa y simulación del DCCavaCava, se realiza a partir de un folder llamado "Partidas". En este, se guardan los torneos, y es donde se pueden cargar estos torneos.


<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

### Cosas implementadas y no implementadas :white_check_mark: :x:

❌ si NO completaste lo pedido
✅ si completaste correctamente lo pedido
🟠 si el item está incompleto o tiene algunos errores

* Programación Orientada a Objetos (42 pts) (35%): Hecha completa ✅
   
    **Diagrama** 
    * Entrega el diagrama respetando el formato solicitado. (2pts): Hecha completa ✅
    * "El diagrama contiene suficientes clases para modelar las entidades y funcionalidades pedidas. 
    Cada clase contiene atributos y métodos respectivos para modelar el programa." (4pts): Hecha completa ✅
    * El diagrama contiene relaciones (agregación, composición y herencia) entre las clases incluídas,
    y mantiene consistencia de modelación. (4pts): Hecha completa ✅
    
    **Definición de clases, atributos, métodos y properties**
    * El Torneo está bien modelado. (6pts): Hecha completa ✅
    * La Arena está bien modelada. (6pts): Hecha completa ✅
    * Los Excavadores están bien modelados. (6pts): Hecha completa ✅
    * Los Ítems están bien modelados. (6pts): Hecha completa ✅

    **Relaciones entre clases**
    * Se utilizan clases abstractas cuando corresponde. (4pts): Hecha completa ✅
    * Utiliza consistentemente relaciones de agregación y composición. (4pts): Hecha completa ✅

* Preparación Programa (11pts) (9%): Hecha completa ✅
    * Se pueden crear una o más partidas de DCCavaCava. (2pts): Hecha completa ✅
    * Se instancian los excavadores correctamente, respetando los valores del archivo. (3pts): Hecha completa ✅
    * Se instancian las arenas correctamente, respetando los valores del archivo. (3pts): Hecha completa ✅
    * Se instancian los tesoros y consumibles correctamente, respetando los valores de los archivos. (3pts): Hecha completa ✅


* Entidades (22pts) (18%): Hecha completa ✅

    **Excavador**
    * Está implementada la acción de cavar. Se respeta la fórmula dependiendo de cada tipo de excavador.(4pts): Hecha completa ✅
    * Está implementada la acción de descansar. El excavador descansa si su energía llega a 0. El descanso dura la cantidad de días correspondientes a la fórmula. (3pts): Hecha completa ✅
    * Los excavadores pueden encontrar ítems. La probabilidad cumple con la fórmula establecida y se respeta la probabilidad de encontrar Tesoros y Consumibles. Todo lo anterior utiliza las fórmulas correspondientes al tipo de Arena. (4pts): Hecha completa ✅
    * Los excavadores pierden energía al momento de cavar. Se respeta la fórmula de pérdida de energía y se modifican las características según el tipo de excavador. (2pts): Hecha completa ✅
    * Está implementada la acción de utilizar consumibles. Los efectos varían según el tipo de excavador. (2pts): Hecha completa ✅
    
    **Arena**
    * La arena posee un nivel de dificultad que se calcula a partir de la fórmula establecida. La dificultad varía según el tipo de Arena. (2pts): Hecha completa ✅
    * Se cambian aleatoriamente las características de la Arena magnética al inicio de cada día. (2pts): Hecha completa ✅
    
    **Torneo**
    * Al simular el día, se calcula correctamente la probabilidad de que ocurra un evento. En caso de que ocurra uno, se aplican los efectos correspondientes. (3pts): Hecha completa ✅

* Flujo del programa (31pts) (26%): Hecha completa ✅

    **Menú de Inicio**
    * Se muestran todas las opciones mínimas pedidas en el menú de inicio. (1pt): Hecha completa ✅
    * Al seleccionar 'Nueva Partida', se inicia una nueva partida. (2pts): Hecha completa ✅
    * Al seleccionar 'Cargar Partida', se carga la partida con los datos almacenados en el archivo DCCavaCava.txt. (2pts): Hecha completa ✅

    **Menú Principal**
    * Se muestran todas las opciones mínimas pedidas para el menú principal. (1pt): Hecha completa ✅

    **Simulación día Torneo**
    * Se muestra la cantidad total de metros excavados durante el día y la cantidad cavada por cada excavador. (2pts): Hecha completa ✅
    * Se muestran los ítems encontrados y su tipo por cada excavador. (2pts): Hecha completa ✅
    * Si ocurre un evento, se muestra el cambio de Arena y su efecto en los excavadores. (2pts): Hecha completa ✅
    * Se muestran los excavadores que han agotado su energía y comienzan a descansar. (2pts): Hecha completa ✅
    
    **Mostrar estado torneo**
    * Se muestra en pantalla toda la información mínima pedida en el enunciado sobre el torneo y los excavadores.  (2pts): Hecha completa ✅
    
    **Menú Ítems**
    * Se muestran todos los ítems encontrados, permitiendo seleccionar uno. (2pts): Hecha completa ✅
    * Al seleccionar un ítem y utilizarlo, desaparece de la mochila. (1pts): Hecha completa ✅

    **Guardar partida**
    * Está implementada la opción de guardar partida. Se informa al usuario si el guardado fue exitoso. (2pts): Hecha completa ✅

    **Robustez**
    * Todos los menus solicitados poseen la opción de volver al menu anterior y salir del  programa. (4pts): Hecha completa ✅
    * Todos los menús son a prueba de cualquier tipo de input. (6pts): Hecha completa ✅

* Manejo de archivos (14pts) (12%): Hecha Completa ✅

    **Archivos CSV**
    * Los archivos csv utilizados son trabajados correctamente. (4pts): Hecha completa ✅

    **Archivos TXT**
    * Se trabaja correctamente con el archivo DCCavaCava.txt. Se lee y escribe correctamente el archivo para cargar y guardar la partida. (4pts): Hecha Completa ✅

    **parametros.py**
    * Utiliza e importa correctamente los parámetros del archivo parametros.py. (2pts): Hecha completa ✅
    * El archivo parametros.py contiene todos los parámetros y constantes que se utilizan a lo largo del programa, además de los especificados en el enunciado. (4pts): Hecha completa ✅

* Bonus (3 décimas): Hecha Completa ✅
    
    **Guardar Partida**
    * Cumple con todos los requisitos de este bonus. (3 décimas): Hecha completa ✅

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```ABC```: ```ABC, abstractmethod / abc```
2. ```random```: ```randint(), choices() / random``` 
3. ```collections```: ```namedtuple() / collections``` 
4. ```sys.exit```: ```sys.exit() / sys``` 
5. ```os```: ```listdir() / os```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```clases.py```: Contiene las Clases Arena, Excavador e Ítem (y sus subclases)
2. ```class_torneo.py```: Contiene la Clase Torneo, donde interactúan las otras clases
3. ```Partidas``` : Directorio donde se pueden guardar y cargar archivos ".txt" del DCCavaCava.
4. ```funciones.py```: Archivo que tiene funciones generales, como de instanciar a los objetos y leer los archivos: arenas.csv, consumibles.csv, excavadores.csv y tesoros.csv.
5. ```parametros.py```: Archivo que contiene todos los parametros utilizados a lo largo del juego DCCavaCava.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. El primer supuesto que realicé es que cuando el excavador está descansando, tiene energía 0, hasta que terminé su descanso. Además, si es que el jugador tiene items de ayuda energética, es decir que aumente la energía de los excavadores, si decide consumirlos se va a interrumpir el descanso de los excavadores, y van a resumir su excavación con la energía proveída por el ítem. Por lo tanto, el uso de este ítem, está a criterio del jugador y sus necesidades.

2. Otro supuesto que realicé es que dos excavadores no pueden tener el mismo nombre. Esto lo consideré pues los nombres de los excavadores son lo que los identifica del resto, y con los cuales los diferenciaré a lo largo del torneo. En adición, el equipo de excavación no podrá tener los mismos excavadores, y de esta manera, si hay un tesoro del tipo 1, y no existe ningun excavador diferente a los que ya estan en el equipo, NO se agregará más excavadores. 

3. Si es que el tesoro es del tipo 2, el item tratará de cambiar la arena igual (dentro de las opciones en el archivo arenas.csv), incluso si el tipo de cambio es del mimso tipo de la arena actual.

-------
## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://github.com/IIC2233/Syllabus/blob/main/Tareas/T1/Sala%20Ayuda/Sala%20Ayuda%20-%20Menus.ipynb: este modela un sistema de múltiples menús, con las opciones generales de "Salir" y "Volver" de dichos menús. Este codigo está implementado a lo largo de todo el archivo <main.py> y hace que se pueda volver del "Menu de Items" al "Menu Principal", y del "Menu Principal" al "Menu Inicial", como también poder salir del programa completamente.


## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
