#!/usr/bin/python
import re

def parse_bytes_from_lines(lines):
    bytes_found = []
    
    for line in lines:
        cleaned_line = re.sub(r'^[0-9a-fA-F]{8}\s+', '', line.strip())
        line_code = re.split(r'\s{2,}', cleaned_line)[0]
        sanitized_code = re.sub(r'[^0-9a-fA-F]', ' ', line_code)
        tokens = re.findall(r'\b[0-9a-fA-F]{2}\b', sanitized_code)
        bytes_found.extend([int(b, 16) for b in tokens])

    return bytes_found

def check_replaced_bytes(bytes_found):
    if not bytes_found:
        print("[-] No valid hex bytes found in input.")
        return

    print(f"\n[+] Extracted {len(bytes_found)} total bytes.")

    expected = 0x01
    replacements = []

    for idx, actual in enumerate(bytes_found):
        if actual == expected:
            expected += 1
            continue

        if actual > expected:
            expected = actual + 1
            continue

        replacements.append({
            "index": idx,
            "expected": expected,
            "actual": actual
        })
        expected += 1

    if not replacements:
        print("[+] No replaced bytes detected.")
    else:
        print(f"\n[!] Found {len(replacements)} replaced byte(s):\n")
        print(f"{'Index':<8} | {'Expected':<10} | {'Actual (Replaced)':<18}")
        print("-" * 42)
        for r in replacements:
            print(f"0x{r['index']:04X}   | 0x{r['expected']:02X}       | 0x{r['actual']:02X}")

if __name__ == "__main__":
    print("Paste your hex dump below. Press ENTER on an empty line when done:\n")
    
    dump_lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            dump_lines.append(line)
        except EOFError:
            break

    bytes_found = parse_bytes_from_lines(dump_lines)
    check_replaced_bytes(bytes_found)
