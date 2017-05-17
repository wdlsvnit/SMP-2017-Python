#include<stdio.h>
int main ()
{
	int i,j,k,n;
	printf("Enter height:\n");
	scanf("%d", &n);
	while(n>23 || n<0)
	{
		printf("Enter height:\n");
		scanf("%d", &n);
	}
	for(i=1;i<=n;i++)
	{
		for(j=0;j<(n-i);j++)
		printf(" ");
		for(k=0;k<=i;k++)
		printf("#");
		printf("\n");
	}
}
