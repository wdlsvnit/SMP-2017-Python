#include<stdio.h>
#include<cs50.h>

int main()
{
    printf("Enter Height");
    int a = GetInt();
    int f=0;
    int b=0;
    while(a>23 || a<0)
    {
        printf("Enter Height");
        a = GetInt();
    }
    for(f=1;f<=a;f++)
    {
        b=a-f;
        for(int z=0;z<b;z++)
        {
            printf(" ");
        }
        for(int i=0;i<f;i++)
        {
            printf("#");
        }
        printf("  ");
        for(int i=0;i<f;i++)
        {
            printf("#");
        }
        printf("\n"); 
    }

}
