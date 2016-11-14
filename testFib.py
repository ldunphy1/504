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
		self.heap.insertNode(0) #known minimum for testing
		for i in range(2, 33):
			self.heap.insertNode(random.randint(1, 200)*i)

		print("\n\nSecond Heap is: \n")
		self.heap2 = FibHeap()
		self.heap2.insertNode(-10) #known minimum for testing
		for i in range(2,33):
			self.heap2.insertNode(random.randint(1, 200)*i)

	def test_findMin(self):
		self.assertEqual(self.heap.findMin().data, 0)
		self.assertEqual(self.heap2.findMin().data,-10)

	def test_mergeHeap(self):
		self.heap.mergeHeap(self.heap2)
		self.assertEqual(self.heap.findMin().data, -10)

	def test_extractMin(self): #getting failure here but not when i test same thing below...
		self.heap.extractMin()
		self.assertEqual(self.heap.findMin().data, 0)





if __name__ == '__main__':
	unittest.main()

	# print("running tests on FibHeap...")
	# heap = FibHeap()
	# print("\nFirst Heap is: \n")
	# heap.insertNode(0) #known minimum for testing
	# for i in range(2, 33):
	# 	heap.insertNode(random.randint(1, 200)*i)
	# # min = heap.findMin().data
	# # print("The minimum is: %d" % min)
	# # heap.extractMin()
	# # print("The new minimum is: % d" % heap.findMin().data)

	# # for i in range(heap.count):
	# # 	heap.extractMin()
	# # 	print("Min is: %d" % heap.findMin().data)
	# print("\n\nSecond Heap is: \n")
	# heap2 = FibHeap()
	# heap2.insertNode(-10) #known minimum for testing
	# for i in range(2,33):
	# 	heap2.insertNode(random.randint(1, 200)*i)
	# heap.mergeHeap(heap2)
	# print("\nMerged two heaps together")
	# # print("New Heap is: \n")
	# # heap3 = [x for x in heap.iterateList(heap.min)]
	# # for i in range(len(heap3)):
	# # 	print(heap3[i].data)
	# print("\nAfter merge min is: %d" % heap.findMin().data)





















