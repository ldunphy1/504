# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:01:41 2016

@author: montgomt
"""

from minheap import MinHeap
import unittest
import random

class MinHeapTest(unittest.TestCase): 
    
    def setUp(self):
        vals = list(range(1,1000))
        random.shuffle(vals)
        self.H = MinHeap()
        '''insert random values into structure'''
        for i in vals:
            self.H.insertNode(i,i)  
    
    def test_extractMin(self):
        '''test extract min'''
        expectedmin = 1
        for _ in range(self.H.count):
            #empty the heap to completion
            v,k = self.H.extractMin()
            self.assertEqual(v,expectedmin)
            expectedmin += 1
        
   
if __name__ == '__main__':
    unittest.main()
       