#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<cs50.h>

int checkal(string alpha);
int algocyph(char plain, int k, int x);

int main(int argc, string argv[])
{
    if(argc!=2 || checkal(argv[1]))
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }
    else
    {
       
        
        printf("plaintext: ");
        string plain = get_string();
        char cypher[50];
        for(int i=0; i<strlen(plain); i++)
        {
            //check whether is an alphabet
            if(isalpha(plain[i]))
            {
                int req;
                if(isupper(plain[i]))
                {
                    k-=65;
                    req = algocyph(plain[i],k,65);
                }
                else
                {
                    k-=97;
                    req = algocyph(plain[i],k,65);   
                }    
                plain[i]=(char)req;                //typecasting
                cypher[i]=plain[i];
            }
            else
                cypher[i]=plain[i];
        }
        printf("ciphertext: ");
        for(int i=0; i<strlen(plain); i++)
            printf("%c",cypher[i]);
        printf("\n");
    }
}



int checkal(string alpha)
{
    for(int i=0; i<strlen(alpha); i++)
    {
        if isalpha(alpha[i])
            continue;
        else 
            return 1;
    }
    return 0;
}

int algocyph(char plain, int k, int x)                  //algorithm same as caesar.c
{
    int req;
    req = plain - x;         
    req = (req+k)%26;            
    req+= x;
    return req;
}