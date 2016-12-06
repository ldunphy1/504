# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:32:41 2016

@author: montgomt
"""

from binomialheap import BinomialHeap
import random
import unittest

class BinomialTest(unittest.TestCase):


    def setUp(self):
        self.H = BinomialHeap()
        vals = list(range(1,26))
        random.shuffle(vals)
        
        '''insert random values into structure'''
        for i in vals:
            self.H.insertNode(i,str(i))  
            
    def test_findMin(self):
        self.assertEqual(self.H.findMin().value,1)

    def test_extractMin(self):
        '''test extract min'''
        expectedmin = 1
        for _ in range(self.H.count):
            #empty the heap to completion
            self.assertEqual(self.H.extractMin()[0],expectedmin)
            expectedmin += 1
            
    def test_delete(self):
        minnode = self.H.findMin()
        self.assertEqual(minnode.value,1)        
        self.H.delete(minnode) #minimum should now be 2
        minnode = self.H.findMin()
        self.assertEqual(minnode.value,2) #this works if we deleted the proper node
            

if __name__ == '__main__':
    unittest.main()
        

   


        

        
            