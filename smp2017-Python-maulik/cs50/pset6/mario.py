height=-1
while not(height <=23 and height >=0) :
        print('Height :',end='')
        height=int(input())

space=height-1

for i in range(height):
    print(' '*space,end='')
    print('#'*(i+1),end='')
    print('  ',end='')
    print('#'*(i+1))
    i+=1;
    space-=1
