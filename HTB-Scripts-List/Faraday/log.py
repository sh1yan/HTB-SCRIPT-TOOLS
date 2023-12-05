#!/usr/bin/python3
import re, urllib.parse

with open("/var/log/apache2/access.log") as file:
    for line in file:
        line = urllib.parse.unquote(line)
        if not "update.php" in line:
            continue
        regex = re.search("\)\)!=(\d+)", line)
        if regex:
            decimal = int(regex.group(1))
            print(chr(decimal), end="")
