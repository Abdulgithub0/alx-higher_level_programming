#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *check_cycle - function to check for a circular list structure
 *@list: the list node
 *Return: 1 if the list is circular or 0 if otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *traveler;

	traveler = list->next;
	while (traveler != NULL)
	{
	       if (list != traveler)
	       {
		       traveler = traveler->next;
		       continue;
	       }
	       return (1);
	}
	return (0);
}

