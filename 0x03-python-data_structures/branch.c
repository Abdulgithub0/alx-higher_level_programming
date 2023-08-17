#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
int is_palindrome_helper(listint_t **left, listint_t *right);

/**
 * is_palindrome - check if a linked-list is palindrome or not
 * @head: pointer to the pointer of the address of head node
 * Return: 0 if it's not palindrome or 1 otherwise
 */

int is_palindrome(listint_t **head)
{
        if (*head == NULL || (*head)->next == NULL) {
                return 1;
        }

        int is_pal = is_palindrome_helper(head, *head);
        return is_pal;
}

int is_palindrome_helper(listint_t **left, listint_t *right)
{
        int is_pal = 1;

        if (right->next != NULL) {
                is_pal = is_palindrome_helper(left, right->next);
        }

        if (is_pal == 1 && (*left)->n == right->n) {
                *left = (*left)->next;
        } else {
                is_pal = 0;
        }

        return is_pal;
}

