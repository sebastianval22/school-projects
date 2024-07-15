import socket
import threading
import pickle
import random
from DCCachos import DCCachos, Bots
import Scripts_Servidor.cripto_servidor as c
import funciones_servidor as f
import sys
import time


class Mensaje:

    def __init__(self, operacion=None, data=None):
        self.operacion = operacion
        self.data = data


class Servidor:

    def __init__(self, port: int, host: str):
        self.chunk_size, self.host, self.port = 2**16, host, port
        self.sockets, self.nombres_utilizados, self.sockets_espera = {}, [], {}
        self.esta_en_juego, self.bots, self.valor_anunciado = False, [], 0
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(8)
        self.data, self.lock = f.cargar_jsno(), threading.Lock()
        self.accept_connections()
        self.nombre_turno_jugador, self.tirar_dado = "", False

    def accept_connections(self) -> None:
        thread = threading.Thread(target=self.iniciar_servicio)
        thread.start()
        f.print_inicial()

    def limite(self, cliente_socket, mensaje):
        nombre_escogido = self.data["nombre_espera"][
                                len(self.sockets_espera)]
        self.sockets_espera[cliente_socket] = nombre_escogido
        mensaje_nombre = Mensaje("set_nombre", nombre_escogido)
        mensaje_limite = Mensaje("limite", mensaje)
        mensaje_jugadores = Mensaje("actualizar_nombres",
                                    self.nombres_utilizados)
        self.enviar_mensaje(mensaje_nombre, cliente_socket, )
        self.enviar_mensaje(mensaje_jugadores, cliente_socket)
        self.enviar_mensaje(mensaje_limite, cliente_socket)
        f.print_logs(self.sockets_espera[cliente_socket],
                     "Conectarse", "-")

    def iniciar_servicio(self):
        while True:
            cliente_socket, cliente_direccion = self.socket_server.accept()
            if self.esta_en_juego is True:
                self.limite(cliente_socket, "empezo_juego")
            else:
                if len(self.sockets) < self.data["NUMERO_JUGADORES"]:
                    self.escoger_nombre(cliente_socket)
                    f.print_logs(self.sockets[cliente_socket], "Conectarse",
                                 "-")
                else:
                    self.limite(cliente_socket, "lleno")
            threading.Thread(target=self.listen_client_thread, args=(
                    cliente_socket,), daemon=True).start()

    def listen_client_thread(self, socket_cliente: socket) -> None:
        while True:
            if len(self.sockets) == 0:
                self.cerrar()
            longitud_bytes = socket_cliente.recv(4)
            largo_mensaje = int.from_bytes(longitud_bytes, 'big')
            bytes_mensaje = socket_cliente.recv(largo_mensaje)
            if largo_mensaje == 0:
                self.descontectarse(socket_cliente)
                break
            try:
                bytes_mensaje = f.decodificar(bytes_mensaje)
                bytes_mensaje = c.desencriptar(bytes_mensaje,
                                               self.data[
                                                   "PONDERADOR_ENCRIPTACION"])
                with self.lock:
                    mensaje = pickle.loads(bytes_mensaje)
                self.manejar_mensaje(mensaje, socket_cliente)
            except (BrokenPipeError, ValueError, ConnectionError) as e:
                e = e
                self.descontectarse(socket_cliente)
                break

    def descontectarse(self, socket_cliente):
        if socket_cliente in self.sockets.keys():
            nombre_desconectado = self.sockets[socket_cliente]
            del self.sockets[socket_cliente]
            f.print_logs(nombre_desconectado, "Desconectarse", "-")
            self.actualizar_nombres(False, nombre_desconectado)
            if self.esta_en_juego is True:
                gano = self.juego.revisar_si_gano()
                if gano is not False:
                    f.print_logs("-", "Termino Partida",
                                 f"{gano} gano la partida DCCachos!!!")
                    self.termino_dccachos(gano)
                self.termino_turno(True)
        elif socket_cliente in self.sockets_espera.keys():
            nombre_desconectado = self.sockets_espera[socket_cliente]
            del self.sockets_espera[socket_cliente]
            f.print_logs(nombre_desconectado, "Desconectarse", "-")

    def manejar_mensaje(self, mensaje: Mensaje, socket_cliente: socket):
        operacion = mensaje.operacion
        nombre = mensaje.data
        if operacion == "empezar_partida":
            if socket_cliente in self.sockets.keys():
                self.esta_en_juego = True
                puestos_faltantes = self.data["NUMERO_JUGADORES"] - len(
                    self.sockets)
                for i in range(0, puestos_faltantes):
                    bot_creado = Bots(i+1)
                    self.bots.append(bot_creado)
                self.lista_jugadores = []
                for nombre in self.sockets.values():
                    self.lista_jugadores.append(nombre)
                for bot in self.bots:
                    self.lista_jugadores.append(bot.nombre)
                indice = random.randint(0, self.data["NUMERO_JUGADORES"]-1)
                self.lista_jugadores[:] = self.lista_jugadores[
                    indice:] + self.lista_jugadores[:indice]
                mensaje = Mensaje("start", self.lista_jugadores)
                f.print_logs("-", "Comenzó la partida",
                             f"Jugadores: {self.lista_jugadores}")
                for sockets in self.sockets.keys():
                    self.enviar_mensaje(mensaje, sockets)
                self.juego = DCCachos(self.lista_jugadores)
                self.actualizar_vidas()
                self.nombre_turno_jugador = self.lista_jugadores[0]
                self.tirar_dados(self.lista_jugadores)
        elif operacion == "dudar":
            if nombre == self.nombre_turno_jugador:
                if self.juego.num_turno != 0:
                    self.mostrar_dados()
                    time.sleep(self.data["TIEMPO_DUDA"])
                    self.verificar_dudar(nombre)
                    self.termino_turno(True)
        elif operacion == "poder":
            if nombre == self.nombre_turno_jugador:
                puede_poder = self.juego.revisar_poder(nombre)
                if puede_poder is False:
                    mensaje = Mensaje("usar_poder", (False, "-"))
                    self.enviar_mensaje(mensaje, socket_cliente)
                else:
                    mensaje_d = Mensaje("tirar_dados",
                                        [nombre, self.juego.jugadores_dados[
                                            nombre]])
                    mensaje_a = Mensaje("avisar_poder", (
                        nombre, puede_poder[1]))
                    for sockets in self.sockets.keys():
                        self.enviar_mensaje(mensaje_d, sockets)
                        self.enviar_mensaje(mensaje_a, sockets)
                    mensaje = Mensaje("usar_poder", puede_poder)
                    self.enviar_mensaje(mensaje, socket_cliente)
        elif operacion == "poder_afectado":
            if nombre[0] == self.nombre_turno_jugador:
                if nombre[1][1] == "Ataque":
                    f.print_logs(f"{nombre[0]}", "Poder",
                                 f"{nombre[0]} ha atacado a {nombre[1][0]}")
                    self.perder_vida(nombre[1][0])
                    self.termino_turno(True)
                else:
                    nueva_vida = self.juego.terremoto(nombre[1][0])
                    f.print_logs(f"{nombre[0]}", "Poder",
                                 f.log_vidas(True, nombre[1][0], nueva_vida))
                    self.actualizar_vidas()
                    self.termino_turno(True)
        elif operacion == "cambiar_dados":
            if nombre == self.nombre_turno_jugador:
                if self.tirar_dado is False:
                    f.print_logs(nombre, "Tirar dados",
                                 f"{nombre} decidió tirar dados de nuevo.")
                    if nombre == self.nombre_turno_jugador:
                        info_dados = self.juego.tirar_dados(nombre)
                        mensaje = Mensaje("tirar_dados", info_dados)
                        self.enviar_mensaje(mensaje, socket_cliente)
                    self.tirar_dado = True
        elif operacion == "pasar_turno":
            if nombre == self.nombre_turno_jugador:
                self.juego.pasar(nombre)
                f.print_logs(nombre, "Pasar", f"{nombre} decidió pasar.")
                self.tirar_dado = False
                self.termino_turno(False)
        elif operacion == "anunciar_valor":
            if nombre[0] == self.nombre_turno_jugador:
                revisar_valor = self.juego.revisar_anunciar(nombre[1])
                if revisar_valor is not True:
                    mensaje = Mensaje("error_valor_anunciado", revisar_valor)
                    self.enviar_mensaje(mensaje, socket_cliente)
                else:
                    self.juego.anunciar_valor((nombre[0], (int(nombre[1]))))
                    f.print_logs(nombre[0], "Anunciar",
                                 f"{nombre[0]} anunció valor {nombre[1]}.")
                    mensaje = Mensaje("valor_anunciado", int(nombre[1]))
                    for sockets in self.sockets.keys():
                        self.enviar_mensaje(mensaje, sockets)
                    mensaje = Mensaje("error_valor_anunciado",
                                      "Ingrese el valor...")
                    self.enviar_mensaje(mensaje, socket_cliente)
                    self.tirar_dado = False
                    self.juego.paso_anterior = False
                    self.termino_turno(False)

    def turno_bot(self, nombre):
        f.print_logs(nombre, "Empezó turno", "-")
        accion = self.juego.turno_bot(nombre)
        if accion == "DUDAR":
            self.mostrar_dados()
            time.sleep(self.data["TIEMPO_DUDA"])
            self.verificar_dudar(nombre)  # DCCachos, actualiza el turno
            self.termino_turno(True)
        elif accion == "ANUNCIAR":
            f.print_logs(nombre, "Tirar dados",
                         f"{nombre} decidió tirar dados de nuevo.")
            valor_anunciado = self.juego.num_mayor_enunciado
            f.print_logs(nombre, "Anunciar",
                         f"{nombre} anuncia el valor {valor_anunciado}")
            time.sleep(self.data["TIEMPO_BOT"])
            mensaje = Mensaje("valor_anunciado", valor_anunciado)
            for sockets in self.sockets.keys():
                self.enviar_mensaje(mensaje, sockets)
            self.termino_turno(False)
        elif accion == "PASAR":
            f.print_logs(nombre, "Tirar dados",
                         f"{nombre} decidió tirar dados de nuevo.")
            time.sleep(self.data["TIEMPO_BOT"])
            f.print_logs(nombre, "Pasar", f"{nombre} decidió pasar.")
            self.termino_turno(False)

    def mostrar_dados(self):
        for sockets in self.sockets.keys():
            for jugador, dados in self.juego.jugadores_dados.items():
                valor_dados = [jugador, dados]
                mensaje = Mensaje("tirar_dados", valor_dados)
                self.enviar_mensaje(mensaje, sockets)

    def verificar_dudar(self, nombre):
        if self.juego.turno_anterior in self.lista_jugadores:
            revisar = [[self.juego.turno_anterior, self.juego.jugadores_dados[
                self.juego.turno_anterior]], self.juego.valor_anterior,
                self.juego.paso_anterior]
            name_mintio = self.juego.revisar_duda(revisar)
            f.print_logs(nombre, "Dudar", f"{nombre} duda a {name_mintio[1]}")
            if name_mintio[0] is True:
                self.perder_vida(name_mintio[1])
            else:
                self.perder_vida(nombre)

    def perder_vida(self, nombre):
        vida_actual_jugador = self.juego.perder_vida(nombre)
        f.print_logs(nombre, "Pierde Vida",
                     f.log_vidas(False, nombre, vida_actual_jugador[1]))
        self.nombre_turno_jugador = nombre
        self.juego.turno_anterior = ""
        self.actualizar_vidas()
        salio = self.juego.revisar_vidas()
        if salio is not False:
            f.print_logs(salio, "Perdio", f"{salio} perdió todas sus vidas.")
            self.nombre_turno_jugador = self.juego.nombre_actual_turno
            self.actualizar_nombres(False, salio)
            mensaje = Mensaje("avisar_perdio", salio)
            for sockets, nombres in self.sockets.items():
                if nombres == salio:
                    self.enviar_mensaje(mensaje, sockets)
                    del self.sockets[sockets]
                    break
            gano = self.juego.revisar_si_gano()
            if gano is not False:
                f.print_logs("-", "Termino Partida",
                             f"{gano} gano la partida DCCachos!!!")
                self.termino_dccachos(gano)

    def termino_dccachos(self, ganador):
        mensaje_final = Mensaje("termino_dccachos", ganador)
        for sockets, nombres in self.sockets.items():
            if nombres == ganador:
                self.enviar_mensaje(mensaje_final, sockets)
                del self.sockets[sockets]
                break
        time.sleep(self.data["TIEMPO_FINAL"])
        self.cerrar()

    def cerrar(self):
        sys.exit()

    def termino_turno(self, dudo_):
        if dudo_ is False:
            self.juego.num_turno += 1
            self.tirar_dado = False
            self.nombre_turno_jugador = self.juego.nombre_actual_turno
            mensaje = Mensaje("turno_actual_anterior", (
                self.nombre_turno_jugador, self.juego.turno_anterior))
            mensaje_2 = Mensaje("reset_turnos", self.juego.num_turno)
            for socket_1 in self.sockets.keys():
                self.enviar_mensaje(mensaje, socket_1)
                self.enviar_mensaje(mensaje_2, socket_1)
            if self.nombre_turno_jugador not in self.sockets.values():
                self.turno_bot(self.nombre_turno_jugador)
        else:
            f.print_logs("-", "Nuevo Turno",
                         f"{self.nombre_turno_jugador} empieza")
            self.juego.paso_anterior = False
            self.tirar_dado = False
            self.tirar_dados(self.lista_jugadores)

    def actualizar_vidas(self):
        dic_jugadores_vidas = self.juego.mostrar_vidas()
        mensaje = Mensaje("actualizar_vidas", dic_jugadores_vidas)
        for sockets in self.sockets.keys():
            self.enviar_mensaje(mensaje, sockets)

    def tirar_dados(self, lista_jugadores):
        self.juego.num_turno = 0
        self.juego.num_mayor_enunciado = 0
        for jugador in lista_jugadores:
            valor_dados = self.juego.tirar_dados(jugador)
            for sockets in self.sockets.keys():
                nombre_jugador = self.sockets[sockets]
                if jugador == nombre_jugador:
                    mensaje = Mensaje("tirar_dados", valor_dados)
                    self.enviar_mensaje(mensaje, sockets)
                    mensaje = Mensaje("reset_turnos", self.juego.num_turno)
                    self.enviar_mensaje(mensaje, sockets)
                    mensaje_1 = Mensaje("turno_actual_anterior", (
                                        self.nombre_turno_jugador, "-"))
                    self.enviar_mensaje(mensaje_1, sockets)
                    mensaje = Mensaje("valor_anunciado",
                                      self.juego.num_mayor_enunciado)
                    self.enviar_mensaje(mensaje, sockets)
                    mensaje_cubrir = Mensaje("cubrir_dados", (
                        nombre_jugador, self.lista_jugadores))
                    self.enviar_mensaje(mensaje_cubrir, sockets)
        if self.nombre_turno_jugador not in self.sockets.values():
            self.turno_bot(self.nombre_turno_jugador)

    def escoger_nombre(self, cliente_socket):
        nombres = self.data["nombres"]
        nombre_escogido = random.choice(nombres)
        while nombre_escogido in self.nombres_utilizados:
            nombre_escogido = random.choice(nombres)
        mensaje = Mensaje("set_nombre", nombre_escogido)
        self.sockets[cliente_socket] = nombre_escogido
        self.enviar_mensaje(mensaje, cliente_socket)
        self.actualizar_nombres(True, nombre_escogido)

    def actualizar_nombres(self, agregar, nombre):
        if agregar is True:
            self.nombres_utilizados.append(nombre)
            mensaje_F = Mensaje("actualizar_nombres",
                                self.nombres_utilizados)
        else:
            if nombre in self.nombres_utilizados:
                self.nombres_utilizados.remove(nombre)
            if self.esta_en_juego is False:
                if len(self.sockets_espera) > 0:
                    first_element = next(iter(self.sockets_espera.items()))
                    socket_agregar = first_element[0]
                    nombre_anterior = first_element[1]
                    self.escoger_nombre(socket_agregar)
                    nombre_agregado = self.sockets[socket_agregar]
                    del self.sockets_espera[socket_agregar]
                    string = ((nombre_anterior) +
                              " entro a la sala de espera con el nombre " + (
                        nombre_agregado))
                    f.print_logs(nombre_agregado, "Entrar", string)
                    mensaje = Mensaje("entro", nombre_agregado)
                    self.enviar_mensaje(mensaje, socket_agregar)
                mensaje_F = Mensaje("actualizar_nombres",
                                    self.nombres_utilizados)
            else:
                self.juego.salio(nombre)
                if nombre in self.lista_jugadores:
                    self.lista_jugadores.remove(nombre)
                mensaje_F = Mensaje("actualizar_nombres", self.lista_jugadores)
                self.nombre_turno_jugador = self.juego.nombre_actual_turno
        for sockets in self.sockets.keys():
            self.enviar_mensaje(mensaje_F, sockets)

    def enviar_mensaje(self, mensaje: Mensaje, socket_cliente: socket) -> None:
        with self.lock:
            bytes_mensaje = pickle.dumps(mensaje)
        bytearray_mensaje = bytearray(bytes_mensaje)
        bytearray_mensaje_encriptado = c.encriptar(
            bytearray_mensaje, self.data["PONDERADOR_ENCRIPTACION"])
        bytearray_mensaje_final = f.codificar(bytearray_mensaje_encriptado)
        socket_cliente.sendall(len(bytearray_mensaje_final).to_bytes(4, 'big'))
        socket_cliente.sendall(bytearray_mensaje_final)


if __name__ == '__main__':
    data = f.cargar_jsno()
    PORT = data["port"] if len(sys.argv) < 2 else int(sys.argv[1])
    HOST = data["host"] if len(sys.argv) < 3 else int(sys.argv[2])
    server = Servidor(PORT, HOST)
