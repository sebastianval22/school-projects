from PyQt5.QtCore import pyqtSignal, QObject, QTimer
import parametros as p
import random as r
from backend.entidades import Ghost_H, Ghost_V, Luigi, Roca, Follower_Villian
import backend.funciones as f


class Juego(QObject):
    senal_empezar_juego = pyqtSignal(str)
    senal_esconder_inicio = pyqtSignal()
    senal_esconder_ventana_juego = pyqtSignal()
    senal_empezar_juego_timer = pyqtSignal(dict, tuple, str)
    senal_mover = pyqtSignal(tuple, tuple, str, int, str)
    senal_choque_fantasma = pyqtSignal()
    senal_eliminar_entidad = pyqtSignal(str, int)
    senal_perdida_vida = pyqtSignal()
    senal_termino_juego = pyqtSignal(bool)
    senal_nombre_juego = pyqtSignal(str, int)
    senal_crear_mapa = pyqtSignal(dict, tuple, tuple)

    def __init__(self) -> None:
        super().__init__()

    def set_nombre(self, nombre: str) -> None:
        self.nombre = nombre

    def seleccionar_mapa(self, mapa: str) -> None:
        self.mapa = mapa
        self.iniciar_juego()

    def pausa(self, pausado: bool):
        self.pausado = pausado
        if self.pausado is True:
            self.tiempo.stop()
        else:
            self.tiempo.start(self.tiempo_movimiento_fantasmas)

    def iniciar_juego(self) -> None:
        self.senal_esconder_inicio.emit()
        self.senal_empezar_juego.emit(self.mapa)

    def entidades(self, diccionario: dict, posicion_l: tuple,
                  posicion_s: tuple, mapa: str) -> None:
        self.tiempo = QTimer()
        ponderador = r.uniform(p.MIN_VELOCIDAD, p.MAX_VELOCIDAD)
        self.tiempo_movimiento_fantasmas = int((1/ponderador)*1000)
        self.tiempo.timeout.connect(self.fantasmas_verticales)
        self.tiempo.timeout.connect(self.fantasmas_horizontales)
        self.tiempo.timeout.connect(self.fantasmas_follower)
        self.fantasmas_h = []
        self.fantasmas_v = []
        self.fantasmas_z = []
        self.rocas = []
        self.diccionario_labels = diccionario
        self.posicion_luigi_inicial = posicion_l
        self.posicion_estrella = posicion_s
        self.senal_crear_mapa.emit(self.diccionario_labels,
                                   self.posicion_luigi_inicial,
                                   self.posicion_estrella)
        self.empezar_juego_timer()
        self.senal_nombre_juego.emit(self.nombre, self.luigi.vidas)
        self.mapa = mapa

    def empezar_juego_timer(self) -> None:
        contador_r = 0
        for items in self.diccionario_labels.items():
            coordenadas = items[0]
            entidad = items[1]
            if entidad == "L":
                self.luigi = Luigi(self.posicion_luigi_inicial)
            elif entidad == "V":
                objeto = Ghost_V(coordenadas, coordenadas, True)
                self.fantasmas_v.append(objeto)
            elif entidad == "H":
                objeto = Ghost_H(coordenadas, coordenadas, True)
                self.fantasmas_h.append(objeto)
            elif entidad == "Z":
                objeto = Follower_Villian(coordenadas, coordenadas, "D")
                self.fantasmas_z.append(objeto)
            elif entidad == "R":
                id = contador_r
                objeto = Roca(coordenadas, coordenadas, id)
                self.rocas.append(objeto)
                contador_r += 1
        self.senal_esconder_ventana_juego.emit()
        self.senal_empezar_juego_timer.emit(self.diccionario_labels,
                                            self.posicion_luigi_inicial,
                                            self.mapa)
        self.tiempo.start(self.tiempo_movimiento_fantasmas)

    def fantasmas_verticales(self) -> None:
        # Per-tick vertical ghost movement: advances each Ghost_V one cell
        # along its current direction, bouncing off walls/rocks, despawning
        # on fire, and triggering choque_fantasma() on colliding with Luigi.
        # -- game-rule logic redacted for showcase repo --
        pass

    def fantasmas_horizontales(self) -> None:
        # Per-tick horizontal ghost movement: same rules as
        # fantasmas_verticales, mirrored onto the horizontal axis.
        # -- game-rule logic redacted for showcase repo --
        pass

    def cheat_1(self):
        eliminar = []
        p = 0
        for i in range(0, len(self.fantasmas_v)):
            fantasma = self.fantasmas_v[i]
            id = i - p
            self.senal_eliminar_entidad.emit("V", id)
            eliminar.append(fantasma)
            p += 1
        for elemento in eliminar:
            self.fantasmas_v.remove(elemento)
        eliminar = []
        p = 0
        for i in range(0, len(self.fantasmas_h)):
            fantasma = self.fantasmas_h[i]
            id = i - p
            self.senal_eliminar_entidad.emit("H", id)
            eliminar.append(fantasma)
            p += 1
        for elemento in eliminar:
            self.fantasmas_h.remove(elemento)
        eliminar = []
        p = 0
        for i in range(0, len(self.fantasmas_z)):
            fantasma = self.fantasmas_z[i]
            id = i - p
            self.senal_eliminar_entidad.emit("Z", id)
            eliminar.append(fantasma)
            p += 1
        for elemento in eliminar:
            self.fantasmas_z.remove(elemento)

    def actualizar_mapa(self, diccionario: dict) -> None:
        self.diccionario_labels = diccionario

    def mover_a_luigi(self, direccion: str) -> None:
        # Resolves Luigi's move attempt: open square -> move, ghost/fire ->
        # lose a life via choque_fantasma(), rock -> delegate to
        # verificar_choque_roca() for pushing.
        # -- game-rule logic redacted for showcase repo --
        pass

    def choque_fantasma(self):
        # Life-loss consequence: ends the game if out of lives, otherwise
        # decrements a life and resets every ghost and rock to its starting
        # position.
        # -- game-rule logic redacted for showcase repo --
        pass

    def cheat_2(self):
        self.luigi.vidas = p.CANTIDAD_VIDAS

    def revisar_si_gano(self):
        # Win condition: Luigi's position matches the star's position.
        # -- game-rule logic redacted for showcase repo --
        pass

    def verificar_choque_roca(self, posicion_antigua, posicion_roca,
                              direccion):
        # Rock-pushing rule: a rock only slides forward (and Luigi follows
        # into its old cell) if the cell beyond it is empty and isn't the
        # star's position.
        # -- game-rule logic redacted for showcase repo --
        pass

    def fantasmas_follower(self):
        # Follower-ghost AI: each tick, ranks the 4 directions by how much
        # closer they'd bring the ghost to Luigi (via calcular_prioridad)
        # and takes the first viable one, handling collisions the same way
        # as the other ghost types.
        # -- game-rule logic redacted for showcase repo --
        pass
