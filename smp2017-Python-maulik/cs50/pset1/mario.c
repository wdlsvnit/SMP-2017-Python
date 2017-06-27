#include <stdio.h>

int main(void)
{
	int i,j,ht,space;

	printf("Enter height of double pyramid :");
	scanf("%d",&ht);

	space=ht;

	for(i=0;i<ht;i++,space--)
	{
		for(j=1;j<space;j++)
			printf(" ");
		for(j=0;j<=i;j++)
			printf("#");
		printf("  ");
		for(j=0;j<=i;j++)
			printf("#");
		printf("\n");
	}

	return 0;
}