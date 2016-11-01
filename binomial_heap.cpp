#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

// Reference: http://www.growingwiththeweb.com/2014/01/binomial-heap.html

struct node { // basic structure of the node
	int value;
	int key;
	struct node* parent;
	struct node* child;
	struct node* relational; // sibling node
};

struct node* heap_FINDMIN();
struct node* heap_DELETEMIN();
struct node* heap_DELETE();
struct node* heap_DECREASE_KEY();
struct node* heap_UNION(struct node*, struct node*);
struct node* heap_MERGE(struct node*, struct node*);
struct node* heap_INSERT(struct node*, struct node*);
struct node* heap_INITIALIZE();
struct node* heap_CREATE_NODE(int);

int main()
{
	printf("Banana");
	return 0;
}

struct node* heap_INITIALIZE()
{
	// initializes the heap structure
	struct node* initial_node;
	initial_node = NULL;
	return initial_node;
}

struct node* heap_CREATE_NODE(int data)
{
	node* initial_node = new node(); // intiailze the node in the heap memory
  	initial_node->value = data; // takes the user data and makes the node's value variable refer to it
  	initial_node->parent = NULL;
  	initial_node->relational = NULL;
  	initial_node->child = NULL;
  	initial_node->key = 0;
	return initial_node;
}

struct node* heap_INSERT(struct node* original, struct node* new_element)
{
	struct node* temp = heap_INITIALIZE();
	temp = new_element;
	original = heap_UNION(original, temp); // does the union function to combine the new element with original
	return original;
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



}

struct node* heap_MERGE(struct node* a, struct node* b)
{
	/*Responsible for mergining to structures together*/
	struct node* output = heap_INITIALIZE();
	struct node* temp_a; struct node* temp_b;

	if (temp_a != NULL)
	{
		if (b != NULL && a->key <= b->key)
		{
			// Case for when the original heap has key value less than or equal to the new heap
			output = a;
		}
		else if (b != NULL && a->key > b->key)
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
		if (a->key < b->key)
		{
			a = a->relational; // the sibling's value becomes the new pointer
		}
		else if (a->key == b->key)
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

