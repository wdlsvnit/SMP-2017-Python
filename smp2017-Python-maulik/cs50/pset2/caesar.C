#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc,char **argv)
{
	char str[100],cry[100];
	int i,j,n;
	if(argc!=2)
	{
		printf("Usage: ./caesar k\n");
		return 1;
	}
	//string to int
	j=atoi(argv[1]);

	printf("plain text: ");
	gets(str);

		i=0;
	    while(str[i]!='\0')
	    {
			if(islower(str[i]))
			{
				n=str[i]-'a'+1; //1 for a , 26 for z
				n=(n+j)%26;  // Algorithm
				n=n-1+'a'; //98 for a
				cry[i]=n;
			}
			else if(isupper(str[i]))
			{
				n=str[i]-'A'+1; //1 for A , 26 for Z
				n=(n+j)%26;  // Algorithm
				n=n-1+'A'; //65 for A
				cry[i]=n;
			}
			else
				cry[i]=str[i];
			i++;
	    }
	    cry[i]='\0';

	    printf("\ncipher text: %s\n",cry);
	    return 0;

}
