import functions as f
import os           # importo libreria os, para ver la existencia de archivos
import sys          # importo libreria sys, para poder cerrar el programa
import tablero

print("*** Menú de Inicio ***")
nombre_archivo = input("Indique el nombre del archivo que desea abrir:")
existencia_archivo = \
 os.path.isfile(str("Archivos/" +
                    nombre_archivo))
if ".txt" not in nombre_archivo:
    existencia_archivo = False
if existencia_archivo is True:      # entro al "Menú de Acciones"
    opcion_elegida = 1
    while opcion_elegida != 0:
        print("*** Menú de Acciones ***" + "\n")
        tablero_archivo = f.cargar_tablero(nombre_archivo)
        lista_acciones = [(1, "Mostrar Tablero"),
                          (2, "Validar bombas y tortugas"),
                          (3, "Validar solución"),
                          (4, "Solucionar tablero"),
                          (0, "Salir del programa")]
        for opcion in lista_acciones:
            print(f"[{opcion[0]}] {opcion[1]}")
        opcion_elegida = str(input("\n" +
                                   "Indique su opción (1, 2, 3, 4, o 0):"))
        while opcion_elegida not in [str(1), str(2), str(3), str(4), str(0)]:
            print("Opcion no valida.")
            opcion_elegida = input("\n" +
                                   "Indique su opción (1, 2, 3, 4, o 0):")
        if opcion_elegida == str(1):
            tablero.imprimir_tablero_con_utf8(tablero_archivo)
        elif opcion_elegida == str(2):
            bombas_invalidas = f.verificar_valor_bombas(tablero_archivo)
            tortugas_invalidas = f.verificar_tortugas(tablero_archivo)
            if (tortugas_invalidas or bombas_invalidas) > 0:
                print("El tablero no es válido")
            else:
                print("Bombas y Tortugas válidas")
        elif opcion_elegida == str(3):
            if f.es_caso_base(tablero_archivo) is True:
                print("Tablero Válido!")
            else:
                print("El tablero no es válido.")
        elif opcion_elegida == str(4):
            tablero_solucionado = f.solucionar_tablero(tablero_archivo)
            if not isinstance(tablero_solucionado, list):
                print("El tablero no se pudo solucionar")
            else:
                nombre_sin_extension, extension = \
                 os.path.splitext(nombre_archivo)
                f.guardar_tablero((nombre_sin_extension + "_sol"
                                  + extension), tablero_solucionado)
                tablero.imprimir_tablero_con_utf8(tablero_solucionado)
        elif opcion_elegida == str(0):
            sys.exit()
    sys.exit()
else:
    print("El archivo no es valido.")
    sys.exit()
