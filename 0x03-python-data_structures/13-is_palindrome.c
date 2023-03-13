#include <stdlib.h>
#include "lists.h"
#include <stdio.h>
int traveler(listint_t **next_head, listint_t *next_tail);

/**
 * is_palindrome - check if a linked-list is palindrome or not
 * @head: pointer to the pointer of the address of head node
 * Return: 0 if it's palindrome or 1 otherwise
 */

int is_palindrome(listint_t **head)
{
	int status_checker;

	status_checker = 1;
	if (*head == NULL)
		return (status_checker);
	status_checker = traveler(head, *head);
	return (status_checker);
}

/**
 * traveler - recursively check both head and tail node for palind.
 * @next_head: pointer to pointer of new head node
 * @next_tail: momentarily tail node for each recursive stack frame open
 * Return: 1 if palindrome or 0 otherwise
 */

int traveler(listint_t **next_head, listint_t *next_tail)
{
	int status;

	status = 1;
	if (next_tail->next != NULL)
		traveler(next_head, next_tail->next);
	if ((*next_head)->n != next_tail->n && status != 0)
		status = 0;
	else
		*next_head = (*next_head)->next;
	return (status);
}
