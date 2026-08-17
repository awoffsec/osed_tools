#!/usr/bin/python
import re

print("Paste your hex dump below (press ENTER on an empty line when done):")

lines = []
while True:
    try:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    except EOFError:
        break

data = "\n".join(lines)

sections = re.findall(r"^(?:[0-9a-fA-F]{8}\s+)?((?:[0-9a-fA-F]{2}[ -]?)+)", data, re.MULTILINE)
byte_list = re.findall(r"[0-9a-fA-F]{2}", " ".join(sections))

print(f"Total Byte Count: {len(byte_list)}")
