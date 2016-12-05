# -*- coding: utf-8 -*-

'''
Python implementation of dijkstra's algorithm:
The value that is used to determine the order of the 
objects in the priority queue is distance. 
When a vertex is first created distance 
is set to a very large number.
Will use this to compare the efficiency between priority 
queue data structures
'''

# Add dependency files and modules
import sys
from graph import Graph
from vertex import Vertex
import heapq 
from fibHeapFinal import FibHeap
from binomialheap import BinomialHeap
from time import time
import random


'''
Pseudocode:
  function Dijkstra(Graph, source):
      create vertex set Q
      for each vertex v in Graph:             // Initialization
          dist[v] ← INFINITY                  // Unknown distance from source to v
          prev[v] ← UNDEFINED                 // Previous node in optimal path from source
          add v to Q                          // All nodes initially in Q (unvisited nodes)
      dist[source] ← 0                        // Distance from source to source
      
      while Q is not empty:
          u ← vertex in Q with min dist[u]    // Source node will be selected first
          remove u from Q 
          
          for each neighbor v of u:           // where v is still in Q.
              alt ← dist[u] + length(u, v)
              if alt < dist[v]:               // A shorter path to v has been found
                  dist[v] ← alt 
                  prev[v] ← u 
      return dist[], prev[]
'''

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        print "The path is now: " 
        print path
        shortest(v.previous, path)
    return


def dijkstra(aGraph, start, queue = "FibHeap"):


	# Set the distance for the start node to zero
	start.set_distance(0)

	# Put the tuple pair into the priority queue
	unvisited_queue = [(v.get_distance,v) for v in aGraph]
	pyheap = False #building and rebuilding this queue is different can eventually just change background code

	if queue == "FibHeap":
		print "Using Fiobonnaci Heap Structure...\n"
		# Initialize new FibHeap
		obj = FibHeap()
	elif queue == "Heapq":
		print "Using Heapq Data Structure From Python...\n"
		pyheap = True
	elif queue == "Binomial":
		print "Using Binomial Heap Structure...\n"
		obj = BinomialHeap()

	if not pyheap:
		for index, item in enumerate(unvisited_queue):
			obj.insertNode(item[1].get_distance(), item)
			for next in item[1].adjacent:
				obj.insertNode(item[1].get_weight(next) + item[1].get_distance(), next) #store in tree based on weights
		
		while(len(unvisited_queue)):
			min, key = obj.extractMin()
			print key
			current = key[1]
			print current
			current.set_visited() #set vertex to visited 

			# now visit adj nodes
			for next in current.adjacent:
				#if already visited just skip
				if next.visited:
					print "adj node already visited"
					continue
				new_dist = current.get_distance() + current.get_weight(next)

				#check if new_dist is smaller
				if new_dist < next.get_distance():
					next.set_distance(new_dist)
					next.set_previous(current)
					print 'updated : current = %s next = %s new_dist = %s' % (current.get_id(), next.get_id(), next.get_distance())
			# rebuild heap
			obj.emptyHeap()
			unvisited_queue = [(v.get_distance, v) for v in aGraph if not v.visited]
			for index, item in enumerate(unvisited_queue):
				obj.insertNode(item[1].get_distance(), item)
				for next in item[1].adjacent:
					 obj.insertNode(item[1].get_weight(next) + item[1].get_distance(), next) #store in tree based on weights

	if (pyheap):

		heapq.heapify(unvisited_queue) #add unvisted nodes to heap

		while (len(unvisited_queue)):
			#pop vertex with smallest distance
			for index, item in enumerate(unvisited_queue):
				print index, item[1].get_distance()
			min = heapq.heappop(unvisited_queue)
			current = min[1]
			print current
			current.set_visited()
			
			#for next in v.adj
			for next in current.adjacent:
				#if visited we dont care so skip
				if next.visited:
					print "adj node has been visited already"
					continue
				new_dist = current.get_distance() + current.get_weight(next)

				if new_dist < next.get_distance():
					next.set_distance(new_dist)
					next.set_previous(current)
					print 'updated : current = %s next = %s new_dist = %s' % (current.get_id(), next.get_id(), next.get_distance())


			#Rebuild heap
			#1. Pop every item
			while len(unvisited_queue):
				heapq.heappop(unvisited_queue)
			
			#2. Put all vertices not visited into the queue
			unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]

			heapq.heapify(unvisited_queue)


if __name__ == '__main__':

	g = Graph()

	g.add_vertex('a')
	g.add_vertex('b')
	g.add_vertex('c')
	g.add_vertex('d')
	g.add_vertex('e')
	g.add_vertex('f')

	g.add_edge('a', 'b', 7)  
	g.add_edge('a', 'c', 9)
	g.add_edge('a', 'f', 14)
	g.add_edge('b', 'c', 10)
	g.add_edge('b', 'd', 15)
	g.add_edge('c', 'd', 11)
	g.add_edge('c', 'f', 2)
	g.add_edge('d', 'e', 6)
	g.add_edge('e', 'f', 9)
	g.add_edge('e', 'g', 18)
	g.add_edge('c','e', 5)
	g.add_edge('f','g', 4)

	print ("Graph data:")
	for v in g:
		for w in v.get_connections():
			vid = v.get_id()
			wid = w.get_id()
			print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

	print "Starting time to calc shortest path in graph...\n"
	t0 = time() #start
	dijkstra(g, g.get_vertex('a'), "Binomial") 

	target = g.get_vertex('g')
	path = [target.get_id()]
	shortest(target, path)
	print ('The shortest path : %s' %(path[::-1]))
	print("done in %.5fs"%(time()-t0))
