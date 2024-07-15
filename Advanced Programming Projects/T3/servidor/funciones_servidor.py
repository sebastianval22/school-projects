import json


def codificar(mensaje):  # MENSAJE ENCRIPTADO LO CODIFICA A UN BYTEARRAY
    bytearray_codificado = bytearray()
    largo_mensaje = len(mensaje)
    bytes_largo = largo_mensaje.to_bytes(4, "little")
    bytearray_codificado += bytes_largo
    chunk = 1
    seguir = True
    while seguir:
        bytes_chunk = chunk.to_bytes(4, "big")
        bytearray_codificado += bytes_chunk
        chunk += 1
        bytes_recursion = b""
        if len(mensaje) < 128:
            pieza = mensaje
            relleno = b'\x00'*(128 - len(pieza))
            bytes_recursion = pieza+relleno
            seguir = False
        else:
            pieza = mensaje[0:128]
            mensaje = mensaje[128:]
            bytes_recursion = pieza
        bytearray_codificado += bytes_recursion

    return bytearray(bytearray_codificado)


def decodificar(mensaje):  # MENSAJE ENCRIPTADO LO DECODIFICO PARA LUEGO
    bytes_largo_mensaje = mensaje[0:4]  # DESINCRIPTARLO
    largo_mensaje = int.from_bytes(bytes_largo_mensaje, "little")
    mensaje_decodificado = b""
    bytes_recursion = mensaje[8:]
    seguir = True
    while seguir:
        if len(bytes_recursion) <= 128:
            bytes_faltantes = largo_mensaje - len(mensaje_decodificado)
            mensaje_decodificado += bytes_recursion[0:bytes_faltantes]
            seguir = False
        else:
            mensaje_decodificado += bytes_recursion[0:128]
            bytes_recursion = bytes_recursion[132:]
    return bytearray(mensaje_decodificado)


def print_logs(cliente, evento, detalle):
    print(f" {cliente:50.50}     |    {evento: ^18s}      | " +
          f"{detalle:70.70s}")


def print_inicial():
    print("Servidor iniciado. Esperando conexiones...")
    print("                       Cliente                          |" +
          "          Evento            |                        Detalles")
    print("-"*150)


def log_vidas(terremoto: bool, nombre, vidas):
    if terremoto is True:
        ms = f"Ha ocurrido un terremoto!!! {nombre} ahora tiene {vidas} vidas."
        return ms
    else:
        return f"{nombre} perdió una vida. {vidas} vidas restantes."


def cargar_jsno():
    with open("servidor/parametros_servidor.json",
              encoding="utf-8") as jsno_file:
        data = json.load(jsno_file)
    return data
