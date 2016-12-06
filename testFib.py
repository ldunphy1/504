
"""
Test script for fibonacci heap 
implementation 
"""

from fibHeapFinal import FibHeap
from binomialheap import BinomialHeap
import random
import unittest

# class TestFib(unittest.TestCase):

# 	def setUp(self):

# 		self.heap = FibHeap()
# 		print("\nFirst Heap is: \n")
# 		self.heap.insertNode(0) #known minimum for testing
# 		self.heap.insertNode(200) #known node for testing
# 		for i in range(2, 33):
# 			self.heap.insertNode(random.randint(1, 200)*i)

# 		print("\n\nSecond Heap is: \n")
# 		self.heap2 = FibHeap()
# 		self.heap2.insertNode(-10) #known minimum for testing
# 		for i in range(2,33):
# 			self.heap2.insertNode(random.randint(1, 200)*i)

# 	def test_findMin(self):
# 		self.assertEqual(self.heap.findMin().data, 0)
# 		self.assertEqual(self.heap2.findMin().data,-10)
# 		print("findMin: OK")

# 	def test_mergeHeap(self):
# 		self.heap.mergeHeap(self.heap2)
# 		self.assertEqual(self.heap.findMin().data, -10)

# 	def test_extractMin(self):
# 		self.heap.mergeHeap(self.heap2)
# 		self.heap.extractMin()
# 		self.assertEqual(self.heap.findMin().data, 0)
# 	def test_delete(self):
# 		self.heap.extractMin() # extract min to rearrange heap
# 		temp = self.heap.findMin()
# 		#temp.data = 200
# 		find = self.heap.search(temp) #look for the key
# 		self.assertEqual(find, -1) # key should not be in the heap anymore






if __name__ == '__main__':
	#unittest.main()

	print("running tests on FibHeap...")
	heap = BinomialHeap()
	print("\nFirst Heap is: \n")
	heap.insertNode(0, 77) #known minimum for testing
	for i in range(2, 7):
		heap.insertNode(random.randint(1, 200)*i, i)
	# min = heap.findMin().data
	# print("The minimum is: %d" % min)
	# heap.extractMin()
	# print("The new minimum is: % d" % heap.findMin().data)
	print heap.count
	for i in range(0, heap.count):
		print("Min is: \n")  
		print(heap.findMin())
		heap.extractMin()

