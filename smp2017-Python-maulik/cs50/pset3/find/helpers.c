/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>

#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
   // TODO: implement a searching algorithm
   
    if(n<=0)
        return false;
        
    int first,last,middle,flag=0;
    
    first=0;last=n-1;
    
    while(last>=first) // if(middle==fisrt || middle==last) break;
    {   
        middle=(first+last)/2;

        
        if(value==values[middle])
        {
            flag=1;
            break;
        }

        else if(value>values[middle])
        {
            first=middle+1;
        }
        else if(value<values[middle])
        {
            last=middle-1;
        }
    }
    if(flag==1)
        return true;
    else
        return false;
    
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // TODO: implement a sorting algorithm
    int i,j,tmp;
    
    for(i=0;i<n-1;i++)
        for(j=0;j<n-1-i;j++)
        {
            if(values[j]>values[j+1])
            {
                tmp=values[j];
                values[j]=values[j+1];
                values[j+1]=tmp;
            }
            
        }
}
