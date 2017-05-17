#include<stdio.h>
main ()
{
	int q,d,n,x;
	float c;
	printf("O hai! How much change is owed?\n");
	scanf("%f", &c);
	while(c<0)
	{
		printf("Enter amount again\n");
		scanf("%f", &c);
	}
	x=c*100;
	q=x/25;
	x=x%25;
	d=x/10;
	x=x%10;
	n=x/5;
	x=x%5;
	printf("Number of coins required is %d", x+n+d+q);
}
