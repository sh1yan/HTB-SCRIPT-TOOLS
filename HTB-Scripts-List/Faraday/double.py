#!/usr/bin/python3
from itertools import product
import string, struct, sys

flag = "FARADAY{d0ubl3_@nd_f1o@t_"

possible = string.ascii_lowercase + string.punctuation

for nxt in product(possible, repeat=5):
    n = "".join(nxt).encode()
    s = b"_" + n[:2] + b"}" + n[2:] + b"@"
    rtn = struct.unpack("<d", s)[0]
    rtn = 1665002837.488342 / rtn
    if abs(rtn - 4088116.817143337) <= 0.0000001192092895507812:
        s = n[:2] + b"@" + n[2:] + b"}"
        print(flag + s.decode())
        sys.exit(0)
