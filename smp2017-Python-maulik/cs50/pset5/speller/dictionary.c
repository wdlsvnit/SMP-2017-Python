/**
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

#include "dictionary.h"

struct node *getNode(void);

/*typedef struct node
{
    bool is_word;
    struct node *children[27];
}
node; */
extern node *ROOT;

long noOfWords=0; //total number of words in the dictionary

node *getNode(void)
{
    node *pNode = NULL;

    pNode = (node *)malloc(sizeof(node));

    if (pNode)
    {
        int i;

        pNode->is_word = false;

        for (i = 0; i < 27; i++)
            pNode->children[i] = NULL;

    }
    return pNode;
}


/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    // TODO

    int wordLength = strlen(word);
    char lowercaseWord[46];
    int j,i;

    node *root=ROOT;

    for(i=0;i<wordLength;i++)
    {
      lowercaseWord[i] = tolower(word[i]) ;

      if(isalpha(lowercaseWord[i]))
        j=(int)lowercaseWord[i]-(int)'a';
      else
        j=26;


      if(root->children[j]==NULL)
        return false;

      root=root->children[j];
    }

    return (root->is_word && root!=NULL);
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary)
{
    // TODO

    int c,i;

    ROOT=getNode();


    FILE *ip=fopen(dictionary,"r");

    if(ip==NULL)
      return false;

    c=getc(ip);
    while(c!=EOF)
    {
        node *root = ROOT;
        for(;c!='\n';c=getc(ip))
        {
          if(isalpha(c))
            i=(int)c-(int)'a';
          else
            i=26;

          if(root->children[i]==NULL)
            root->children[i]=getNode();

          root=root->children[i];
        }
        root->is_word=true;
        noOfWords++;

        c=getc(ip);
    }

    fclose(ip);

    return true;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    // TODO

    return noOfWords;
}

void free_all(node* curs)
{
    int i;

    // recursive case (go to end of trie)
    for (i = 0; i < 27; i++)
    {
        if (curs->children[i] != NULL)
        {
            free_all(curs->children[i]);
        }
    }

    // base case
    free(curs);
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    // TODO
    free_all(ROOT);

    return true;
}
