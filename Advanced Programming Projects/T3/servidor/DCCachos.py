import random
import json


class DCCachos:

    def __init__(self, jugadores) -> None:
        with open("servidor/parametros_servidor.json") as jsno_file:
            data = json.load(jsno_file)
        self.data = data
        vidas_iniciales = self.data["NUMERO_VIDAS"]
        self.jugadores_vidas = {}
        self.jugadores_dados = {}
        for jugador in jugadores:
            self.jugadores_vidas[jugador] = vidas_iniciales
            self.jugadores_dados[jugador] = (0, 0)
        self.num_turno = 0
        self.num_mayor_enunciado = 0
        self.valor_anterior = 0
        self.turno_anterior = ""
        self.paso_anterior = False
        self.nombre_actual_turno = jugadores[0]
        self.turno_num_recursivo = 0
        self.lista_jugadores_actuales = jugadores
        self.info_dudar = []

    def tirar_dados(self, nombre):
        valor_dado_1 = random.randint(1, 6)
        valor_dado_2 = random.randint(1, 6)
        self.jugadores_dados[nombre] = (valor_dado_1, valor_dado_2)
        return [nombre, (valor_dado_1, valor_dado_2)]

    def mostrar_vidas(self):
        return self.jugadores_vidas

    def turno_bot(self, nombre):
        # Bot AI turn decision: advances the turn pointer, then (weighted by
        # PROB_DUDAR/PROB_ANUNCIAR from config) decides to doubt, announce a
        # higher value, or pass, rolling dice and updating turn-state fields
        # as needed. Returns one of "DUDAR"/"ANUNCIAR"/"PASAR".
        pass

    def pasar(self, nombre):
        self.turno_num_recursivo = (self.lista_jugadores_actuales.index(
            nombre)) + 1
        if self.turno_num_recursivo >= len(self.lista_jugadores_actuales):
            self.turno_num_recursivo = 0
            self.nombre_actual_turno = self.lista_jugadores_actuales[
                self.turno_num_recursivo]
        else:
            self.nombre_actual_turno = self.lista_jugadores_actuales[
                self.turno_num_recursivo]
        self.turno_anterior = nombre
        self.valor_anterior = self.data["VALOR_PASO"]
        self.paso_anterior = True

    def revisar_duda(self, lista):
        # Resolves a "doubt" challenge against the previous player's
        # announced value and actual dice roll, per the doubt/pass rules.
        # Returns (was_the_doubted_player_wrong, name_of_doubted_player).
        pass

    def perder_vida(self, nombre):
        vida_anterior = self.jugadores_vidas[nombre]
        vida_ahora = vida_anterior - 1
        self.jugadores_vidas[nombre] = vida_ahora
        return (nombre, vida_ahora)

    def revisar_vidas(self):
        for jugador, vida in self.jugadores_vidas.items():
            if vida <= 0:
                return (jugador)
        return False

    def salio(self, nombre):
        if nombre == self.nombre_actual_turno:
            self.turno_num_recursivo = (self.lista_jugadores_actuales.index(
                nombre)) + 1
            if self.turno_num_recursivo >= len(self.lista_jugadores_actuales):
                self.turno_num_recursivo = 0
                self.nombre_actual_turno = self.lista_jugadores_actuales[
                        self.turno_num_recursivo]
            else:
                self.nombre_actual_turno = self.lista_jugadores_actuales[
                                            self.turno_num_recursivo]
        self.lista_jugadores_actuales.remove(nombre)
        del self.jugadores_dados[nombre]
        del self.jugadores_vidas[nombre]

    def revisar_si_gano(self):
        if len(self.lista_jugadores_actuales) <= 1:
            ganador = self.lista_jugadores_actuales[0]
            return ganador
        else:
            return False

    def anunciar_valor(self, nombre_valor):
        self.turno_num_recursivo = (self.lista_jugadores_actuales.index(
            nombre_valor[0])) + 1
        if self.turno_num_recursivo >= len(self.lista_jugadores_actuales):
            self.turno_num_recursivo = 0
            self.nombre_actual_turno = self.lista_jugadores_actuales[
                self.turno_num_recursivo]
        else:
            self.nombre_actual_turno = self.lista_jugadores_actuales[
                self.turno_num_recursivo]
        self.num_mayor_enunciado = nombre_valor[1]
        self.valor_anterior = nombre_valor[1]
        self.turno_anterior = nombre_valor[0]
        self.paso_anterior = False

    def revisar_poder(self, nombre):
        # Checks the player's current dice roll against the fixed
        # combinations that unlock a power ("Ataque" / "Terremoto").
        pass

    def terremoto(self, afectado):
        # "Earthquake" power effect: resets the affected player's lives to
        # a random value within the configured range.
        pass

    def revisar_anunciar(self, valor):
        # Validates a player's announced value against the numeric range
        # and the "must exceed the current highest announcement" rule.
        pass


class Bots:

    def __init__(self, id) -> None:
        self.id = id
        self.nombre = "BOT" + str(self.id)
