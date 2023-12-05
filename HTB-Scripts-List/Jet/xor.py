#!/usr/bin/python3
import binascii

def makeList(stringVal):
    return [c for c in stringVal]

def decrypt(hexVal, keyVal):
    keyPos = 0
    key = makeList(keyVal)
    xored = b''
    for i in range(0, len(hexVal), 2):
        byte = bytes.fromhex(hexVal[i:i+2])[0]
        xored += bytes([byte ^ ord(key[keyPos])])
        if keyPos == len(key) - 1:
            keyPos = 0
        else:
            keyPos += 1
    return xored.decode()

with open('encrypted.txt', 'rb') as f:
    content = f.read()

message = decrypt(content.hex(), 'securewebincrocks')

print(message)
