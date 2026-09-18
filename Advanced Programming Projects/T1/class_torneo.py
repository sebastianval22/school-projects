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
        # Simulates one tournament day: reshuffles a "magnetica" arena's
        # stats, has each rested digger dig (or rest if out of energy) and
        # roll for a found item, then rolls whether a random event
        # (rain/earthquake/collapse) fires, resolving its arena-type
        # transition and team happiness penalty accordingly. Solution logic
        # redacted for showcase repo.
        pass

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
