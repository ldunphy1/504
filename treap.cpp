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

void treap_INSERT(struct node* element, int data)
{
	if(element == NULL)
	{
		element = new node();
		element->left = element->right = NULL; // initialize with NULL pointer
		element->key = data;
		adjust = rand();
	}
	else
	{
		if (element->key == data)
		{
			return 0;	
		}
		else
		{
			if (data < element->key)
			{
				treap_INSERT(element->left,data); // recursive call
				if (element->left->adjust > element->adjust)
				{
					rightR(element); // need to implement
				}
			}
			else
			{
				treap_INSERT(element->right, data);
				if (element->right->adjust > element->adjust)
				{
					leftR(element);
				}
			}
		}			
	}
}