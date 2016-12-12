# -*- coding: utf-8 -*-
"""
Based on max-heap pseudocode from CLRS.  **Note: Python indexing starts from 0,
whereas CLRS starts from 1, leading to minor differences in the code here.
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
        self.decrease_key(self.count-1,value)
        self.minHeapify()
        
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
        bh = self
        A = bh.A
        if self.count <0:
            print('error - heap underflow')
            return
            
        ref_to_min = A[0]
        A[0] = A[1]
        del A[:bh.count-1] #truncate array by 1
        bh.count -= 1
        self.__minHeapify(A,0)
        return ref_to_min.value, ref_to_min.key

    def emptyHeap(self):
        #empty the heap quickly 
        self.minimum = None
        self.count = 0
        self.A = []
        
    def parent(self,i):
        return int(m.floor((i-1)/2))
        
    def left(self,i):
        return int((2*i) + 1)
    
    def right(self,i):
        return int((2*(i) + 2))