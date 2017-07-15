import cs50

print("Enter no: not bigger than 23: ", end="")
n=cs50.get_int()
        
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(" ", end="")
    for k in range(1,i+1):
        print("#", end="")
    print("  ",end="")
    for l in range(1,i+1):
        print("#",end="")
    print("\n",end="")