#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>

int main(void)
{
    string first=get_string();
    char second[50];
    second[0]=first[0];
    int counter = 1;
    for(int i=1; i<strlen(first); i++)
    {
        if(first[i]==' ')
        {
            second[counter]=first[i+1];
            counter++;
        }
    }
    for(int i=0; i<counter; i++)
        printf("%c",toupper(second[i]));
    printf("\n");
}