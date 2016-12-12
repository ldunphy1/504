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
		for i in vals:
			self.H.insertNode(i, str(i))
		self.H2 = BinomialHeap()
		vals = list(range(26,50))
		random.shuffle(vals)
		for i in vals:
			self.H2.insertNode(i,str(i))

	def test_findMin(self):
		self.assertEqual(self.H.findMin().value,1)

	def test_union(self):
		self.H.union(self.H2)
		d = self.H.findMin()
		self.assertEqual(d.value, -10)

	def test_extractMin(self):
		expectedmin = 1
		for _ in range(self.H.count):
			#empty the heap to completion
			self.assertEqual(self.H.extractMin()[0], expectedmin)
			expectedmin += 1
			
	def test_delete(self):
		minnode = self.H.findMin()
		self.assertEqual(minnode.value, 1)
		self.H.delete(minnode) #minimum should now be 2
		minnode = self.H.findMin()
		self.assertEqual(minnode.value, 2) #this works if we deleted the proper node

if __name__ == '__main__':
	unittest.main()