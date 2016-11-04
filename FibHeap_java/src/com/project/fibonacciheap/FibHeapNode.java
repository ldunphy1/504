package com.project.fibonacciheap;

import com.google.common.collect.Lists;
//import org.apache.commons.lang3.builder.ToStringBuilder;

import java.util.ArrayList;


/**
 * Created by jmeunier28 on 10/30/16.
 */



public class FibHeapNode<Integer> {

    // protected members can be accessed by package

        protected FibHeapNode child, parent, right, left; //parent or children if any in list
        protected int key; // key for the node
        protected Integer value; // value for the node
        protected int degree; // Number of children
        protected boolean mark; // Whether this node is marked



        //constructor for new node is Fib Heap

        public FibHeapNode(int key, Integer value)
        {

            this.key = key;
            this.value = value;

        }

        public int getKey()
        {
            return key;
        }

        public Integer getValue()
        {
            return value;
        }

    // List of Data in Structure

    public ArrayList<FibHeapNode<Integer>> nodelist()
    {
        ArrayList<FibHeapNode<Integer>> list = Lists.newArrayList();
        list.add(this);
        FibHeapNode<Integer> next = right;
        while (next != this) {
            list.add(next);
            next = next.right;
        }
        return list;
    }

}
