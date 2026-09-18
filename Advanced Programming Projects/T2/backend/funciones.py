import parametros as p
import random as r


def revisar_alrededores(coordenadas: tuple, info: dict, objetivo: str):
    # Checks whether any of the 4 orthogonally-adjacent cells holds the
    # target entity type.
    # -- game-rule logic redacted for showcase repo --
    return False


def entrega_nueva_posicion(coordenadas: tuple, direccion: str):
    # Translates a cell's bounding-box coordinates one 25px grid step in
    # the given direction (W/S/D/A = up/down/right/left).
    # -- game-rule logic redacted for showcase repo --
    return coordenadas


def calcular_prioridad(posicion_inicial: tuple, posicion_meta: tuple):
    # Follower-ghost pathing: ranks the 4 move directions by how much
    # closer each gets the ghost to the target position, with randomized
    # tie-breaking among equally-good orderings so movement doesn't look
    # too mechanical.
    # -- game-rule logic redacted for showcase repo --
    return ["W", "A", "S", "D"]


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
