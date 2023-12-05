#!/usr/bin/python3
from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot

message_encrypted = 70407336670535933819674104208890254240063781538460394662998902860952366439176467447947737680952277637330523818962104685553250402512989897886053
exponent = 3

message_original = iroot(message_encrypted, exponent)[0]
flag = long_to_bytes(message_original)

print(flag.decode())
