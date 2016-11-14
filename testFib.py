"""

Test script for fibonacci heap 
implementation 

"""

from heapfib2 import FibHeap
import random


if __name__ == '__main__':

	print("running tests on FibHeap...")
	heap = FibHeap()
	print("\nFirst Heap is: \n")
	for i in range(2, 33):
		heap.insertNode(random.randint(1, 200)*i)
	min = heap.findMin().data
	print("The minimum is: %d" % min)
	heap.extractMin()
	print("The new minimum is: % d" % heap.findMin().data)

	# for i in range(heap.count):
	# 	heap.extractMin()
	# 	print("Min is: %d" % heap.findMin().data)
	print("\n\nSecond Heap is: \n")
	heap2 = FibHeap()
	for i in range(2,33):
		heap2.insertNode(random.randint(1, 200)*i)
	heap.mergeHeap(heap2)
	# print("\nMerged two heaps together")
	# print("New Heap is: \n")
	# heap3 = [x for x in heap.iterateList(heap.min)]
	# for i in range(heap.count):
	# 	print(heap3[i])
	print("\nAfter merge min is: %d" % heap.findMin().data)





















