#!/usr/bin/python3
import ctypes

plain_text = list(bytearray.fromhex("4c6f72656d20697073756d20646f6c6f722073697420616d65742c20636f6e7365637465747565722061646970697363696e6720656c69742e2041656e65616e20636f6d6d6f646f206c6967756c612e"))
crypt_text = list(bytearray.fromhex("6a5b13ae21bd06b2426eb4c5fbe6f0c432c3e24e904daf6e064063dcbb5d9dd953bd85e038a2eb2b9495e3dffd58e0cc275a1e6f0fd262bf5371bab8969256b789bc66c9c8f6303a21d6400925e056ff"))

plain_text = [int.from_bytes(bytes(plain_text[i * 4 : i * 4 + 4]), "big") for i in range(16)]
crypt_text = [int.from_bytes(bytes(crypt_text[i * 4 : i * 4 + 4]), "big") for i in range(16)]

def inner(state):
    def quarterRound(a, b, c, d):
        def rotate(v, c):
            return ((v >> c) & 0xffffffff) | v << (32 - c) & 0xffffffff

        state[b] = rotate(state[b], 7) ^ state[c]
        state[c] = (state[c] - state[d]) & 0xffffffff
        state[d] = rotate(state[d], 8) ^ state[a]
        state[a] = (state[a] - state[b]) & 0xffffffff
        state[b] = rotate(state[b], 12) ^ state[c]
        state[c] = (state[c] - state[d]) & 0xffffffff
        state[d] = rotate(state[d], 16) ^ state[a]
        state[a] = (state[a] - state[b]) & 0xffffffff

    for i in range(10):
        quarterRound(3, 4, 9, 14)
        quarterRound(2, 7, 8, 13)
        quarterRound(1, 6, 11, 12)
        quarterRound(0, 5, 10, 15)
        quarterRound(3, 7, 11, 15)
        quarterRound(2, 6, 10, 14)
        quarterRound(1, 5, 9, 13)
        quarterRound(0, 4, 8, 12)

    return b"".join([i.to_bytes(4, byteorder="little") for i in state][0:12]).decode()

def xor(a, b):
    a1 = ctypes.c_ulong(a).value
    b1 = ctypes.c_ulong(b).value

    a = f"{a1:08x}"
    b = f"{b1:08x}"

    if len(a) == 16:
        a = a[8:]

    if len(b) == 16:
        b = b[8:]

    value = ""

    for i in range(3, -1, -1):
        t = (hex(int("0x" + a[i * 2 : i * 2 + 2], 0) ^ int("0x" + b[i * 2 : i * 2 + 2], 0)))[2:]

        if len(t) == 1:
            t = "0" + t

        value += t

    return "0x" + value

password = inner([int(xor(plain_text[i], crypt_text[i]), 16) for i in range(16)])[16:]

print(password)
