#include <stddef.h>
#include "lists.h"

/**
 * check_palindrome - Recursive helper to evaluate node values symmetrically
 * @left: Double pointer to the forward moving node from start
 * @right: Pointer to the backward moving node from end via stack frames
 * Return: 1 if palindrome matches up to this stack state, 0 otherwise
 */
int check_palindrome(listint_t **left, listint_t *right)
{
	int response;

	if (right == NULL)
		return (1);

	response = check_palindrome(left, right->next);
	if (response == 0)
		return (0);

	response = (right->n == (*left)->n);
	*left = (*left)->next;

	return (response);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_palindrome(head, *head));
}
