#!/usr/bin/python3
import string, itertools

base = 'securewebinc'

length = 17

keys = [base + s for s in map(''.join, itertools.product(string.ascii_lowercase, repeat=length-len(base)))]

with open('keys.txt', 'w') as file:
    for key in keys:
        file.write(key + '\n')
