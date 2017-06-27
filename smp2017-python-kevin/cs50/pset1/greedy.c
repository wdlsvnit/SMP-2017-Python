#include<stdio.h>
#include<math.h>
#include<cs50.h>

int main(void)
{
    float m;
    do
    {
        printf("How much change is owed?\n");
        m = get_float();
    }
    while(m<0);
    m = roundf(m*100);                                  //for approximation because of float errors
    int coin=0;
    
    while(m!=0)
    {
        if(m>=25)
            m-=25;
        else if(m>=10)
            m-=10;
        else if(m>=5)
            m-=5;
        else if(m>=1)
            m-=1;
        coin++;
        
    }
    printf("%i\n",coin);
}