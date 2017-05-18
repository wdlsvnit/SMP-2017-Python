#include <stdio.h>

#include <string.h>

#include <math.h>

#include <stdlib.h>

#include <cs50.h>

#include <ctype.h>

int main(int argc, char *argv[])

{

  int i, j[1000],p=0;

  char  b[1000],c[100];

  string a;
  for(i=0; argv[1][i]!='\0';i++)

  {

  	argv[1][i]=toupper(argv[1][i]);

  }

  
  for(i=0; argv[1][i]!='\0';i++)

  {
  	c[i]=argv[1][i];

  }

  
  if(argc != 2)

  {

      printf("Incorrect input");

      return 1;

  }

  for( i=0;i<strlen(c);i++)

  {

    if(c[i]<'A'|| c[i]>'Z')

     {
    
      printf("Incorrect input");

          return 1;

     }

  }

  
printf("Plaintext:");

  a = get_string();

  for(i=0; i<=strlen(a);i++)

  {

  	if(a[i]>='A'&& a[i]<='Z')

	{

		j[i]=(a[i]+c[p]-64-65)%26;

		if(j[i]==0)

		{

			j[i]=26;

		}

		b[i]=(char)(j[i]+64);

		p=(p+1)%strlen(c);

	}

  	else if(a[i]>='a'&& a[i]<='z')

  	{

  		j[i]=(a[i]+c[p]-96-65)%26;

  		if(j[i]==0)

		{

			j[i]=26;

		}

  		b[i]=(char)(j[i] + 96);

  		p=(p+1)%strlen(c);

	}

	else

	{

		b[i]=a[i];
	}
  }

  printf("\n");

  printf("Ciphertext:");

  puts(b);

  return 0;

}