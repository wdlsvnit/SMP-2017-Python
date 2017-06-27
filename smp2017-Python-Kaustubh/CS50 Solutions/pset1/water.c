#include<stdio.h>
#include<cs50.h>
int main(void)
{
    printf("Enter number of minutes:");
    int min=get_int();
    printf("The number of bottles you use is:%d\n",min*12);
}