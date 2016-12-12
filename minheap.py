# -*- coding: utf-8 -*-
"""
Based on max-heap pseudocode from CLRS.  **Note: Python indexing starts from 0,
whereas CLRS starts from 1, leading to minor differences in the code here

This implementation stores and operates on value,key pairs.  'value' refers to
the numerical value and 'key' refers to the label for the node object we're storing.
If working solely with numbers, you can use key = str(value).


So, example use would be:

from minheap import MinHeap

H = MinHeap()
H.insertNode(5,str(5)) 

or 

H.insertNode(5,'a') 


"""

import math as m

class MinHeap:
        
        
    class node():
        def __init__(self,value, key):  # key is vertex, value is weight
            self.value = value
            self.key = key
                
        def __str__(self):
            return str(self.value)
            
    def __init__(self,A = []):
        self.A =  A
        self.count = len(A)
        if self.A:  
            self.build_heap(self.A)
            self.minimum = self.A[0]
        else:
            self.minimum = None
            
    def __str__(self):
        
        L = [None]*self.count
        for index, item in enumerate(self.A):
            L[index] = str(item.value)
            
        return str(L)
                        
    def build_heap(self,A):
        for i in range(int(m.floor((len(A)-1)/2)),-1,-1):  
            self.__minHeapify(A,i)
            
    def __minHeapify(self,A,i):
        l = self.left(i)
        r = self.right(i)
        
        if l<= len(A)-1 and A[l].value < A[i].value:
            smallest_idx = l
        else:
            smallest_idx = i
            
        
        if r<= len(A)-1 and A[r].value < A[smallest_idx].value:
            smallest_idx = r        
        if smallest_idx != i:
            '''exchange A[i] and A[largest]'''
            temp = A[i]
            A[i] = A[smallest_idx]
            A[smallest_idx] = temp
            self.__minHeapify(A,smallest_idx)
    
    def minHeapify(self):
        self.__minHeapify(self.A,0)
        
    def insertNode(self,value,key): #value is weight, key is reference to vertex
        '''appends new node with max value, then decreases its value to desired number'''
        self.count +=1 
        n = self.node(float('inf'),key) #value is the weight
        self.A.insert(0,n)
        self.decrease_key(0,value)
        self.minHeapify()
        print n.value
        
    def decrease_key(self,i,value):
        A = self.A
        if value > A[i].value:
            #print('error new value is larger than current key')
            return
            
        A[i].value = value
        while i>0 and A[self.parent(i)].value > A[i].value:
            temp = A[i].value
            A[i].value = A[self.parent(i)].value
            A[self.parent(i)].value = temp
            i = self.parent(i)
            
    def extractMin(self):
        if self.count <0:
            print('error - heap underflow')
            return
            
        ref_to_min = self.A[0]
        self.A.remove(self.A[0]) #remove from list
        self.count -= 1
        self.__minHeapify(self.A,0)
        return ref_to_min.value, ref_to_min.key

    def emptyHeap(self):
        #empty the heap quickly 
        self.minimum = None
        self.count = 0
        self.A = []
        
    def parent(self,i):
        return int(m.floor((i-1)/2))
        
    def left(self,i):
        return int((i) + 1)
    
    def right(self,i):
        return int(((i) + 2))
