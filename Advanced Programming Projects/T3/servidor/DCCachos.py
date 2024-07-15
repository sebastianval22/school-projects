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
        self.turno_num_recursivo = (self.lista_jugadores_actuales.index(
            nombre)) + 1
        if self.turno_num_recursivo >= len(self.lista_jugadores_actuales):
            self.turno_num_recursivo = 0
            self.nombre_actual_turno = self.lista_jugadores_actuales[
                self.turno_num_recursivo]
        else:
            self.nombre_actual_turno = self.lista_jugadores_actuales[
                self.turno_num_recursivo]
        if self.num_turno == 0:  # ACA NO PUEDO DUDAR
            e = self.tirar_dados(nombre)
            prob_anunciar = random.choices(["ANUNCIAR", "NO_ANUNCIAR"],
                                           weights=[self.data[
                                                   "PROB_ANUNCIAR"],
                                                 1-self.data["PROB_ANUNCIAR"]],
                                           k=1)[0]
            if prob_anunciar == "ANUNCIAR":
                if self.num_mayor_enunciado < 12:
                    numero_anunciado = random.randint(
                        self.num_mayor_enunciado + 1, 12)
                else:
                    numero_anunciado = 0
                if numero_anunciado > self.num_mayor_enunciado:
                    if numero_anunciado == 12:
                        self.valor_anterior = numero_anunciado
                        self.turno_anterior = nombre
                        self.valor_anterior = self.data["VALOR_PASO"]
                        self.paso_anterior = True
                        return "PASAR"
                    else:
                        self.num_mayor_enunciado = numero_anunciado
                        self.valor_anterior = numero_anunciado
                        self.turno_anterior = nombre
                        self.paso_anterior = False
                        return "ANUNCIAR"
                else:
                    self.turno_anterior = nombre
                    self.valor_anterior = self.data["VALOR_PASO"]
                    self.paso_anterior = True
                    return "PASAR"
            else:
                self.turno_anterior = nombre
                self.valor_anterior = self.data["VALOR_PASO"]
                self.paso_anterior = True
                return "PASAR"
        else:
            prob_dudar = random.choices(["DUDAR", "NO_DUDAR"],
                                        weights=[self.data["PROB_DUDAR"],
                                                 1-self.data["PROB_DUDAR"]],
                                        k=1)[0]
            if prob_dudar == "DUDAR":
                self.nombre_actual_turno = nombre
                return "DUDAR"

            else:
                e = self.tirar_dados(nombre)
                e
                prob_anunciar = random.choices(["ANUNCIAR", "NO_ANUNCIAR"],
                                               weights=[self.data[
                                                   "PROB_ANUNCIAR"],
                                                 1-self.data["PROB_ANUNCIAR"]],
                                               k=1)[0]
                if prob_anunciar == "ANUNCIAR":
                    numero_anunciado = random.randint(
                        self.valor_anterior + 1, 12)
                    if self.num_mayor_enunciado < 12:
                        numero_anunciado = random.randint(
                            self.num_mayor_enunciado + 1, 12)
                    else:
                        numero_anunciado = 0
                    if numero_anunciado > self.num_mayor_enunciado:
                        if numero_anunciado == 12:
                            self.valor_anterior = numero_anunciado
                            self.turno_anterior = nombre
                            self.valor_anterior = self.data["VALOR_PASO"]
                            self.paso_anterior = True
                            return "PASAR"
                        else:
                            self.num_mayor_enunciado = numero_anunciado
                            self.valor_anterior = numero_anunciado
                            self.turno_anterior = nombre
                            self.paso_anterior = False
                            return "ANUNCIAR"
                    else:
                        self.turno_anterior = nombre
                        self.valor_anterior = self.data["VALOR_PASO"]
                        self.paso_anterior = True
                        return "PASAR"
                else:
                    self.turno_anterior = nombre
                    self.valor_anterior = self.data["VALOR_PASO"]
                    self.paso_anterior = True
                    return "PASAR"

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
        paso = lista[2]
        valor_a_comparar = lista[1]
        nombre_a_dudar = lista[0][0]
        valor_dados = lista[0][1]
        suma_dados = valor_dados[0] + valor_dados[1]
        if paso is True:
            if valor_a_comparar != suma_dados:
                return (True, nombre_a_dudar)
            else:
                return (False, nombre_a_dudar)
        else:
            if valor_a_comparar > suma_dados:
                return (True, nombre_a_dudar)
            else:
                return (False, nombre_a_dudar)

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
        valor_dados = self.jugadores_dados[nombre]
        if (valor_dados[0] == 1 and valor_dados[1] == 2) or (
             valor_dados[0] == 2 and valor_dados[1] == 1):
            return (True, "Ataque")
        elif (valor_dados[0] == 3 and valor_dados[1] == 1) or (
             valor_dados[0] == 1 and valor_dados[1] == 3):
            return (True, "Terremoto")
        else:
            return False

    def terremoto(self, afectado):
        nueva_vida = random.randint(1, self.data["NUMERO_VIDAS"])
        self.jugadores_vidas[afectado] = nueva_vida
        return nueva_vida

    def revisar_anunciar(self, valor):
        valor = f"{valor}"
        if valor.isdigit() is True:
            valor = int(valor)
            if (12 < valor) or (1 >= valor):
                return "Valor inválido"
            elif self.num_mayor_enunciado >= valor:
                return f"Tiene que ser >{self.num_mayor_enunciado}"
            else:
                return True
        else:
            return "Tiene que ser numero"


class Bots:

    def __init__(self, id) -> None:
        self.id = id
        self.nombre = "BOT" + str(self.id)
