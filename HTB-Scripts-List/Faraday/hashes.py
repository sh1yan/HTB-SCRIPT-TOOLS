#!/usr/bin/python3
from werkzeug.security import check_password_hash

hashes = open('hashes', 'r')
for hashl in hashes:
    hash = hashl.split(":")[1].strip()
    user = hashl.split(":")[-2].strip()

    with open('/usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt', 'r', errors='ignore') as file:
        for line in file:
            password = line.strip()
            if check_password_hash(hash, password):
                print(f"[\033[1;32m+\033[1;37m] Credencial valida: {user}:{password}")
