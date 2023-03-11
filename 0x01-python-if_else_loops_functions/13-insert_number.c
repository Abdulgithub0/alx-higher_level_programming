#include "lists.h"
#include <stdio.h>
/**
 * insert_node - function that insert a number in a sorted singly-linked list
 * @head: address of the head node
 * @number: number to be insert
 * Return: address of the new inserted node or NULL if otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *traveler, *prev_node;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	traveler = (*head)->next;
	prev_node = *head;
	if (prev_node->n > new_node->n)
	{
		new_node->next = prev_node;
		*head = new_node;
		return (new_node);
	}
	while (traveler != NULL)
	{
		if (traveler->n < new_node->n)
		{
			prev_node = traveler;
			traveler = traveler->next;
			continue;
		}
		else if (traveler->n == new_node->n)
		{
			new_node->next = traveler;
			prev_node->next = new_node;
			return (new_node);
		}
		else
		{
			new_node->next = traveler;
			prev_node->next = new_node;
			return (new_node);
		}
	}
	new_node->next = NULL;
	prev_node->next = new_node;
	return (prev_node->next);
}
