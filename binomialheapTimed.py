
# -*- coding: utf-8 -*-
"""
Binomial Heap based on pseudocode found in Ch. 19 of CLRS 'Intro. to Algorithms' (2001) 
"""

import time

class BinomialHeap():

    class node():
        def __init__(self,value, key):  # key is vertex, value is weight
            self.value = value
            self.key = key
            self.degree = 0
            self.parent = None
            self.child = None
            self.sibling = None
            
            
        def __str__(self,indent=0):
            '''Basic printout for nodes in tree. Level of indentation = depth in tree.
            For each new line, +1 indentation indicates a child node.  -1 indentation
            indicates moving to a different branch in a tree.  0 indentation indicates
            a root node and thus any +indentation will be part of that root's tree
            until the next root node occurs.'''
            
            ret = "  "*indent+str(self.value)
            
            if self.child != None:
                ret += "\n" + self.child.__str__(indent+1)
            
            if self.sibling != None:
                ret += "\n" + self.sibling.__str__(indent)
                
            return ret

    def __init__(self):
        self.head = None 
        self.count = 0  
        
    def __str__(self):
        return self.head.__str__()
            
    def insertNode(self,value, key): #value will be the weight and the key is the vertex
        timelog = [[]]
        t0 = time.time()
        temp = BinomialHeap()
        n = self.node(value, key)
        temp.head = n
        unionlog = self.union(temp)
        self.count +=1 #increase node count
        
        
        t1 = time.time()
        for e in unionlog:
            timelog.append(['']+e)
            
        timelog[0] = ['insert',str(t1-t0)]
        
        return timelog

    def emptyHeap(self):
        #need this to clear heap in dijkstra
        self.head = None
        self.count = 0

    def isEmpty(self):
        #boolean method to check if heap empty
        return self.head == None

    def extractMin(self):
        '''will return the minimum node's value, its key, and an accounting of the major operation times'''
        
        timelog = [[]]
        extratime = 0
        t0 = time.time()        
        iternode = self.head 
        minkey = iternode.value
        minnode = iternode #will store ref to minimum node 
        minprev = None #ref to upstream node from min node
        
        '''find minimum node in root list'''
        while iternode.sibling != None:
            nextnode = iternode.sibling           
            nextkey = nextnode.value
            if nextkey < minkey:
                minkey = nextkey
                minnode = nextnode
                minprev = iternode
            iternode = nextnode
        
        current = minnode.child
        tempheap = BinomialHeap()
        
        if current != None:
            '''if minimum node has children, reverse order of their linked list'''
            
            prev = None
            nxt = current.sibling
            current.parent = None

            while nxt != None:
                current.sibling = prev
                prev = current  
                current = nxt 
                nxt = current.sibling 
                
            current.sibling = prev
            current.parent = None
            
            '''set former last child as head of temp heap'''    
            tempheap.head = current
                        
            '''remove minimum node, reassign head if needed'''
            if self.head == minnode:
                self.head = self.head.sibling
            else:
               minprev.sibling = minnode.sibling
            
            '''unify original root list (minus minimum) w/ min node's child list''' 
            unionlog = self.union(tempheap)
            
            '''-------time logging----'''
            tx = time.time()
            for e in unionlog:
                timelog.append(['']+e)  
            extratime += time.time()-tx
            '''-----------------------'''
            
        else:
            '''no children, existing BinomialHeap valid. Remove w/o rebalancing'''
            self.head = self.head.sibling
        
        t1 = time.time()
        timelog[0] = ['extractMin', str(t1-t0-extratime)]
        
        return minkey, minnode.key, timelog
                
        
    def decrease_key(self,n,value):
        if n.value < value:
            print('Error, new key larger than old key')
            return
            
        n.value = value
        y = n
        z = y.parent
        
        while z != None and y.value < z.value:
            tempval = y.value
            y.value = z.value
            z.value = tempval
            y = z
            z = y.parent
            
    def delete(self,n):
        self.decrease_key(n,float('-inf'))
        self.extractMin()


    def link(self,y,z):
        timelog = [[]]
        t0 = time.time()
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1
        t1 = time.time()
        timelog[0] = ['link', str(t1-t0)]
        return timelog
        
    def merge(self,H2):
        timelog = [[]]
        t0 = time.time()
        
        if not self.head:
            self.head = H2.head #Joining empty list, no need to continue
            
            t1 = time.time()
            timelog[0] = ['merge',str(t1-t0)]
            return self.head, timelog
            
        a = self.head
        b = H2.head
    
        if b.degree < a.degree:
            '''choose head of combined rootlist to be smaller of the two list heads'''
            self.head = b
        
        if self.head == b:
            '''H2 head is overall head, H1 head is now the second in line'''
            b = a
            
        a = self.head
        
        
        while b != None:
            '''iterate over root list until none remain'''
            
            if a.sibling == None:
                '''first list only has head, simply append it to second list'''
                a.sibling = b
                t1 = time.time()
                timelog[0] = ['merge',str(t1-t0)]
                return self.head, timelog
                
            elif a.sibling.degree < b.degree:
                '''a's sibling smaller degree than other. Compare a.sibling to b next'''
                a = a.sibling

            else:
                '''b smaller/ or the same degree as a. Make b.sibling next 
                comparison, and put b next to a in combined rootlist'''
                c = b.sibling
                b.sibling = a.sibling
                a.sibling = b
                a = a.sibling
                b = c
       
        del H2
        t1 = time.time()
        timelog[0] = ['merge',str(t1-t0)]
        
        return self.head, timelog
        
    def union(self,H2):
        timelog = [[]]
        extratime = 0
        t0 = time.time()        
        H = self     
        H.head, mergelog = self.merge(H2)
        
        '''-------time logging----'''
        tx = time.time()
        for e in mergelog:
            timelog.append(['']+e)
        extratime += time.time()-tx
        '''-----------------------'''
        
        if H.head == None:
              return timelog
        
        prev = None
        x = H.head
        after = x.sibling

        self.count += H2.count


        while after != None:
            if (x.degree != after.degree) or (after.sibling != None and after.sibling.degree == x.degree):
                prev = x
                x = after
            else:
                if x.value <= after.value:

                    x.sibling = after.sibling
                    linklog = self.link(after,x)
                    
                         
                else:
                    if prev == None:
                        H.head = after

                    else:
                        prev.sibling = after
                        
                    linklog = self.link(x,after)
                    x = after
                      
                '''-------time logging----'''
                tx = time.time()
                for e in linklog:
                    timelog.append(['']+e)
                extratime += time.time() - tx
                
                '''-----------------------'''
                
            after = x.sibling
        t1 = time.time()
        timelog[0] = ['union',str(t1-t0)]
        
        return timelog
    
    def findMin(self):
        '''Returns reference to the minimum node in the heap'''
        
        y = None
        x = self.head 
        
        m = float('inf')
        
        while x != None:
            if x.value < m:
                m = x.value
                y = x
            x = x.sibling   
        return y