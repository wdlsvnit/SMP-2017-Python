#! python3
# regex version of strip()

#If no other arguments are passed other than the string to
#strip, then whitespace characters will be removed from the beginning and
#end of the string. Otherwise, the characters speci ed in the second argu-
#ment to the function will be removed from the string.

import re

def myStrip(string,arg):
    if arg=="":
        
        stripRegex=re.compile(r"^\s+ | \s+$")        
        newString=stripRegex.sub("",string)
    else :
        stripRegex=re.compile(r"(\s)?"+arg+r"(\s)?",re.I)
        newString=stripRegex.sub(" ",string)

    return newString

def main():
    string=input("Input your string: ")
    stripElement=input("Input string to strip: ")

    modifiedString=myStrip(string,stripElement)

    print(modifiedString)

if __name__=="__main__":
    main()
