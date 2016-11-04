package com.project.fibonacciheap;

import java.util.*;
import java.lang.Number;

/**
 * Created by jmeunier28 on 10/30/16.
 */


//Java Implementation of a Fibonacci Heap Data Structure
    // EC504 Data Structures Project


public class FibonacciHeap<Integer> {

    private FibHeapNode root;
    private FibHeapNode min; //points to min element in heap
    private int count; //count of nodes in heap

    //constructor

    public FibonacciHeap()
    {
        min = null;
        count = 0;
    }

    //check if heap is empty
    public boolean isEmpty()
    {
        return root == null;
    }

    //make heap empty
    public void emptyHeap()
    {
        min = null;
        count = 0;
    }

    //insert into the heap
    public void insert(FibHeapNode node) {

        /* Initialize lone wolf node who has no friends
            or family and wants to be loved */
        //System.out.print("\nInserted node with key " + key + " ,value " + node);

        node.degree = 0;
        node.child = null;
        node.parent = null;
        node.right = node;
        node.left = node;
        node.mark = false;

        System.out.print("\nWe inserted " + node.getValue().toString());
        /*System.out.print("\nType of: " + node.getValue().toString().getClass().getName());
        System.out.print("\nParseInt: " + java.lang.Integer.parseInt(node.getValue().toString()));*/


        // merge new node with root list:

        min = addToRoot(min, node);

        //Update the pointer to the minimum node of the heap if necessary

        if (min == null ||
                java.lang.Integer.parseInt(node.getValue().toString()) <
                        java.lang.Integer.parseInt(min.getValue().toString()))
        {
            min = node;
        }

        count++; //increase count of nodes
    }


    private FibHeapNode addToRoot(FibHeapNode head, FibHeapNode node)
    {
        if (head == null) { // node is alone in the heap
            node.left = node;
            node.right = node;
            return node;

        }
        else // node isn't alone lets add to root list
        {
            node.left = head; // node has head to the left
            node.right = head.right; // node inserted to right of head
            head.right = node; // update where head.right points to
            node.right.left = node; // update node pointers
            return head;
        }
    }


    public FibHeapNode getMin()
    {
        return min; //return pointer to minimum element
    }

    public void delete(int element)
    {
        //Delete Key
        //Call consolidate

    }

    public FibHeapNode deleteMin()
    {
        //Delete min key
        //Call consolidate
        FibHeapNode x = min; // save ptr to min node
        if (x != null)
        {
            if(x.child != null) //if x has kids we gotta bring dem up to the root list
            {
                for (Object cur : x.child.nodelist())  //make all children of x roots in the heap
                {
                    System.out.print("\n\nMoving kids to root list...");
                    min = addToRoot(min, (FibHeapNode)cur);
                    x.parent = null;
                }
            }

            min = removeNode(min, x); //remove the minimum
            if (x == x.right) { //x has no children and is only node in root list
                this.emptyHeap();
            }
            else // check out the root list
            {
                min = x.right; //point to other node in root list

                //call consolidate method
                System.out.print("\n\nConsolidating...");
                this.consolidate();
            }
            count--; // decrease node count
        }

        return x; //return the min
    }

    private FibHeapNode removeNode(FibHeapNode head, FibHeapNode node)
    {
        // node points at itself... doesn't have any friends anyways

        if(node.left == node)
        {
            return null;
        }

        //node doesn't point to anywhere in root list --> no more friends -__-

        node.left.right = node.right;
        node.right.left = node.left;
        return head;
    }

    private void consolidate()

            /*
                need to determine how to take it apart and then put back together via a new
                Array List ??? no idea how forget how this works slash im tired as fuck
             */
    {
        //Consolidate according to fib heap rules
        ArrayList<Integer> tempList = new ArrayList<Integer>(); // make temp list to store stuff in

        if (min != null)
        {
            for(Object cur : min.nodelist())
            { // iterate through the root list
                FibHeapNode x = (FibHeapNode)cur; // store current at x
                int dx = x.degree; // degree of node in root list

                //compare degrees of nodes in list
                int dm = min.degree;
                if (dx == dm) // degrees are same so compare node values
                {
                    System.out.print("\nDx: " + dx);
                    System.out.print(" Dm: " + dm);

                    if (java.lang.Integer.parseInt(x.getValue().toString()) <
                                java.lang.Integer.parseInt(min.getValue().toString()))
                    {
                        // x is smaller so it becomes parent of next
                        System.out.print("\nCase min is bigger");
                        this.makeChild(x,min);
                    }
                    else
                    {
                        System.out.print("\nCase min is still min");
                        this.makeChild(min,x); // min is smaller so make it parent
                    }
                }

            }
        }


    }

    private void makeChild(FibHeapNode head, FibHeapNode node)
    {
        min = removeNode(min, node); //remove from root list

        // node is child of head

        node.parent = head;  //new parent
        node.left = node;  //doubly linked list with itself
        node.right = node;
        head.child = addToRoot(head.child, node); // create root list for child node

        head.degree++; // increase degree of parent
        node.mark = false; //mark is set to false
    }

    public void decreaseKey(int key, int newKey)
    {
        //modify Fib Heap to decrease key value
        //Call Consolidate
    }

    public void mergeHeap(FibonacciHeap heapOne, FibonacciHeap heapTwo){

        // method to merge two Fibonacci Heaps together

    }

}
