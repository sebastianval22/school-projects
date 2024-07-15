import collections as c


def encriptar(msg: bytearray, N) -> bytearray:
    if N >= len(msg):
        N = N % len(msg)
    desplazo_derecha = N
    deque_msg = c.deque(msg)
    deque_msg.rotate(desplazo_derecha)
    bytearray_msg = bytearray(deque_msg)
    bytearray_msg[0], bytearray_msg[desplazo_derecha] = bytearray_msg[
        desplazo_derecha], bytearray_msg[0]
    return bytearray_msg


def desencriptar(msg: bytearray, N):
    if N >= len(msg):
        N = N % len(msg)
    desplazo_izquierda = N
    msg[0], msg[desplazo_izquierda] = msg[desplazo_izquierda], msg[0]
    parte_1 = msg[desplazo_izquierda:]
    parte_2 = msg[:desplazo_izquierda]
    msg[:] = parte_1 + parte_2
    return msg


if __name__ == "__main__":
    # Testear encriptar
    N = 100
    msg_original = bytearray(
        b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x00\x01\x02\x03\x04\x05')
    msg_esperado = bytearray(
        b'\x01\x05\x02\x03\x04\x05\x06\x07\x08\x09\x00\x01\x02\x03\x04')
    msg_encriptado = encriptar(msg_original, N)
    print(msg_encriptado)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")

    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_encriptado, N)
    print(msg_desencriptado)
    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")
