import socket
import sys
import pickle
import threading
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSignal
from frontend.ventana_inicio import Ventana_Inicio
from frontend.ventana_juego import Ventana_Juego
from backend.backend import Cliente_Ventana
import json
import Scripts.cripto as c
import funciones as f
import time


class ShootApplication():
    def __init__(self, cliente) -> None:
        self.frontend_inicio = Ventana_Inicio()
        self.backend_cliente = Cliente_Ventana()
        self.cliente = cliente
        self.frontend_juego = Ventana_Juego()

    def conectar(self) -> None:
        self.cliente.senal_nombre.connect(self.backend_cliente.set_nombre)
        self.backend_cliente.senal_set_nombre.connect(
            self.frontend_inicio.set_nombre_i)
        self.cliente.senal_actualizar_jugadores.connect(
            self.backend_cliente.actualizar_nombres)
        self.backend_cliente.senal_set_jugadores.connect(
            self.frontend_inicio.actualizar_jugadores)
        self.cliente.senal_limite.connect(self.backend_cliente.avisar_limite)
        self.backend_cliente.senal_limite.connect(
            self.frontend_inicio.avisar_limite)
        self.frontend_inicio.senal_presiono_comenzar.connect(
            self.backend_cliente.empezar_partida)
        self.backend_cliente.senal_empezar_partida.connect(
            self.cliente.empezar_partida)
        self.cliente.senal_start.connect(self.backend_cliente.start)
        self.backend_cliente.senal_start.connect(self.frontend_juego.mostrar)
        self.backend_cliente.senal_esconder_ventana.connect(
            self.frontend_inicio.esconder)
        self.cliente.senal_actualizar_jugadores_juego.connect(
            self.backend_cliente.actualizar_nombres_juego)
        self.backend_cliente.senal_actualizar_jugadores.connect(
            self.frontend_juego.actualizar_jugadores)
        self.cliente.senal_espera_entro.connect(
            self.backend_cliente.notificar_entro)
        self.backend_cliente.senal_notificar_entro.connect(
            self.frontend_inicio.avisar_entro)
        self.cliente.senal_actualizar_vidas.connect(
            self.backend_cliente.actualizar_vidas)
        self.backend_cliente.senal_actualizar_vidas.connect(
            self.frontend_juego.actualizar_vidas)
        self.cliente.senal_tirar_dados.connect(
            self.backend_cliente.lanzar_dados)
        self.backend_cliente.senal_establecer_dados.connect(
            self.frontend_juego.establecer_dados)
        self.cliente.senal_cambiar_valor_anunciado.connect(
            self.backend_cliente.cambiar_valor_anunciado)
        self.backend_cliente.senal_actualizar_valor_anunciado.connect(
            self.frontend_juego.actualizar_num_mayor_anunciado)
        self.cliente.senal_avisar_perdio.connect(
            self.backend_cliente.avisar_que_perdio)
        self.backend_cliente.senal_avisar_que_perdio.connect(
            self.frontend_juego.avisar_que_perdio)
        self.cliente.senal_actualizar_turnos.connect(
            self.backend_cliente.actualizar_turnos)
        self.backend_cliente.senal_actualizar_turnos.connect(
            self.frontend_juego.actualizar_turnos)
        self.frontend_juego.senal_dudar.connect(
            self.backend_cliente.presiono_boton_dudar)
        self.backend_cliente.senal_presiono_boton_dudar.connect(
            self.cliente.presiono_boton_dudar)
        self.frontend_juego.senal_poder.connect(
            self.backend_cliente.presiono_boton_poder)
        self.backend_cliente.senal_presiono_boton_poder.connect(
            self.cliente.presiono_boton_poder)
        self.frontend_juego.senal_cambiar_dados.connect(
            self.backend_cliente.presiono_boton_cambiar_dados)
        self.backend_cliente.senal_presiono_boton_cambiar_dados.connect(
            self.cliente.presiono_boton_cambiar_dados)
        self.frontend_juego.senal_pasar_turno.connect(
            self.backend_cliente.presiono_boton_pasar_turno)
        self.backend_cliente.senal_presiono_boton_pasar_turno.connect(
            self.cliente.presiono_boton_pasar_turno)
        self.frontend_juego.senal_anunciar_valor.connect(
            self.backend_cliente.boton_anunciar_valor)
        self.backend_cliente.senal_boton_anunciar_valor.connect(
            self.cliente.presiono_boton_anunciar_valor)
        self.cliente.senal_usar_poder.connect(
            self.backend_cliente.usar_poder)
        self.backend_cliente.senal_avisar_uso_poder.connect(
            self.frontend_juego.usa_poder)
        self.cliente.senal_avisar_poder.connect(
            self.backend_cliente.avisar_todos_poder)
        self.backend_cliente.senal_avisar_juego_poder.connect(
            self.frontend_juego.avisar_juego_poder)
        self.cliente.senal_reset_num_turnos.connect(
            self.backend_cliente.reset_num_turnos)
        self.backend_cliente.senal_reset_num_turnos.connect(
            self.frontend_juego.reset_num_turnos)
        self.cliente.senal_termino_partida.connect(
            self.backend_cliente.termino_partida)
        self.backend_cliente.senal_termino_partida.connect(
            self.frontend_juego.termino_partida)
        self.frontend_juego.senal_escogio_afectado_poder.connect(
            self.backend_cliente.escogio_afectado_poder)
        self.backend_cliente.senal_afectado_poder.connect(
            self.cliente.afectado_poder)
        self.cliente.senal_cubrir_dados.connect(
            self.backend_cliente.cubrir_dados)
        self.backend_cliente.senal_cubrir_dados.connect(
            self.frontend_juego.cubrir_dados)
        self.frontend_juego.senal_mostrar_dados_see.connect(
            self.backend_cliente.see)
        self.backend_cliente.senal_see.connect(
            self.cliente.enviar_see)
        self.cliente.senal_cayo_servidor.connect(
            self.backend_cliente.cayo_servidor)
        self.backend_cliente.senal_cayo_servidor.connect(
            self.frontend_juego.desconexion)
        self.cliente.senal_error_anunciado.connect(
            self.backend_cliente.error_anunciado)
        self.backend_cliente.senal_error_anunciado.connect(
            self.frontend_juego.cambiar_qlinedit_anunciado)

    def iniciar(self):
        # Comenzar el juego
        self.conectar()
        self.cliente.init_2()
        self.frontend_inicio.show()


class Mensaje:

    def __init__(self, operacion=None, data=None):
        # Guarda el tipo de operación: listar o descargar
        self.operacion = operacion
        # Guarda la información necesaria según la consulta
        self.data = data


class Cliente(QObject):
    senal_nombre = pyqtSignal(str)
    senal_actualizar_jugadores = pyqtSignal(list)
    senal_limite = pyqtSignal(str)
    senal_start = pyqtSignal(list)
    senal_espera_entro = pyqtSignal(str)
    senal_actualizar_jugadores_juego = pyqtSignal(list)
    senal_actualizar_vidas = pyqtSignal(dict)
    senal_tirar_dados = pyqtSignal(list)
    senal_cambiar_valor_anunciado = pyqtSignal(int)
    senal_avisar_perdio = pyqtSignal(str)
    senal_actualizar_turnos = pyqtSignal(tuple)
    senal_anunciar_valor = pyqtSignal(int)
    senal_usar_poder = pyqtSignal(tuple)
    senal_avisar_poder = pyqtSignal(tuple)
    senal_reset_num_turnos = pyqtSignal(int)
    senal_termino_partida = pyqtSignal(str)
    senal_cubrir_dados = pyqtSignal(tuple)
    senal_cayo_servidor = pyqtSignal()
    senal_error_anunciado = pyqtSignal(str)

    def __init__(self, port: int, host: str):
        super().__init__()
        self.conectado = False
        self.port = port
        self.chunk_size = 2**7
        self.host = host
        self.ya_en_juego = False
        with open("cliente/parametros.json", encoding="utf-8") as jsno_file:
            data = json.load(jsno_file)
        self.data = data
        self.pond_enc = self.data["PONDERADOR_ENCRIPTACION"]
        self.lock = threading.Lock()

    def init_2(self):
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.connect_to_server()
            self.conectado = True
            self.iniciar_servicio()
        except ConnectionError:
            self.socket_cliente.close()
            self.conectado = False
            sys.exit()

    def connect_to_server(self):
        self.socket_cliente.connect((self.host, self.port))

    def iniciar_servicio(self):
        threading.Thread(target=self.listen_server_thread, args=(
                        self.socket_cliente,), daemon=True).start()

    def listen_server_thread(self, socket_server: socket) -> None:
        while True:
            try:
                mensaje = self.recibir_mensaje()
                if mensaje is None:
                    self.senal_cayo_servidor.emit()
                    time.sleep(self.data["TIEMPO_ESPERA"])
                    sys.exit()
                else:
                    self.manejar_mensaje(mensaje)
            except (BrokenPipeError, ConnectionError,
                    ValueError, socket.error) as e:
                e = e
                self.senal_cayo_servidor.emit()
                time.sleep(self.data["TIEMPO_ESPERA"])
                sys.exit()

    def manejar_mensaje(self, mensaje: Mensaje):
        if mensaje.operacion == "set_nombre":
            self.nombre = mensaje.data
            self.senal_nombre.emit(self.nombre)
        elif mensaje.operacion == "actualizar_nombres":
            if self.ya_en_juego is True:
                self.senal_actualizar_jugadores_juego.emit(mensaje.data)
            else:
                self.senal_actualizar_jugadores.emit(mensaje.data)
        elif mensaje.operacion == "limite":
            self.senal_limite.emit(mensaje.data)
        elif mensaje.operacion == "start":
            self.ya_en_juego = True
            self.senal_start.emit(mensaje.data)
        elif mensaje.operacion == "entro":
            self.senal_espera_entro.emit(mensaje.data)
        elif mensaje.operacion == "actualizar_vidas":
            self.senal_actualizar_vidas.emit(mensaje.data)
        elif mensaje.operacion == "tirar_dados":
            self.senal_tirar_dados.emit(mensaje.data)
        elif mensaje.operacion == "valor_anunciado":
            self.senal_cambiar_valor_anunciado.emit(mensaje.data)
        elif mensaje.operacion == "avisar_perdio":
            self.senal_avisar_perdio.emit(mensaje.data)
        elif mensaje.operacion == "turno_actual_anterior":
            self.senal_actualizar_turnos.emit(mensaje.data)
        elif mensaje.operacion == "usar_poder":
            self.senal_usar_poder.emit(mensaje.data)
        elif mensaje.operacion == "avisar_poder":
            self.senal_avisar_poder.emit(mensaje.data)
        elif mensaje.operacion == "reset_turnos":
            self.senal_reset_num_turnos.emit(mensaje.data)
        elif mensaje.operacion == "termino_dccachos":
            self.senal_termino_partida.emit(mensaje.data)
        elif mensaje.operacion == "cubrir_dados":
            self.senal_cubrir_dados.emit(mensaje.data)
        elif mensaje.operacion == "error_valor_anunciado":
            self.senal_error_anunciado.emit(mensaje.data)

    def enviar_mensaje(self, mensaje: Mensaje) -> None:
        with self.lock:
            bytes_mensaje = pickle.dumps(mensaje)
        bytearray_mensaje = bytearray(bytes_mensaje)
        bytearray_mensaje_encriptado = c.encriptar(bytearray_mensaje,
                                                   self.pond_enc)
        bytearray_mensaje_final = f.codificar(bytearray_mensaje_encriptado)
        self.socket_cliente.sendall(len(bytearray_mensaje_final).to_bytes(
            4, 'big'))
        self.socket_cliente.sendall(bytearray_mensaje_final)

    def recibir_mensaje(self) -> Mensaje:
        # TODO: Completar para recibir un Mensaje
        longitud_bytes = self.socket_cliente.recv(4)
        largo = int.from_bytes(longitud_bytes, 'big')
        if largo == 0:
            return None
        with self.lock:
            mensahe = pickle.loads(self.recibir_bytes(largo))
        return mensahe

    def recibir_bytes(self, cantidad: int) -> bytearray:
        # TODO: Completar para recibir un bytearray de largo "cantidad"
        bytes_leidos = bytearray()
        while len(bytes_leidos) < cantidad:
            cantidad_restante = cantidad - len(bytes_leidos)
            bytes_leer = min(self.chunk_size, cantidad_restante)
            respuesta = self.socket_cliente.recv(bytes_leer)
            bytes_leidos += respuesta
        bytes_leidos = f.decodificar(bytes_leidos)
        bytes_leidos = c.desencriptar(bytes_leidos, self.pond_enc)
        bytes_leidos = bytes(bytes_leidos)
        return bytes_leidos

    def cerrar_conexion(self):
        self.socket_cliente.close()

    def empezar_partida(self):
        mensaje = Mensaje("empezar_partida", self.nombre)
        self.enviar_mensaje(mensaje)

    def presiono_boton_dudar(self):
        mensaje = Mensaje("dudar", self.nombre)
        self.enviar_mensaje(mensaje)

    def presiono_boton_poder(self):
        mensaje = Mensaje("poder", self.nombre)
        self.enviar_mensaje(mensaje)

    def presiono_boton_cambiar_dados(self):
        mensaje = Mensaje("cambiar_dados", self.nombre)
        self.enviar_mensaje(mensaje)

    def presiono_boton_pasar_turno(self):
        mensaje = Mensaje("pasar_turno", self.nombre)
        self.enviar_mensaje(mensaje)

    def presiono_boton_anunciar_valor(self, valor):
        mensaje = Mensaje("anunciar_valor", (self.nombre, valor))
        self.enviar_mensaje(mensaje)

    def afectado_poder(self, afectado_poder):
        mensaje = Mensaje("poder_afectado", (self.nombre, afectado_poder))
        self.enviar_mensaje(mensaje)

    def enviar_see(self):
        mensaje = Mensaje("see", self.nombre)
        self.enviar_mensaje(mensaje)


if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)
    with open("cliente/parametros.json", encoding="utf-8") as jsno_file:
        data = json.load(jsno_file)
    PORT = data["port"] if len(sys.argv) < 2 else int(sys.argv[1])
    HOST = data["host"] if len(sys.argv) < 3 else int(sys.argv[2])
    client = Cliente(PORT, HOST)
    sys.__excepthook__ = hook

    app = QApplication([])
    game = ShootApplication(client)
    game.iniciar()

    sys.exit(app.exec())

    # TODO: Completar con el uso de sys.argv para dar parámetros por consola
    # Por ejemplo: python3 cliente.py 4444 localhost
