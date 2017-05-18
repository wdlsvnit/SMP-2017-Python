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
bool search(int value, int values[], int n);
void sort(int values[], int n);
bool search(int value, int values[], int n)
{
    // TODO: implement a searching algorithm
    if(n<1)
    {
        return false;
    }
    int i;
    for(i=0;i<n;i++)
    {
        if(values[i]==value)
        return true;
        
    }
    return false;
    
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // TODO: implement a sorting algorithm
    int i,j, temp;
    for(i=0;i<(n-1);i++)
    {
        for(j=1;j<n;j++)
        {
            if (values[i]>values[j])
            {
                temp=values[i];
                values[i]=values[j];
                values[j]=temp;
            }
        }
    }
    return;
}
