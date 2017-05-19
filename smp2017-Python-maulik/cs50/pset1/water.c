#include <stdio.h>
#include <cs50.h>

int main(void)
{
	int min;
	
	printf("How much time do you spend in shower? Enter in minutes :");
	scanf("%d",&min);
	
	printf("\nEquivalent number of bottles are %d\n",min*12);
	return 0;
}