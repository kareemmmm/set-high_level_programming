#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Double pointer to the head of the linked list.
 * @number: The number to insert into the list.
 * Return: Address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	current = *head;

	/* Insert at the beginning if list is empty or number is smaller than head */
	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	/* Traverse to find correct placement position */
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
