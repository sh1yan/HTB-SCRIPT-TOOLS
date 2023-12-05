#!/usr/bin/python3

t2 = "477b7a6177527d77557a7d727f32323213"
t2 = bytes.fromhex(t2)

key = 19

result = bytes([i ^ key for i in t2])

print(result.decode())
