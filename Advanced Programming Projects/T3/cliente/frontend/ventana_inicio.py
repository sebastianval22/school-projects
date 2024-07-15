from PyQt5.QtWidgets import (QLabel, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import pyqtSignal
import sys
import json


class Ventana_Inicio(QWidget):

    senal_presiono_comenzar = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        with open("cliente/parametros.json") as jsno_file:
            data = json.load(jsno_file)
        self.data = data
        self.inicializa_gui()

    def inicializa_gui(self):
        self.setGeometry(500, 500, 500, 500)
        self.generar_widgets()
        self.conectar_botones()
        self.generar_layout()

    def generar_widgets(self):
        self.background = QLabel("", self)
        self.background.setGeometry(0, 0, 500, 500)
        pixeles = QPixmap(self.data["path_background"])
        pixeles = pixeles.scaled(500, 500)
        self.background.setPixmap(pixeles)
        # Label
        self.label = QLabel("", self)
        self.label.setText("SALA DE ESPERA")
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        self.label.setFont(font)
        # Botones
        self.boton_ingresar = QPushButton("Comenzar", self)
        self.boton_salir = QPushButton("Salir", self)
        # Jugadores
        self.labels_jugadores = []
        self.icons_jugadores = []
        self.jugador_1 = QLabel("", self)
        self.labels_jugadores.append(self.jugador_1)
        self.jugador_2 = QLabel("", self)
        self.labels_jugadores.append(self.jugador_2)
        self.jugador_3 = QLabel("", self)
        self.labels_jugadores.append(self.jugador_3)
        self.jugador_4 = QLabel("", self)
        self.labels_jugadores.append(self.jugador_4)
        self.jugador_1_icon = QLabel("", self)
        self.icons_jugadores.append(self.jugador_1_icon)
        self.jugador_2_icon = QLabel("", self)
        self.icons_jugadores.append(self.jugador_2_icon)
        self.jugador_3_icon = QLabel("", self)
        self.icons_jugadores.append(self.jugador_3_icon)
        self.jugador_4_icon = QLabel("", self)
        self.icons_jugadores.append(self.jugador_4_icon)

    def conectar_botones(self):
        # Comenzar
        self.boton_ingresar.clicked.connect(self.enviar_info)
        # Salir
        self.boton_salir.clicked.connect(self.salir)

    def salir(self):
        sys.exit()

    def set_nombre_i(self, nombre):
        self.nombre = nombre

    def enviar_info(self):
        self.senal_presiono_comenzar.emit()

    def avisar_limite(self, razon):
        if razon == "lleno":
            msg = QMessageBox()
            msg.setWindowTitle("SALA LLENA")
            msg.setText("LA SALA ESTÁ LLENA... POR FAVOR ESPERE")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("SALA EN JUEGO")
            msg.setText("LA SALA ESTÁ JUGANDO... POR FAVOR ESPERE")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()

    def avisar_entro(self, nombre):
        msg = QMessageBox()
        msg.setWindowTitle("NOTIFICACIÓN")
        msg.setText(f"¡¡SE LIBERÓ UN CUPO!! Entraste con el nombre {nombre}")
        msg.setIcon(QMessageBox.Information)
        msg.exec()

    def actualizar_jugadores(self, lista_nombre):
        pixeles = QPixmap(self.data["path_user_logo"])
        pixeles = pixeles.scaled(60, 60)
        contador = 0
        for nombre in lista_nombre:
            label_jugador = self.labels_jugadores[contador]
            label_jugador.setText(nombre)
            icon_jugador = self.icons_jugadores[contador]
            icon_jugador.setPixmap(pixeles)
            contador += 1
        for i in range(contador, 4):
            label_jugador = self.labels_jugadores[i]
            label_jugador.setText("")
            icon_jugador = self.icons_jugadores[i]
            icon_jugador.clear()

    def generar_layout(self):
        # Generamos el layout principal
        vbox = QVBoxLayout()
        # Generamos un layout para los botones centrales
        hbox = QHBoxLayout()
        hbox_jugadores = QHBoxLayout()
        hbox_jugadores.addWidget(self.jugador_1)
        hbox_jugadores.addWidget(self.jugador_2)
        hbox_jugadores.addWidget(self.jugador_3)
        hbox_jugadores.addWidget(self.jugador_4)
        hbox_jugadores_icon = QHBoxLayout()
        hbox_jugadores_icon.addWidget(self.jugador_1_icon)
        hbox_jugadores_icon.addWidget(self.jugador_2_icon)
        hbox_jugadores_icon.addWidget(self.jugador_3_icon)
        hbox_jugadores_icon.addWidget(self.jugador_4_icon)

        vbox.addWidget(self.label)
        vbox.addStretch(2)
        vbox.addLayout(hbox_jugadores_icon)
        vbox.addLayout(hbox_jugadores)
        vbox.addStretch(10)
        vbox.addWidget(self.boton_ingresar)
        vbox.addWidget(self.boton_salir)

        hbox.addStretch(4)
        hbox.addLayout(vbox)
        hbox.addStretch(4)
        # Setteamos el layout
        self.setLayout(hbox)
        self.setWindowTitle("Ventana Inicio")

        self.show()

    def esconder(self):
        self.close()
