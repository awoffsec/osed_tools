## Current Scripts

- **find_ppr.wds**
  - You can copy use this script in WinDbg to find a list of POP POP RET instructions in a module. You will need to replace the `10000000 10226000` values with the addresses of the module, which you can get with `lm m module_name`.
- **findgoodaddress.py**
  - You can add bad bytes to the `badchars` variable. Then, you run the script and paste in an output of addresses (typically using something like a POP POP RET finder). It will output addresses that don't contain any of the bad bytes.
- **findreplacedbytes.py**
  - You run the script and paste in a list of byte output from WinDbg. It will find any replaced bytes and return them back, it will skip any bytes that are missing.
- **gethashfromstring.py**
  - You run this with a function name as the next argument and it will return a quick hash of the function name to find in a PIC shellcode: `python3 gethashfromstring.py CreateProcessA`
- **getnumbytes.py**
  - You run the script and paste in a list of byte output from WinDbg. It will return the number of bytes in the byte array.
