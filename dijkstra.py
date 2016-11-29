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
import heapq # example using heapq
from fibHeapFinal import FibHeap


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
        shortest(v.previous, path)
    return


def dijkstra(aGraph, start):

	# Initialize new FibHeap
	fib = FibHeap()

	# Set the distance for the start node to zero
	start.set_distance(0)

	# Put the tuple pair into the priority queue
	unvisited_queue = [(v.get_distance,v) for v in aGraph]
	for index, item in enumerate(unvisited_queue):
		fib.insertNode(index) # index of v is how its stored in queue

	heapq.heapify(unvisited_queue)
	while not fib.isEmpty() and len(unvisited_queue):
		#pop vertex with smallest distance
		#uv = heapq.heappop(unvisited_queue)
		uv = fib.extractMin() #get index of smallest element stored in tree
		print uv
		lala = unvisited_queue[uv]
		print "uv is: " 
		current = lala[1]
		#current = uv[1]
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
				print('updated current = %s next = %s new_dist = %s'
					%(current.get_id(), next.get_id(), next.get_distance()))

			else:
				print('not updated: current = %s next = %s new_dist = %s'
					%(current.get_id(), next.get_id(), next.get_distance()))


		# Rebuild heap
		# 1. Pop every item
		# for i in range(0,fib.count):
		# 	print "Min is: %d" % fib.findMin()
		# 	fib.extractMin()
			#heapq.heappop(unvisited_queue)
		# 2. Put all vertices not visited into the queue
		#unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
		# print "HJDHAKJD"
		# print len(unvisited_queue)

		# #heapq.heapify(unvisited_queue)
		# for index, item in enumerate(unvisited_queue):
		# 	fib.insertNode(index)


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

	print ("Graph data:")
	for v in g:
		for w in v.get_connections():
			vid = v.get_id()
			wid = w.get_id()
			print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))


	dijkstra(g, g.get_vertex('a')) 

	target = g.get_vertex('f')
	path = [target.get_id()]
	shortest(target, path)
	print ('The shortest path : %s' %(path[::-1]))
