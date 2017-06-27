ccn=int(input('Enter your credit card number : '))

smpl=ccn
cnt=1
s=0

while smpl > 0 :
    i=smpl%10

    if(cnt%2==0):
        n=2*i
        while n > 0:
            s+=n%10
            n=n//10
    else:
        s+=i

    cnt+=1;
    smpl=smpl//10


if(s%10==0) :
    print('Your Credit card is legit.')
else :
    print('You cheated.Invlaid credit card!')
