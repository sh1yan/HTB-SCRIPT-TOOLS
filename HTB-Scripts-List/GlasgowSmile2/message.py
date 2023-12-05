#!/usr/bin/python3
with open("new.txt") as file:
    for line in file:
        line = line.strip()
        rest = int(line[:len(line)-1])
        if line[-1] == "F":
            rest -= 2154
        if line[-1] == "A":
            rest -= 2190
        print(chr(rest))
