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
  int i=0,j=0;
  string a = argv[1];
  int len = strlen(a);
  
  for(i=0;i<len;i++)
  {
    if(!(isalpha(a[i])))
    {
    printf("error");
    return 1;
    }
  }
  i=0;
  while(a[i]!='\0')
  {
    a[i]=(char)tolower(a[i]);
    i++;
  }
  printf("plaintext:");
  string b = GetString();
  int no[len];
  for(i=0;i<len;i++)
  {
      no[i]=(int)a[i]-97;
  }
  j=0;
  int flag = 1;
  for(i=0;i<strlen(b);i++)
  {
     
      if(!(((int)b[i]>64 && (int)b[i]<91) || ((int)b[i]>96 && (int)b[i]<123)))
      {
          flag=2;
          continue;
      }
      
      if((int)b[i]>64 && (int)b[i]<91)
      {
        flag=0;
      }
      else
      flag=1;
      
      b[i]=(char)((int)b[i]+no[j]);
      if(!(((int)b[i]>64 && (int)b[i]<91) || ((int)b[i]>96 && (int)b[i]<123)))
      {
        b[i]=(char)((int)b[i]-26);
      }
      if(((int)b[i]>96 && (int)b[i]<123) && flag==0)
      {
        b[i]=(char)((int)b[i]-26);
      } 
      j++;
      if(j>=len)
      {
          j=0;
      }
  }
  printf("ciphertext:%s\n",b);
  return 0;
}