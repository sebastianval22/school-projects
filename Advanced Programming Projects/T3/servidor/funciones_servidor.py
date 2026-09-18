import json


def codificar(mensaje):  # MENSAJE ENCRIPTADO LO CODIFICA A UN BYTEARRAY
    # Frames an encrypted message into the protocol's byte format: a 4-byte
    # little-endian total-length header, followed by 128-byte blocks each
    # prefixed with a 4-byte big-endian block id, zero-padding the last block.
    pass


def decodificar(mensaje):  # MENSAJE ENCRIPTADO LO DECODIFICO PARA LUEGO
    # Inverse of codificar: reads the length header, then reassembles the
    # original bytes from the 128-byte blocks, dropping the zero padding.
    pass


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
