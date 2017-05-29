#include <stdio.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc,char * argv[])
{
  if(argc!=2)
  {
    fprintf(stderr,"Usage : ./recover filename");
    return 1;
  }

  FILE *ip;
  FILE *op=NULL;
  ip=fopen(argv[1],"r");

  if(ip==NULL)
  {
    fprintf(stderr,"Could not open file.");
    return 2;
  }

  int count=0;

  BYTE buff[512];

  while(fread(buff,512,1,ip))
  {
    if(buff[0]==0xff && buff[1]==0xd8 && buff[2]==0xff)
    {
      int flag=0;
      for(int n=0xe0;n<=0xef;n++)
      {
        if(buff[3]==n)
        {
          flag=1;
          break;
        }
      }
      if(flag == 1)
      {
        if(op!=NULL)
          fclose(op);

        char name[20];
        sprintf(name,"%03d.jpeg",count);

        op=fopen(name,"w");

        count ++;
      }
    }

    if(op!=NULL)
      fwrite(buff,512,1,op);

    if(feof(ip)!=0)
      break;

  }

  if(op!=NULL)
    fclose(op);

  fclose(ip);

  return 0;

}
