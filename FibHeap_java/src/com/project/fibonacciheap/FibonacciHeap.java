package com.project.fibonacciheap;

import java.util.*;
import java.lang.Number;

/**
 * Created by jmeunier28 on 10/30/16.
 */


/*
    Java Implementation of a Fibonacci Heap Data Structure
    EC504 Data Structures Project
    Follow steps according to pseudo code on pgs 505-519 of CLRS
*/


//Data structure is ordered based on Value not based on Key
    // I think this is wrong but for showing how it works will do it this way for now

public class FibonacciHeap<T> { // generic type

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

        //System.out.print("\nWe inserted:\nkey: " + node.getKey() + ", " + node.getValue());
        /*System.out.print("\nType of: " + node.getValue().toString().getClass().getName());
        System.out.print("\nParseInt: " + java.lang.Integer.parseInt(node.getValue().toString()));*/


        // merge new node with root list:

        min = addToRoot(min, node);

        //Update the pointer to the minimum node of the heap if necessary

        if (min == null || node.key < min.key)
                //java.lang.Integer.parseInt(node.getValue().toString()) <
                //        java.lang.Integer.parseInt(min.getValue().toString()))
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

    public void delete(FibHeapNode node)
    {
        // call Decrease Key to -inf

        this.decreaseKey(node, Integer.MIN_VALUE);
        this.deleteMin();

    }

    public int size()
    {
        return count;
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

    {
        //Consolidate according to fib heap rules
        ArrayList<FibHeapNode> tempList = new ArrayList<>(); // make temp list to store stuff in
        int num = (int) Math.floor(Math.log(count));
        System.out.print(num);
        for (int i = 0; i < min.nodelist().size(); i++){
        //for(int i =0; i < num; i++) {
            tempList.add(null); // fill new array with null values
        }

        if (min != null)
        {
            for(Object cur : min.nodelist())
            { // iterate through the root list
                FibHeapNode x = (FibHeapNode)cur; // store current at x
                int dx = x.degree; // degree of node in root list

                while (tempList.get(dx) != null)
                {
                    FibHeapNode y = tempList.get(dx);
                    //if(java.lang.Integer.parseInt(x.getValue().toString()) >
                      //      java.lang.Integer.parseInt(y.getValue().toString()))
                    if(x.key > y.key)
                    {
                        // x is bigger so it becomes child
                        FibHeapNode temp = x;
                        x = y;
                        y = temp; // exchange x and y
                    }
                    this.makeChild(x,y);
                    tempList.set(dx, null);
                    dx++;
                }
                tempList.set(dx, x);

                min = null;

            } //end iteration of Root List

            for(int i = 0; i < tempList.size();i++)
            {
                if (tempList.get(i) != null)
                {
                    min = addToRoot(min, tempList.get(i));
                    if (min == null || tempList.get(i).key < min.key)//java.lang.Integer.parseInt(tempList.get(i).getValue().toString())
                            //< java.lang.Integer.parseInt(min.getValue().toString()))
                    {
                        min = tempList.get(i); // reassign min pointer
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

    public void decreaseKey(FibHeapNode key, Integer newKey)
    {
        //modify Fib Heap to decrease key value
        //Call Consolidate

        if( newKey > key.key)//java.lang.Integer.parseInt(newKey.toString()) >
              //  java.lang.Integer.parseInt(key.getValue().toString()))
        {
            System.out.print("\nERROR:\nNew Key Greater Than Original");
            return;
        }

        key.value = newKey;

        FibHeapNode y = key.parent;

        /*
            Check if key is root aka parent is null and also check to see if
            the newKey is still smaller than parent... if it is we cut it from
            its parent and add it to the root list
         */

        if(y != null && key.key < y.key)//java.lang.Integer.parseInt(key.getValue().toString())
                //< java.lang.Integer.parseInt(y.getValue().toString()))
        {
            //call cut
            //call cascading cut
            this.cut(key, y);
            this.cascadingCut(y);
        }


    }

    private void cut(FibHeapNode child, FibHeapNode parent)
    {
        // cut link between child and parent nodes
        parent.child = removeNode(parent.child, child);
        parent.degree--; // decrement parents degree
        min = addToRoot(min, child); // add child to root list

        child.parent = null; // child has no parent anymore wahh
        child.mark = false;

    }

    private void cascadingCut(FibHeapNode node)
    {
        FibHeapNode z = node.parent; // store z as parent node

        if (z != null)
        {
            // node has a parent
            if (node.mark == false)
            {
                node.mark = true;
            }
            else
            {
                this.cut(node, z);
                this.cascadingCut(z);
            }
        }
    }

    public void mergeHeap(FibonacciHeap heap){

        // method to merge two Fibonacci Heaps together

        min = addToHeap(min, heap.min);

        if (min == null || (heap.min != null && heap.min.key < min.key))//java.lang.Integer.parseInt(heap.min.getValue().toString()) <
                //java.lang.Integer.parseInt(min.getValue().toString())))
        {
            min = heap.min; // update min pointer if necessary
        }

        count += heap.count; // increase num nodes in heap

    }

    public FibHeapNode addToHeap(FibHeapNode node1, FibHeapNode node2)
    {
        if (node1 == null){
            return node2;
        }
        else if (node2 == null)
        {
            return node1;
        }
        else
        {
            node1.right.left = node2.left;
            node2.left.right = node1.right;
            node2.right = node1;
            node1.left = node2;
            return node1;
        }
    }


}
