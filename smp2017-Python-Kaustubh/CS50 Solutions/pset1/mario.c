#include<stdio.h>
#include<cs50.h>
int main(void)
{
    int h=0;
    do
    {
      printf("Height :");
      h=get_int();
    }
    while(h<0 || h>23);
    for(int i=1;i<=h;i++)
    {
        for(int r=1;r<=(h-i);r++) 
        {
            printf(" ");
        }
        for(int r=1;r<=i;r++)
        {
            printf("#");
        }
        printf("  ");
        for(int r=1;r<=i;r++)
        {
            printf("#");
        }
        printf("\n");
    }
}