import sys
import parametros as p
import random
import funciones as f
import class_torneo as cf
from os import listdir

opcion_elegida = 0


def menu_inicio():
    retorno_menu = None
    while retorno_menu != "Salir":
        print()
        print("*** Menú de Inicio ***")
        print("------------------------")
        lista_acciones = [(1, "Nueva partida"),
                          (2, "Cargar partida"),
                          ("X", "Salir")]
        for opcion in lista_acciones:
            print(f"[{opcion[0]}] {opcion[1]}")
        opcion_elegida = str(input("\n" +
                                   "Indique su opción (1, 2 o X):"))
        while opcion_elegida not in [str(1), str(2), "X"]:
            print("Opcion no valida.")
            opcion_elegida = input("\n" +
                                   "Indique su opción (1, 2 o X):")
        if opcion_elegida == str(1):
            while True:  # Escoger Arena
                indice = random.randint(0, len(f.info_arenas) - 1)
                if f.info_arenas[indice][1] == p.ARENA_INICIAL:
                    objeto_arena = f.instanciar_arena(f.info_arenas[indice])
                    break
            torneo_principal = cf.Torneo(objeto_arena, f.eventos,
                                         p.METROS_META, p.DIAS_TORNEO)
            cantidad_excavadores = p.CANTIDAD_EXCAVADORES_INICIALES
            excavadores = []
            while len(torneo_principal.equipo) < cantidad_excavadores:
                indice = random.randint(0, len(f.info_excavadores) - 1)
                info_excavador = f.info_excavadores[indice]
                if info_excavador not in excavadores:
                    excavadores.append(info_excavador)
                    objeto_excavador = f.instanciar_excavador(info_excavador)
                    torneo_principal.equipo.append(objeto_excavador)
            retorno_menu = menu_principal(torneo_principal)
        elif opcion_elegida == str(2):
            contenido = listdir("Partidas")
            print("Archivos disponibles:")
            opciones_disponibles = ["X"]
            for i in range(len(contenido)):
                opcion = f"[{i + 1}] {contenido[i]}"
                opciones_disponibles.append(str(i+1))
                print(opcion)
            opcion_elegida = input("Escoga partida para cargar" +
                                   " (X para volver):")
            while opcion_elegida not in opciones_disponibles:
                print("Opción inválida.")
                opcion_elegida = input("Escoga partida para cargar" +
                                       " (X para volver):")
            if opcion_elegida != "X":
                indice_archivo = int(opcion_elegida) - 1
                nombre_archivo = contenido[indice_archivo]
                archivo = open(("Partidas/"
                                + nombre_archivo), "r")
                info_partida = (archivo.readlines())
                info_torneo = ((info_partida[0]).strip("\n")).split(",")
                metros_cavados = float(info_torneo[0])
                metros_meta = float(info_torneo[1])
                dias_transcurridos = int(info_torneo[2])
                dias_totales = int(info_torneo[3])
                print(dias_totales)
                info_arena = (info_partida[2]).strip("\n").split(",")
                objeto_arena = f.instanciar_arena(info_arena)
                i = 4
                equipo = []
                while len(info_partida[i]) != 1:
                    info_excavador = ((info_partida[i]).strip("\n").split(","))
                    if info_excavador[0] == "*****ITEMS*****":
                        break
                    objeto_excava = f.instanciar_excavador(info_excavador[:7])
                    dias_descansando = int(info_excavador[7])
                    objeto_excava.dias_descansando = dias_descansando
                    equipo.append(objeto_excava)
                    i += 1
                mochila = []
                for j in range(i+1, len(info_partida)):
                    info_item = ((info_partida[j]).strip("\n").split(","))
                    tipo = info_item[len(info_item) - 1]
                    if tipo == "consumible":
                        objeto_item = f.instanciar_consumible(info_item[:6])
                    else:
                        objeto_item = f.instanciar_tesoro(info_item[:4])
                    mochila.append(objeto_item)
                torneo_principal = cf.Torneo(objeto_arena, f.eventos,
                                             metros_meta, dias_totales)
                torneo_principal.metros_cavados = metros_cavados
                torneo_principal.dias_transcurridos = dias_transcurridos
                torneo_principal.equipo = equipo
                torneo_principal.mochila = mochila
            retorno_menu = menu_principal(torneo_principal)
        elif opcion_elegida == "X":
            sys.exit()


def menu_principal(torneo_principal):
    while True:
        print()
        print("*** Menú Principal ***")
        print("------------------------")
        lista_acciones = [(1, "Simular día torneo"),
                          (2, "Ver estado torneo"),
                          (3, "Ver ítems"),
                          (4, "Guardar partida"),
                          (5, "Volver"),
                          ("X", "Salir del programa")]
        for opcion in lista_acciones:
            print(f"[{opcion[0]}] {opcion[1]}")
        opcion_elegida = str(input("\n" +
                                   "Indique su opción (1, 2, 3, 4, 5 o X):"))
        while opcion_elegida not in [str(1), str(2), str(3),
                                     str(4), str(5), "X"]:
            print("Opcion no valida.")
            opcion_elegida = input("\n" +
                                   "Indique su opción (1, 2, 3, 4, 5 o X):")
        if opcion_elegida == str(1):
            print()
            torneo_principal.simular_dia()
            torneo_principal.dias_transcurridos += 1
            dias_totales = torneo_principal.dias_totales
            if torneo_principal.dias_transcurridos > dias_totales:
                print("RESULTADOS FINALES".center(60, "-"))
                print("Metros cavados:", torneo_principal.metros_cavados)
                print("Metros meta:", torneo_principal.meta)
                if torneo_principal.metros_cavados > torneo_principal.meta:
                    print("¡¡¡¡ HÁS GANADO !!!")
                else:
                    print("Hás perdido...")
                return "Volver"
        elif opcion_elegida == str(2):
            torneo_principal.mostrar_estado()
        elif opcion_elegida == str(3):
            retorno_menu = menu_items(torneo_principal)
            if retorno_menu == "Salir":
                return "Salir"
        elif opcion_elegida == str(4):
            nombre_archivo = input(str("Indique el nombre con el cual se" +
                                       "quiere guardar la partida:"))
            archivo = open(("Partidas/" +
                            nombre_archivo + ".txt"), "w")
            # agregar info_torneo
            string_archivo = ""
            string_archivo += str(str(torneo_principal.metros_cavados) + ","
                                  + str(torneo_principal.meta) + "," +
                                  str(torneo_principal.dias_transcurridos) +
                                  "," + str(torneo_principal.dias_totales))
            string_archivo += "\n*****ARENA*****\n"
            arena = torneo_principal.arena
            string_archivo += str((arena.nombre) + "," + (arena.tipo) + "," +
                                  str(arena.rareza) + "," + str(arena.humedad)
                                  + "," + str(arena.dureza) + "," +
                                  str(arena.estatica))
            string_archivo += "\n*****EXCAVADORES*****\n"
            for i in range(0, len(torneo_principal.equipo)):
                excavador = torneo_principal.equipo[i]
                string_archivo += str((excavador.nombre) + "," +
                                      (excavador.tipo) + "," +
                                      str(excavador.edad) + "," +
                                      str(excavador.energia) + "," +
                                      str(excavador.fuerza) + "," +
                                      str(excavador.suerte) + "," +
                                      str(excavador.felicidad) + "," +
                                      str(excavador.dias_descansando) + "\n")
            string_archivo += "*****ITEMS*****"
            for i in range(0, len(torneo_principal.mochila)):
                item = torneo_principal.mochila[i]
                if item.tipo == "tesoro":
                    string_archivo += str("\n" + (item.nombre) + "," +
                                          (item.descripcion) + "," +
                                          str(item.calidad) + "," +
                                          (item.cambio) + "," + item.tipo)
                else:
                    string_archivo += str("\n" + (item.nombre) + "," +
                                          (item.descripcion) + "," +
                                          str(item.energia) + "," +
                                          str(item.fuerza) + "," +
                                          str(item.suerte) + "," +
                                          str(item.felicidad) + "," +
                                          item.tipo)
            archivo.write(str(string_archivo))
            archivo.close()
            print("Partida", nombre_archivo, "guardada con existo")
            return "Volver"
        elif opcion_elegida == str(5):
            return "Volver"
        elif opcion_elegida == "X":
            return "Salir"


def menu_items(torneo_principal):
    while True:
        print()
        torneo_principal.ver_mochila()
        opciones = []
        string = "Indique su opción ("
        for i in range(0, len(torneo_principal.mochila)):
            opciones.append(str(i+1))
            string += str(i + 1) + ", "
        opciones.append(str(len(torneo_principal.mochila) + 1))
        string = string + str(len(torneo_principal.mochila) + 1) + " o X): "
        opciones.append("X")
        print(opciones)
        opcion_elegida = (input("\n" + string))
        while opcion_elegida not in opciones:
            print("Opcion no valida.")
            opcion_elegida = input("\n" + string)
        if opcion_elegida == "X":
            return "Salir"
        else:
            num_elegido = int(opcion_elegida)
            if num_elegido == (len(torneo_principal.mochila) + 1):
                return "Volver"
            else:
                item_a_aplicar = torneo_principal.mochila[num_elegido - 1]
                if item_a_aplicar.tipo == "tesoro":
                    if item_a_aplicar.calidad == 1:
                        posibles_excavadores = []
                        tipo_de_excavador = item_a_aplicar.cambio
                        # agrandar al equipo
                        nombres_equipo = []
                        lista_equipo = torneo_principal.equipo
                        for i in range(0, len(lista_equipo)):
                            nombre = lista_equipo[i].nombre
                            nombres_equipo.append(nombre)
                        for i in range(0, len(f.info_excavadores)):
                            info_excavador = f.info_excavadores[i]
                            objeto = f.instanciar_excavador((info_excavador))
                            if objeto.tipo == tipo_de_excavador:
                                posibles_excavadores.append(objeto.nombre)
                        while posibles_excavadores != []:
                            posible_indice = len(posibles_excavadores) - 1
                            indice = random.randint(0, posible_indice)
                            excavador = posibles_excavadores[indice]
                            if excavador not in nombres_equipo:
                                (torneo_principal.equipo).append(excavador)
                                print("Se utilizó el tesoro " +
                                      (item_a_aplicar.nombre) +
                                      ". Se añade el excavador " +
                                      (excavador.nombre) + " del tipo " +
                                      (excavador.tipo) + " al equipo!")
                                torneo_principal.mochila.pop(num_elegido - 1)
                                break
                            posibles_excavadores.pop(indice)
                        if posibles_excavadores == []:
                            print("No hay excavadores de este tipo...")
                            print("No se puede aplicar este tesoro")
                    else:
                        tipo_de_arena = item_a_aplicar.cambio
                        while True:  # Escoger Arena
                            indice = random.randint(0, len(f.info_arenas) - 1)
                            if f.info_arenas[indice][1] == tipo_de_arena:
                                objeto_arena = f.instanciar_arena(f.info_arenas
                                                                  [indice])
                                torneo_principal.arena = objeto_arena
                                print("Se utilizó el tesoro " +
                                      (item_a_aplicar.nombre) +
                                      ". Se cambia la arena a tipo " +
                                      (objeto_arena.tipo))
                                torneo_principal.mochila.pop(num_elegido - 1)
                                break
                else:
                    for i in range(0, len(torneo_principal.equipo)):
                        excavador = torneo_principal.equipo[i]
                        excavador.consumir(item_a_aplicar)
                    print("Se utilizó el consumible " +
                          (item_a_aplicar.nombre) +
                          "." + (item_a_aplicar.descripcion)
                          + " a todos los excavadores del equipo.")
                    torneo_principal.mochila.pop(num_elegido - 1)


menu_inicio()
