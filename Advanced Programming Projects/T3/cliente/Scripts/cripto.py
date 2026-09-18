import collections as c


def encriptar(msg: bytearray, N) -> bytearray:
    # Byte-rotation cipher keyed by N (derived from player id): rotates the
    # message N positions and swaps byte 0 with byte N. O(n).
    pass


def desencriptar(msg: bytearray, N):
    # Inverse of encriptar: undoes the byte-0/byte-N swap and the rotation.
    pass


if __name__ == "__main__":
    # Self-test demonstrating the cipher on a worked example — omitted from
    # this showcase to avoid exposing the exact cipher behavior.
    pass
