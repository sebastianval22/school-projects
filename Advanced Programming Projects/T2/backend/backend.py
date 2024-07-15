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
        eliminar = []
        p = 0
        for i in range(len(self.fantasmas_v)):
            fantasma = self.fantasmas_v[i]
            id = i - p
            posicion_1 = fantasma.posicion
            if fantasma.arriba is False:
                posible_posicion = f.entrega_nueva_posicion(posicion_1, "S")
                lista = list(self.diccionario_labels.keys())
                if posible_posicion in lista:
                    entidad = self.diccionario_labels[posible_posicion]
                    if ((entidad == "-") or (entidad == "H") or (
                         entidad == "V") or (entidad == "Z")):
                        self.senal_mover.emit(posicion_1, posible_posicion,
                                              "V", id, "S")
                        fantasma.posicion = posible_posicion
                    elif entidad == "F":
                        self.senal_eliminar_entidad.emit("V", id)
                        eliminar.append(fantasma)
                        p += 1
                    elif entidad == "L":
                        self.luigi.posicion_luigi = self.posicion_luigi_inicial
                        self.senal_mover.emit(posible_posicion,
                                              self.posicion_luigi_inicial, "L",
                                              0, "D")
                        self.senal_mover.emit(posicion_1, posible_posicion,
                                              "V", id, "S")
                        fantasma.posicion = posible_posicion
                        self.choque_fantasma()
                    elif ((entidad == "R") or (entidad == "P")):
                        fantasma.arriba = True
                else:
                    fantasma.arriba = True
            else:
                posible_posicion = f.entrega_nueva_posicion(posicion_1, "W")
                lista = list(self.diccionario_labels.keys())
                if posible_posicion in lista:
                    entidad = self.diccionario_labels[posible_posicion]
                    if ((entidad == "-") or (entidad == "H") or (
                         entidad == "V") or (entidad == "Z")):
                        self.senal_mover.emit(posicion_1, posible_posicion,
                                              "V", id, "W")
                        fantasma.posicion = posible_posicion
                    elif entidad == "F":
                        self.senal_eliminar_entidad.emit("V", id)
                        eliminar.append(fantasma)
                        p += 1
                    elif entidad == "L":
                        self.luigi.posicion_luigi = self.posicion_luigi_inicial
                        self.senal_mover.emit(posible_posicion,
                                              self.posicion_luigi_inicial, "L",
                                              0, "D")
                        self.senal_mover.emit(posicion_1, posible_posicion,
                                              "V", id, "W")
                        fantasma.posicion = posible_posicion
                        self.choque_fantasma()
                    elif ((entidad == "R") or (entidad == "P")):
                        fantasma.arriba = False
                else:
                    fantasma.arriba = False
        for elemento in eliminar:
            self.fantasmas_v.remove(elemento)

    def fantasmas_horizontales(self) -> None:
        eliminar = []
        p = 0
        for i in range(len(self.fantasmas_h)):
            fantasma = self.fantasmas_h[i]
            id = i - p
            posicion_1 = fantasma.posicion
            if fantasma.derecha is False:
                posible_posicion = f.entrega_nueva_posicion(posicion_1, "A")
                lista = list(self.diccionario_labels.keys())
                if posible_posicion in lista:
                    entidad = self.diccionario_labels[posible_posicion]
                    if ((entidad == "-") or (entidad == "H") or (
                         entidad == "V") or (entidad == "Z")):
                        self.senal_mover.emit(posicion_1, posible_posicion,
                                              "H", id, "A")
                        fantasma.posicion = posible_posicion
                    elif entidad == "F":
                        self.senal_eliminar_entidad.emit("H", id)
                        eliminar.append(fantasma)
                        p += 1
                    elif entidad == "L":
                        self.luigi.posicion_luigi = self.posicion_luigi_inicial
                        self.senal_mover.emit(posible_posicion,
                                              self.posicion_luigi_inicial, "L",
                                              0, "D")
                        self.senal_mover.emit(posicion_1, posible_posicion,
                                              "H", id, "A")
                        fantasma.posicion = posible_posicion
                        self.choque_fantasma()
                    elif ((entidad == "R") or (entidad == "P")):
                        fantasma.derecha = True
                else:
                    fantasma.derecha = True
            else:
                posible_posicion = f.entrega_nueva_posicion(posicion_1, "D")
                lista = list(self.diccionario_labels.keys())
                if posible_posicion in lista:
                    entidad = self.diccionario_labels[posible_posicion]
                    if ((entidad == "-") or (entidad == "H") or (
                         entidad == "V") or (entidad == "Z")):
                        self.senal_mover.emit(posicion_1, posible_posicion,
                                              "H", id, "D")
                        fantasma.posicion = posible_posicion
                    elif entidad == "F":
                        self.senal_eliminar_entidad.emit("H", id)
                        eliminar.append(fantasma)
                        p += 1
                    elif entidad == "L":
                        self.luigi.posicion_luigi = self.posicion_luigi_inicial
                        self.senal_mover.emit(posible_posicion,
                                              self.posicion_luigi_inicial, "L",
                                              0, "D")
                        self.senal_mover.emit(posicion_1, posible_posicion,
                                              "H", id, "D")
                        fantasma.posicion = posible_posicion
                        self.choque_fantasma()
                    elif ((entidad == "R") or (entidad == "P")):
                        fantasma.derecha = False
                else:
                    fantasma.derecha = False
        for elemento in eliminar:
            self.fantasmas_h.remove(elemento)

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
        posicion_a = self.luigi.posicion_luigi
        posible_posicion = f.entrega_nueva_posicion(posicion_a, direccion)
        lista = list(self.diccionario_labels.keys())
        if posible_posicion in lista:
            entidad = self.diccionario_labels[posible_posicion]
            if entidad == "-":
                self.senal_mover.emit(posicion_a, posible_posicion,
                                      "L", 0, direccion)
                self.luigi.posicion_luigi = posible_posicion
            elif ((entidad == "V") or (entidad == "H") or (entidad == "Z")):
                self.luigi.posicion_luigi = self.posicion_luigi_inicial
                self.senal_mover.emit(posicion_a, self.posicion_luigi_inicial,
                                      "L", 0, "D")
                self.choque_fantasma()
            elif entidad == "R":
                self.verificar_choque_roca(posicion_a,
                                           posible_posicion, direccion)
            elif (self.diccionario_labels[posible_posicion]) == "F":
                self.luigi.posicion_luigi = self.posicion_luigi_inicial
                self.senal_mover.emit(posicion_a, self.posicion_luigi_inicial,
                                      "L", 0, "D")
                self.choque_fantasma()

    def choque_fantasma(self):
        if self.luigi.vidas <= 0:
            self.senal_termino_juego.emit(False)
            self.pausa(True)
        else:
            self.senal_perdida_vida.emit()
            self.luigi.vidas -= 1
            for i in range(0, len(self.fantasmas_h)):
                fantasma = self.fantasmas_h[i]
                self.senal_mover.emit(fantasma.posicion,
                                      fantasma.posicion_inicial, "H",
                                      i, "D")
                fantasma.derecha = True
                fantasma.posicion = fantasma.posicion_inicial
            for i in range(0, len(self.fantasmas_v)):
                fantasma = self.fantasmas_v[i]
                self.senal_mover.emit(fantasma.posicion,
                                      fantasma.posicion_inicial, "V",
                                      i, "W")
                fantasma.posicion = fantasma.posicion_inicial
                fantasma.arriba = True
            for i in range(0, len(self.fantasmas_z)):
                fantasma = self.fantasmas_z[i]
                self.senal_mover.emit(fantasma.posicion,
                                      fantasma.posicion_inicial, "Z",
                                      i, "D")
                fantasma.posicion = fantasma.posicion_inicial
                fantasma.arriba = True
            for roca in self.rocas:
                self.senal_mover.emit(roca.posicion,
                                      roca.posicion_inicial, "R",
                                      roca.id, "W")
                roca.posicion = roca.posicion_inicial

    def cheat_2(self):
        self.luigi.vidas = p.CANTIDAD_VIDAS

    def revisar_si_gano(self):
        if self.posicion_estrella == self.luigi.posicion_luigi:
            self.senal_termino_juego.emit(True)
            self.pausa = True

    def verificar_choque_roca(self, posicion_antigua, posicion_roca,
                              direccion):
        for roca in self.rocas:
            if roca.posicion == posicion_roca:
                roca_mover = roca
        nueva_posicion_roca = f.entrega_nueva_posicion(posicion_roca,
                                                       direccion)
        lista = list(self.diccionario_labels.keys())
        if nueva_posicion_roca in lista:
            if (self.diccionario_labels[nueva_posicion_roca] == "-") and (
                 nueva_posicion_roca != self.posicion_estrella):
                self.senal_mover.emit(posicion_roca, nueva_posicion_roca,
                                      "R", roca_mover.id, "D")
                self.senal_mover.emit(posicion_antigua, posicion_roca, "L",
                                      0, direccion)
                self.luigi.posicion_luigi = posicion_roca
                roca_mover.posicion = nueva_posicion_roca

    def fantasmas_follower(self):
        eliminar = []
        p = 0
        for i in range(len(self.fantasmas_z)):
            fantasma = self.fantasmas_z[i]
            id = i - p
            posicion_1 = fantasma.posicion
            prioridades = f.calcular_prioridad(posicion_1,
                                               self.luigi.posicion_luigi)
            for direccion in prioridades:
                posible_posicion = f.entrega_nueva_posicion(posicion_1,
                                                            direccion)
                lista = list(self.diccionario_labels.keys())
                if (posible_posicion in lista):
                    entidad = self.diccionario_labels[posible_posicion]
                    if ((entidad == "-") or (entidad == "H") or (
                         entidad == "V") or (entidad == "Z")):
                        self.senal_mover.emit(posicion_1, posible_posicion,
                                              "Z", id, direccion)
                        fantasma.posicion = posible_posicion
                        break
                    elif entidad == "F":
                        self.senal_eliminar_entidad.emit("Z", id)
                        eliminar.append(fantasma)
                        p += 1
                        break
                    elif entidad == "L":
                        self.luigi.posicion_luigi = self.posicion_luigi_inicial
                        self.senal_mover.emit(posible_posicion,
                                              self.posicion_luigi_inicial, "L",
                                              0, "D")
                        self.senal_mover.emit(posicion_1,
                                              posible_posicion, "Z",
                                              id, direccion)
                        fantasma.posicion = posible_posicion
                        self.choque_fantasma()
                        break
        for elemento in eliminar:
            self.fantasmas_z.remove(elemento)
