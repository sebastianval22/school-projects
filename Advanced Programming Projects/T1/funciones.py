from collections import namedtuple
import clases as c

Tipos_de_arenas = ["normal", "mojada", "rocosa", "magnetica"]

eventos = ["lluvia", "terremoto", "derrumbe"]

# EXCAVADORES
info_excavadores = []
with open("excavadores.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = [linea.split(",") for linea in csv_file]
    csv_reader.pop(0)
    for linea in csv_reader:
        linea[6] = linea[6].strip("\n")
        info_excavadores.append(linea)


# ARENA
info_arenas = []
with open("arenas.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = [linea.split(",") for linea in csv_file]
    csv_reader.pop(0)
    for linea in csv_reader:
        linea[5] = linea[5].strip("\n")
        info_arenas.append(linea)

# TESORO
info_tesoros = []
with open("tesoros.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = [linea.split(",") for linea in csv_file]
    csv_reader.pop(0)
    for linea in csv_reader:
        linea[3] = linea[3].strip("\n")
        info_tesoros.append(linea)


# CONSUMIBLES
info_consumibles = []
with open("consumibles.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = [linea.split(",") for linea in csv_file]
    csv_reader.pop(0)
    for linea in csv_reader:
        linea[5] = linea[5].strip("\n")
        info_consumibles.append(linea)


def instanciar_arena(info: list) -> object:
    parametros = ["nombre", "tipo", "rareza", "humedad", "dureza", "estatica"]
    Arena_Tuple = namedtuple(typename="Arena_Tuple",
                             field_names=parametros)
    arena = Arena_Tuple(info[0], info[1], info[2], info[3], info[4], info[5])
    objeto_arena = c.Arena(arena)
    return objeto_arena


def instanciar_tesoro(info: list) -> object:
    tipo = "tesoro"
    objeto_tesoro = c.Tesoro(nombre=info[0], tipo=tipo, descripcion=info[1],
                             calidad=info[2], cambio=info[3])
    return objeto_tesoro


def instanciar_consumible(info: list) -> object:
    tipo = "consumible"
    objeto_consumible = c.Consumible(nombre=info[0], tipo=tipo,
                                     descripcion=info[1], energia=info[2],
                                     fuerza=info[3], suerte=info[4],
                                     felicidad=info[5])
    return objeto_consumible


def instanciar_excavador(info: list) -> object:
    parametros = ["nombre", "edad", "energia", "fuerza", "suerte", "felicidad"]
    Excavador_Tuple = namedtuple(typename="Excavador_Tuple",
                                 field_names=parametros)
    excavador = Excavador_Tuple(info[0], info[2], info[3],
                                info[4], info[5], info[6])
    tipo = info[1]
    if tipo == "docencio":
        objeto_excavador = c.ExcavadorDocencio(excavador)
    elif tipo == "tareo":
        objeto_excavador = c.ExcavadorTareo(excavador)
    else:
        objeto_excavador = c.ExcavadorHibrido(excavador)
    return objeto_excavador
