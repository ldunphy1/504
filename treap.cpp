#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

/* Reference: http://www.cs.cornell.edu/courses/cs312/2003sp/lectures/lec26.html
 */

struct node {
	int data, key;
	struct node* left;
	struct node* right;
};

struct node* treap_INITIALIZE();
void treap_INSERT(struct node*, int);
struct node* root;

int main()
{
	return 0;
}



struct node* treap_INITIALIZE()
{
	struct node* initial_node = new node(); // initialize in heap memory
	initial_node = NULL;
	return initial_node;
}