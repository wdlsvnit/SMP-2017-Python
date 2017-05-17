#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>
int main(int argc,char* argv[])
{
  
  if(argc!=2)
  {
    printf("%d", argc);
    return 1;
  }
  int i=0,a=atoi(argv[1]);
  if(a<0)
  {
      printf("%d",a);
      return 1;
  }
  while(a>26)
  {
      a-=26;
  }
  printf("plaintext:");
  string b = GetString();
  int len=strlen(b);
  int flag=2;
  for(i=0;i<len;i++)
  {
    if(!(((int)b[i]>64 && (int)b[i]<91) || ((int)b[i]>96 && (int)b[i]<123)))
      {
          continue;
      }
    if((int)b[i]>64 && (int)b[i]<91)
      {
        flag=0;
      }
      else
      flag=1;
      
    b[i]=(char)((int)b[i]+a); 
    
    if(!(((int)b[i]>64 && (int)b[i]<91) || ((int)b[i]>96 && (int)b[i]<123)))
      {
        b[i]=(char)((int)b[i]-26);
      }
      if(((int)b[i]>96 && (int)b[i]<123) && flag==0)
      {
        b[i]=(char)((int)b[i]-26);
      }
  }
  printf("ciphertext:%s\n",b);
  return 0;
}