/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>
#include<string.h>
#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    // TODO: implement a searching algorithm
    static int max;
    static int min=0;
    static bool a;
    int middle;
    max=n-1;
    if(max>=min)
    {
        middle=(max+min)/2;
        if(value>values[middle])
        {
            min=middle + 1;
            a=search(value,values,max+1);
        }
        else if(value<values[middle])
        {
            a=search(value,values,middle);
        }
        else if(value==values[middle])
        {
            max=min=0;
            return true;
        }
    }
    else
    {
    max=min=0;
    }
    if(a)
    {
        return true;
    }
    return false;
}
/**
 * Sorts array of n values.
 */void mod_count_sort(int arr[], int size, int divi)
{
    int end=9,start=0;
    int no[end-start+1];
    int op[size];
    memset(no, 0, sizeof no);
    memset(op, 0, sizeof op);
    for(int i=0;i<size;i++)
    {
        no[(arr[i]/divi)%10-start]++;//0010410000
    }
    for(int i=0;i<end-start;i++)
    {
        no[i+1]+=no[i];//0011456666
    }
    for(int i=size-1;i>=0;i--)
    {
        op[no[(arr[i]/divi)%10-start]-1]=arr[i];
        no[(arr[i]/divi)%10-start]--;
    }
   
    for(int i=0;i<size;i++)
    {
        arr[i]=op[i];
    }
    
}

int max(int arr[], int size)
{
    int temp=arr[0];
    for(int i=1;i<size;i++)
    {
        if(temp<arr[i])
        temp=arr[i];
    }
    return temp;
}
/**
 * Sorts array of n values.
 */
void sort(int arr[], int size)
{
    // TODO: implement a sorting algorithm RADIX SORT
   int a = max(arr,size);
   int divi=1;
   do
   {
        mod_count_sort(arr,size,divi);
        divi*=10;
   }while(a/=10);

 
    return;
}
