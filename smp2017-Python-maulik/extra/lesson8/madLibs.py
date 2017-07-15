#! python3
#To read from text files and let user add their own text anywhere the word-
#ADJECTIVE, NOUN, ADVERB or VERB

import re,sys

try:
    fileAddress=input("Enter path of file :")
    file = open(fileAddress)
except FileNotFoundError:
    print("Please enter an existing path.")
    sys.exit(1)
fileContent = file.read()
file.close()
print(fileContent) 

findRegex = re.compile(r'''ADJECTIVE|NOUN|ADVERB|VERB''')
fo=findRegex.search(fileContent)

while(fo != None):
    print("Enter " + fo.group().lower() + ":")
    replacement=input()
    
    replaceRegex=re.compile(fo.group())
    fileContent=replaceRegex.sub(replacement,fileContent,count=1)
    
    fo=findRegex.search(fileContent)

newFileAddress=input("Enter path of new file:")
print("")

file=open(newFileAddress,"w")
file.write(fileContent)
file.close()

print("Following text written to new file at " + newFileAddress)
print(fileContent)
