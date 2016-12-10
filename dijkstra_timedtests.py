# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 13:41:35 2016

@author: montgomt
"""


import csv
from graph import Graph
from time import time
import dijkstrapy3


'''create graph from file'''
def graph_from_file(filename,num_nodes):

    g = Graph()
    for i in range(1,num_nodes+1):
        g.add_vertex(str(i))
        
    with open(filename,'r') as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            g.add_edge(row[0],row[1],int(row[2]))  
    return g
        
def single_timed_test(g,u,v,structure):
    
    t0 = time()
    dijkstrapy3.dijkstra(g,g.get_vertex(u),structure)
    target = g.get_vertext(v)
    path = [target.get_id()]
    dijkstrapy3.shortest(target, path)
    t1 = time()
    
    return t1-t0
    
def repeat_timed_test(G,u,v,numtests):
    
    '''tests all graphs in G for shortest path from u to v a repeated number of
    times using all three data structures.  Returns results as a 2D list, with rows 
    representing test and columns representing data structure result for that test.'''
    
    results = [[None,None,None] for i in range(numtests)]
    for i in range(numtests):
        bin_duration = single_timed_test(G[i],str(u),str(v),'Binomial')
        fib_duration = single_timed_test(G[i],str(u),str(v),'FibHeap')
        minh_duration = single_timed_test(G[i],str(u),str(v),'Heapq')
        
        results[i] = [bin_duration,fib_duration,minh_duration]

    return results
    
if __name__ == '__main__':

    numtests = 20
    '''repeated tests of 25 node, 10% density graphs-- testing 20 graphs'''
    
    '''build graphs from edgelists'''
    g25_10 = [None]*numtests
    g50_10 = [None]*numtests
    g75_10 = [None]*numtests
    
    for i in range(numtests):
        filename25 = 'E25_10_' +str(i+1) +'.csv'
        filename50 = 'E50_10_' +str(i+1) +'.csv'
        filename75 = 'E75_10_' +str(i+1) +'.csv'
        g25_10[i] = graph_from_file(filename25,25)
        g50_10[i] = graph_from_file(filename50,50)
        g75_10[i] = graph_from_file(filename75,75)

    
    '''time dijkstra for different structures and numbers of nodes'''
    results25_10 = repeat_timed_test(g25_10,1,25,numtests)
    results50_10 = repeat_timed_test(g50_10,1,50,numtests)
    results75_10 = repeat_timed_test(g75_10,1,75,numtests)
    
   