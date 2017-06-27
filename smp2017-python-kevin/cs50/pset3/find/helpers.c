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
    int left=0,right=n-1,middle;
    while(left<=right)
    {
        middle=(left+right)/2;
        if(values[middle]==value)
            return true;
        else if(value>values[middle])
            left=middle+1;
        else if(value<values[middle])
            right=middle-1;
        
    }
    return false;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    int swapcount=-1,t;
    while(swapcount!=0)
    {
        swapcount=0;
        for(int i=0; i<n ; i++)
        {
            for(int j=0; j<n-i-1; j++)
            {
                if(values[j]>values[j+1])
                {
                    t=values[j];
                    values[j]=values[j+1];
                    values[j+1]=t;
                    swapcount++;
                }
            }
        }
    }
}
