# Tarea 0: DCCeldas 💣🐢🏰


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

Esta entrega, especificamente, el archivo principal: main.py logra modelar el plan de defensa de un castillo que involucra tortugas y bombas con cierto alcance. El código se caracteriza por seguir las 5 reglas descritas en el enunciado de la tarea 0 para construir y validar las soluciones de los tableros, que modelan el sistema de defensa del castillo de Lily416. 

Primero que todo, modela dos menús con el cual el usuario interactúa. El primer menú, menú de inicio, le pide al usuario el archivo de tablero a abrir, como tambíen comprueba que este sea un archivo válido. Luego, el segundo menú expone cinco opciones de acciones que puede realizar el codigo con el archivo introducido, y le da de ecoger al usuario.

Finalmente, de acuerdo a la elección escogida el programa realiza la acción con la ayuda de las diferentes funciones en módulos como functions.py y tablero.py.

### Cosas implementadas y no implementadas :white_check_mark: :x:

❌ si NO completaste lo pedido
✅ si completaste correctamente lo pedido
🟠 si el item está incompleto o tiene algunos errores

* Menú de Inicio (5pts) (7%): Hecha completa ✅
    * Seleccionar Archivo (2pts): Hecha completa ✅
    * Validar Archivo (3pts): Hecha completa ✅

* Menú de Acciones (11pts) (15%): Hecha completa ✅
    * Opciones (2pts): Hecha completa ✅
    * Mostrar tablero (2pts): Hecha completa ✅
    * Validar bombas y tortugas (2pts): Hecha completa ✅
    * Revisar solución (2pts): Hecha completa ✅
    * Solucionar tablero (2pts): Hecha completa ✅
    * Salir (1pt): Hecha completa ✅

* Funciones (34pts) (45%): Hecha completa ✅
    * Cargar tablero (3pts): Hecha completa ✅
    * Guardar tablero (3pts): Hecha completa ✅
    * Valor bombas (3pts): Hecha completa ✅
    * Alcance bomba (6pts): Hecha completa ✅
    * Verificar tortugas (4pts): Hecha completa ✅
    * Solucionar tablero (15pt): Hecha completa ✅

* General (19pts) (25%): Hecha completa ✅
    * Manejo de Archivos (4pts): Hecha completa ✅
    * Menús (2pts): Hecha completa ✅
    * tablero.py (2pts): Hecha completa ✅
    * Módulos (5pts): Hecha completa ✅
    * PEP8 (6pts): Hecha completa ✅

* Bonus (6 décimas):
    * Funciones atómicas (2 décimas): No hecho ❌
    * Regla 5 (4 décimas): Hecha Completa ✅


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. 


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys.exit```: ```sys.exit() / sys```
2. ```os```: ```os.path.isfile() / os``` 
3. ```copy```: ```copy.deepcopy() / copy```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```functions.py```: Constituida con todas las funciones necesarias para válidar cada regla del tablero
2. ```tablero.py```: Modulo importado para utilizar la función imprimir_tablero_con_utf8(), que imprime el tablero

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. El primer supuesto que realicé es que para solucionar los tableros se podía resolver mediante una serie de movimientos limitados. Es decir, que se puedo solucionar mediante un movimiento como por ejemplo, ir subiendo en filas y aumentando en columnas, ó, ir bajando en filas, y disminuyendo en columnas, entre las demás condiciones. Esto es una justificacion válida pues además de que las combinaciones de movimientos son muchas, también existen muchas soluciones a un dicho tablero, por lo cuál alguna solución se podría encontrar con estos movimientos de recorrer el tablero.

## Consideraciones adicionales

1. Al intentar resolver el bonus incorporé la función verificar_islas(tablero) en functions.py, y la utilicé para los comandos de acción como: Válidar Tablero, y Solucionar Tablero. Sin embargo, si mi programa no logra resolver estos tableros, o existe errores al resolver algunos (aunque intenté con varios ejemplos de tableros), no quisiera que esta implementación de la regla 5, me "quite" todo el puntaje de estas acciones dentro del menú de acción. Por lo tanto, las lineas que se tendrían que eliminar ó no considerar para el funcionamiento del programa SIN el bonus son: 

* linea: 259-270 en functions.py

def es_caso_base(tablero: list) -> bool:  # Caso base-> ya esta solucionado
    alcances = verificar_alcance_todas_bombas(tablero)  # R1
    bombas_invalidas = verificar_valor_bombas(tablero)  # R2
    unicidad_celdas = verificar_unicidad_celdas(tablero)  # R3
    tortugas_invalidas = verificar_tortugas(tablero)  # R4
    hay_islas = verificar_islas(tablero)  # R5
    if ((alcances is True) and (bombas_invalidas == 0) and
       (unicidad_celdas == 0) and (tortugas_invalidas == 0)
       and (hay_islas is True)): **<- solo se tendría que eliminar esta linea (y colocar un ":", en la fila superior)**
        return True
    else:
        return False
    
* linea: 322 - 344

def colocar_tortugas(tablero: list, coordenada: tuple) -> list:
    i = coordenada[0]  # Función para colocar tortugas
    j = coordenada[1]  # de acuerdo a las 5 reglas
    if tablero[i][j] == "-":
        tablero[i][j] = "T"
        if verificar_tortugas(tablero) != 0:
            tablero[i][j] = "-"
        if verificar_alcance_todas_bombas_mas_o_igual(tablero) is False:
            tablero[i][j] = "-"
        hay_bombas = False
        for k in range(0, len(tablero)):
            if isinstance(tablero[i][k], int):
                hay_bombas = True
        for k in range(0, len(tablero[0])):
            if isinstance(tablero[k][j], int):
                hay_bombas = True
        if hay_bombas is False:
            tablero[i][j] = "-"
        if verificar_islas(tablero) is False: **<-- solo se tendrian que eliminar estas dos filas**
            tablero[i][j] = "-" **<--**
        if es_necesario_colocar(tablero, i, j) is False:
            tablero[i][j] = "-"
    return tablero

## Referencias de codigo externo
Para realizar mi tarea saqué codigo de:

1. https://github.com/IIC2233/Syllabus/blob/main/Tareas/T0/Sala%20Ayuda/laberinto.py. Específicamente, utilicé la función: es_valida(tablero, i, j), y está implmentada en el archivo functions.py, en las líneas 160. Esta función revisa y verifica que si este una coordenada (i, j), en el tablero, es decir que las coordenadas no se salgan del tablero. 
2. https://github.com/IIC2233/Syllabus/blob/main/Tareas/T0/Sala%20Ayuda/laberinto.py. Aunque no utilicé la función completa, utilicé la estructura, y parte del codigo, en las funciones: solucionar_tablero_rec(tablero: list, nueva_posicion: tuple,ruta_actual: list, direcciones) y solucionar_tablero(tablero: list), en las lineas 321 y 339 del archivo functions.py. Estas funciones revisan y solucionan el tablero recursivamente.
3. https://www.lawebdelprogramador.com/foros/Python/1453225-Explicacion-de-una-funcion-de-permutaciones.html. Esta  es una función que, al no poder utilizar la libreria itertools, permuta todos los elementos de una lista. Esto me sirvió para poder permutar los diferentes movimientos para moverse dentro del tablero, y así abarcar la mayor cantidad de casos/soluciones posibles. Esta función se ve implementada en el archivo functions.py, en la linea 312.
    