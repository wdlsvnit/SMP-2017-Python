#include<stdio.h>
#include<cs50.h>
#include<ctype.h>
#include<string.h>
int main(void)
{
    int k=0;
    string n=get_string();
    while(n[k] == 32)
    {
        k++;
    }
    printf("%c",toupper(n[k]));
    for(int i=k,l=strlen(n);i<l;i++)
    {
        if(n[i]==32)
        {
        int j=i;
        while(n[j] == 32)
        {
            j++;
        }
        printf("%c",toupper(n[j]));
        i=j-1;
        }
    }
    printf("\n");
    
}