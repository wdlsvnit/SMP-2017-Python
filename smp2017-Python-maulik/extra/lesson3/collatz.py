#Collatz sequence
def collatz(number):
    if number%2 == 0:
        number=number//2
    else:
        number=3*number + 1
        
    print(number)
    return number

def main():
    try:
        x=input("Enter an integer: ")
    
        while int(x) != 1 :
            x=collatz(int(x))

    except ValueError:
        print("Please enter an integer value.")        

if __name__=="__main__":
    main()
