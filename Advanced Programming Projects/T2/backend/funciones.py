import parametros as p
import random as r


def revisar_alrededores(coordenadas: tuple, info: dict, objetivo: str):
    # arriba
    coordenadas_x_min = coordenadas[0]
    coordenadas_x_max = coordenadas[1]
    coordenadas_y_min = coordenadas[2] - 25
    coordenadas_y_max = coordenadas[3] - 25
    posible_posicion = (coordenadas_x_min, coordenadas_x_max,
                        coordenadas_y_min, coordenadas_y_max)
    lista = list(info.keys())
    if posible_posicion in lista:
        if info[posible_posicion] == objetivo:
            return True
    # abajo
    coordenadas_x_min = coordenadas[0]
    coordenadas_x_max = coordenadas[1]
    coordenadas_y_min = coordenadas[2] + 25
    coordenadas_y_max = coordenadas[3] + 25
    posible_posicion = (coordenadas_x_min, coordenadas_x_max,
                        coordenadas_y_min, coordenadas_y_max)
    lista = list(info.keys())
    if posible_posicion in lista:
        if info[posible_posicion] == objetivo:
            return True
    # izq
    coordenadas_x_min = coordenadas[0] - 25
    coordenadas_x_max = coordenadas[1] - 25
    coordenadas_y_min = coordenadas[2]
    coordenadas_y_max = coordenadas[3]
    posible_posicion = (coordenadas_x_min, coordenadas_x_max,
                        coordenadas_y_min, coordenadas_y_max)
    lista = list(info.keys())
    if posible_posicion in lista:
        if info[posible_posicion] == objetivo:
            return True
    # derecha
    coordenadas_x_min = coordenadas[0] + 25
    coordenadas_x_max = coordenadas[1] + 25
    coordenadas_y_min = coordenadas[2]
    coordenadas_y_max = coordenadas[3]
    posible_posicion = (coordenadas_x_min, coordenadas_x_max,
                        coordenadas_y_min, coordenadas_y_max)
    lista = list(info.keys())
    if posible_posicion in lista:
        if info[posible_posicion] == objetivo:
            return True
    return False


def entrega_nueva_posicion(coordenadas: tuple, direccion: str):
    # arriba
    if direccion == "W":
        coordenadas_x_min = coordenadas[0]
        coordenadas_x_max = coordenadas[1]
        coordenadas_y_min = coordenadas[2] - 25
        coordenadas_y_max = coordenadas[3] - 25
        posible_posicion = (coordenadas_x_min, coordenadas_x_max,
                            coordenadas_y_min, coordenadas_y_max)
        return posible_posicion
    # abajo
    elif direccion == "S":
        coordenadas_x_min = coordenadas[0]
        coordenadas_x_max = coordenadas[1]
        coordenadas_y_min = coordenadas[2] + 25
        coordenadas_y_max = coordenadas[3] + 25
        posible_posicion = (coordenadas_x_min, coordenadas_x_max,
                            coordenadas_y_min, coordenadas_y_max)
        return posible_posicion
    # derecha
    elif direccion == "D":
        coordenadas_x_min = coordenadas[0] + 25
        coordenadas_x_max = coordenadas[1] + 25
        coordenadas_y_min = coordenadas[2]
        coordenadas_y_max = coordenadas[3]
        posible_posicion = (coordenadas_x_min, coordenadas_x_max,
                            coordenadas_y_min, coordenadas_y_max)
        return posible_posicion
    # izq
    elif direccion == "A":
        coordenadas_x_min = coordenadas[0] - 25
        coordenadas_x_max = coordenadas[1] - 25
        coordenadas_y_min = coordenadas[2]
        coordenadas_y_max = coordenadas[3]
        posible_posicion = (coordenadas_x_min, coordenadas_x_max,
                            coordenadas_y_min, coordenadas_y_max)
        return posible_posicion


def calcular_prioridad(posicion_inicial: tuple, posicion_meta: tuple):
    x = posicion_inicial[0]
    y = posicion_inicial[2]
    x_meta = posicion_meta[0]
    y_meta = posicion_meta[2]
    prioridad = []
    if x == x_meta:
        if y > y_meta:
            lista = ["W", "D", "A", "S"]
            lista_1 = ["W", "D", "S", "A"]
            lista_2 = ["W", "A", "S", "D"]
            lista_3 = ["W", "A", "D", "S"]
            lista_4 = ["W", "S", "D", "A"]
            lista_5 = ["W", "S", "A", "D"]
            prioridades = []
            prioridades.append(lista)
            prioridades.append(lista_1)
            prioridades.append(lista_2)
            prioridades.append(lista_3)
            prioridades.append(lista_4)
            prioridades.append(lista_5)
            indice = r.randint(0, 5)
            prioridad = prioridades[indice]

        else:
            lista = ["S", "D", "A", "W"]
            lista_1 = ["S", "D", "W", "A"]
            lista_2 = ["S", "A", "W", "D"]
            lista_3 = ["S", "A", "D", "W"]
            lista_4 = ["S", "W", "D", "A"]
            lista_5 = ["S", "W", "A", "D"]
            prioridades = []
            prioridades.append(lista)
            prioridades.append(lista_1)
            prioridades.append(lista_2)
            prioridades.append(lista_3)
            prioridades.append(lista_4)
            prioridades.append(lista_5)
            indice = r.randint(0, 5)
            prioridad = prioridades[indice]
    elif y == y_meta:
        if x > x_meta:
            lista = ["A", "D", "S", "W"]
            lista_1 = ["A", "D", "W", "S"]
            lista_2 = ["A", "S", "W", "D"]
            lista_3 = ["A", "S", "D", "W"]
            lista_4 = ["A", "W", "D", "S"]
            lista_5 = ["A", "W", "S", "D"]
            prioridades = []
            prioridades.append(lista)
            prioridades.append(lista_1)
            prioridades.append(lista_2)
            prioridades.append(lista_3)
            prioridades.append(lista_4)
            prioridades.append(lista_5)
            indice = r.randint(0, 5)
            prioridad = prioridades[indice]
        else:
            lista = ["D", "A", "S", "W"]
            lista_1 = ["D", "A", "W", "S"]
            lista_2 = ["D", "S", "W", "A"]
            lista_3 = ["D", "S", "A", "W"]
            lista_4 = ["D", "W", "A", "S"]
            lista_5 = ["D", "W", "S", "A"]
            prioridades = []
            prioridades.append(lista)
            prioridades.append(lista_1)
            prioridades.append(lista_2)
            prioridades.append(lista_3)
            prioridades.append(lista_4)
            prioridades.append(lista_5)
            indice = r.randint(0, 5)
            prioridad = prioridades[indice]
    else:
        if (x_meta > x) and (y_meta > y):
            lista = ["D", "A", "S", "W"]
            lista_1 = ["D", "A", "W", "S"]
            lista_2 = ["D", "S", "W", "A"]
            lista_3 = ["D", "S", "A", "W"]
            lista_4 = ["D", "W", "A", "S"]
            lista_5 = ["D", "W", "S", "A"]
            lista_6 = ["S", "D", "A", "W"]
            lista_7 = ["S", "D", "W", "A"]
            lista_8 = ["S", "A", "W", "D"]
            lista_9 = ["S", "A", "D", "W"]
            lista_10 = ["S", "W", "D", "A"]
            lista_11 = ["S", "W", "A", "D"]
            prioridades = []
            prioridades.append(lista)
            prioridades.append(lista_1)
            prioridades.append(lista_2)
            prioridades.append(lista_3)
            prioridades.append(lista_4)
            prioridades.append(lista_5)
            prioridades.append(lista_6)
            prioridades.append(lista_7)
            prioridades.append(lista_8)
            prioridades.append(lista_9)
            prioridades.append(lista_10)
            prioridades.append(lista_11)
            indice = r.randint(0, 11)
            prioridad = prioridades[indice]

        elif (x_meta > x) and (y_meta < y):
            lista = ["D", "A", "S", "W"]
            lista_1 = ["D", "A", "W", "S"]
            lista_2 = ["D", "S", "W", "A"]
            lista_3 = ["D", "S", "A", "W"]
            lista_4 = ["D", "W", "A", "S"]
            lista_5 = ["D", "W", "S", "A"]
            lista_6 = ["W", "D", "A", "S"]
            lista_7 = ["W", "D", "S", "A"]
            lista_8 = ["W", "A", "S", "D"]
            lista_9 = ["W", "A", "D", "S"]
            lista_10 = ["W", "S", "D", "A"]
            lista_11 = ["W", "S", "A", "D"]
            prioridades = []
            prioridades.append(lista)
            prioridades.append(lista_1)
            prioridades.append(lista_2)
            prioridades.append(lista_3)
            prioridades.append(lista_4)
            prioridades.append(lista_5)
            prioridades.append(lista_6)
            prioridades.append(lista_7)
            prioridades.append(lista_8)
            prioridades.append(lista_9)
            prioridades.append(lista_10)
            prioridades.append(lista_11)
            indice = r.randint(0, 11)
            prioridad = prioridades[indice]
        elif (x_meta < x) and (y_meta < y):
            lista = ["A", "D", "S", "W"]
            lista_1 = ["A", "D", "W", "S"]
            lista_2 = ["A", "S", "W", "D"]
            lista_3 = ["A", "S", "D", "W"]
            lista_4 = ["A", "W", "D", "S"]
            lista_5 = ["A", "W", "S", "D"]
            lista_6 = ["W", "D", "A", "S"]
            lista_7 = ["W", "D", "S", "A"]
            lista_8 = ["W", "A", "S", "D"]
            lista_9 = ["W", "A", "D", "S"]
            lista_10 = ["W", "S", "D", "A"]
            lista_11 = ["W", "S", "A", "D"]
            prioridades = []
            prioridades.append(lista)
            prioridades.append(lista_1)
            prioridades.append(lista_2)
            prioridades.append(lista_3)
            prioridades.append(lista_4)
            prioridades.append(lista_5)
            prioridades.append(lista_6)
            prioridades.append(lista_7)
            prioridades.append(lista_8)
            prioridades.append(lista_9)
            prioridades.append(lista_10)
            prioridades.append(lista_11)
            indice = r.randint(0, 11)
            prioridad = prioridades[indice]
        elif (x_meta < x) and (y_meta > y):
            lista = ["A", "D", "S", "W"]
            lista_1 = ["A", "D", "W", "S"]
            lista_2 = ["A", "S", "W", "D"]
            lista_3 = ["A", "S", "D", "W"]
            lista_4 = ["A", "W", "D", "S"]
            lista_5 = ["A", "W", "S", "D"]
            lista_6 = ["S", "D", "A", "W"]
            lista_7 = ["S", "D", "W", "A"]
            lista_8 = ["S", "A", "W", "D"]
            lista_9 = ["S", "A", "D", "W"]
            lista_10 = ["S", "W", "D", "A"]
            lista_11 = ["S", "W", "A", "D"]
            prioridades = []
            prioridades.append(lista)
            prioridades.append(lista_1)
            prioridades.append(lista_2)
            prioridades.append(lista_3)
            prioridades.append(lista_4)
            prioridades.append(lista_5)
            prioridades.append(lista_6)
            prioridades.append(lista_7)
            prioridades.append(lista_8)
            prioridades.append(lista_9)
            prioridades.append(lista_10)
            prioridades.append(lista_11)
            indice = r.randint(0, 11)
            prioridad = prioridades[indice]
            prioridad = prioridades[indice]
    return prioridad


def sprites(i, entidad, direccion):
    if entidad == "L":
        if direccion == "W":
            pixmap = p.L_sprite_U[i]
            return pixmap
        elif direccion == "A":
            pixmap = p.L_sprite_L[i]
            return pixmap
        elif direccion == "S":
            pixmap = p.L_sprite_D[i]
            return pixmap
        elif direccion == "D":
            pixmap = p.L_sprite_R[i]
            return pixmap
    elif entidad == "H":
        if direccion == "A":
            pixmap = p.H_sprite_L[i]
            return pixmap
        elif direccion == "D":
            pixmap = p.H_sprite_R[i]
            return pixmap
    elif entidad == "V":
        pixmap = p.V_sprite[i]
        return pixmap
    elif entidad == "Z":
        if direccion == "W":
            pixmap = p.V_sprite_FW[i]
            return pixmap
        elif direccion == "A":
            pixmap = p.FW_sprite_L[i]
            return pixmap
        elif direccion == "S":
            pixmap = p.V_sprite_FW[i]
            return pixmap
        elif direccion == "D":
            pixmap = p.FW_sprite_R[i]
            return pixmap


def update_timer(current_value: list):
    minutos = int(current_value[0])
    segundos = int(current_value[1])
    if (segundos == 0) and (minutos != 0):
        current_value[0] = str(minutos-1)
        current_value[1] = str(59)
    elif (segundos == 0) and (minutos == 0):
        return None
    else:
        current_value[1] = str(segundos - 1)
        if segundos - 1 < 10:
            segundos = str(0) + str(segundos - 1)
            current_value[1] = segundos
    return current_value
