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
      int high=n-1,low=0,mid;
    while(high>=low)
    {
        mid=(low+high)/2;
       /*
        if(n%2==0 && i==0)
        {
            mid--;
        }
        */
        if(values[mid]==value)
        {
            return true;
        }
       else if(values[mid]>value)
        {
            high=mid-1;
        }
        else if(values[mid]<value)
        {
            low=mid+1;
        }
        
    }
  

    return false;
} 

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // TODO: implement an O(n^2) sorting algorithm
    int i,j,t;
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-1;j++)
        {
            if(values[j]>values[j+1])
            {
                t=values[j+1];
                values[j+1]=values[j];
                values[j]=t;
            }
        }
    }
    return;
}
