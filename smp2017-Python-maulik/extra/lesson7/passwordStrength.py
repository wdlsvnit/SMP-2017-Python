#! python3
#To detect strength of password using regex

import re

def upperCheck(password):
    upperRegex=re.compile(r"[A-Z]+")
    if upperRegex.search(password) == None:
        return False
    return True

def lowerCheck(password):
    lowerRegex=re.compile(r"[a-z]+")
    if lowerRegex.search(password) == None:
        return False
    return True

def digitCheck(password):
    digitRegex=re.compile(r"\d+")
    if digitRegex.search(password) == None:
        return False
    return True
    
def passwordStrength(password):
    if len(password) < 8:
        print("Password must be minimum 8 characters long")
        return False
    
    elif upperCheck(password) == False:
        print("Password must contain atleast one Uppercase character")
        return False
    
    elif lowerCheck(password) == False:
        print("Password must contain atleast one Lowercase character")
        return False
    
    elif digitCheck(password) == False:
        print("Password must contain atleast one integer")
        return False
    
    else:
        return True
    
def main():
    password=input("Enter passsword to make sure it is strong : ")
    print("")
    strong=passwordStrength(password)
    if strong == True:
        print("Strength : Good")

        
if __name__=="__main__":
    main()
    
