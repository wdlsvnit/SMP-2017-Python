/**
 * fifteen.c
 *
 * Implements Game of Fifteen (generalized to d x d).
 *
 * Usage: fifteen d
 *
 * whereby the board's dimensions are to be d x d,
 * where d must be in [DIM_MIN,DIM_MAX]
 *
 * Note that usleep is obsolete, but it offers more granularity than
 * sleep and is simpler to use than nanosleep; `man usleep` for more.
 */
 
#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// constants
#define DIM_MIN 3
#define DIM_MAX 9

// board
int board[DIM_MAX][DIM_MAX];

// dimensions
int d;

// prototypes
void clear(void);
void greet(void);
void init(void);
void draw(void);
bool move(int tile);
bool won(void);

int main(int argc, string argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        printf("Usage: fifteen d\n");
        return 1;
    }
   // ensure valid dimensions
    d = atoi(argv[1]);
    if (d < DIM_MIN || d > DIM_MAX)
    {
        printf("Board must be between %i x %i and %i x %i, inclusive.\n",
            DIM_MIN, DIM_MIN, DIM_MAX, DIM_MAX);
        return 2;
    }

    // open log
    FILE *file = fopen("log.txt", "w");
    if (file == NULL)
    {
        return 3;
    }

    // greet user with instructions
    greet();

    // initialize the board
    init();

    // accept moves until game is won
    while (true)
    {
        // clear the screen
        clear();
        

        // draw the current state of the board
        draw();

        // log the current state of the board (for testing)
        for (int i = 0; i < d; i++)
        {
            for (int j = 0; j < d; j++)
            {
                fprintf(file, "%i", board[i][j]);
                if (j < d - 1)
                {
                    fprintf(file, "|");
                }
            }
            fprintf(file, "\n");
        }
        fflush(file);
         printf("Tile to move: ");
        int tile = get_int();
        //to move the tile
       /*
        if(move(tile))
        {
            int b=0;
            b=board[r][c];
            board[r][c]=board[row][col];
            board[row][col]=b;
            printf("%d %d \n",row,col);
        }
        // check for win
       */
        if (won())
        {
            clear(); //clears the screen before drawing the won board
            draw(); //to draw the new board after the game is won
            printf("ftw!\n");
            break;
        }

        // prompt for move
       
        
        // quit if user inputs 0 (for testing)
        if (tile == 0)
        {
            break;
        }

        // log move (for testing)
        fprintf(file, "%i\n", tile);
        fflush(file);

        // move if possible, else report illegality
        
        if (!move(tile))
        {
            printf("\nIllegal move.\n");
            usleep(500000);
        }
        
        // sleep thread for animation's sake
        usleep(500000);
    }
    
    // close log
    fclose(file);

    // success
    return 0;
}
/**
 * Clears screen using ANSI escape sequences.
 */
void clear(void)
{
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}

/**
 * Greets player.
 */
void greet(void)
{
    clear();
    printf("WELCOME TO GAME OF FIFTEEN\n");
    usleep(2000000);
}
/**
 * Initializes the game's board with tiles numbered 1 through d*d - 1
 * (i.e., fills 2D array with values but does not actually print them).  
 */
void init(void)
{
    int i=d*d-1,t;
    for(int j=0;j<d;j++)
    {
        for(int k=0;k<d;k++)
        {
        
        	board[j][k]=i;
           	i--;
        
        
        }
    }
    if(d%2==0)
    {
        t=board[d-1][d-3];
        board[d-1][d-3]=board[d-1][d-2];
        board[d-1][d-2]=t;
    }
    
}
/**
 * Prints the board in its current state.
 */
void draw(void)
{
    for(int j=0;j<d;j++)
    {
        for(int k=0;k<d;k++)
        {
            if(board[j][k]!=0)
            {
                printf("%3d",board[j][k]);
            }
            else
            {
                printf("  _");
            }
        }
        printf("\n \n");
    }
}

/**
 * If tile borders empty space, moves tile and returns true, else
 * returns false. 
 */
bool move(int tile)
{
    int t=9,r,c;
   for(int i=0;i<d;i++)
    {
        for(int j=0;j<d;j++)
        {
            if(board[i][j]==tile)
            {
                r=i;
                c=j;
                break;
            }
        }
    }

    if(board[r-1][c]==0 && r>0)
    {
        t=board[r-1][c];
       board[r-1][c]=board[r][c] ;
       board[r][c]=t;
        return true;
    }
    else if(board[r+1][c]==0 && r<d-1)
    {
        t=board[r+1][c];
        board[r+1][c]=board[r][c];
        board[r][c]=t;
        
        return true;
    }
    else if(board[r][c-1]==0 && c>0)
    {
        t=board[r][c-1];
        board[r][c-1]=board[r][c];
        board[r][c]=t;
        
        return true;
    }
    else if(board[r][c+1]==0 && c<d-1)
    {
        t=board[r][c+1];
        board[r][c+1]=board[r][c];
        board[r][c]=t;
        
        return true;
    }

  
  return false;
  
    
}
/**
 * Returns true if game is won (i.e., board is in winning configuration), 
 * else false.
 */
bool won(void)
{

   if(board[d-1][d-1]!=0)
   {
       return false;
   }
   /*
    for(int i=0;i<d;i++)
    {
        for(int j=0;j<d-2;j++)
        {
            if(board[i][j]>board[i][j+1])
            {
                return false;
                break;
            }
        }
    }
    for(int i=0;i<d-2;i++)
    {
        for(int j=0;j<d;j++)
        {
            if(board[i][j]>board[i+1][j])
            {
                return false;
                break;
            }
        }
    }
    for(int i=0;i<d-2;i++)
    {
        if(board[d-1][i]>board[d-1][i+1])
            return false;
    }
    for(int i=0;i<d-2;i++)
    {
        if(board[i][d-1]>board[i+1][d-1])
            return false;
    }
    */
    int ctr=1,r,c;
    for(int i=0;i<d;i++)
    {
        r=i;
        for(int j=0;j<d;j++)
        {
           c=j;
            if(r==d-1 && c==d-1)
            {
                break;
            }
            if(board[i][j]!=ctr/* && r!=d-1 && d!=d-1*/)
            {
                return false;
            }
            ctr++;
        }
    }
    /*
    for(int i=0;i<d-1;i++)
    {
        if(board[d-1][i]!=ctr)
        {
            return false;
        }
    }
    */
    return true;
}


