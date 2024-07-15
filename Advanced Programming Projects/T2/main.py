from PyQt5.QtWidgets import QApplication
import sys
from frontend.ventana_inicio import Ventana_Inicio  # Se agrega import
from frontend.ventana_juego import Ventana_Juego
from frontend.ventana_juego_timer import Ventana_Juego_Timer
from frontend.ventana_final import Ventana_Final
from backend.backend import Juego


class ShootApplication():
    def __init__(self) -> None:
        self.frontend_mapa = Ventana_Inicio()
        self.frontend_juego = Ventana_Juego()
        self.frontend_juego_timer = Ventana_Juego_Timer()
        self.backend = Juego()
        self.frontend_juego_final = Ventana_Final()
        self.mapa = " "

    def conectar(self) -> None:
        # frontend.ventana_inicio avisa al backend sobre el mapa y nombre
        self.frontend_mapa.senal_nombre.connect(self.backend.set_nombre)
        self.frontend_mapa.senal_mapa.connect(self.backend.seleccionar_mapa)
        # backend le avisa al frontend del juego que empieza el juego
        self.backend.senal_empezar_juego.connect(
            self.frontend_juego.empezar_juego)
        # backend le avisa al fronte end de inicio a esconderse
        self.backend.senal_esconder_inicio.connect(
            self.frontend_mapa.esconder_ventana)
        # frontend.ventana_juego avisa al backend sobre las entidades y empezar
        self.frontend_juego.senal_jugar.connect(self.backend.entidades)
        # backend le avisa al frontend del juego/timer que empieza el juego
        self.backend.senal_empezar_juego_timer.connect(
            self.frontend_juego_timer.empezar_juego)
        # backend le avisa al fronteend de juego a esconderse
        self.backend.senal_esconder_ventana_juego.connect(
            self.frontend_juego.esconder_ventana)
        # frontend.ventana_juego_timer le avisa a backend mover a luigi
        self.frontend_juego_timer.senal_nueva_posicion_luigi.connect(
            self.backend.mover_a_luigi)
        # backend le entrega la nueva posicion de luigi
        self.backend.senal_mover.connect(self.frontend_juego_timer.nuevo_lugar)
        # frontend_ventana_juego_timer le avisa a backend nuevas posiciones
        self.frontend_juego_timer.senal_actualizar_info_mapa.connect(
            self.backend.actualizar_mapa)
        # backend le avisa a frontend_ventana_juego_timer cuando perdio un vida
        self.backend.senal_perdida_vida.connect(
            self.frontend_juego_timer.perdio_vida)
        # backend le avisa a frontend_ventana_juego_timer_ a esconderse
        self.backend.senal_termino_juego.connect(
            self.frontend_juego_timer.esconder)
        # frontend_juego_ventana_timer le avisa a ventana_final si gano
        self.frontend_juego_timer.senal_termino.connect(
            self.frontend_juego_final.final)
        # backend le avisa a frontend_juego_ventana_timer eliminar fantasma
        self.backend.senal_eliminar_entidad.connect(
            self.frontend_juego_timer.eliminar_entidad)
        # frontend_juego_ventana_timer le avisa a backend si agarro la S
        self.frontend_juego_timer.senal_revisar_si_gano.connect(
            self.backend.revisar_si_gano)
        # backend le avisa a frontend_ventana_final el nombre
        self.backend.senal_nombre_juego.connect(
            self.frontend_juego_final.nombre)
        # frontend_juego_ventana_timer le avisa a backend si pauso
        self.frontend_juego_timer.senal_pausa.connect(self.backend.pausa)
        # frontend_juego_ventana_timer le avisa a backend si hizo cheat_1
        self.frontend_juego_timer.senal_cheat_1.connect(self.backend.cheat_1)
        # frontend_juego_ventana_timer le avisa a backend si hizo cheat_2
        self.frontend_juego_timer.senal_cheat_2.connect(self.backend.cheat_2)
        self.frontend_juego_final.senal_volver_a_empezar.connect(
            self.try_again)
        self.backend.senal_crear_mapa.connect(
            self.frontend_juego_final.crear_mapa)

    def iniciar(self):
        # Comenzar el juego
        self.frontend_mapa.show()

    def try_again(self, mapa: str, nombre: str):
        self.frontend_juego_final.close()
        self.frontend_juego = Ventana_Juego()
        self.frontend_juego_timer = Ventana_Juego_Timer()
        self.backend = Juego()
        self.frontend_juego_final = Ventana_Final()
        self.mapa = mapa
        self.nombre = nombre
        self.conectar_otra_vez()
        self.backend.set_nombre(self.nombre)
        self.backend.seleccionar_mapa(self.mapa)

    def conectar_otra_vez(self):
        self.backend.senal_empezar_juego.connect(
            self.frontend_juego.empezar_juego)
        # frontend.ventana_juego avisa al backend sobre las entidades y empezar
        self.frontend_juego.senal_jugar.connect(self.backend.entidades)
        # backend le avisa al frontend del juego/timer que empieza el juego
        self.backend.senal_empezar_juego_timer.connect(
            self.frontend_juego_timer.empezar_juego)
        # backend le avisa al fronteend de juego a esconderse
        self.backend.senal_esconder_ventana_juego.connect(
            self.frontend_juego.esconder_ventana)
        # frontend.ventana_juego_timer le avisa a backend mover a luigi
        self.frontend_juego_timer.senal_nueva_posicion_luigi.connect(
            self.backend.mover_a_luigi)
        # backend le entrega la nueva posicion de luigi
        self.backend.senal_mover.connect(self.frontend_juego_timer.nuevo_lugar)
        # frontend_ventana_juego_timer le avisa a backend nuevas posiciones
        self.frontend_juego_timer.senal_actualizar_info_mapa.connect(
            self.backend.actualizar_mapa)
        # backend le avisa a frontend_ventana_juego_timer cuando perdio un vida
        self.backend.senal_perdida_vida.connect(
            self.frontend_juego_timer.perdio_vida)
        # backend le avisa a frontend_ventana_juego_timer_ a esconderse
        self.backend.senal_termino_juego.connect(
            self.frontend_juego_timer.esconder)
        # frontend_juego_ventana_timer le avisa a ventana_final si gano
        self.frontend_juego_timer.senal_termino.connect(
            self.frontend_juego_final.final)
        # backend le avisa a frontend_juego_ventana_timer eliminar fantasma
        self.backend.senal_eliminar_entidad.connect(
            self.frontend_juego_timer.eliminar_entidad)
        # frontend_juego_ventana_timer le avisa a backend si agarro la S
        self.frontend_juego_timer.senal_revisar_si_gano.connect(
            self.backend.revisar_si_gano)
        # backend le avisa a frontend_ventana_final el nombre
        self.backend.senal_nombre_juego.connect(
            self.frontend_juego_final.nombre)
        # frontend_juego_ventana_timer le avisa a backend si pauso
        self.frontend_juego_timer.senal_pausa.connect(self.backend.pausa)
        # frontend_juego_ventana_timer le avisa a backend si hizo cheat_1
        self.frontend_juego_timer.senal_cheat_1.connect(self.backend.cheat_1)
        # frontend_juego_ventana_timer le avisa a backend si hizo cheat_2
        self.frontend_juego_timer.senal_cheat_2.connect(self.backend.cheat_2)
        self.frontend_juego_final.senal_volver_a_empezar.connect(
            self.try_again)
        self.backend.senal_crear_mapa.connect(
            self.frontend_juego_final.crear_mapa)


if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    game = ShootApplication()
    game.conectar()
    game.iniciar()

    sys.exit(app.exec())
