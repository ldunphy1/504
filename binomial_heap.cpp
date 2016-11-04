#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

/* Reference: http://www.growingwiththeweb.com/2014/01/binomial-heap.html
 * https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/BinomialHeaps.pdf
 */

struct node { // basic structure of the node
	int value;
	int degree;
	struct node* parent;
	struct node* child;
	struct node* relational; // sibling node
};



struct node* heap_UNION(struct node*, struct node*);
struct node* heap_MERGE(struct node*, struct node*);
struct node* heap_INSERT(struct node*, struct node*);
struct node* heap_INITIALIZE();
struct node* heap_CREATE_NODE(int);
struct node* heap_SEARCH(struct node*, int);
struct node* heap_EXTRACT_MIN(struct node*);

void heap_DELETE(struct node*, int);
void heap_DECREASE_KEY(struct node*, int, int);
void heap_ORIGINAL(struct node*);
void heap_LINK(struct node*, struct node*);

struct node* other;
struct node* initial;

int main()
{
	printf("Fried Chicken");
	return 0;
}

struct node* heap_INITIALIZE()
{
	// initializes the heap structure
	struct node* initial_node;
	initial_node = NULL;
	return initial_node;
}

void heap_ORIGINAL(struct node* a)
{
	if (a->relational != NULL)
	{
		heap_ORIGINAL(a->relational);
		(a->relational)->relational = a; // makes this the original node
	}
	else
	{
		other = a;
	}
}

struct node* heap_CREATE_NODE(int data)
{
	node* initial_node = new node(); // intiailze the node in the heap memory
  	initial_node->value = data; // takes the user data and makes the node's value variable refer to it
  	initial_node->parent = NULL;
  	initial_node->relational = NULL;
  	initial_node->child = NULL;
  	initial_node->degree = 0;
	return initial_node;
}

struct node* heap_SEARCH(struct node* original, int data)
{
	struct node* temp = NULL; // holds the node where the node in question exists
	if (original->value == data)
	{
		temp = original;
		return original;
	}

	if (original->child != NULL && temp == NULL)
	{
		temp = heap_SEARCH(original->child, value); // recursively search
	}

	if (original->relational != NULL && temp == NULL)
	{
		temp = heap_SEARCH(original->relational, value); // recursively search
	}

	return original;

}

struct node* heap_INSERT(struct node* original, struct node* new_element)
{
	struct node* temp = heap_INITIALIZE();
	temp = new_element;
	original = heap_UNION(original, temp); // does the union function to combine the new element with original
	return original;
}	

void heap_LINK(struct node* a, struct node* b)
{ 	// Performs the basic linking between two elements
	a->parent = b;
	a->relational = b->child;
	b->child = a;
	b->degree = b->degree + 1; // increases the degree value
}
struct node* heap_UNION(struct node* a, struct node* b)
{
	struct node* before = NULL;
	struct node* after = NULL; 
	struct node* temp;

	struct node* output = heap_INITIALIZE(); //initializes a heap in memory
	output = heap_MERGE(a, b); // performs the merging of the nodes

	if (output == NULL)
	{
		return output; // outputs a NULL value, if non-existant
	}

	temp = output;
	after = output->relational;

	while (after != NULL) // provided the relation is not reached to be NULL
	{
		if ((output->degree != after->degree) || ((after->relation != NULL) && (after->relational)->degree == output->degree))
		{
			// swap
			before = output;
			output = after;
		}
		else
		{
			if (output->value <= after->value)
			{
				output->relational = after->relational; // replace with the next element
				heap_LINK(output, after);
			}
			else
			{
				if (before == NULL)
				{
					output = after;
				}
				else
				{
					before->relational = after;
					heap_LINK(output, after);
					output = after;
				}
			}
		}
		after = output->relational;
	}

	return output;
}

struct node* heap_MERGE(struct node* a, struct node* b)
{
	/*Responsible for mergining to structures together*/
	struct node* output = heap_INITIALIZE();
	struct node* temp_a; struct node* temp_b;

	if (temp_a != NULL)
	{
		if (b != NULL && a->degree <= b->degree)
		{
			// Case for when the original heap has degree value less than or equal to the new heap
			output = a;
		}
		else if (b != NULL && a->degree > b->degree)
		{
			output = b;
		}
	}
	else
	{
		output = b; // if the original heap is no existant, the new heap becomes the original
	}

	// traversal and changing the structure 
	while (a != NULL && b != NULL)
	{
		if (a->degree < b->degree)
		{
			a = a->relational; // the sibling's value becomes the new pointer
		}
		else if (a->degree == b->degree)
		{
			temp_a = a->relational;
			a->relational = b; // swap
			a = temp_a;
		}
		else
		{
			temp_b = b->relational;
			b->relational = a; // swap
			b = temp_b;
		}

	}
	return output;
}

void heap_DELETE(struct node* original, int data)
{
	
	if (original == NULL)
	{
		// Heap does not exist
		printf("HEAP DOES NOT EXIST\n");
		return 0; // exit function
	}

	heap_DECREASE_KEY(output, data. -1000);
	if (heap_EXTRACT_MIN(output) != NULL)
	{
		// The function will only function if the node is the smallest
		printf("Deleted\n");	
	} 

}

void heap_DECREASE_KEY(struct node* original, int value, int infi)
{
	struct node* temp;
	struct node* temp_a; struct node* temp_b;
	temp = heap_SEARCH(original, value);

	if ((heap_SEARCH(original, value) == NULL) || (infi > temp->value))
	{
		printf("Key value incorrect!\n");
	}

	temp->value = infi;
	temp_a = temp; temp_b = temp->parent;

	while (temp_b != NULL && temp_a->value < temp_b->value)
	{	// readjustment - child becomes parent
		temp = temp_a->value;
		temp_a->value = temp_b->value; // replacing current with parent's value
		temp_b->value = temp; // replacing parent with current
		temp_a = temp_b; 
		temp_b = temp_b->parent;
	}
	printf("Decrease completed\n");
}


struct node* heap_EXTRACT_MIN(struct node* original)
{
	other = NULL; // clears value
	int minimum = 0; // initalize as 0
	struct node* temp1, temp2, temp3;

	if (original == NULL)
	{
		printf("HEAP does not exist\n");
		return 0;
	}

	temp1 = original; temp2 = temp1; temp3 = temp1;
	while (temp2->relational != NULL)
	{
		if ((temp2->relation)->value < minimum)
		{
			minimum = (temp2->relational)->value;
			temp3 = temp2;
			temp1 = temp2->relational; // replaces 
		}
		temp2 = temp2->relational;
	}

	if (temp3 == NULL && temp1->relational == NULL)
	{
		original = NULL; // returns NULL value
	}
	else if (temp3 == NULL)
	{
		original = temp1->relational;
	}
	else if (temp3->relational == NULL)
	{
		temp3 = NULL;
	}
	else
	{
		temp3->relational = temp1->relational;
	}


	if (temp1->child != NULL)
	{
		heap_ORIGINAL(temp1->child);
		(temp1->child)->relational = NULL;
	}

	initial = heap_UNION(original, other)

	return temp1; // returns minimum value


}