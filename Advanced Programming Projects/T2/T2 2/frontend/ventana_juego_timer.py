from PyQt5.QtCore import pyqtSignal, QTimer, QPropertyAnimation, QPoint
from PyQt5.QtWidgets import (QLabel, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import (QPixmap, QKeyEvent)
from PyQt5.QtMultimedia import QSound
import parametros as p
import backend.funciones as f
import sys


class Ventana_Juego_Timer(QWidget):
    senal_nueva_posicion_luigi = pyqtSignal(str)
    senal_actualizar_info_mapa = pyqtSignal(dict)
    senal_termino = pyqtSignal(str, str, bool, str)
    senal_revisar_si_gano = pyqtSignal()
    senal_pausa = pyqtSignal(bool)
    senal_cheat_1 = pyqtSignal()
    senal_cheat_2 = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.bloquear = False
        self.fantasmas_h = []
        self.fantasmas_v = []
        self.fantasmas_z = []
        self.rocas = []

    def empezar_juego(self, diccionario_labels: dict, posicion_inicial: tuple,
                      mapa: str):
        self.boton_salir = QPushButton("Salir", self)
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Jugando...")
        self.diccionario_labels = diccionario_labels
        self.generar_layout()
        self.set_animation()
        self.timers_entidad()
        self.timer.start()
        self.vertical_i = 0
        self.timer_v.start()
        self.horizontal_i = 0
        self.timer_h.start()
        self.follower = 0
        self.timer_z.start()
        self.pausa = False
        self.posicion_inicial = posicion_inicial
        self.cantidad_vidas = p.CANTIDAD_VIDAS
        self.orden = ""
        self.cheat_2 = False
        self.mapa = mapa

    def generar_layout(self):
        for i in range(0, p.LARGO_GRILLA):
            self.pared = QLabel("P", self)
            self.pared.setGeometry(215, 50+(i*25), 25, 25)
            pixeles = (QPixmap(p.PARED_FRONTERA)).scaled(25, 25)
            self.pared.setPixmap(pixeles)
            self.pared = QLabel("P", self)
            self.pared.setGeometry(465, 50+(i*25), 25, 25)
            self.pared.setPixmap(pixeles)
        for k in range(1, p.ANCHO_GRILLA - 1):
            self.pared = QLabel("P", self)
            self.pared.setGeometry(215+(k*25), 50, 25, 25)
            pixeles = (QPixmap(p.PARED_FRONTERA)).scaled(25, 25)
            self.pared.setPixmap(pixeles)
            self.pared = QLabel("P", self)
            self.pared.setGeometry(215+(k*25), 425, 25, 25)
            self.pared.setPixmap(pixeles)
        self.boton_pausa = QPushButton("Pausar", self)
        self.descripcion_tiempo = QLabel("Tiempo:      ", self)
        self.descripcion_vidas = QLabel("Vidas:    ", self)
        self.tiempo = QLabel("", self)
        self.vidas = QLabel("", self)
        minutos_iniciales = p.TIEMPO_CUENTA_REGRESIVA//60
        segundos_iniciales = p.TIEMPO_CUENTA_REGRESIVA % 60
        if segundos_iniciales < 10:
            segundos_iniciales = str(0) + str(segundos_iniciales)
        self.tiempo.setText((str(minutos_iniciales)+":" +
                             str(segundos_iniciales)))
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.conectar_timer()
        self.conectar_boton()
        self.vidas.setText(str(p.CANTIDAD_VIDAS))
        lista_info = list(self.diccionario_labels.values())
        contador = 0
        for j in range(0, 14):
            for k in range(0, 9):
                objeto = lista_info[contador]
                posicion = ((240+(k*25)), 240+((k+1)*25), 75+(j*25),
                            75+((j+1)*25))
                if objeto == "L":
                    self.casilla_luigi = QLabel("L", self)
                    self.casilla_luigi.setGeometry(240+(k*25), 75+(j*25),
                                                   25, 25)
                    pixeles = (QPixmap(p.LUIGI_R_1)).scaled(25, 25)
                    self.casilla_luigi.setPixmap(pixeles)
                    self.posicion_luigi = posicion
                elif objeto == "P":
                    self.casilla_pared = QLabel("P", self)
                    self.casilla_pared.setGeometry(240+(k*25), 75+(j*25),
                                                   25, 25)
                    pixeles = (QPixmap(p.WALL)).scaled(25, 25)
                    self.casilla_pared.setPixmap(pixeles)
                elif objeto == "F":
                    self.casilla_fuego = QLabel("F", self)
                    self.casilla_fuego.setGeometry(240+(k*25), 75+(j*25),
                                                   25, 25)
                    pixeles = (QPixmap(p.FIRE)).scaled(25, 25)
                    self.casilla_fuego.setPixmap(pixeles)
                elif objeto == "H":
                    self.casilla_horizontal = QLabel("H", self)
                    self.casilla_horizontal.setGeometry(240+(k*25), 75+(j*25),
                                                        25, 25)
                    pixeles = (QPixmap(p.WHITE_GHOST_R_1)).scaled(25, 25)
                    self.casilla_horizontal.setPixmap(pixeles)
                    self.fantasmas_h.append([self.casilla_horizontal, "D"])
                elif objeto == "V":
                    self.casilla_vertical = QLabel("V", self)
                    self.casilla_vertical.setGeometry(240+(k*25), 75+(j*25),
                                                      25, 25)
                    pixeles = (QPixmap(p.RED_GHOST_V_1)).scaled(25, 25)
                    self.casilla_vertical.setPixmap(pixeles)
                    self.fantasmas_v.append(self.casilla_vertical)
                elif objeto == "Z":
                    self.casilla_follower = QLabel("Z", self)
                    self.casilla_follower.setGeometry(240+(k*25), 75+(j*25),
                                                      25, 25)
                    pixeles = (QPixmap(p.RED_GHOST_V_1)).scaled(25, 25)
                    self.casilla_follower.setPixmap(pixeles)
                    self.fantasmas_z.append([self.casilla_follower, "D"])
                elif objeto == "S":
                    self.casilla_estrella = QLabel("S", self)
                    self.casilla_estrella.setGeometry(240+(k*25), 75+(j*25),
                                                      25, 25)
                    pixeles = (QPixmap(p.OSSTAR)).scaled(25, 25)
                    self.casilla_estrella.setPixmap(pixeles)
                    objeto = "-"
                    self.posicion_estrella = posicion
                elif objeto == "R":
                    self.casilla_roca = QLabel("R", self)
                    self.casilla_roca.setGeometry(240+(k*25), 75+(j*25),
                                                  25, 25)
                    pixeles = (QPixmap(p.ROCK)).scaled(25, 25)
                    self.casilla_roca.setPixmap(pixeles)
                    self.rocas.append(self.casilla_roca)
                self.diccionario_labels[posicion] = objeto
                contador += 1
        self.senal_actualizar_info_mapa.emit(self.diccionario_labels)
        vbox1 = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addStretch(3)
        hbox1.addWidget(self.descripcion_tiempo)
        hbox1.addWidget(self.tiempo)
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.descripcion_vidas)
        hbox2.addWidget(self.vidas)
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.boton_pausa)
        vbox1.addStretch(3)
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)
        vbox1.addStretch(16)
        hbox_general = QHBoxLayout()
        hbox_general.addLayout(vbox1)
        hbox_general.addStretch(14)
        self.setLayout(hbox_general)
        self.show()

    def update_timer(self):
        current_value = (self.tiempo.text()).split(":")
        new = f.update_timer(current_value)
        if new is None:
            self.timer.stop()
            self.esconder(False)
        else:
            texto = ":".join(new)
            self.tiempo.setText(str(texto))
            self.tiempo.show()

    def conectar_timer(self):
        self.timer.timeout.connect(self.update_timer)

    def conectar_boton(self):
        self.boton_pausa.clicked.connect(self.pausar)
        self.boton_salir.clicked.connect(self.salir)

    def salir(self):
        sys.exit()

    def eliminar_entidad(self, entidad: str, id: int):
        if entidad == "V":
            fantasma = self.fantasmas_v[id]
            posicion = (fantasma.pos().x(), fantasma.pos().x() + 25,
                        fantasma.pos().y(), fantasma.pos().y() + 25)
            self.diccionario_labels[posicion] = "-"
            fantasma.setParent(None)
            self.fantasmas_v.pop(id)
            self.animaciones_v.pop(id)
        elif entidad == "H":
            fantasma = self.fantasmas_h[id][0]
            posicion = (fantasma.pos().x(), fantasma.pos().x() + 25,
                        fantasma.pos().y(), fantasma.pos().y() + 25)
            self.diccionario_labels[posicion] = "-"
            fantasma.setParent(None)
            self.fantasmas_h.pop(id)
            self.animaciones_h.pop(id)
        elif entidad == "Z":
            fantasma = self.fantasmas_z[id][0]
            posicion = (fantasma.pos().x(), fantasma.pos().x() + 25,
                        fantasma.pos().y(), fantasma.pos().y() + 25)
            self.diccionario_labels[posicion] = "-"
            fantasma.setParent(None)
            self.fantasmas_z.pop(id)
            self.animaciones_z.pop(id)
        self.senal_actualizar_info_mapa.emit(self.diccionario_labels)

    def pausar(self):
        if self.pausa is False:
            self.timer.stop()
            self.pausa = True
            self.senal_pausa.emit(True)
            self.boton_pausa.setText("Continuar")
            self.boton_pausa.show()
        else:
            self.timer.start()
            self.pausa = False
            self.senal_pausa.emit(False)
            self.boton_pausa.setText("Pausar")
            self.boton_pausa.show()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        self.orden += (event.text().upper())
        if (self.pausa is False) and (self.bloquear is False):
            if (event.text().upper()) in "WASD":
                self.senal_nueva_posicion_luigi.emit((event.text().upper()))
            elif (event.text().upper()) == "G":
                self.senal_revisar_si_gano.emit()
        if (event.text().upper()) == "P":
            self.pausar()
        if "KIL" in self.orden:
            self.senal_cheat_1.emit()
        if "INF" in self.orden:
            self.cheat_2 = True
            self.timer.stop()
            minutos_iniciales = p.TIEMPO_CUENTA_REGRESIVA//60
            segundos_iniciales = p.TIEMPO_CUENTA_REGRESIVA % 60
            if segundos_iniciales < 10:
                segundos_iniciales = str(0) + str(segundos_iniciales)
            self.tiempo.setText(str(minutos_iniciales)+":" +
                                str(segundos_iniciales))
            self.vidas.setText(str(p.CANTIDAD_VIDAS))
            self.cantidad_vidas = p.CANTIDAD_VIDAS

    def set_animation(self):
        self.luigi_animation = QPropertyAnimation(self.casilla_luigi, b"pos")
        self.luigi_animation.finished.connect(self.handleAnimationFinished)
        self.luigi_animation.setDuration(800)
        self.animaciones_h = []
        for fantasma_bool in self.fantasmas_h:
            fantasma = fantasma_bool[0]
            self.animacion = QPropertyAnimation(fantasma, b"pos")
            self.animacion.setDuration(800)
            self.animaciones_h.append(self.animacion)
        self.animaciones_v = []
        for fantasma in self.fantasmas_v:
            self.animacion = QPropertyAnimation(fantasma, b"pos")
            self.animacion.setDuration(800)
            self.animaciones_v.append(self.animacion)
        self.animaciones_z = []
        for fantasma_bool in self.fantasmas_z:
            fantasma = fantasma_bool[0]
            self.animacion = QPropertyAnimation(fantasma, b"pos")
            self.animacion.setDuration(800)
            self.animaciones_z.append(self.animacion)
        self.animaciones_roca = []
        for roca in self.rocas:
            self.animacion = QPropertyAnimation(roca, b"pos")
            self.animacion.setDuration(400)
            self.animaciones_roca.append(self.animacion)

    def timers_entidad(self):
        self.timer_sprite_L = QTimer()
        self.timer_sprite_L.setInterval(200)
        self.timer_sprite_L.timeout.connect(self.update_pixmap_L)
        self.timer_h = QTimer()
        self.timer_h.setInterval(200)
        self.timer_h.timeout.connect(self.update_pixmap_h)
        self.timer_v = QTimer()
        self.timer_v.setInterval(200)
        self.timer_v.timeout.connect(self.update_pixmap_v)
        self.timer_z = QTimer()
        self.timer_z.setInterval(200)
        self.timer_z.timeout.connect(self.update_pixmap_z)

    def update_pixmap_L(self):
        if self.bloquear is not False:
            if self.i > 2:
                self.i = 0
            pixmap = f.sprites(self.i, "L", self.direccion)
            pixeles = (QPixmap(pixmap)).scaled(25, 25)
            self.casilla_luigi.setPixmap(pixeles)
            self.i += 1

    def update_pixmap_v(self):
        if self.pausa is False:
            for fantasma in self.fantasmas_v:
                if self.vertical_i > 2:
                    self.vertical_i = 0
                pixmap = f.sprites(self.vertical_i, "V", "")
                pixeles = (QPixmap(pixmap)).scaled(25, 25)
                fantasma.setPixmap(pixeles)
            self.vertical_i += 1

    def update_pixmap_h(self):
        if self.pausa is False:
            for fantasma_bool in self.fantasmas_h:
                direccion = fantasma_bool[1]
                if self.horizontal_i > 2:
                    self.horizontal_i = 0
                pixmap = f.sprites(self.horizontal_i, "H", direccion)
                pixeles = (QPixmap(pixmap)).scaled(25, 25)
                fantasma_bool[0].setPixmap(pixeles)
            self.horizontal_i += 1

    def update_pixmap_z(self):
        if self.pausa is False:
            for fantasma_bool in self.fantasmas_z:
                direccion = fantasma_bool[1]
                if self.follower > 2:
                    self.follower = 0
                pixmap = f.sprites(self.follower, "Z", direccion)
                pixeles = (QPixmap(pixmap)).scaled(25, 25)
                fantasma_bool[0].setPixmap(pixeles)
            self.follower += 1

    def nuevo_lugar(self, p_1: tuple, new_p: tuple,
                    entidad: str, id: int, direccion: str):
        self.diccionario_labels[p_1] = "-"
        self.diccionario_labels[new_p] = entidad
        if entidad == "L":
            self.i = 0
            self.bloquear = True
            self.posicion_luigi = new_p
            self.direccion = direccion
            self.luigi_animation.setStartValue(QPoint(p_1[0], p_1[2]))
            self.luigi_animation.setEndValue(QPoint(new_p[0], new_p[2]))
            self.timer_sprite_L.start()
            self.luigi_animation.start()
        elif entidad == "V":
            self.animaciones_v[id].setStartValue(QPoint(p_1[0], p_1[2]))
            self.animaciones_v[id].setEndValue(QPoint(new_p[0], new_p[2]))
            self.animaciones_v[id].start()
        elif entidad == "H":
            self.fantasmas_h[id][1] = direccion
            self.animaciones_h[id].setStartValue(QPoint(p_1[0], p_1[2]))
            self.animaciones_h[id].setEndValue(QPoint(new_p[0], new_p[2]))
            self.animaciones_h[id].start()
        elif entidad == "Z":
            self.fantasmas_z[id][1] = direccion
            self.animaciones_z[id].setStartValue(QPoint(p_1[0], p_1[2]))
            self.animaciones_z[id].setEndValue(QPoint(new_p[0], new_p[2]))
            self.animaciones_z[id].start()
        elif entidad == "R":
            self.animaciones_roca[id].setStartValue(QPoint(p_1[0], p_1[2]))
            self.animaciones_roca[id].setEndValue(QPoint(new_p[0], new_p[2]))
            self.animaciones_roca[id].start()
        self.senal_actualizar_info_mapa.emit(self.diccionario_labels)

    def handleAnimationFinished(self):
        self.bloquear = False

    def perdio_vida(self):
        self.cantidad_vidas -= 1
        if self.cheat_2 is True:
            self.cantidad_vidas = p.CANTIDAD_VIDAS
            self.senal_cheat_2.emit()
        self.vidas.setText(str(self.cantidad_vidas))

    def esconder(self, gano: bool):
        self.timer.stop()
        tiempo_final = self.tiempo.text()
        vidas_finales = self.vidas.text()
        if gano is True:
            QSound.play(p.SOUND_GANO)
        else:
            QSound.play(p.SOUND_PERDIO)
        self.senal_termino.emit(tiempo_final, vidas_finales, gano,
                                self.mapa)
        self.hide()
