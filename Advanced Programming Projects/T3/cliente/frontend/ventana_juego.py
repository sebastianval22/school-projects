from PyQt5.QtWidgets import (QLabel, QWidget, QPushButton,
                             QMessageBox, QLineEdit, QComboBox)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import pyqtSignal
import sys
import json


class Ventana_Juego(QWidget):

    senal_dudar = pyqtSignal()
    senal_poder = pyqtSignal()
    senal_cambiar_dados = pyqtSignal()
    senal_pasar_turno = pyqtSignal()
    senal_anunciar_valor = pyqtSignal(str)
    senal_escogio_afectado_poder = pyqtSignal(tuple)
    senal_mostrar_dados_see = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        with open("cliente/parametros.json") as jsno_file:
            data = json.load(jsno_file)
        self.data = data
        self.sprites_dados = self.data["sprites_dados"]
        self.turno = 0
        self.orden = ""

    def mostrar(self, lista_jugadores):
        self.lista_jugadores = lista_jugadores
        self.setGeometry(0, 0, 800, 700)
        self.generar_widgets()
        self.conectar_botones()
        self.mostrar_jugadores(lista_jugadores)
        self.generar_layout()

    def generar_widgets(self):
        self.background = QLabel("", self)
        self.background.setGeometry(0, 0, 800, 700)
        pixeles = QPixmap(self.data["path_background_juego"])
        pixeles = pixeles.scaled(800, 700)
        self.background.setPixmap(pixeles)
        # Label_de_Arriba
        self.label_turno = QLabel("", self)
        self.label_turno.setText("Turno de:")
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_turno.setFont(font)

        self.label_numero_mayor = QLabel("", self)
        self.label_numero_mayor.setText("Numero mayor anunciado:")
        self.label_numero_mayor.setFont(font)

        self.label_turno_anterior = QLabel("", self)
        self.label_turno_anterior.setText("Turno anterior fue:")
        self.label_turno_anterior.setFont(font)

        self.label_numero_turno = QLabel("", self)
        self.label_numero_turno.setText("Numero Turno:")
        self.label_numero_turno.setFont(font)

        self.label_poder = QLabel("", self)

        # Botones
        font_2 = QFont()
        font_2.setFamily("Times New Roman")
        font_2.setPointSize(11)
        self.boton_anunciar_valor = QPushButton("Anunciar Valor", self)
        self.boton_anunciar_valor.setFont(font_2)
        self.text_anunciar_valor = QLineEdit(self)
        self.text_anunciar_valor.setFont(font_2)
        self.text_anunciar_valor.setPlaceholderText("Ingrese el valor...")
        self.boton_pasar_turno = QPushButton("Pasar turno", self)
        self.boton_pasar_turno.setFont(font_2)
        self.boton_cambiar_dados = QPushButton("Cambiar dados", self)
        self.boton_cambiar_dados.setFont(font_2)
        self.boton_usar_poder = QPushButton("Usar poder", self)
        self.boton_usar_poder.setFont(font_2)
        self.boton_dudar = QPushButton("Dudar", self)
        self.boton_dudar.setFont(font_2)

        # Jugadores
        self.labels_jugadores = []
        self.icons_jugadores = []
        self.vidas_jugadores = []
        self.dado_1_jugadores = []
        self.dado_2_jugadores = []
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
        self.jugador_1_vida = QLabel("", self)
        self.vidas_jugadores.append(self.jugador_1_vida)
        self.jugador_2_vida = QLabel("", self)
        self.vidas_jugadores.append(self.jugador_2_vida)
        self.jugador_3_vida = QLabel("", self)
        self.vidas_jugadores.append(self.jugador_3_vida)
        self.jugador_4_vida = QLabel("", self)
        self.vidas_jugadores.append(self.jugador_4_vida)
        self.jugador_1_dado_1 = QLabel("", self)
        self.dado_1_jugadores.append(self.jugador_1_dado_1)
        self.jugador_2_dado_1 = QLabel("", self)
        self.dado_1_jugadores.append(self.jugador_2_dado_1)
        self.jugador_3_dado_1 = QLabel("", self)
        self.dado_1_jugadores.append(self.jugador_3_dado_1)
        self.jugador_4_dado_1 = QLabel("", self)
        self.dado_1_jugadores.append(self.jugador_4_dado_1)
        self.jugador_1_dado_2 = QLabel("", self)
        self.dado_2_jugadores.append(self.jugador_1_dado_2)
        self.jugador_2_dado_2 = QLabel("", self)
        self.dado_2_jugadores.append(self.jugador_2_dado_2)
        self.jugador_3_dado_2 = QLabel("", self)
        self.dado_2_jugadores.append(self.jugador_3_dado_2)
        self.jugador_4_dado_2 = QLabel("", self)
        self.dado_2_jugadores.append(self.jugador_4_dado_2)

    def conectar_botones(self):
        self.boton_anunciar_valor.clicked.connect(self.anunciar_valor)
        self.boton_pasar_turno.clicked.connect(self.pasar_turno)
        self.boton_cambiar_dados.clicked.connect(self.cambiar_dados)
        self.boton_usar_poder.clicked.connect(self.usar_poder)
        self.boton_dudar.clicked.connect(self.dudar)

    def salir(self):
        sys.exit()

    def set_nombre_i(self, nombre):
        self.nombre = nombre

    def anunciar_valor(self):
        valor = (self.text_anunciar_valor.text())
        self.senal_anunciar_valor.emit(str(valor))

    def cambiar_qlinedit_anunciado(self, mensaje):
        self.text_anunciar_valor.setPlaceholderText(mensaje)

    def actualizar_num_mayor_anunciado(self, valor):
        nuevo_valor = f"Numero mayor anunciado:   {valor}"
        self.label_numero_mayor.setText(nuevo_valor)

    def pasar_turno(self):
        self.senal_pasar_turno.emit()

    def reset_num_turnos(self, num_turnos):
        self.label_numero_turno.setText(f"Numero Turno: {num_turnos}")
        if num_turnos == 0:
            self.label_poder.setText("")

    def avisar_juego_poder(self, nombre_poder):
        self.label_poder.setText(
            f"{nombre_poder[0]} invocó el poder de {nombre_poder[1]}")

    def actualizar_turnos(self, turno_actual_anterior):
        self.label_turno.setText(f"Turno de: {turno_actual_anterior[0]}")
        self.label_turno_anterior.setText(
            f"Turno anterior fue: {turno_actual_anterior[1]}")

    def establecer_dados(self, valor_dados):
        nombre_a_cambiar = valor_dados[0]
        dado_1 = valor_dados[1][0]
        dado_2 = valor_dados[1][1]
        contador = 0
        for qlabel in self.labels_jugadores:
            nombre = qlabel.text()
            if nombre == nombre_a_cambiar:
                label_dado_1 = self.dado_1_jugadores[contador]
                label_dado_2 = self.dado_2_jugadores[contador]
                label_dado_1.clear()
                label_dado_2.clear()
                pixeles_1 = QPixmap(self.sprites_dados[dado_1-1])
                pixeles_1 = pixeles_1.scaled(40, 40)
                pixeles_2 = QPixmap(self.sprites_dados[dado_2-1])
                pixeles_2 = pixeles_2.scaled(40, 40)
                label_dado_1.setPixmap(pixeles_1)
                label_dado_2.setPixmap(pixeles_2)
                break
            contador += 1

    def desconexion(self):
        msg = QMessageBox()
        msg.setWindowTitle("DESCONEXIÓN")
        msg.setText(
            "Se perdio la conexión con el servidor. Debes salir del programa")
        msg.setIcon(QMessageBox.Critical)
        boton_salir = msg.addButton("Salir", QMessageBox.RejectRole)
        boton_salir.clicked.connect(self.salir)
        msg.exec()

    def avisar_que_perdio(self, nombre_perdio):
        msg = QMessageBox()
        msg.setWindowTitle("NOTIFICACIÓN")
        msg.setText(f"Perdiste {nombre_perdio}... Debes salirte del programa")
        msg.setIcon(QMessageBox.Information)
        boton_salir = msg.addButton("Salir", QMessageBox.RejectRole)
        boton_salir.clicked.connect(self.salir)
        msg.exec()

    def usa_poder(self, bool_poder):
        if bool_poder[0] is False:
            msg = QMessageBox()
            msg.setWindowTitle("NOTIFICACIÓN")
            msg.setText("No tienes poderes...")
            msg.setIcon(QMessageBox.Information)
            msg.exec()
        else:
            lista = []
            for jugador in self.labels_jugadores:
                if jugador.text() != "":
                    lista.append(jugador.text())
            font = QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(15)
            self.poder_escoger = QComboBox(self)
            self.poder_escoger.addItems(lista)
            self.poder_escoger.setGeometry(330, 340, 100, 30)
            self.boton_escogio = QPushButton("Escoger", self)
            self.poder = bool_poder[1]
            self.boton_escogio.setFont(font)
            self.boton_escogio.setGeometry(445, 340, 100, 30)
            self.boton_escogio.clicked.connect(self.escogio_poder)
            self.poder_escoger.setVisible(True)
            self.boton_escogio.setVisible(True)

    def escogio_poder(self):
        nombre = self.poder_escoger.currentText()
        self.senal_escogio_afectado_poder.emit((nombre, self.poder))
        self.poder_escoger.setParent(None)
        self.boton_escogio.setParent(None)
        self.poder = ""

    def cambiar_dados(self):
        self.senal_cambiar_dados.emit()

    def cubrir_dados(self, nombre_lista):
        excepto_nombre = nombre_lista[0]
        pixeles_1 = QPixmap(self.data["sprite_dado_1"])
        pixeles_1 = pixeles_1.scaled(40, 40)
        pixeles_2 = QPixmap(self.data["sprite_dado_2"])
        pixeles_2 = pixeles_2.scaled(40, 40)
        for nombre in nombre_lista[1]:
            if excepto_nombre != nombre:
                for i in range(0, len(self.labels_jugadores)):
                    qlabel = self.labels_jugadores[i]
                    nombre_label = qlabel.text()
                    if nombre == nombre_label:
                        label_d_1 = self.dado_1_jugadores[i]
                        label_d_2 = self.dado_2_jugadores[i]
                        label_d_1.setPixmap(pixeles_1)
                        label_d_2.setPixmap(pixeles_2)

    def usar_poder(self):
        self.senal_poder.emit()

    def dudar(self):
        self.senal_dudar.emit()

    def termino_partida(self, ganador):
        msg = QMessageBox()
        msg.setWindowTitle("FELICIDADES")
        msg.setText(f"{ganador} has ganado DCCACHOS!!! FELICITACIONES!!!")
        msg.setIcon(QMessageBox.Information)
        boton_salir = msg.addButton("Salir", QMessageBox.RejectRole)
        boton_salir.clicked.connect(self.salir)
        msg.exec()

    def actualizar_jugadores(self, lista_nombre):
        for i in range(0, len(self.labels_jugadores)):
            label_jugador = self.labels_jugadores[i]
            if label_jugador.text() not in lista_nombre:
                label_jugador.setText("")
                icon_jugador = self.icons_jugadores[i]
                icon_jugador.clear()
                dado_1 = self.dado_1_jugadores[i]
                dado_1.clear()
                dado_2 = self.dado_2_jugadores[i]
                dado_2.clear()
                vida_jugador = self.vidas_jugadores[i]
                vida_jugador.clear()

    def actualizar_vidas(self, dic_jugador_vida):
        for nombres, vidas in dic_jugador_vida.items():
            for i in range(0, len(self.labels_jugadores)):
                label_jugador = self.labels_jugadores[i]
                if label_jugador.text() == nombres:
                    label_vida = self.vidas_jugadores[i]
                    pixeles = QPixmap(self.data["sprites_dados"][vidas-1])
                    pixeles = pixeles.scaled(50, 50)
                    label_vida.clear()
                    label_vida.setPixmap(pixeles)

    def mostrar_jugadores(self, jugadores):
        pixeles = QPixmap(self.data["path_user_logo"])
        pixeles = pixeles.scaled(70, 70)
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        pixeles_1 = QPixmap(self.data["sprite_dado_1"])
        pixeles_1 = pixeles_1.scaled(40, 40)
        pixeles_2 = QPixmap(self.data["sprite_dado_2"])
        pixeles_2 = pixeles_2.scaled(40, 40)
        contador = 0
        for nombre in jugadores:
            label_jugador = self.labels_jugadores[contador]
            label_jugador.setText(nombre)
            label_jugador.setFont(font)
            icon_jugador = self.icons_jugadores[contador]
            icon_jugador.setPixmap(pixeles)
            dado_1 = self.dado_1_jugadores[contador]
            dado_1.setPixmap(pixeles_1)
            dado_2 = self.dado_2_jugadores[contador]
            dado_2.setPixmap(pixeles_2)
            contador += 1
        string = f"Turno de: {self.jugador_1.text()}"
        self.label_turno.setText(string)
        string = f"Numero Turno: {self.turno}"
        self.label_numero_turno.setText(string)

    def generar_layout(self):
        self.label_numero_mayor.setGeometry(10, 25, 200, 40)
        self.jugador_4_vida.setGeometry(70, 300, 50, 50)
        self.jugador_4_icon.setGeometry(150, 300, 70, 70)
        self.jugador_4_dado_1.setGeometry(250, 250, 40, 40)
        self.jugador_4_dado_2.setGeometry(250, 300, 40, 40)
        self.jugador_4.setGeometry(120, 390, 130, 20)
        self.label_turno.setGeometry(310, 5, 150, 15)
        self.label_turno_anterior.setGeometry(300, 25, 175, 40)
        self.jugador_3_icon.setGeometry(380, 100, 70, 70)
        self.jugador_3_vida.setGeometry(460, 100, 50, 50)
        self.jugador_3.setGeometry(370, 190, 130, 20)
        self.jugador_3_dado_1.setGeometry(380, 230, 40, 40)
        self.jugador_3_dado_2.setGeometry(430, 230, 40, 40)
        self.label_poder.setGeometry(10, 650, 250, 30)
        self.jugador_1_dado_1.setGeometry(380, 450, 40, 40)
        self.jugador_1_dado_2.setGeometry(430, 450, 40, 40)
        self.jugador_1_icon.setGeometry(380, 500, 70, 70)
        self.jugador_1_vida.setGeometry(460, 500, 50, 50)
        self.jugador_1.setGeometry(370, 590, 130, 20)
        self.label_numero_turno.setGeometry(600, 25, 175, 40)
        self.jugador_2_dado_1.setGeometry(550, 250, 40, 40)
        self.jugador_2_dado_2.setGeometry(550, 300, 40, 40)
        self.jugador_2_icon.setGeometry(600, 300, 70, 70)
        self.jugador_2_vida.setGeometry(680, 300, 50, 50)
        self.jugador_2.setGeometry(600, 390, 130, 20)
        self.boton_anunciar_valor.setGeometry(550, 500, 100, 50)
        self.boton_pasar_turno.setGeometry(550, 570, 100, 50)
        self.boton_usar_poder.setGeometry(550, 640, 100, 50)
        self.text_anunciar_valor.setGeometry(670, 500, 100, 50)
        self.boton_cambiar_dados.setGeometry(670, 570, 100, 50)
        self.boton_dudar.setGeometry(670, 640, 100, 50)
        self.setWindowTitle("Ventana de Juego")
        self.show()
