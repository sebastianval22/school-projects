from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QLineEdit,
                             QMessageBox)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import (QColor, QFont)
import parametros as p
import sys
import copy


class Ventana_Final(QWidget):
    senal_volver_a_empezar = pyqtSignal(str, str)

    def __init__(self) -> None:
        super().__init__()

    def nombre(self, nombre: str, vidas: int):
        self.nombre_usuario = nombre

    def crear_mapa(self, diccionario: dict, posicion_luigi: tuple,
                   posicion_estrella: tuple):
        self.diccionario = copy.deepcopy(diccionario)
        self.diccionario[posicion_luigi] = "L"
        self.diccionario[posicion_estrella] = "S"
        info_mapa = ""
        for j in range(0, 14):
            for k in range(0, 9):
                entidad = self.diccionario[(240+(k*25)), 240+((k+1)*25),
                                           75+(j*25), 75+((j+1)*25)]
                info_mapa += entidad
            info_mapa += "\n"
        self.info_mapa = info_mapa

    def final(self, tiempo_final: str, vidas_finales: str, gano: bool,
              mapa: str):
        self.mapa = mapa
        self.setGeometry(500, 500, 500, 500)
        self.vidas_finales = int(vidas_finales)
        lista = tiempo_final.split(":")
        seg_final = int((int(lista[0])*60)+(int(lista[1])))
        if gano is True:
            self.setWindowTitle("GANASTE!!!")
            self.background = QLabel("", self)
            self.background.setGeometry(0, 0, 500, 500)
            color = QColor(0, 255, 0)
            self.background.setStyleSheet(
                "background-color: {}".format(color.name()))
            puntaje = int((seg_final*p.MULTIPLICADOR_PUNTAJE)/(
                p.CANTIDAD_VIDAS + 1 - int(vidas_finales)))
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(24)
            font.setBold(True)
            msg = self.nombre_usuario + ", has ganado!!!"
            self.mensaje = QLabel("", self)
            self.mensaje.setText(msg)
            self.mensaje.setGeometry(100, 100, 400, 100)
            self.mensaje.setFont(font)
            self.boton_salir = QPushButton("Salir", self)
            self.puntaje = QLabel("", self)
            puntaje_msg = "Tu puntaje fue: " + str(puntaje)
            self.puntaje.setText(puntaje_msg)
            self.puntaje.setFont(font)
            self.puntaje.setGeometry(100, 200, 400, 100)
            self.boton_salir = QPushButton("Salir", self)
            self.boton_jugar_otra_vez = QPushButton(
                "Volver a jugar!! (presiona acá)", self)
            self.boton_jugar_otra_vez.setFont(font)
            self.boton_jugar_otra_vez.setGeometry(50, 300, 400, 100)
            if self.mapa == "Modo constructor":
                self.texto_nombre = QLineEdit(self)
                self.texto_nombre.setGeometry(50, 400, 400, 40)
                self.texto_nombre.setPlaceholderText("Guardar archivo como...")
            self.conectar_botones()
        else:
            if self.vidas_finales <= 0:
                extra_msg = "Se te acabaron las vidas "
            else:
                extra_msg = "Se te acabo el tiempo "
            self.setWindowTitle("PERDISTE!!!")
            self.background = QLabel("", self)
            self.background.setGeometry(0, 0, 500, 500)
            color = QColor(255, 0, 0)
            self.background.setStyleSheet(
                "background-color: {}".format(color.name()))
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(24)
            font.setBold(True)
            self.boton_salir = QPushButton("Salir", self)
            self.mensaje = QLabel("", self)
            msg = str(extra_msg + self.nombre_usuario)
            self.mensaje.setText(msg)
            self.mensaje.setGeometry(70, 140, 400, 100)
            self.mensaje.setFont(font)
            self.boton_jugar_otra_vez = QPushButton(
                "Intenta otra vez!(presiona acá)", self)
            self.boton_jugar_otra_vez.setFont(font)
            self.boton_jugar_otra_vez.setGeometry(70, 300, 400, 100)
            if self.mapa == "Modo constructor":
                self.texto_nombre = QLineEdit(self)
                self.texto_nombre.setGeometry(70, 400, 400, 40)
                self.texto_nombre.setPlaceholderText("Guardar archivo como...")
            self.conectar_botones()
        self.show()

    def conectar_botones(self):
        self.boton_salir.clicked.connect(self.salir)
        self.boton_jugar_otra_vez.clicked.connect(self.enviar_info)

    def enviar_info(self):
        if self.mapa == "Modo constructor":
            nombre = self.texto_nombre.text()
            bool = (("á" in nombre) or ("é" in nombre) or ("í" in nombre) or
                    ("ó" in nombre) or ("ú" in nombre))
            if ((nombre.isalnum() is False)):
                mensaje = "El nombre tiene que ser alfanumérico"
                msg = QMessageBox()
                msg.setWindowTitle("ERORR")
                msg.setText(mensaje)
                msg.setIcon(QMessageBox.Warning)
                msg.exec()
            elif (bool is True):
                mensaje = "No puede leer tildes..."
                msg = QMessageBox()
                msg.setWindowTitle("ERORR")
                msg.setText(mensaje)
                msg.setIcon(QMessageBox.Warning)
                msg.exec()
            else:
                self.mapa = nombre
                path = "./mapas/" + self.mapa + ".txt"
                with open(path, "w") as file:
                    file.write(self.info_mapa)
                self.senal_volver_a_empezar.emit(self.mapa + ".txt",
                                                 self.nombre_usuario)
        else:
            self.senal_volver_a_empezar.emit(self.mapa,
                                             self.nombre_usuario)

    def salir(self):
        sys.exit()
