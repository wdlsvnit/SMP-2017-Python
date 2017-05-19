#include <stdio.h>
#include <string.h>

int main()
{
	char name[100],sup[100];
	int i=0;

	printf("Enter your full name :");
	gets(name);

	while(name[i]!='\0')
	{
		if(name[i]>='a' && name[i]<='z')
			sup[i]=name[i] + 'A' - 'a';
		else
			sup[i]=name[i];
		i++;
	}
	sup[i]='\0';

	printf("\nYour name in caps :%s\n",sup);
	printf("\nInitials : ");
	for(i=0;sup[i]!='\0';)
	{
		while(sup[i]==' ')
			i++;
		if(sup[i]!='\0')
		{
			printf("%c",sup[i]);
			while(sup[i]!='\0' && sup[i]!=' ')
				i++;
		}
		if(sup[i]!='\0')
				i++;
 	}   
 	printf("\n");
 	return 0;

}