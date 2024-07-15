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

    return (bytearray_codificado)


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
