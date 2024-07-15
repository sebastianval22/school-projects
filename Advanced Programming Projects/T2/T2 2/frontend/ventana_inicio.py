from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (QLabel, QComboBox, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QLineEdit, QMessageBox)
from PyQt5.QtGui import QPixmap, QKeyEvent
import sys
import os
import parametros as p


class Ventana_Inicio(QWidget):
    senal_mapa = pyqtSignal(str)
    senal_comenzar = pyqtSignal()
    senal_salir = pyqtSignal()
    senal_nombre = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self):
        self.setGeometry(500, 500, 500, 500)

        self.generar_widgets()
        self.generar_layout()
        self.conectar_botones()

    def generar_widgets(self):
        self.background = QLabel("", self)
        self.background.setGeometry(0, -100, 500, 500)
        pixeles = QPixmap(p.FONDO_INICIO)
        pixeles = pixeles.scaled(500, 500)
        self.background.setPixmap(pixeles)

        self.background2 = QLabel("", self)
        self.background2.setGeometry(0, 400, 500, 100)
        pixeles2 = QPixmap(p.PARED_FRONTERA)
        pixeles2 = pixeles2.scaled(500, 500)
        self.background2.setPixmap(pixeles2)

        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap(p.LOGO))
        self.logo.setScaledContents(True)
        self.logo.setGeometry(70, 20, 300, 120)

        # Creamos el selector que vamos a necesitar en la ventana de Inicio
        self.selector_mapa = QComboBox(self)
        mapas = os.listdir("mapas")
        mapas.append("Modo constructor")
        self.selector_mapa.addItems(mapas)

        # Botones
        self.boton_ingresar = QPushButton("Empezar juego", self)
        self.boton_salir = QPushButton("Salir", self)

        # Linea de texto editable
        self.texto_nombre = QLineEdit(self)
        self.texto_nombre.setPlaceholderText("Ingresa tu nombre...")

    def generar_layout(self):
        # Generamos el layout principal
        vbox = QVBoxLayout()

        # Generamos un layout para los botones centrales
        hbox = QHBoxLayout()
        hbox.addWidget(self.selector_mapa)
        hbox.addWidget(self.boton_ingresar)

        hbox2 = QHBoxLayout()
        hbox2.addStretch()
        hbox2.addStretch()
        hbox2.addStretch()
        hbox2.addWidget(self.boton_salir)

        vbox.addLayout(hbox2)
        vbox.addStretch()
        vbox.addWidget(self.texto_nombre)
        vbox.addLayout(hbox)

        # Setteamos el layout
        self.setLayout(vbox)
        self.setWindowTitle("Ventana Inicio")

        self.show()

    def conectar_botones(self):
        # Comenzar
        self.boton_ingresar.clicked.connect(self.enviar_info)
        # Salir
        self.boton_salir.clicked.connect(self.salir)

    def salir(self):
        sys.exit()

    def esconder_ventana(self):
        self.hide()

    def enviar_info(self) -> None:
        # Le avisamos al backend el mapa escogido
        nombre = self.texto_nombre.text()
        bool = (("á" in nombre) or ("é" in nombre) or ("í" in nombre) or
                ("ó" in nombre) or ("ú" in nombre))
        if ((nombre.isalnum() is False) or
            ((p.MIN_CARACTERES <= len(nombre) <= p.MAX_CARACTERES) is False)
           or (bool is True)):
            if p.MIN_CARACTERES > len(nombre):
                mensaje = "Nombre muy corto..."
            elif p.MAX_CARACTERES < len(nombre):
                mensaje = "Nombre muy laaaaaargo....."
            elif (nombre.isalnum() is False):
                mensaje = "El nombre tiene que ser alfanumérico"
            else:
                mensaje = "No puede leer tildes..."
            msg = QMessageBox()
            msg.setWindowTitle("ERORR")
            msg.setText(mensaje)
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        else:
            nombre = self.texto_nombre.text()
            self.senal_nombre.emit(nombre)
            text = self.selector_mapa.currentText()
            self.senal_mapa.emit(text)

    # Detectar cuando se presiona enter para también enviar_info
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.enviar_info()
