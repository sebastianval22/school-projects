from PyQt5.QtCore import QObject, pyqtSignal


class Cliente_Ventana(QObject):

    senal_set_nombre = pyqtSignal(str)
    senal_set_jugadores = pyqtSignal(list)
    senal_limite = pyqtSignal(str)
    senal_empezar_partida = pyqtSignal()
    senal_start = pyqtSignal(list)
    senal_esconder_ventana = pyqtSignal()
    senal_actualizar_jugadores = pyqtSignal(list)
    senal_notificar_entro = pyqtSignal(str)
    senal_actualizar_vidas = pyqtSignal(dict)
    senal_establecer_dados = pyqtSignal(list)
    senal_actualizar_valor_anunciado = pyqtSignal(int)
    senal_avisar_que_perdio = pyqtSignal(str)
    senal_actualizar_turnos = pyqtSignal(tuple)
    senal_presiono_boton_dudar = pyqtSignal()
    senal_presiono_boton_poder = pyqtSignal()
    senal_presiono_boton_cambiar_dados = pyqtSignal()
    senal_presiono_boton_pasar_turno = pyqtSignal()
    senal_boton_anunciar_valor = pyqtSignal(str)
    senal_avisar_uso_poder = pyqtSignal(tuple)
    senal_avisar_juego_poder = pyqtSignal(tuple)
    senal_reset_num_turnos = pyqtSignal(int)
    senal_termino_partida = pyqtSignal(str)
    senal_afectado_poder = pyqtSignal(tuple)
    senal_cubrir_dados = pyqtSignal(tuple)
    senal_see = pyqtSignal()
    senal_cayo_servidor = pyqtSignal()
    senal_error_anunciado = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_nombre(self, nombre):
        self.nombre = nombre
        self.senal_set_nombre.emit(nombre)

    def actualizar_nombres(self, lista_nombres):
        self.jugadores = lista_nombres
        self.senal_set_jugadores.emit(lista_nombres)

    def avisar_limite(self, razon):
        self.senal_limite.emit(razon)

    def empezar_partida(self):
        self.senal_empezar_partida.emit()

    def start(self, lista_jugadores: list):
        self.senal_start.emit(lista_jugadores)
        self.senal_esconder_ventana.emit()

    def actualizar_nombres_juego(self, lista_nombres):
        self.senal_actualizar_jugadores.emit(lista_nombres)

    def notificar_entro(self, nombre):
        self.senal_notificar_entro.emit(nombre)

    def actualizar_vidas(self, dic_jugador_vida):
        self.senal_actualizar_vidas.emit(dic_jugador_vida)

    def lanzar_dados(self, valor_dados):
        self.senal_establecer_dados.emit(valor_dados)

    def cambiar_valor_anunciado(self, valor):
        self.senal_actualizar_valor_anunciado.emit(valor)

    def avisar_que_perdio(self, nombre):
        self.senal_avisar_que_perdio.emit(nombre)

    def actualizar_turnos(self, turno_actual_anterior):
        self.senal_actualizar_turnos.emit(turno_actual_anterior)

    def presiono_boton_dudar(self):
        self.senal_presiono_boton_dudar.emit()

    def presiono_boton_poder(self):
        self.senal_presiono_boton_poder.emit()

    def presiono_boton_cambiar_dados(self):
        self.senal_presiono_boton_cambiar_dados.emit()

    def presiono_boton_pasar_turno(self):
        self.senal_presiono_boton_pasar_turno.emit()

    def boton_anunciar_valor(self, valor):
        self.senal_boton_anunciar_valor.emit(valor)

    def usar_poder(self, bool_poder):
        self.senal_avisar_uso_poder.emit(bool_poder)

    def avisar_todos_poder(self, nombre_poder):
        self.senal_avisar_juego_poder.emit(nombre_poder)

    def reset_num_turnos(self, int):
        self.senal_reset_num_turnos.emit(int)

    def termino_partida(self, ganador):
        self.senal_termino_partida.emit(ganador)

    def escogio_afectado_poder(self, afectado_poder):
        self.senal_afectado_poder.emit(afectado_poder)

    def cubrir_dados(self, nombre):
        self.senal_cubrir_dados.emit(nombre)

    def see(self):
        self.senal_see.emit()

    def cayo_servidor(self):
        self.senal_cayo_servidor.emit()

    def error_anunciado(self, mensaje):
        self.senal_error_anunciado.emit(mensaje)
