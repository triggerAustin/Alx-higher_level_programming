#include "lists.h"

/**
 * check_cycle - check whether a singly linked list
 * has a cycle (using tortoise and hare)
 * list: the singly linked list
 * Return: 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	/* initialize the fast and slow pointers*/
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		/*move fst pointer two steps*/
		fast = fast->next->next;

		/*if slow and fast == there is a cycle*/
		if (slow == fast)
			return (1);
	}

	return (0);
}
