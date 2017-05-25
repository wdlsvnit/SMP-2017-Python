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
        printf("Usage: ./vigenere str\n");
        return 1;
    }
    else
    {
       
        
        printf("plaintext: ");
        string plain = get_string();
        char cypher[50];
        int Len1=0;
        for(int i=0; i<strlen(plain); i++)
        {
            //check whether is an alphabet
            if(isalpha(plain[i]))
            {
                
                if(Len1==strlen(argv[1]))                    //this is so that argv starts over from first character
                    Len1=0;
                int req;
                char* k=&argv[1][Len1];
                if(isupper(plain[i]))
                {
                    req = algocyph(plain[i],*k-65,65);
                }
                else
                {
                    req = algocyph(plain[i],*k-97,97);   
                }    
                plain[i]=(char)req;                //typecasting
                cypher[i]=plain[i];
                Len1++;
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