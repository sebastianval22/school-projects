import parametros as p
import random
import funciones as f
import clases as c


class Torneo:

    def __init__(self, arena: c.Arena, eventos: list,
                 meta: float, dias_totales: int):
        self.arena = arena
        self.eventos = eventos
        self.equipo = []
        self.mochila = []
        self.metros_cavados = 0
        self.meta = meta
        self.dias_transcurridos = 1
        self.dias_totales = dias_totales

    def simular_dia(self):
        if self.arena.tipo == "magnetica":
            self.arena.humedad = random.randint(1, 10)
            self.arena.dureza = random.randint(1, 10)
        string = "Día " + str(self.dias_transcurridos)
        print(string.center(60, " "))
        print("-"*60)
        print("Metros Cavados:")
        contador_con = 0
        contador_tes = 0
        descansando = []
        metros_dia = 0
        for i in range(0, len(self.equipo)):
            objeto_excavador = self.equipo[i]
            if objeto_excavador.energia == 0:
                objeto_excavador.descansar()
                descansando.append(objeto_excavador.nombre)
            else:
                metros_cavados = float(objeto_excavador.cavar(self.arena))
                nombre = objeto_excavador.nombre
                print(nombre, "ha cavado", metros_cavados, "metros.")
                metros_dia += metros_cavados
        self.metros_cavados = round(self.metros_cavados + metros_dia, 2)
        print("El equipo consiguió excavar", round(metros_dia, 2), "metros.")
        print("\nItems Encontrados:")
        for k in range(0, len(self.equipo)):
            objeto_excavador = self.equipo[k]
            if objeto_excavador.nombre not in descansando:
                item = objeto_excavador.encontrar_item(self.arena)
                nombre = objeto_excavador.nombre
                if item is False:
                    print(nombre, "no consiguió nada.")
                elif item.tipo == "consumible":
                    contador_con += 1
                    self.mochila.append(item)
                    print(nombre, "consiguió", item.nombre,
                          "del tipo consumible.")
                else:
                    contador_tes += 1
                    self.mochila.append(item)
                    print(nombre, "consiguió", item.nombre, "del tipo tesoro.")
        print("Se han encontrado", (contador_tes + contador_con), "ítems:")
        print("-", contador_con, "consumibles.\n-", contador_tes, "tesoros.\n")
        print()
        evento = random.choices([True, False],
                                weights=[p.PROB_INICIAR_EVENTO,
                                         1 - p.PROB_INICIAR_EVENTO], k=1)[0]
        if evento is False:
            print("No ha ocurrido ningun evento...")
        else:
            tipo_evento = random.choices(self.eventos,
                                         weights=[p.PROB_LLUVIA,
                                                  p.PROB_TERREMOTO,
                                                  p.PROB_DERRUMBE], k=1)[0]
            if tipo_evento == "lluvia":
                print("¡¡Durante el día de trabajo ocurrió una lluvia!!")
                if self.arena.tipo == "normal":
                    while True:  # Escoger Arena
                        indice = random.randint(0, len(f.info_arenas) - 1)
                        if f.info_arenas[indice][1] == "mojada":
                            objeto_arena = f.instanciar_arena(f.info_arenas
                                                              [indice])
                            break
                    self.arena = objeto_arena
                if self.arena.tipo == "rocosa":
                    while True:  # Escoger Arena
                        indice = random.randint(0, len(f.info_arenas) - 1)
                        if f.info_arenas[indice][1] == "magnetica":
                            objeto_arena = f.instanciar_arena(f.info_arenas
                                                              [indice])
                            break
                    self.arena = objeto_arena
            elif tipo_evento == "terremoto":
                print("¡¡Durante el día de trabajo ocurrió un terremoto!!")
                if self.arena.tipo == "normal":
                    while True:  # Escoger Arena
                        indice = random.randint(0, len(f.info_arenas) - 1)
                        if f.info_arenas[indice][1] == "rocosa":
                            objeto_arena = f.instanciar_arena(f.info_arenas
                                                              [indice])
                            break
                    self.arena = objeto_arena
                if self.arena.tipo == "mojada":
                    while True:  # Escoger Arena
                        indice = random.randint(0, len(f.info_arenas) - 1)
                        if f.info_arenas[indice][1] == "magnetica":
                            objeto_arena = f.instanciar_arena(f.info_arenas
                                                              [indice])
                            break
                    self.arena = objeto_arena
            else:
                print("¡¡Durante el día de trabajo ocurrió un derrumbe!!")
                while True:  # Escoger Arena
                    indice = random.randint(0, len(f.info_arenas) - 1)
                    if f.info_arenas[indice][1] == "normal":
                        objeto_arena = f.instanciar_arena(f.info_arenas
                                                          [indice])
                        break
                self.arena = objeto_arena
                restar = p.METROS_PERDIDOS_DERRUMBE
                self.metros_cavados = self.metros_cavados - restar
            for o in range(0, len(self.equipo)):
                excavador = self.equipo[o]
                excavador.felicidad -= p.FELICIDAD_PERDIDA
            print("La arena final es del tipo", self.arena.tipo)
            print("Tu equipo ha perdido", p.FELICIDAD_PERDIDA, "de felicidad")
        print()
        self.metros_cavados = round(self.metros_cavados, 2)
        print("Metros totales cavados:", (self.metros_cavados))
        for j in range(0, len(descansando)):
            print(descansando[j], "está descansando...")

    def mostrar_estado(self):
        print("\n*** Estado Torneo ***".center(60, " "))
        print("-"*60)
        print("Día actual:", self.dias_transcurridos)
        print("Tipo de arena:", self.arena.tipo)
        print("Nombre arena:", self.arena.nombre)
        print("Dificultad arena:", self.arena.dificultad_arena())
        print(f"Metros excavados: {self.metros_cavados}/{self.meta}")
        print("-"*60)
        print("Excavadores".center(60, " "))
        print("  Nombre  |   Tipo   | Energía | Fuerza | Suerte | Felicidad")
        print("-"*60)
        for i in range(0, len(self.equipo)):
            excavador = self.equipo[i]
            print(f" {excavador.nombre:9.9s} | {excavador.tipo: ^8s} | " +
                  f"{excavador.energia: ^7d} | {excavador.fuerza: ^6d} |" +
                  f" {excavador.suerte: ^6d} | {excavador.felicidad: ^9d}")

    def ver_mochila(self):
        print("*** Menú Ítems ***".center(150, " "))
        print("-"*150)
        print("                       Nombre                          |" +
              "     Tipo     |                              Descripcion")
        print("-"*150)
        for i in range(0, len(self.mochila)):
            item = self.mochila[i]
            print(f"[{i+1}] {item.nombre:50.50} | {item.tipo: ^12s} | " +
                  f"{item.descripcion:70.70s}")
        print("-"*150)
        print(f"[{len(self.mochila)+1}] Volver")
        print("[X] Salir del programa")
