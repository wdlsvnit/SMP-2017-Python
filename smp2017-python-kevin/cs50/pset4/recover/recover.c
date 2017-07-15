#include<cs50.h>
#include<stdio.h>

int main(int argc, char *argv[])
{
    if(argc!=2)
    {
        fprintf(stderr,"Usage: ./recover image\n");
        return 1;
    }
    
    char *file = argv[1];
    FILE *ptr = fopen(file,"r");
    
    if(ptr == NULL)
    {
        fprint(stderr,"file not created\n");
        return 2;
    }