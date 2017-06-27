/**
 * Resizes a BMP piece by piece, just because.
 */

#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize n infile outfile\n");
        return 1;
    }

    int n=atoi(argv[1]); // resize factor

    if(n<0)
    {
      fprintf(stderr, "Usage: ./resize n infile outfile, n should be positive\n");
      return 1;
    }

    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf,nbf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);
    nbf = bf;

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi,nbi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);
    nbi=bi;

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // determine padding for scanlines
    int old_padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    nbi.biWidth*=n;
    nbi.biHeight*=n;

    int padding = (4 - (nbi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    nbi.biSizeImage=nbi.biWidth*abs(nbi.biHeight)*sizeof(RGBTRIPLE) + nbi.biWidth*padding;
    nbf.bfSize = nbi.biSizeImage + 54;

    // write outfile's BITMAPFILEHEADER
    fwrite(&nbf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&nbi, sizeof(BITMAPINFOHEADER), 1, outptr);





    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        for(int a=0; a< n; a++)
        {
        // iterate over pixels in scanline
          for (int j = 0; j < bi.biWidth; j++)
          {
              // temporary storage
              RGBTRIPLE triple;

              // read RGB triple from infile
              fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
              for(int b=0;b<n;b++)
              {
                // write RGB triple to outfile
                fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
              }

            }

          // skip over padding, if any
          fseek(inptr, old_padding, SEEK_CUR);

          // then add it back (to demonstrate how)
          for (int k = 0; k < padding; k++)
          {
              fputc(0x00, outptr);
          }

          if(a<n-1)
           fseek(inptr,-((bi.biWidth*3) + old_padding), SEEK_CUR);
     }
  }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
