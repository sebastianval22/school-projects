from PyQt5.QtCore import pyqtSignal, QObject
import parametros as p


class Luigi(QObject):

    def __init__(self, posicion_luigi: tuple) -> None:
        super().__init__()
        self.vidas = p.CANTIDAD_VIDAS
        self.posicion_luigi = posicion_luigi


class Ghost_V(QObject):
    senal_mover_ghost_v = pyqtSignal()

    def __init__(self, pos_inicial, posicion, arriba: bool) -> None:
        super().__init__()
        self.posicion = posicion
        self.posicion_inicial = pos_inicial
        self.arriba = arriba


class Ghost_H(QObject):
    def __init__(self, pos_inicial, posicion, derecha: bool) -> None:
        super().__init__()
        self.posicion = posicion
        self.posicion_inicial = pos_inicial
        self.derecha = derecha


class Roca(QObject):
    def __init__(self, posicion, posicion_inical, id) -> None:
        super().__init__()
        self.posicion = posicion
        self.posicion_inicial = posicion_inical
        self.id = id


class Follower_Villian(QObject):
    def __init__(self, pos_inicial, posicion, direccion) -> None:
        super().__init__()
        self.posicion = posicion
        self.posicion_inicial = pos_inicial
        self.direccion = direccion
