#include<stdio.h>
#include<cs50.h>
#include<stdarg.h>
#include<string.h>
int main(int argc,char *argv[])
{
    if(argc!=2)
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }
    int k=atoi(argv[1]);
    k=k%26;
    printf("plaintext:");
    string s=get_string();
    printf("ciphertext:");
    for(int i=0,n=strlen(s);i<n;i++)
    {
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
            printf("%c",s[i]);
        
    }
    printf("\n");
}