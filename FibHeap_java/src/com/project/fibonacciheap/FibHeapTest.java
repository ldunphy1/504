package com.project.fibonacciheap;
import javax.print.attribute.standard.Fidelity;
import java.util.*;

/**
 * Created by jmeunier28 on 10/30/16.
 */
public class FibHeapTest {

        public static void main(String[] args) {

            System.out.println("FibonacciHeap Test\n\n");
            FibonacciHeap fh = new FibonacciHeap<Integer>();
            ArrayList<FibHeapNode> arr = new ArrayList<FibHeapNode>();

            for (int i = 15; i > 0; i--) {
                FibHeapNode node = new FibHeapNode(i, (int) Math.floor(Math.random() * i*200)); // populate random array
                fh.insert(node);
                //System.out.print("\n\nThe min is: " + fh.getMin().getValue());
            }

            System.out.print("\n\nThe min is: " + fh.getMin().getValue());
            fh.deleteMin();
            System.out.print("\n\nNew min is: " + fh.getMin().getValue());


        }
}
