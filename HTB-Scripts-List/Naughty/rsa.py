#!/usr/bin/python3
from Crypto.PublicKey import RSA
from gmpy2 import iroot

file = open("wh1tedrvg0n.pem", "r")
key = RSA.importKey(file.read())

n = key.n
e = key.e

for k in range(1, 100000):
    if iroot(1 + 4 * e * k * n, 2)[1] == True:
        q = (1 + int(iroot(1 + 4 * e * k * n, 2)[0])) // (2 * e)
        if n % q == 0:
            break

p = (n // q)

m = n - (p + q - 1)

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
private = key.exportKey().decode()

file = open("private.key", "w")
file.write(private)
print(private)
