#!/usr/bin/python

# Resources: http://opendatastructures.org/ods-python/7_2_Treap_Randomized_Binary.html
# http://www.cs.uml.edu/~jlu1/doc/source/report/BinarySearchTree1.html
import random


class Node(object): # initializes the node structure
	def __init__(self, data, key):
		self.key = key
		self.ran = random.random()
		self.right = None
		self.left = None
		self.data = data



class treap(object):
	def __init__(self):
		self.root = None

	def insert(self, element, data, key):
		if element == None:
			self.root = element
			return self.root # contains the node
		
		# traversal
		if key < element.key: 
			element.left = self.insert(element.left, data, key)
			if element.left.ran < element.ran:
				element = self.rightR(element)
		else:
			element.right = self.insert(element.right, data, key)
			element = self.leftR(element)
				
		return element
		
		
	def rightR(self, element): # rotate right
		temp = element.left
		element.left = temp.right
		temp.right = element
		element = temp
	
	def leftR(self, element): # rotate left
		temp = element.right
		element.right = temp.left
		temp.left = element
		element = temp

if __name__ == "__main__":
	print "Treap testing"