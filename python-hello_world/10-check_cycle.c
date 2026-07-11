#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/* If the list is empty or has only one element, it can't have a cycle */
	if (list == NULL)
		return (0);

	/* Traverse the list with two pointers at different speeds */
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;          /* moves 1 step at a time */
		fast = fast->next->next;    /* moves 2 steps at a time */

		/* If the fast pointer catches up to the slow pointer, a cycle exists */
		if (slow == fast)
			return (1);
	}

	/* If fast reaches the end (NULL), there is no cycle */
	return (0);
}
