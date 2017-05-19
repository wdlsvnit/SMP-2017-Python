#include <stdio.h>

int main(void)
{
	unsigned long long int ccn,smpl;
	int cnt=1,sum=0,i;

	printf("Enter your credit card number :");
	scanf("%lld",&ccn);

	smpl=ccn;

	while(smpl>0)
	{
		i=smpl%10;

		if(cnt%2!=0)
			sum+=(2*i);
		else
			sum+=i;
		cnt++;
		smpl=smpl/10;
	}

	if(sum%10)
		printf("\nYour Credit card is Legit.\n");
	else
		printf("You cheated.Invalid credit card!\n");
}