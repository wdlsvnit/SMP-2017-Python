#include<stdio.h>
#include<cs50.h>
int main(void)
{
    int n,ct;
    float amt;
    printf("O hai!");
    do
    {
    printf("How much change is owed?\n");
    amt=get_float();
    }
    while(amt<0);
    n=amt*100;
    ct=n/25;
    n=n%25;
    ct=ct+n/10;
    n=n%10;
    ct=ct+n/5;
    n=n%5;
    ct=ct+n;
    printf("%d\n",ct);
}
