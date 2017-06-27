import sys

if len(sys.argv) is not 2 :
    print('Usage: Python3 caesar.py k')
    exit(1)
cyp=[]
j=int(sys.argv[1])

pText=input('plain text: ')

for i in range(len(pText)):

    if pText[i].islower():
        n=ord(pText[i])-ord('a')+1
        n=(n+j)%26
        n=n-1+ord('a')
        cyp.append(chr(n))

    elif  pText[i].isupper():
        n=ord(pText[i])-ord('A')+1
        n=(n+j)%26
        n=n-1+ord('A')
        cyp.append(chr(n))

    else:
        cyp.append(pText[i])

print('Cipher text: ',end='')
for i in range(len(cyp)):
    print(cyp[i],end='')

print('')
