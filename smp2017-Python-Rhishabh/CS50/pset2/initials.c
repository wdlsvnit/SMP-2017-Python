#include<stdio.h>
#include<string.h>
int main ()
{
	char a[20], b[10];
	int i,j=1;
	printf("Enter your name:\n");
	gets(a);
	b[0]=a[0];
	for(i=0;a[i]!='\0';i++)
	{
		if (a[i] == ' ')
		{
			b[j]=a[i+1];
			j++;
		}
	
	}
	b[j]= '\n';
	puts(b);
	
}