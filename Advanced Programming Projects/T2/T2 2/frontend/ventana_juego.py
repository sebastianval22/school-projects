from PyQt5.QtCore import Qt, pyqtSignal, QMimeData
from PyQt5.QtWidgets import (QComboBox, QHBoxLayout, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import (QPixmap, QMouseEvent, QIcon, QDrag)
import parametros as p
import sys


class Ventana_Juego(QWidget):
    senal_click_pantalla = pyqtSignal(int, int)
    senal_jugar = pyqtSignal(dict, tuple, tuple, str)
    senal_limpiar_ventana_juego_timer = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.labels_casillas = {}
        self.setAcceptDrops(True)

    def empezar_juego(self, mapa: str) -> None:
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle(str("DCCazafantasmas: " + mapa))
        self.mapa = mapa
        if mapa != "Modo constructor":
            self.generar_layout_mapa()
        else:
            self.generar_layout_constructor()

    def generar_layout(self, constructor: bool):
        self.boton_salir = QPushButton("Salir", self)
        for i in range(0, p.LARGO_GRILLA):
            self.pared = QLabel("P", self)
            self.pared.setGeometry(215, 50+(i*25), 25, 25)
            pixeles = QPixmap(p.PARED_FRONTERA)
            pixeles = pixeles.scaled(25, 25)
            self.pared.setPixmap(pixeles)
        for j in range(0, p.LARGO_GRILLA):
            self.pared = QLabel("P", self)
            self.pared.setGeometry(465, 50+(j*25), 25, 25)
            pixeles = QPixmap(p.PARED_FRONTERA)
            pixeles = pixeles.scaled(25, 25)
            self.pared.setPixmap(pixeles)
        for k in range(1, p.ANCHO_GRILLA - 1):
            self.pared = QLabel("P", self)
            self.pared.setGeometry(215+(k*25), 50, 25, 25)
            pixeles = QPixmap(p.PARED_FRONTERA)
            pixeles = pixeles.scaled(25, 25)
            self.pared.setPixmap(pixeles)
        for o in range(1, p.ANCHO_GRILLA - 1):
            self.pared = QLabel("P", self)
            self.pared.setGeometry(215+(o*25), 425, 25, 25)
            pixeles = QPixmap(p.PARED_FRONTERA)
            pixeles = pixeles.scaled(25, 25)
            self.pared.setPixmap(pixeles)
        # Botones
        self.boton_limpiar = QPushButton("Limpiar", self)
        self.boton_jugar = QPushButton("Jugar", self)
        self.conectar_botones()
        hbox_general = QHBoxLayout()

        vbox1 = QVBoxLayout()

        if constructor is True:
            self.crear_botones()
            self.generar_selector_objeto()
            hbox2 = QHBoxLayout()
            hbox2.addWidget(self.selector_objeto)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.boton_limpiar)
        hbox.addWidget(self.boton_jugar)

        if constructor is True:
            vbox1.addStretch(1)
            vbox1.addLayout(hbox2)
            vbox1.addWidget(self.boton_luigi)
            vbox1.addWidget(self.boton_pared)
            vbox1.addWidget(self.boton_roca)
            vbox1.addWidget(self.boton_fuego)
            vbox1.addWidget(self.boton_estrella)
            vbox1.addWidget(self.boton_fantasma_v)
            vbox1.addWidget(self.boton_fantasma_h)
            vbox1.addWidget(self.boton_fantasma_z)
            vbox1.addStretch(5)
            vbox1.addLayout(hbox)
            vbox1.addStretch(1)
        else:
            vbox1.addStretch(20)
            vbox1.addLayout(hbox)
            vbox1.addStretch(1)

        hbox_general.addLayout(vbox1)
        hbox_general.addStretch(17)
        self.setLayout(hbox_general)

    def crear_botones(self):
        self.boton_luigi = Buttons(p.LUIGI_R_1, "(1)", "L", 1)
        self.boton_pared = Buttons(p.WALL, f"({p.MAXIMO_PARED})", "P",
                                   p.MAXIMO_PARED)
        self.boton_roca = Buttons(p.ROCK, f"({p.MAXIMO_ROCA})", "R",
                                  p.MAXIMO_ROCA)
        self.boton_fuego = Buttons(p.FIRE, f"({p.MAXIMO_FUEGO})", "F",
                                   p.MAXIMO_FUEGO)
        self.boton_estrella = Buttons(p.OSSTAR, "(1)", "S", 1)
        self.boton_fantasma_v = Buttons(p.RED_GHOST_V_1,
                                        f"({p.MAXIMO_FANTASMAS_VERTICAL})",
                                        "V", p.MAXIMO_FANTASMAS_VERTICAL)
        self.boton_fantasma_h = Buttons(p.WHITE_GHOST_R_1,
                                        f"({p.MAXIMO_FANTASMAS_HORIZONTAL})",
                                        "H", p.MAXIMO_FANTASMAS_HORIZONTAL)
        self.boton_fantasma_z = Buttons(p.RED_GHOST_V_2,
                                        f"({p.MAXIMO_FANTASMAS_FOLLOWER})",
                                        "Z", p.MAXIMO_FANTASMAS_FOLLOWER)

    def dragEnterEvent(self, event) -> None:
        event.accept()

    def dropEvent(self, event) -> None:
        position = event.pos()
        string = event.mimeData().text()
        lista_info = string.split("***")
        if int(lista_info[2]) <= 0:
            msg = QMessageBox()
            msg.setWindowTitle("ERORR")
            msg.setText("No hay suficientes entidades...")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
        else:
            self.colocar_entidad(position.x(), position.y(),
                                 lista_info[0], lista_info[1])
        event.accept()

    def colocar_entidad(self, x, y, icon_path, id):
        if (240 <= x <= 465) and (75 <= y <= 425):
            for j in range(0, 14):
                for k in range(0, 9):
                    x_min = (240+(k*25))
                    x_max = 240+((k+1)*25)
                    y_min = 75+(j*25)
                    y_max = 75+((j+1)*25)
                    if (x_min <= x < x_max) and (y_min <= y < y_max):
                        entidad = self.labels_casillas[(240+(k*25)),
                                                       240+((k+1)*25),
                                                       75+(j*25),
                                                       75+((j+1)*25)]
                        if entidad == "-":
                            self.labels_casillas[(240+(k*25)),
                                                 240+((k+1)*25),
                                                 75+(j*25),
                                                 75+((j+1)*25)] = id
                            self.casilla = QLabel("", self)
                            self.casilla.setGeometry(240+(k*25), 75+(j*25),
                                                     25, 25)
                            pixeles = QPixmap(icon_path)
                            pixeles = pixeles.scaled(25, 25)
                            self.casilla.setPixmap(pixeles)
                            if id == "L":
                                self.posicion_luigi = (240+(k*25),
                                                       240+((k+1)*25),
                                                       75+(j*25),
                                                       75+((j+1)*25))
                            if id == "S":
                                self.posicion_estrella = (240+(k*25),
                                                          240+((k+1)*25),
                                                          75+(j*25),
                                                          75+((j+1)*25))
                            self.casilla.show()
                            self.disminuir_cantidad_entidades(id)
                            break

    def disminuir_cantidad_entidades(self, id):
        if id == "L":
            self.boton_luigi.disminuir_cantidad()
        elif id == "P":
            self.boton_pared.disminuir_cantidad()
        elif id == "R":
            self.boton_roca.disminuir_cantidad()
        elif id == "F":
            self.boton_fuego.disminuir_cantidad()
        elif id == "H":
            self.boton_fantasma_h.disminuir_cantidad()
        elif id == "V":
            self.boton_fantasma_v.disminuir_cantidad()
        elif id == "Z":
            self.boton_fantasma_z.disminuir_cantidad()
        elif id == "S":
            self.boton_estrella.disminuir_cantidad()

    def generar_selector_objeto(self):
        self.selector_objeto = QComboBox(self)
        lista = ["Todos", "Bloques", "Entidades"]
        self.selector_objeto.addItems(lista)
        self.selector_objeto.currentIndexChanged.connect(self.change_widget)

    def change_widget(self, index: int):
        self.boton_luigi.setVisible(index == 0 or index == 2)
        self.boton_pared.setVisible(index == 0 or index == 1)
        self.boton_roca.setVisible(index == 0 or index == 1)
        self.boton_fuego.setVisible(index == 0 or index == 1)
        self.boton_estrella.setVisible(index == 0 or index == 1)
        self.boton_fantasma_v.setVisible(index == 0 or index == 2)
        self.boton_fantasma_h.setVisible(index == 0 or index == 2)
        self.boton_fantasma_z.setVisible(index == 0 or index == 2)

    def generar_layout_mapa(self):
        self.generar_layout(False)
        path = "./mapas/" + self.mapa
        with open(path, "r") as file:
            info_mapa = file.readlines()
        for i in range(0, 14):
            info_mapa[i] = list(info_mapa[i].strip(" \n"))
        for j in range(0, 14):
            for k in range(0, 9):
                objeto = info_mapa[j][k]
                if objeto == "-":
                    self.labels_casillas[(240+(k*25)), 240+((k+1)*25),
                                         75+(j*25), 75+((j+1)*25)] = "-"
                elif objeto == "L":
                    self.casilla_luigi = QLabel("L", self)
                    self.casilla_luigi.setGeometry(240+(k*25), 75+(j*25),
                                                   25, 25)
                    pixeles = QPixmap(p.LUIGI_R_1)
                    pixeles = pixeles.scaled(25, 25)
                    self.casilla_luigi.setPixmap(pixeles)
                    self.labels_casillas[(240+(k*25)), 240+((k+1)*25),
                                         75+(j*25), 75+((j+1)*25)] = "L"
                    self.posicion_luigi = (240+(k*25), 240+((k+1)*25),
                                           75+(j*25), 75+((j+1)*25))
                elif objeto == "P":
                    self.casilla_pared = QLabel("P", self)
                    self.casilla_pared.setGeometry(240+(k*25), 75+(j*25),
                                                   25, 25)
                    pixeles = QPixmap(p.WALL)
                    pixeles = pixeles.scaled(25, 25)
                    self.casilla_pared.setPixmap(pixeles)
                    self.labels_casillas[(240+(k*25)), 240+((k+1)*25),
                                         75+(j*25), 75+((j+1)*25)] = "P"
                elif objeto == "F":
                    self.casilla_fuego = QLabel("F", self)
                    self.casilla_fuego.setGeometry(240+(k*25), 75+(j*25),
                                                   25, 25)
                    pixeles = QPixmap(p.FIRE)
                    pixeles = pixeles.scaled(25, 25)
                    self.casilla_fuego.setPixmap(pixeles)
                    self.labels_casillas[(240+(k*25)), 240+((k+1)*25),
                                         75+(j*25), 75+((j+1)*25)] = "F"
                elif objeto == "H":
                    self.casilla_horizontal = QLabel("H", self)
                    self.casilla_horizontal.setGeometry(240+(k*25), 75+(j*25),
                                                        25, 25)
                    pixeles = QPixmap(p.WHITE_GHOST_R_1)
                    pixeles = pixeles.scaled(25, 25)
                    self.casilla_horizontal.setPixmap(pixeles)
                    self.labels_casillas[(240+(k*25)), 240+((k+1)*25),
                                         75+(j*25), 75+((j+1)*25)] = "H"
                elif objeto == "V":
                    self.casilla_vertical = QLabel("V", self)
                    self.casilla_vertical.setGeometry(240+(k*25), 75+(j*25),
                                                      25, 25)
                    pixeles = QPixmap(p.RED_GHOST_V_1)
                    pixeles = pixeles.scaled(25, 25)
                    self.casilla_vertical.setPixmap(pixeles)
                    self.labels_casillas[(240+(k*25)), 240+((k+1)*25),
                                         75+(j*25), 75+((j+1)*25)] = "V"
                elif objeto == "Z":
                    self.casilla_follower = QLabel("Z", self)
                    self.casilla_follower.setGeometry(240+(k*25), 75+(j*25),
                                                      25, 25)
                    pixeles = QPixmap(p.RED_GHOST_V_1)
                    pixeles = pixeles.scaled(25, 25)
                    self.casilla_follower.setPixmap(pixeles)
                    self.labels_casillas[(240+(k*25)), 240+((k+1)*25),
                                         75+(j*25), 75+((j+1)*25)] = "Z"
                elif objeto == "S":
                    self.casilla_estrella = QLabel("E", self)
                    self.casilla_estrella.setGeometry(240+(k*25), 75+(j*25),
                                                      25, 25)
                    pixeles = QPixmap(p.OSSTAR)
                    pixeles = pixeles.scaled(25, 25)
                    self.casilla_estrella.setPixmap(pixeles)
                    self.labels_casillas[(240+(k*25)), 240+((k+1)*25),
                                         75+(j*25), 75+((j+1)*25)] = "S"
                    self.posicion_estrella = (240+(k*25), 240+((k+1)*25),
                                              75+(j*25), 75+((j+1)*25))
                else:
                    self.casilla_roca = QLabel("R", self)
                    self.casilla_roca.setGeometry(240+(k*25), 75+(j*25),
                                                  25, 25)
                    pixeles = QPixmap(p.ROCK)
                    pixeles = pixeles.scaled(25, 25)
                    self.casilla_roca.setPixmap(pixeles)
                    self.labels_casillas[(240+(k*25)), 240+((k+1)*25),
                                         75+(j*25), 75+((j+1)*25)] = "R"
        self.show()

    def generar_layout_constructor(self):
        self.generar_layout(True)
        for j in range(0, 14):
            for k in range(0, 9):
                self.labels_casillas[(240+(k*25)), 240+((k+1)*25),
                                     75+(j*25), 75+((j+1)*25)] = "-"
        self.show()

    def enviar_info_1(self):
        diccionario_mapa = self.labels_casillas
        if ("S" in diccionario_mapa.values()) and (
           "L" in diccionario_mapa.values()):
            self.senal_jugar.emit(diccionario_mapa, self.posicion_luigi,
                                  self.posicion_estrella, self.mapa)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("ERORR")
            msg.setText("Tienes que colocar a Luigi y la Estrella")
            msg.setIcon(QMessageBox.Information)
            msg.exec()

    def salir(self):
        sys.exit()

    def conectar_botones(self):
        # Comenzar
        self.boton_salir.clicked.connect(self.salir)
        self.boton_jugar.clicked.connect(self.enviar_info_1)
        # Limpiar
        if self.mapa == "Modo constructor":
            self.boton_limpiar.clicked.connect(self.limpiar)

    def limpiar(self):
        for j in range(0, 14):
            for k in range(0, 9):
                posicion = (240+(k*25)), 75+(j*25)
                child_widget = self.childAt(*posicion)
                if child_widget is not None and isinstance(child_widget,
                                                           QLabel):
                    child_widget.setParent(None)
                self.labels_casillas[(240+(k*25)), 240+((k+1)*25),
                                     75+(j*25), 75+((j+1)*25)] = "-"
        if self.mapa == "Modo constructor":
            self.actualizar_cantidades()

    def actualizar_cantidades(self):
        self.boton_luigi.actualizar_cantidad()
        self.boton_pared.actualizar_cantidad()
        self.boton_roca.actualizar_cantidad()
        self.boton_fuego.actualizar_cantidad()
        self.boton_fantasma_h.actualizar_cantidad()
        self.boton_fantasma_v.actualizar_cantidad()
        self.boton_fantasma_z.actualizar_cantidad()
        self.boton_estrella.actualizar_cantidad()

    def esconder_ventana(self):
        self.hide()


class Buttons(QPushButton):
    def __init__(self, icon_path: str, text: str, id: str, cantidad: int):
        super().__init__()
        self.icon_path = icon_path
        self.icon = QIcon(icon_path)
        self.setIcon(self.icon)
        self.setText(text)
        self.id = id
        self.cantidad = cantidad
        self.cantidad_default = cantidad

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        if e.buttons() == Qt.LeftButton:
            mimeData = QMimeData()
            info = (self.icon_path)+"***"+str(self.id)+"***"+str(self.cantidad)
            mimeData.setText(info)
            drag = QDrag(self)
            pixeles = QPixmap(self.icon_path).scaled(25, 25)
            drag.setPixmap(pixeles)
            drag.setMimeData(mimeData)
            drag.exec(Qt.MoveAction)

    def disminuir_cantidad(self):
        self.cantidad -= 1
        self.setText(f"({self.cantidad})")
        self.show()

    def actualizar_cantidad(self):
        self.cantidad = self.cantidad_default
        self.setText(f"({self.cantidad})")
        self.show()
