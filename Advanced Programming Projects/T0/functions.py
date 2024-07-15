import copy


def cargar_tablero(nombre_archivo: str) -> list:
    archivo = open(("Archivos/"
                    + nombre_archivo), "r")
    info_archivo = (archivo.read()).split(",")
    archivo.close()
    dimension = int(info_archivo[0])
    info_archivo = info_archivo[1::]
    tablero_archivo = [[0 for col in range(dimension)]
                       for row in range(dimension)]
    contador = 0
    for i in range(0, dimension):
        for j in range(0, dimension):
            info_posicion = info_archivo[contador]
            if info_posicion.isdigit() is True:
                info_posicion = int(info_posicion)
            tablero_archivo[i][j] = info_posicion
            contador += 1
    return (tablero_archivo)


def guardar_tablero(nombre_archivo: str, tablero: list) -> None:
    archivo = open(("Archivos/" +
                    nombre_archivo), "w")
    dimension = len(tablero)
    string_archivo = ""
    string_archivo += (f"{dimension}")
    for i in range(0, len(tablero)):
        for j in range(0, len(tablero[0])):
            info_posicion = tablero[i][j]
            string_archivo += (f",{info_posicion}")
    archivo.write(str(string_archivo))
    archivo.close()


def verificar_valor_bombas(tablero: list) -> int:   # Regla 2
    bombas_invalidas = []
    for i in range(0, len(tablero)):
        for j in range(0, len(tablero[0])):
            info_posicion = str(tablero[i][j])
            if info_posicion.isdigit() is True:
                limite_superior = ((2 * len(tablero))-1)
                info_posicion = int(info_posicion)
                if (info_posicion < 2) or (info_posicion > limite_superior):
                    bombas_invalidas.append(info_posicion)
    return (len(bombas_invalidas))


def verificar_unicidad_celdas(tablero: list) -> int:        # Regla 3
    contador = 0
    for i in range(0, len(tablero)):
        for j in range(0, len(tablero[0])):
            info_posicion = str(tablero[i][j])
            if len(info_posicion) != 1:
                contador += 1
    return contador


def verificar_alcance_bomba(tablero: list, coordenada: tuple) -> int:  # Regla1
    fila = coordenada[0]
    columna = coordenada[1]
    posible_bomba = str(tablero[fila][columna])
    if posible_bomba.isdigit() is False:
        return (0)
    else:
        contador = 1
        # vertical_arriba
        for i in range(1, len(tablero)):
            if (fila - i) >= 0:
                posicion = tablero[fila - i][columna]
                if posicion != "T":
                    contador += 1
                else:
                    break
        # vertical_abajo
        for i in range(1, len(tablero)):
            if (fila + i) < len(tablero):
                posicion = tablero[fila + i][columna]
                if posicion != "T":
                    contador += 1
                else:
                    break
        # horizontal_derecha
        for i in range(1, len(tablero)):
            if (columna + i) < len(tablero):
                posicion = tablero[fila][columna + i]
                if posicion != "T":
                    contador += 1
                else:
                    break
        # horizontal_izquierda
        for i in range(1, len(tablero)):
            if (columna - i) >= 0:
                posicion = tablero[fila][columna - i]
                if posicion != "T":
                    contador += 1
                else:
                    break
    return contador


def verificar_alcance_todas_bombas(tablero: list) -> bool:    # Regla 1,
    for i in range(0, len(tablero)):        # para todas las bombas del tablero
        for j in range(0, len(tablero[0])):
            posicion_actual = str(tablero[i][j])
            if posicion_actual.isdigit() is True:
                numero_bomba = int(posicion_actual)
                alcance_calculado = verificar_alcance_bomba(tablero, (i, j))
                if alcance_calculado != numero_bomba:
                    return False
    return True


def verificar_alcance_todas_bombas_mas_o_igual(tablero: list) -> bool:
    for i in range(0, len(tablero)):  # Función recursiva, para ir revisando
        for j in range(0, len(tablero[0])):  # alcance de bombas para que sean,
            posicion_actual = str(tablero[i][j])  # igual o mayor que su número
            if posicion_actual.isdigit() is True:
                numero_bomba = int(posicion_actual)
                alcance_calculado = verificar_alcance_bomba(tablero, (i, j))
                if alcance_calculado < numero_bomba:
                    return False
    return True


def verificar_tortugas(tablero: list) -> int:  # Regla 4
    contador = 0
    for i in range(0, len(tablero)):
        for j in range(0, len(tablero[0])):
            posicion_actual = tablero[i][j]
            tortuga_mala = False
            if posicion_actual == "T":
                tortuga_mala = False
                # derecha
                if (j+1) < (len(tablero)):
                    posible_tortuga = tablero[i][j+1]
                    if posible_tortuga == "T":
                        tortuga_mala = True
                # abajo
                if (i+1) < (len(tablero)):
                    posible_tortuga = tablero[i+1][j]
                    if posible_tortuga == "T":
                        tortuga_mala = True
                # izquierda
                if (j-1) >= 0:
                    posible_tortuga = tablero[i][j-1]
                    if posible_tortuga == "T":
                        tortuga_mala = True
                # arriba
                if (i-1) >= 0:
                    posible_tortuga = tablero[i-1][j]
                    if posible_tortuga == "T":
                        tortuga_mala = True
            if tortuga_mala is True:
                contador += 1
    return contador


def es_valida(tablero, i, j, regla_5):
    # Funcion recursiva, para verificar posiciones del tablero
    if i < 0 or i >= len(tablero):
        return False
    if j < 0 or j >= len(tablero[0]):
        return False
    if regla_5 is False:
        if tablero[i][j] == 'T':
            return False
    return True


def verificar_islas(tablero: list) -> bool:  # Regla 5
    for i in range(0, len(tablero)):
        for j in range(0, len(tablero[0])):
            contador = 0
            if tablero[i][j] != "T":
                if es_valida(tablero, i-1, j, True):
                    posicion = tablero[i-1][j]
                    if posicion != "T":
                        contador += 1
                if es_valida(tablero, i+1, j, True):
                    posicion = tablero[i+1][j]
                    if posicion != "T":
                        contador += 1
                if es_valida(tablero, i, j+1, True):
                    posicion = tablero[i][j+1]
                    if posicion != "T":
                        contador += 1
                if es_valida(tablero, i, j-1, True):
                    posicion = tablero[i][j-1]
                    if posicion != "T":
                        contador += 1
                if contador == 0:
                    return False
    i = 0          # Diagonal parte 1
    for g in range(0, len(tablero[0])):
        j = 0
        i = g
        lista_recursiva = []
        for k in range(0, len(tablero[0])):
            lista_recursiva.append(str(tablero[i][j]))
            if es_valida(tablero, i + 1, j + 1, True):
                i += 1
                j += 1
            else:
                break
        if ("".join(lista_recursiva) == "T"*(len(lista_recursiva))) and \
                len(lista_recursiva) != 1:
            return False
    i = len(tablero) - 1  # Diagonal parte 2
    for g in range(0, len(tablero[0])):
        j = 0
        i = len(tablero) - 1 - g
        lista_recursiva = []
        for k in range(0, len(tablero[0])):
            lista_recursiva.append(str(tablero[i][j]))
            if es_valida(tablero, i - 1, j + 1, True):
                i -= 1
                j += 1
            else:
                break
        if ("".join(lista_recursiva) == "T"*(len(lista_recursiva))) and \
                len(lista_recursiva) != 1:
            return False
    i = 0  # Diagonal parte 3
    for g in range(0, len(tablero[0])):
        i = g
        j = len(tablero) - 1
        lista_recursiva = []
        for k in range(0, len(tablero[0])):
            lista_recursiva.append(str(tablero[i][j]))
            if es_valida(tablero, i + 1, j - 1, True):
                i += 1
                j -= 1
            else:
                break
        if ("".join(lista_recursiva) == "T"*(len(lista_recursiva))) and \
                len(lista_recursiva) != 1:
            return False
    i = len(tablero) - 1  # Diagonal parte 4
    for g in range(0, len(tablero[0])):
        i = len(tablero) - 1 - g
        j = len(tablero) - 1
        lista_recursiva = []
        for k in range(0, len(tablero[0])):
            lista_recursiva.append(str(tablero[i][j]))
            if es_valida(tablero, i - 1, j - 1, True):
                i -= 1
                j -= 1
            else:
                break
        if ("".join(lista_recursiva) == "T"*(len(lista_recursiva))) and \
                len(lista_recursiva) != 1:
            return False
    return True


def es_caso_base(tablero: list) -> bool:  # Caso base-> ya esta solucionado
    alcances = verificar_alcance_todas_bombas(tablero)  # R1
    bombas_invalidas = verificar_valor_bombas(tablero)  # R2
    unicidad_celdas = verificar_unicidad_celdas(tablero)  # R3
    tortugas_invalidas = verificar_tortugas(tablero)  # R4
    hay_islas = verificar_islas(tablero)  # R5
    if ((alcances is True) and (bombas_invalidas == 0) and
       (unicidad_celdas == 0) and (tortugas_invalidas == 0)
       and (hay_islas is True)):
        return True
    else:
        return False


def resetear_tablero(tablero: list, tortugas_no_cambiar):
    for i in range(0, len(tablero)):  # Quita todas las tortugas
        for j in range(0, len(tablero[i])):
            if tablero[i][j] == "T":
                if (i, j) not in tortugas_no_cambiar:
                    tablero[i][j] = "-"
    return tablero


def es_necesario_colocar(tablero, i, j):
    p = i - 1
    while p >= 0:
        if es_valida(tablero, p, j, True):
            posicion = tablero[p][j]
            if isinstance(posicion, int):  # es una bomba
                return True
            elif posicion == "T":
                break
        p -= 1
    p = i + 1
    while p < len(tablero):
        if es_valida(tablero, p, j, True):
            posicion = tablero[p][j]
            if isinstance(posicion, int):  # es una bomba
                return True
            elif posicion == "T":
                break
        p += 1
    p = j - 1
    while p >= 0:
        if es_valida(tablero, i, p, True):
            posicion = tablero[i][p]
            if isinstance(posicion, int):  # es una bomba
                return True
            elif posicion == "T":
                break
        p -= 1
    p = j + 1
    while p < len(tablero):
        if es_valida(tablero, i, p, True):
            posicion = tablero[i][p]
            if isinstance(posicion, int):  # es una bomba
                return True
            elif posicion == "T":
                break
        p += 1
    return False


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
        if verificar_islas(tablero) is False:
            tablero[i][j] = "-"
        if es_necesario_colocar(tablero, i, j) is False:
            tablero[i][j] = "-"
    return tablero


def permu(xs):  # Función que permuta los elementos de una lista
    if len(xs) <= 1:
        yield xs
    else:
        for i in range(len(xs)):
            for p in permu(xs[:i] + xs[i + 1:]):
                yield [xs[i]] + p


def solucionar_tablero_rec(tablero: list, nueva_posicion: tuple,
                           ruta_actual: list, direcciones):
    if es_caso_base(tablero):
        return tablero
    for direccion in direcciones:
        nueva_pos_1 = (nueva_posicion[0] + (direccion[0]),
                       nueva_posicion[1] + direccion[1])
        if es_valida(tablero, nueva_pos_1[0], nueva_pos_1[1], False) and \
                (nueva_pos_1 not in ruta_actual):
            nueva_pos = nueva_pos_1
            tablero = colocar_tortugas(tablero, nueva_pos)
            ruta_actual.append(nueva_pos)
            return solucionar_tablero_rec(tablero, nueva_pos,
                                          ruta_actual, direcciones)

    return None


def solucionar_tablero(tablero: list):  # OBLIGATORIA
    direccion = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    todas_direcciones = list(permu(direccion))
    list_empty = []
    tortugas_NO_cambiar = []
    for m in range(0, len(tablero)):
        for n in range(0, len(tablero)):
            if tablero[m][n] == "T":
                tortugas_NO_cambiar.append((m, n))
    for p in range(0, len(todas_direcciones)):
        direcciones = todas_direcciones[p]
        for i in range(0, len(tablero)):
            for j in range(0, len(tablero[0])):
                tablero = resetear_tablero(tablero, tortugas_NO_cambiar)
                ruta_inicial = copy.deepcopy(list_empty)
                None_o_tablero = solucionar_tablero_rec(tablero, (i, j),
                                                        ruta_inicial,
                                                        direcciones)
                if isinstance(None_o_tablero, list):
                    return None_o_tablero
    return None
