#!/usr/bin/python3
import bcrypt

password = "password"
salt = bcrypt.gensalt(rounds=10)
encoded = bcrypt.hashpw(password.encode(),salt)

print(encoded)
