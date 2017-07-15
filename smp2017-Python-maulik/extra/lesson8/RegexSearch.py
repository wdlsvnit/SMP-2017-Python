#! python3
#RegexSearch.py - opens all files in folder and searches for expression

import re,os,sys

expression = input("Enter expression :")
expRegex = re.compile(expression)

folder=input("Enter path of folder :")
os.chdir(folder)


for sub in os.listdir("."):
    
    if sub.endswith(".txt")
        file=open("./" + sub )
        fileContent=file.readlines()
        
        for lines in fileContent:
            found=expRegex.search(lines)
            if found == None:
                continue
            print("IN "+ folder +"/"+ sub +" :" + lines)
        file.close()
                
            
        


