#!/usr/bin/python3
from pwn import remote, log
import sys, re

if len(sys.argv) < 2:
    log.failure(f"Uso: python3 {sys.argv[0]} <host:port>")
    sys.exit(1)

host, port = sys.argv[1].split(":")
shell = remote(host, port)

shell.sendline(b"1")

output = shell.recvall()
match = re.search(b"HTB\{.*\}", output)
log.success(f"Flag: {match.group(0).decode()}")
