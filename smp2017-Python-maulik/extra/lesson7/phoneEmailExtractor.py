#! python3
#To extract phone numbers and email address form copied text

import pyperclip,re

phoneRegex=re.compile(r'''(
        (\d{4}|\(\d{4}\))?       #area code
        (\s|-|\.)                #separator
        (\d{3})                  #first 3 digits
        (\s|-|\.)                #separator
        (\d{4})                  #last 4 digits
        )''',re.VERBOSE)

emailRegex=re.compile(r'''(\
        [a-zA-Z0-9._%+-]+        #username
        @                        
        [a-zA-Z0-9.-]+           #domain
        (\.[a-zA-Z]{2,4})        #dot-something
        )''',re.VERBOSE)

text=str(pyperclip.paste())

matches=[]

for groups in phoneRegex.findall(text):
    pNum="-".join([groups[1],groups[3],groups[5]])
    matches.append(pNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print("\n".join(matches))

else:
    print("No phone number or email address found.")
