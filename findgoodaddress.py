#!/usr/bin/python

print("Paste your addresses below (press ENTER on an empty line when done):")

lines = []
while True:
    try:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    except EOFError:
        break

badchars = r'\x00\x0A\x0D' # add all bad bytes here

badbytes = [
    int(badchars[i + 2 : i + 4], 16)
    for i in range(0, len(badchars), 4)
]

print('\n\n===================================================================')
print('THE FOLLOWING ADDRESSES ARE CLEAN:\n\n')

# Changed `data` to `lines` here
for line in lines:
    line = line.strip()
    if not line:
        continue

    try:
        address = int(line, 16)
    except ValueError:
        print(f"Skipping non-hex input: {line}")
        continue

    # Use 4 bytes for 32-bit architecture (or change to 8 for 64-bit)
    addrbytes = address.to_bytes(4, byteorder='big')

    if not any(b in badbytes for b in addrbytes):
        print(f"0x{address:08x}")
