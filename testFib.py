
"""
Test script for fibonacci heap 
implementation 
"""

from fibHeapFinal import FibHeap
import random
import unittest

class TestFib(unittest.TestCase):

	def setUp(self):
		self.heap = FibHeap()
		print("\nFirst Heap is: \n")
		self.heap.insertNode(0, 0) #known minimum for testing
		self.heap.insertNode(200, 200) #known node for testing
		for i in range(2, 33):
			n = random.randint(1, 200)*i
			self.heap.insertNode(n, n)
		print("\n\nSecond Heap is: \n")
		self.heap2 = FibHeap()
		self.heap2.insertNode(-10, -10) #known minimum for testing
		for i in range(2,33):
			n = random.randint(1, 200)*i
			self.heap2.insertNode(n, n)

	def test_findMin(self):
		d, k = self.heap.findMin()
		self.assertEqual(d, 0)
		print("findMin: OK")

	def test_mergeHeap(self):
		self.heap.mergeHeap(self.heap2)
		d, k = self.heap.findMin()
		self.assertEqual(d, -10)

	def test_extractMin(self):
		self.heap.mergeHeap(self.heap2)
		self.heap.extractMin()
		d, k = self.heap.findMin()
		self.assertEqual(d, 0)
		
	def test_delete(self):
		self.heap.extractMin() # extract min to rearrange heap
		temp = self.heap.findMin()
		find = self.heap.search(temp) #look for the key
		self.assertEqual(find, -1) # key should not be in the heap anymore

if __name__ == '__main__':

	print("running tests on FibHeap...")
	unittest.main()

