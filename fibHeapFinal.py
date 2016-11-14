"""
Fib Heap implementation

would like to implement better way to iterate that is faster

"""
import math

class FibHeap:

	class Node:

		def __init__(self, data):
			self.data = data
			self.parent = self.child = None
			self.left = self.right = None
			self.degree = 0
			self.mark = False

	def __init__(self):

		self.root = None
		self.min = None
		self.count = 0
		#print("Creating new FibHeap...")

	def insertNode(self, data):
		node = self.Node(data)
		node.left = node.right = node
		self.min = self.addToRoot(self.min, node)
		print(node.data)

		if self.min is None or node.data < self.min.data:
			self.min = node

		self.count += 1


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


	def isEmpty(self):
		return root == None

	def emptyHeap(self):
		min = None
		count = 0

	def findMin(self):
		return self.min

	def addToRoot(self, head, node):

		if head is None:
			node.left = node.right = node
			return node
		else:
			node.left = head
			node.right = head.right
			head.right = node
			node.right.left = node
			return head
	
	def removeNode(self, head, node):
		if (node.left is None):
			return None
		node.left.right = node.right
		node.right.left = node.left
		return head

	def extractMin(self):

		x = self.min #temp var for min
		if x is not None:
			if x.child is not None:
				#print("\n\niterating childlist")
				#iterate child node list:
				child = [x for x in self.iterateList(x.child)]
				for i in range(0, len(child)):
					#print("Moving kids to root list...")
					self.min = self.addToRoot(self.min, child[i]) #move children to root list
					x.parent = None
			#print("removing min assigning as rando num")
			self.min = self.removeNode(self.min, x)

			if(x == x.right):
				self.emptyHeap() #node is alone in heap... empty it
			else:
				self.min = x.right # point to other node in root list
				self.consolidate()
		self.count -= 1 #decrease node count

	def consolidate(self):

		#consolidate according to fib heap rules
		tempList = [None] * self.count
		nodeList = [x for x in self.iterateList(self.min)] 
		for i in range(0, len(nodeList)):
			x = nodeList[i]
			dx = x.degree
			while (tempList[dx] is not None):
				y = tempList[dx]

				if (x.data > y.data):
					#print(x.data), print("Is larger than "), print(y.data)
					temp = x
					x = y
					y = temp #exchange x and y

				self.makeChild(x,y)
				tempList[dx] = None
				dx += 1
			tempList[dx] = x
			min = None #end iteration

		# find new minimum
		for i in range(0, len(tempList)):
			if(tempList[i] is not None):
				self.min = self.addToRoot(self.min, tempList[i])
				if (self.min is None or tempList[i].data < self.min.data):
					self.min = tempList[i] # reassign min pointer


	def makeChild(self, head, node):
		self.min = self.removeNode(self.min, node)

		node.parent = head
		node.left = node.right = node
		head.child = self.addToRoot(head.child, node) #create root list for child node

		head.degree += 1
		node.mark = False #set mark to false

	def delete(self,node):
		
		self.decreaseKey(node,-math.inf)
		self.extractMin()


	def decreaseKey(self, key, newKey):
		
		if (newKey > key.data):
			print("ERROR new key is greater than old key... doing nothing")
			return None

		key.data = newKey
		y = key.parent # set parent of key ptr to y

		if ((y is not None) and key.data < y.data):
			self.cut(key, y)
			self.cascadingCut(y)

		if (x.data < self.min.data):
			self.min = x

	def cut(self, child, parent):
		parent.child = removeNode(parent.child, child)
		parent.degree -= 1
		self.min = self.addToRoot(self.min, child)

		child.parent = None #child has no more parent anymore
		child.mark = False

	def cascadingCut(self, node):
		x = node.parent #x is ptr to node's parent

		if x is not None:
			if node.mark is False:
				node.mark = True

			else:
				self.cut(node, x)
				self.cascadingCut(x)

	def mergeHeap(self, heap):
		self.min = self.addToHeap(self.min, heap.min)

		if((self.min is None) or (heap.min is not None and heap.min.data < self.min.data)):
			self.min = heap.min

		self.count += heap.count

	def addToHeap(self, node1, node2):
		if(node1 is None):
			return node2

		elif(node2 is None):
			return node1

		else:
			node1.right.left = node2.left
			node2.left.right = node1.right

			node2.right = node1
			node1.left = node2
			return node1