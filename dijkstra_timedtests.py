# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 13:41:35 2016

@author: montgomt
"""
from itertools import combinations
from imp import reload
import csv
from graph import Graph
from time import time
import dijkstra
reload(dijkstra)
import os

def graph_from_file(filename,num_nodes):
    '''reads edgelist from file and creates a graph object'''
    
    g = Graph()
    for i in range(1,num_nodes+1):
        g.add_vertex(str(i))
        
    with open(filename,'r') as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            g.add_edge(row[0],row[1],int(row[2]))  
    return g
        
def single_timed_test(g,u,v,structure):
    '''runs a single instance of the Dijkstra algorithm on a graph g with starting 
    node u and ending node v.  structure refers to the type data structure used'''
    
    t0 = time()
    dijkstra.dijkstra(g,g.get_vertex(u),structure)
    target = g.get_vertex(v)
    path = [target.get_id()]
    dijkstra.shortest(target, path)
    t1 = time()
    
    return t1-t0
    
def repeat_timed_test(G,u,v,numtests):
    
    '''tests all graphs in G for shortest path from u to v a repeated number of
    times using all three data structures.  Returns results as a 2D list, with rows 
    representing test and columns representing data structure result for that test.'''
    
    results = [[None,None,None] for i in range(numtests)]
    for i in range(numtests):
        print(' Running Test #',i)
        bin_duration = single_timed_test(G[i],str(u),str(v),'Binomial')
        fib_duration = single_timed_test(G[i],str(u),str(v),'FibHeap')
        minh_duration = single_timed_test(G[i],str(u),str(v),'Heapq')
        
        results[i] = [bin_duration,fib_duration,minh_duration]

    return results
    
'''------------run the tests when file is executed--------------'''
if __name__ == '__main__':

    '''Testing by graph size in number of nodes and by density
    There are 'numtests' versions of each graph for each size/density'''
    
    numtests = 5
    
    '''graph containers'''
    g100_10 = [None]*numtests
    g200_10 = [None]*numtests
    g300_10 = [None]*numtests
    g400_10 = [None]*numtests
    g500_10 = [None]*numtests
    
    g100_75 = [None]*numtests
    g200_75 = [None]*numtests
    g300_75 = [None]*numtests
    g400_75 = [None]*numtests
    g500_75 = [None]*numtests
    
    '''build graphs for each test of each graph size and density'''
    script_dir = os.path.dirname("__file__")
    for i in range(numtests):
        filename100_10 = os.path.join(script_dir,'Edgelists/E100_10_' +str(i+1) +'.csv')
        filename200_10 = os.path.join(script_dir,'Edgelists/E200_10_' +str(i+1) +'.csv')
        filename300_10 = os.path.join(script_dir,'Edgelists/E300_10_' +str(i+1) +'.csv')
        filename400_10 = os.path.join(script_dir,'Edgelists/E400_10_' +str(i+1) +'.csv')
        filename500_10 = os.path.join(script_dir,'Edgelists/E500_10_' +str(i+1) +'.csv')
        filename100_75 = os.path.join(script_dir,'Edgelists/E100_75_' +str(i+1) +'.csv')
        filename200_75 = os.path.join(script_dir,'Edgelists/E200_75_' +str(i+1) +'.csv')
        filename300_75 = os.path.join(script_dir,'Edgelists/E300_75_' +str(i+1) +'.csv')
        filename400_75 = os.path.join(script_dir,'Edgelists/E400_75_' +str(i+1) +'.csv')
        filename500_75 = os.path.join(script_dir,'Edgelists/E500_75_' +str(i+1) +'.csv')
        
        g100_10[i] = graph_from_file(filename100_10,100)
        g200_10[i] = graph_from_file(filename200_10,200)
        g300_10[i] = graph_from_file(filename300_10,300)
        g400_10[i] = graph_from_file(filename400_10,400)
        g500_10[i] = graph_from_file(filename500_10,500)
        g100_75[i] = graph_from_file(filename100_75,100)
        g200_75[i] = graph_from_file(filename200_75,200)
        g300_75[i] = graph_from_file(filename300_75,300)
        g400_75[i] = graph_from_file(filename400_75,400)
        g500_75[i] = graph_from_file(filename500_75,500)
        
    r100to500_10 = [None]*5
    print('Running Dijkstra tests for 100 nodes,10% density...')
    r100to500_10[0] = repeat_timed_test(g100_10,1,100,numtests)
    print('Running Dijkstra tests for 200 nodes,10% density...')
    r100to500_10[1] = repeat_timed_test(g200_10,1,200,numtests)
    print('Running Dijkstra tests for 300 nodes,10% density...')
    r100to500_10[2]= repeat_timed_test(g300_10,1,300,numtests)
    print('Running Dijkstra tests for 400 nodes,10% density...')
    r100to500_10[3] = repeat_timed_test(g400_10,1,400,numtests)
    print('Running Dijkstra tests for 500 nodes,10% density...')
    r100to500_10[4] = repeat_timed_test(g500_10,1,500,numtests)
    
    r100to500_75 = [None]*5
    print('Running Dijkstra tests for 100 nodes,75% density...')
    r100to500_75[0] = repeat_timed_test(g100_75,1,100,numtests)
    print('Running Dijkstra tests for 200 nodes,75% density...')
    r100to500_75[1] = repeat_timed_test(g200_75,1,200,numtests)
    print('Running Dijkstra tests for 300 nodes,75% density...')
    r100to500_75[2]= repeat_timed_test(g300_75,1,300,numtests)
    print('Running Dijkstra tests for 400 nodes,75% density...')
    r100to500_75[3] = repeat_timed_test(g400_75,1,400,numtests)
    print('Running Dijkstra tests for 500 nodes,75% density...')
    r100to500_75[4] = repeat_timed_test(g500_75,1,500,numtests)
  
    for n in range(100,200,100):
        
        filename = 'results' +str(n)+'_10.csv'
        with open(filename,'wb') as f:
            writer = csv.writer(f,delimiter=',')
            for i in range(numtests):
                writer.writerow(r100to500_10[int(n/100)-1][i])
        
        filename = 'results' +str(n)+'_75.csv'
        with open(filename,'wb') as f:
            writer = csv.writer(f,delimiter=',')
            for i in range(numtests):
                writer.writerows(r100to500_75[int(n/100)-1][i])
                
    
    '''Testing by trying all combinations of start/finish nodes
    ***Currently only runs test on one graph..need to change hardcode to use different ones***'''
    
    sfnodes = list(combinations(range(1,200),2))
    results_combos = [None]*len(sfnodes)
    
    for i,combo in enumerate(sfnodes):
        print('Start/Finish combination test #', i)
        results_combos[i] = repeat_timed_test(g200_10,combo[0],combo[1],1)
    
    with open('results_combos_200.csv','wb') as fn:
        writer = csv.writer(fn,delimiter=',')
        for row in results_combos:
            writer.writerow(row)
            
       
   
    