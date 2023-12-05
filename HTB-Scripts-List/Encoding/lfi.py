#!/usr/bin/python3
import requests, json, sys

if len(sys.argv) < 2:
    print(f"\n\033[1;37m[\033[1;31m-\033[1;37m] Uso: python3 {sys.argv[0]} <file>\n")
    exit(1)

json_data = {"action": "str2hex", "file_url": f"file://{sys.argv[1]}"}

request = requests.post('http://api.haxtables.htb/v3/tools/string/index.php', json=json_data)

json = json.loads(request.text)
string = json["data"]

if string == "":
    print(f"\n\033[1;37m[\033[1;31m-\033[1;37m] El archivo especificado no existe o está vacío\n")
    exit(0)

bytes = bytes.fromhex(string)
file = bytes.decode()

print(file.strip())
