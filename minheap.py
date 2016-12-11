# -*- coding: utf-8 -*-
"""
Based on max-heap pseudocode from CLRS.  **Note: Python indexing starts from 0,
whereas CLRS starts from 1, leading to minor differences in the code here.
"""

import math as m

class MinHeap:
        
    def __init__(self,A = []):
        self.A =  A
        self.heapsize = len(A)
        if self.A:  
            self.__build_heap(self.A)
            self.minimum = self.A[0]
        else:
            self.minimum = None
                
        
    def __str__(self):
        return str(self.A)
        
    def __build_heap(self,A):
        for i in range(int(m.floor((len(A)-1)/2)),-1,-1):  
            self.__min_heapify(A,i)
            
    def __min_heapify(self,A,i):
        l = self.left(i)
        r = self.right(i)
        
        if l<= len(A)-1 and A[l] < A[i]:
            smallest = l
        else:
            smallest = i
            
        if r<= len(A)-1 and A[r] < A[smallest]:
            smallest = r
            
        if smallest != i:
            '''exchange A[i] and A[largest]'''
            temp = A[i]
            A[i] = A[smallest]
            A[smallest] = temp
            self.__min_heapify(A,smallest)
    
    def minHeapify(self):
        '''public method to heapify the entire tree'''
        self.__min_heapify(self.A,0)

    def insert(self,key):
        self.heapsize +=1 
        self.A.append(float('inf'))
        self.decrease_key(self.heapsize-1,key)
        
    def decrease_key(self,i,key):
        A = self.A
        if key > A[i]:
            print('error new key is larger than current key')
            return
            
        A[i] = key
        while i>0 and A[self.parent(i)] > A[i]:
            temp = A[i]
            A[i] = A[self.parent(i)]
            A[self.parent(i)] = temp
            i = self.parent(i)
            
    def extractMin(self):
        bh = self
        A = bh.A
        if bh.heapsize <1:
            print('error - heap underflow')
            return
            
        minimum = A[0]
        A[0] = A[bh.heapsize-1]
        del A[bh.heapsize-1:] #truncate array by 1
        bh.heapsize -= 1
        self.__min_heapify(A,0)
        return minimum
        
    def parent(self,i):
        return m.floor((i-1)/2)
        
    def left(self,i):
        return (2*i) + 1
    
    def right(self,i):
        return (2*(i) + 2)