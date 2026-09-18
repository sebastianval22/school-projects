def codificar(mensaje):  # MENSAJE ENCRIPTADO LO CODIFICA A UN BYTEARRAY
    # Frames an encrypted message into the protocol's byte format: a 4-byte
    # little-endian total-length header, followed by 128-byte blocks each
    # prefixed with a 4-byte big-endian block id, zero-padding the last block.
    pass


def decodificar(mensaje):  # MENSAJE ENCRIPTADO LO DECODIFICO PARA LUEGO
    # Inverse of codificar: reads the length header, then reassembles the
    # original bytes from the 128-byte blocks, dropping the zero padding.
    pass
