#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <cs50.h>
int main(int argc, string argv[])
{
  if(argc != 2)
  {
      printf("Incorrect input");
      return 1;
  }
  int k,i,j[1000];
  char b[100];
  k=atoi(argv[1]);
  printf("Plaintext:");
  string a = get_string();
  for(i=0; i<=strlen(a);i++)
  {
  	if(a[i]>='A'&& a[i]<='Z')
	{
		j[i]=(a[i]+k-64)%26;
                if(j[i]==0)
		{
			j[i]=26;
		}
		b[i]=(char)(j[i]+64);
	}
  	else if(a[i]>='a'&& a[i]<='z')
  	{
  	j[i]=(a[i]+k-96)%26;
		if(j[i]==0)
		{
			j[i]=26;
		}


  		b[i]=(char)(j[i] + 96);
	}
	else
	b[i]=a[i];
  }
  printf("\n");
  printf("Ciphertext:");
  puts(b);
  return 0;
}
