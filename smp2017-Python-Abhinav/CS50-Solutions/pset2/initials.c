#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>
int main()
{
    string name = GetString();
    if(name[0]!=' ')
    {
        if((isupper(name[0])))
        printf("%c",name[0]);
        else
        printf("%c", toupper(name[0]));
    }    
    for(int i=0; i<strlen(name);i++)
    {
        if(name[i]==' ' && (name[i+1]!=' ' && name[i+1]!='\0'))
        {
            if(isupper(name[i+1]))
            printf("%c", name[i+1]);
            else
            printf("%c", toupper(name[i+1]));
        }
    }
    printf("\n");
}