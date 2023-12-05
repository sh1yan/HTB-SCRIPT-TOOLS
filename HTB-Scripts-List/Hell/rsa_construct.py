#!/usr/bin/python3
from Crypto.PublicKey import RSA

file = open("public.crt", "r")
key = RSA.importKey(file.read())

n = key.n
e = key.e

p = 13833273097933021985630468334687187177001607666479238521775648656526441488361370235548415506716907370813187548915118647319766004327241150104265530014047083
q = 20196596265430451980613413306694721666228452787816468878984356787652099472230934129158246711299695135541067207646281901620878148034692171475252446937792199

m = n-(p+q-1)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise
    else:
        return x % m

d = modinv(e, m)

key = RSA.construct((n, e, d, p, q))
print(key.exportKey().decode())
