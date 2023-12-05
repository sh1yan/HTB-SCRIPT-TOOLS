#!/usr/bin/python3
from pwn import log
import requests

target = "http://naughty.htb/admin.html"

bar = log.progress("")
counter = 1

with open("headers.txt", "r") as file:
    for line in file:
        header = "Naughty" + line.strip()
        bar.status(f"Probando header ({counter}/2588): {header}")
        headers = {header: "1"}
        request = requests.get(target, headers=headers)
        counter += 1

        if len(request.content) != 1681:
            bar.success(f"Header válido: {header}")
            exit(0)
