#include<cs50.h>
#include<stdio.h>

int main(void)
{

    int ht;
    do
    {
        printf("Height: ");
        ht = get_int();
    }
    while(ht<0 || ht>23);
    for(int i=0; i<ht; i++)
    {
        for(int j=0; j<(ht+1); j++)
        {
            if((i+j)>=(ht-1))
                printf("#");
            else
                printf(" ");
            }
        printf("\n");
    }
}