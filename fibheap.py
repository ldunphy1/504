# Python Implementation of Fibonacci Heap Data Structure 

import math

class FibHeap:
	n = 0
	min, root = None, None
	
	class Node:

		def __init__(self, key):
			self.key = key
			self.degree = 0
			self.left = self.right = self.parent = self.child = None
			self.mark = False
			
	def findMin(self):
		return self.min
		
	def Link(self, y, x):
		
		min = self.removefromRoot(x, y)

		y.parent = x
		y.left = y
		y.right = y
		x.child = self.addToRoot(x.child, y)

		x.degree += 1
		y.mark = False

		# if x.child is None:
		# 	x.child = y 
		# else:
		# 	x.right = y.child.right
		# 	x.left = y.child
		# 	y.child.right.left = x
		# 	y.child.right = x
		# y.parent = x
		# x.degree += 1
		# y.mark = False

	def addToRoot(self, head, node):
		if head == None:
			node.right = node
			node.left = node
			return node
		else:
			node.left = head
			node.right = head.right
			head.right = node
			node.right.left = node
			return head

		
	def Consolidate(self):
		if min is None:
			return
		A = [None] * self.upperBound()
		rootList = []
		rootList.append(self.listIter(root))
		for rootedNode in range(0, len(rootList)):
			x = rootedNode
			d = x.degree
			while A[d] is not None:
				y = A[d]
				if x.key > y.key:
					temp = x
					x = y
					y = temp
				self.Link(y, x)
				A[d] = None
				d += 1
			A[d] = x
		self.min = None
		for i in range(0, self.upperBound()):
			if A[i] is not None:
				if self.min is None:
					self.min = A[i]
				else:
					self.mergewithRoot(A[i])
					if A[i].key < self.min.key:
						self.min = A[i]
	
	def mergewithRoot(self, node):
		if self.root is None:
			self.root = node
		else:
			node.right = self.root.right
			node.left = self.root
			self.root.right.left = node
			self.root.right = node					
	
	def upperBound(self):
		D = math.floor(math.log10(self.n))
		return D
		
	# def listIter(self, node):
	# 	current = node
	# 	while current is not None:
	# 		yield current
	# 		current = current.right

	def listIter(self, head):
		node = stop = head
		flag = False
		while True:
			if node == stop and flag is True:
				break
			elif node == stop:
				flag == True
			yield node
			node = node.right
		
	def removefromRoot(self, head, node):
		if node.left == node:
			#node points at itself
			return None
		node.left.right = node.right #disconnect from root
		node.right.left = node.left
		return head
		# if node == self.root:
		# 	self.root = node.right
		# node.left.right = node.right
		# node.right.left = node.left
		
	def Union(self, H1, H2):
		H = FibHeap()
		if H1.min is None and H2.min is None:
			return H
		elif H2.min is not None and H2.min.key < H1.min.key:
			H.min = H2.min
		else:
			H.min = H1.min
		H.mergewithRoot(H2.root)
		H.n = H1.n + H2.n
		return H
		
	def Insert(self, k):
		x = self.Node(k)
		if self.min is None:
			self.min = x
		else:
			self.mergewithRoot(x)
			if x.key < self.min.key:
				self.min = x
		self.n += 1
		
	def extractMin(self):
		minNode = self.min
		if x is not None:
			children = []
			children.append(self.listIter(minNode.child))
			for x in range(0, len(children)):
				self.mergewithRoot(x)
				x.parent = None
				self.removefromRoot(minNode)
				if minNode == minNode.right:
					self.min = None
				else:
					self.min = minNode.right
					self.Consolidate()
		return minNode
		
	def decreaseKey(self, x, k):
		if k > x.key:
			return None
		x.key = k
		y = x.parent
		if y is not None and x.key < y.key:
			self.Cut(x, y)
			self.cascadingCut(y)
		if x.key < self.min.key:
			self.min = x
			
	def Cut(self, x, y):
		x.left.right = x.right
		x.right.left = x.left
		y.degree = y.degree - 1
		y.child = x.right
		if x == x.right:
			y.child = None
		self.mergewithRoot(x)
		x.parent = None
		x.mark = False
		
	def cascadingCut(self, node):
		z = node.parent
		if node.mark is False:
			node.mark = True
		else:
			self.Cut(node, z)
			self.cascadingCut(z)
	def Delete(self, node):
		self.decreaseKey(node, float('-inf'))
		self.extractMin()
