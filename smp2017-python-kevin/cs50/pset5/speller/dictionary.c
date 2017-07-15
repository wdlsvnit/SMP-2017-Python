/**
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include <strings.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>
#include <cs50.h>


#include "dictionary.h"


typedef struct node
{
    char word[LENGTH+1];
    struct node *next;
}node;

node *head[26];


//hash function from https://www.youtube.com/watch?v=h2d9b_nEzoA

int hash_function(const char *letter)
{
    //hash on first letter of string
    int hash = toupper(letter[0]) - 'A';
    return hash % 26;
}
/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    for(int i = 0; i < 26; i++)
    {
        node *cursor = head[i];

        while(cursor!=NULL)
        {
            if(strcasecmp(word, cursor->word)==0)
                return true;
            cursor = cursor->next;
        }
    }
    return false;
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary)
{
        char w[LENGTH+1];
        FILE *fp = fopen(dictionary, "r");
        while(fscanf(fp,"%s",w)!=EOF)
        {   
            node *new_node = malloc(sizeof(node));
            
            if(new_node == NULL)
            {
                unload();
                return false;
            }
            
            strcpy(new_node->word,w);
            
            int index = hash_function(new_node->word);
            
            if (head[index] == NULL)
            {
                
                head[index] = new_node;
                new_node->next = NULL;
            }
            else
            {
                new_node->next=head[index];
                head[index] = new_node;
                new_node->next = NULL;
            }
            free(new_node);
        }
        
        // close text
        fclose(fp);
        
        return true;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    int f = 0;
    for(int i = 0; i < 26; i++)
    {
        node *cursor = head[i];
        
        while(cursor!=NULL)
        {
            f++;
            cursor = cursor->next;
        }
    }
    return f;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    for(int i = 0; i < 26; i++)
    {
        node *cursor = head[i];
        
        while(cursor!=NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}