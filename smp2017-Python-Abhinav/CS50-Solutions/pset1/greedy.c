#include <stdio.h>
#include <cs50.h>
#include <math.h>
int main()
{
    int tf=0;
    int t=0;
    int five=0;
    int one=0;
    printf("O hai! How much change is owed?");
    float f = GetFloat();
    while(f<0)
    {
        printf("O hai! How much change is owed?");
        f = GetFloat();
    }
    int a = roundf(f * 100);
    tf=a/25;
    a=a%25;
    t=a/10;
    a=a%10;
    five=a/5;
    a=a%5;
    one=a;
    printf("%d\n", tf+t+five+one);
}