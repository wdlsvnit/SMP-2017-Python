#list to string

def listToString(spam):
    string=""
    for i in range(len(spam)-1):
        string += str(spam[i]) + ", "

    i+=1
    string += "and " + str(spam[i])

    return string

def main():
    spam=[]
    x=input("Enter list value (Enter ^ to stop) : ")
    
    while x!="^":
        spam.append(x)
        x=input("Enter list value (Enter ^ to stop) : ")
        
    spam=listToString(spam)

    print("Your list items :")
    print(spam)

if __name__=="__main__":
    main()

        
        
        
