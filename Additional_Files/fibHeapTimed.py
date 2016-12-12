"""
Fib Heap implementation
"""
import math
import time

class FibHeap:

	class Node:

		def __init__(self, data, key):
			self.data = data
			self.key = key
			self.parent = self.child = None
			self.left = self.right = None
			self.degree = 0
			self.mark = False

	def __init__(self):
		self.root = None 
		self.min = None
		self.count = 0
		
	def __str__(self):
		return self.head.__str__()

	def insertNode(self, data, key):
		timelog = [[]]
		t0 = time.time()
		node = self.Node(data, key)
		node.left = node.right = node
		self.min, addToRootlog = self.addToRoot(self.min, node)
		print(node.data)
		if self.min is None or node.data < self.min.data:
			self.min = node
		self.count += 1
		t1 = time.time()
		for e in addToRootlog:
			timelog.append(['']+e)
		timelog[0] = ['insert', str(t1-t0)]
		return timelog

	def getValue(self, node):
		return node.data

	def getKey(self, node):
		return node.key

	def iterateList(self, head):
		node = stop = head
		flag = False
		while True:
			if node == stop and flag is True:
				break
			elif node == stop:
				flag = True
			yield node
			node = node.right

	def search (self, element):
		current = self.root
		index = 1
		while current != None:
		    if current.data == element:
		        return index
		    current = current.next_node
		    index += 1
		return -1

	def isEmpty(self):
		return self.min == None

	def emptyHeap(self):
		self.min = None
		self.count = 0

	def findMin(self):
		timelog = [[]]
		timelog[0] = ['findMin', str(time.time())]
		return self.min.data, self.min.key, timelog

	def addToRoot(self, head, node):
		timelog = [[]]
		t0 = time.time()
		#if root list is empty
		if head is None: 
			node.left = node.right = node 
			t1 = time.time()
			timelog[0] = ['addToRoot', str(t1-t0)]
			return node, timelog
		else:
			#else connect the node to the head of the root list
			node.left = head
			node.right = head.right
			head.right = node
			node.right.left = node
			t1 = time.time()
			timelog[0] = ['addToRoot', str(t1-t0)]
			return head, timelog
	
	def removeNode(self, head, node):
		timelog = [[]]
		t0 = time.time()
		if (node.left is None):
			return None
		node.left.right = node.right
		node.right.left = node.left
		t1 = time.time()
		timelog[0] = ['removeNode', str(t1-t0)]
		return head, timelog

	def extractMin(self):
		timelog = [[]]
		t0 = time.time()
		x = self.min #temp var for min
		if x is not None:
			if x.child is not None:
				print("\n\niterating childlist")
				#iterate child node list:
				child = [x for x in self.iterateList(x.child)]
				for i in range(0, len(child)):
					print(child[i].data)
					print("Moving kids to root list...")
					self.min, addToRootlog = self.addToRoot(self.min, child[i]) #move children to root list
					child[i].parent = None
				for e in addToRootlog:
					timelog.append(['']+e)
			if(x == x.right):
				self.count -= 1 
				self.min, removeNodelog = self.removeNode(x, self.min)
				for e in removeNodelog:
					timelog.append(['']+e)
				t1 = time.time()
				timelog[0] = ['extractMin', str(t1-t0)]
				return x.data, x.key, timelog
			else:
				self.min, removeNodelog = self.removeNode(x, self.min)
				self.min = x.right # point to other node in root list
				consolidatelog = self.consolidate()
				self.count -= 1 #decrease node count
				for e in removeNodelog:
					timelog.append(['']+e)
				for e in consolidatelog:
					timelog.append(['']+e)
				t1 = time.time()
				timelog[0] = ['extractMin', str(t1-t0)]
				return x.data, x.key, timelog

	def consolidate(self):
		timelog = [[]]
		t0 = time.time()
		#consolidate according to fib heap rules
		tempList = [None] * self.count
		nodeList = [x for x in self.iterateList(self.min)] 
		for i in range(0, len(nodeList)):
			x = nodeList[i]
			dx = x.degree
			while (tempList[dx] is not None):
				y = tempList[dx]
				if (x.data > y.data):
					temp = x
					x = y
					y = temp #exchange x and y
				makeChildlog = self.makeChild(x,y)
				for e in makeChildlog:
					timelog.append(['']+e)
				tempList[dx] = None
				dx += 1
			tempList[dx] = x
			min = None #end iteration
		# find new minimum
		for i in range(0, len(tempList)):
			if(tempList[i] is not None):
				self.min, addToRootlog = self.addToRoot(self.min, tempList[i])
				if (self.min is None or tempList[i].data < self.min.data):
					self.min = tempList[i] # reassign min pointer
		
		for e in addToRootlog:
			timelog.append(['']+e)
		t1 = time.time()
		timelog[0] = ['consolidate', str(t1-t0)]
		return timelog				

	def makeChild(self, head, node):
		timelog = [[]]
		t0 = time.time()
		self.min, removeNodelog = self.removeNode(head,node)
		node.parent = head
		node.left = node.right = node
		head.child, addToRootlog = self.addToRoot(head.child, node) #create root list for child node
		head.degree += 1
		node.mark = False #set mark to false
		for e in removeNodelog:
			timelog.append(['']+e)
		for e in addToRootlog:
			timelog.append(['']+e)
		t1 = time.time()
		timelog[0] = ['makeChild', str(t1-t0)]
		return timelog	

	def delete(self,node):
		self.decreaseKey(node,-math.inf)
		self.extractMin()
		
	def decreaseKey(self, key, newKey):	
		timelog = [[]]
		t0 = time.time()
		if (newKey > key.data):
			print("ERROR new key is greater than old key... doing nothing")
			return None
		key.data = newKey
		y = key.parent # set parent of key ptr to y
		if ((y is not None) and key.data < y.data):
			cutlog = self.cut(key, y)
			cascadingCutlog = self.cascadingCut(y)
		if (key.data < self.min.data):
			self.min = key
		for e in cutlog:
			timelog.append(['']+e)
		for e in cascadingCutlog:
			timelog.append(['']+e)
		t1 = time.time()
		timelog[0] = ['decreaseKey', str(t1-t0)]
		return timelog

	def cut(self, child, parent):
		timelog = [[]]
		t0 = time.time()
		parent.child, removeNodelog = removeNode(parent.child, child) 
		parent.degree -= 1
		self.min, addToRootlog = self.addToRoot(self.min, child)
		child.parent = None #child has no more parent anymore
		child.mark = False
		for e in removeNodelog:
			timelog.append(['']+e)
		for e in addToRootlog:
			timelog.append(['']+e)
		t1 = time.time()
		timelog[0] = ['cut', str(t1-t0)]
		return timelog

	def cascadingCut(self, node):
		timelog = [[]]
		t0 = time.time()
		x = node.parent #x is ptr to node's parent
		if x is not None:
			if node.mark is False:
				node.mark = True
			else:
				cutlog = self.cut(node, x)
				cascadingCutlog = self.cascadingCut(x)
		for e in cutlog:
			timelog.append(['']+e)
		for e in cascadingCutlog:
			timelog.append(['']+e)
		t1 = time.time()
		timelog[0] = ['cascadingCut', str(t1-t0)]
		return timelog

	def mergeHeap(self, heap):
		timelog = [[]]
		t0 = time.time()
		self.min, addToHeaplog = self.addToHeap(self.min, heap.min)
		if((self.min is None) or (heap.min is not None and heap.min.data < self.min.data)):
			self.min = heap.min
		self.count += heap.count
		for e in addToHeaplog:
			timelog.append(['']+e)
		t1 = time.time()
		timelog[0] = ['mergeHeap', str(t1-t0)]
		return timelog

	def addToHeap(self, node1, node2):
		timelog = [[]]
		t0 = time.time()
		if(node1 is None):
			t1 = time.time()
			timelog[0] = ['addToHeap', str(t1-t0)]
			return node2, timelog
		elif(node2 is None):
			t1 = time.time()
			timelog[0] = ['addToHeap', str(t1-t0)]
			return node1, timelog
		else:
			node1.right.left = node2.left
			node2.left.right = node1.right
			node2.right = node1
			node1.left = node2
			t1 = time.time()
			timelog[0] = ['addToHeap', str(t1-t0)]
			return node1, timelog
			
			