#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<cs50.h>

int algocyph(char plain, int k, int x);

int main(int argc, string argv[])
{
    if(argc!=2)
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }
    else
    {
        int k = atoi(argv[1]);
        printf("plaintext: ");
        string plain = get_string();
        char cypher[50];
        for(int i=0; i<strlen(plain); i++)
        {
            //check whether is an alphabet
            if(isalpha(plain[i]))
            {
                int req;
                //checking whether upper or lower
                if(isupper(plain[i]))
                    req = algocyph(plain[i],k,65);              
                else
                    req = algocyph(plain[i],k,97);   
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


int algocyph(char plain, int k, int x)
{
    int req;
    req = plain - x;         
    req = (req+k)%26;            
    req+= x;
    return req;
}