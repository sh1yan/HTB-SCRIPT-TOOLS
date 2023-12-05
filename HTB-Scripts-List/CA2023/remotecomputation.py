#!/usr/bin/python3
from pwn import log, remote
import warnings, re, sys

if len(sys.argv) < 2:
    log.failure(f"Uso: python3 {sys.argv[0]} <host:port>")
    sys.exit(1)

host, port = sys.argv[1].split(":")
shell = remote(host, port)

warnings.simplefilter("ignore")

bar = log.progress("")

shell.sendline(b"1")

for id in range(1, 10):
    data = shell.recvuntil("= ?").decode()
    operation = data[data.find(f"[00{str(id)}]: ") + 7:data.find("= ?")]

    try:
        result = round(eval(operation), 2)
        if -1337.00 <= result <= 1337.00:
            shell.sendline(str(result).encode())
            bar.status(f"\033[0;37mResults:\n[\033[0;34m*\033[0;37m] id:\t\t{id}\n[\033[0;34m*\033[0;37m] operation: {operation}\n[\033[0;32m+\033[0;37m] result:\t{result}")
        else:
            shell.sendline(b"MEM_ERR")
    except ZeroDivisionError:
        shell.sendline(b"DIV0_ERR")
    except SyntaxError:
        shell.sendline(b"SYNTAX_ERR")

for id in range(10, 100):
    data = shell.recvuntil("= ?").decode()
    operation = data[data.find(f"[0{str(id)}]: ") + 7:data.find("= ?")]

    try:
        result = round(eval(operation), 2)
        if -1337.00 <= result <= 1337.00:
            shell.sendline(str(result).encode())
            bar.status(f"\033[0;37mResults:\n[\033[0;34m*\033[0;37m] id:\t\t{id}\n[\033[0;34m*\033[0;37m] operation: {operation}\n[\033[0;32m+\033[0;37m] result:\t{result}")
        else:
            shell.sendline(b"MEM_ERR")
    except ZeroDivisionError:
        shell.sendline(b"DIV0_ERR")
    except SyntaxError:
        shell.sendline(b"SYNTAX_ERR")

for id in range(100, 501):
    data = shell.recvuntil("= ?").decode()
    operation = data[data.find(f"[{str(id)}]: ") + 7:data.find("= ?")]

    try:
        result = round(eval(operation), 2)
        if -1337.00 <= result <= 1337.00:
            shell.sendline(str(result).encode())
            bar.status(f"\033[0;37mResults:\n[\033[0;34m*\033[0;37m] id:\t\t{id}\n[\033[0;34m*\033[0;37m] operation: {operation}\n[\033[0;32m+\033[0;37m] result:\t{result}")
        else:
            shell.sendline(b"MEM_ERR")
    except ZeroDivisionError:
        shell.sendline(b"DIV0_ERR")
    except SyntaxError:
        shell.sendline(b"SYNTAX_ERR")

output = shell.recvall()
match = re.search(b"HTB\{.*\}", output)
bar.success(f"Flag: {match.group(0).decode()}")
