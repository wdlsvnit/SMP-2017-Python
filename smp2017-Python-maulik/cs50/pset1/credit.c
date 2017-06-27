#include <stdio.h>

int main(void)
{
	unsigned long long int ccn,smpl;
	int cnt=1,sum=0,i,n;

	printf("Enter your credit card number :");
	scanf("%lld",&ccn);

	smpl=ccn;

	while(smpl>0)
	{
		i=smpl%10;
		n=i;
		if(cnt%2==0)
		{
			n=2*i;
			while(n>0)
			{
				sum+=n%10;
				n=n/10;
			}
		}
		else
		{
			sum+=i;
		}
		cnt++;
		smpl=smpl/10;
	}

	if(sum%10==0)
		printf("\nYour Credit card is Legit.\n");
	else
		printf("\nYou cheated.Invalid credit card!\n");
}
