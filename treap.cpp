#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

/* Reference: http://www.cs.cornell.edu/courses/cs312/2003sp/lectures/lec26.html
 */

struct node {
	int data, adjust;
	struct node* left;
	struct node* right;
};

struct node* treap_INITIALIZE();
void treap_INSERT(struct node*, int);
void treap_DELETE(struct node*, int);
void leftR(struct node*);
void rightR(struct node*);

struct node* root;

int main()
{
	return 0;
}

void leftR(struct node* n)
{
	// left rotation
	struct node* temp;
	temp = n->right;
	n->right = temp->left;
	temp->left = n;
	n = temp;
}

void rightR(struct node* n)
{
	struct node* temp;
	temp = n->left;
	n->left = temp->right;
	temp->right = n;
	n = temp;
}



struct node* treap_INITIALIZE()
{
	struct node* initial_node = new node(); // initialize in heap memory
	initial_node = NULL;
	root = NULL; // need to check
	return initial_node;
}


void treap_DELETE(struct node* element, int value)
{
	if (element == NULL)
	{
		printf("Element does not exist, cannot be deleted!\n");
	}
	
	if (value > element->data)
		treap_DELETE(element->right, value); // recursively go right
	else if (value < element->data)
		treap_DELETE(element->left, value); // recursively go left down the tree
	else
	{
		if (element->left == NULL && element->right == NULL)
		{
			delete element; // if no children exists, destination reached, delete node
			element = NULL; // set that node to NULL to eliminate free address
		}
		else if (element->left = NULL) // case of right child
		{
			struct node* temp = element; // hold elements value
			element = element->right; // move the right child up. 
			delete temp; // delete from memory
		}
		else if (element->right = NULL) // case of left child
		{
			struct node* temp = element; 
			element = element->left;
			delete temp;
		}
		else
		{	// rotation
			if (element->left->adjust < element->right->adjust)
			{
				leftR(element); // rotate left
				treap_DELETE(element->left, value);
			}
			else
			{
				rightR(element);
				treap_DELETE(element->right, value);
			}
		}
	}
}

void treap_INSERT(struct node* element, int value)
{
	if(element == NULL)
	{
		element = new node();
		element->left = element->right = NULL; // initialize with NULL pointer
		element->data = value;
		element->adjust = rand();
	}
	else
	{
		if (element->data == value)
		{
			printf("Data already exists, cannot be added!\n");	
		}
		else
		{
			if (value < element->data)
			{
				treap_INSERT(element->left,value); // recursive call
				if (element->left->adjust > element->adjust)
				{
					rightR(element); // need to implement
				}
			}
			else
			{
				treap_INSERT(element->right, value);
				if (element->right->adjust > element->adjust)
				{
					leftR(element);
				}
			}
		}			
	}
}