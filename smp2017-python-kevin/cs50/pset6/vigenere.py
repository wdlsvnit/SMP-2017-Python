import cs50
import sys

if len(sys.argv) != 2:
    print("Invalid arguments")
    exit(1)

if sys.argv[1].isalpha() == False:
    print("Invalid keyword!")
    exit(1)
    
text = cs50.get_string()
translated = []
index = 0
length = len(sys.argv[1])

for sym in text:
    if sym.isalpha():
        key = ord(sys.argv[1][index % length].lower()) - 97
        index += 1
        translated.append(caesar(sym, key))
    else:
        translated.append(sym)

print("".join(translated))
exit(0)
    
def caesar(char, key):
    if char.isupper():
        return chr(((ord(char) - 65 + key) % 26) + 65)
    else:
        return chr(((ord(char) - 97 + key) % 26) + 97)
