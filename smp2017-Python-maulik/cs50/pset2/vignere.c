#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc,char **argv)
{
    char str[100],cry[100];
    int i,j,n,len,key[100];
    
    if(argc<2)
    {
        printf("Usage: ./vigenere k");
        return 1;
    }
    for(j=0;argv[1][j]!='\0';j++)
    {
        if(!isalpha(argv[1][j]))
        {
            printf("Usage: ./vigenere ka");
            return 1;
        }
        
    }
    for(j=0;argv[1][j]!='\0';j++) 
    {
        if(islower(str[i]))
            key[j]=(argv[1][j] - 'a');
        else if(isupper(str[i]))
            key[j]=(argv[1][j] - 'A');
    }
    len=j;
    
    printf("plain text:");
    gets(str);
    
    i=0;j=0;
    while(str[i]!='\0')
    {
        if(islower(str[i]))
        {
            n=str[i]-'a'; //1 for a , 26 for z
            n=(n+key[j])%26;  // Algorithm
            n=n+'a'; //98 for a
            cry[i]=n;
            j++;
        }
        else if(isupper(str[i]))
        {
            n=str[i]-'A'; //1 for A , 26 for Z
            n=(n+key[j])%26;  // Algorithm
            n=n+'A'; //65 for A
            cry[i]=n;
            j++;
        }
        else
            cry[i]=str[i];
        i++;
        
        if(j==len)
            j=0; //Cycle
    }
    cry[i]='\0';
    
    printf("\ncipher text:%s\n",cry);   
}