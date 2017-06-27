#include<stdio.h>
#include<cs50.h>
#include<stdarg.h>
#include<string.h>
#include<stdlib.h>
int main(int argc,char *argv[])
{
    if(argc!=2)
    {
        printf("Usage: ./vigenere k\n");
        return 1;
    }
    int l=strlen(argv[1]);
     for(int r=0;r<l;r++)
    {
        if('A'>argv[1][r] || ('Z'<argv[1][r] && 'a'>argv[1][r]) || 'z'<argv[1][r])
        {
            printf("Usage: ./vigenere k\n");
            return 1;
        }
    }
   
    
    int k,j;
    
    printf("plaintext:");
    string s=get_string();
    printf("ciphertext:");
    for(int i=0,m=0,n=strlen(s);i<n;i++,m++)
    {
       j=m%l;//by taking % value of j never exceeds the number of characters in argv[1]
       if(argv[1][j]>='A' && argv[1][j]<='Z')
       {
           k=argv[1][j]-65;
       }
       else
       {
            k=argv[1][j]-97;
       }
       if(s[i]>='A' && s[i]<='Z')
       {
            if(s[i]+k>90)
            {
                printf("%c",s[i]+k-26);
            }
            else
            {
                printf("%c",s[i]+k);
            }
       }
       else if(s[i]>='a' && s[i]<='z')
       {
           if(s[i]+k>122)
           {
               printf("%c",s[i]+k-26);
           }
           else
           {
               printf("%c",s[i]+k);
           }
       }
       else
       {
            printf("%c",s[i]);
            m--;//m is incremented only if this case is false
       }
    }
    printf("\n");
}