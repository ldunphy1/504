# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:31:18 2016

@author: montgomt
"""


        
class node():
    def __init__(self,value = None):
        self.value = value
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
      
class BinomialHeap():
    def __init__(self):
        self.head = None   
        
    def __str__(self):
        return self.head.__str__()
            
    def insert(self,key):
        temp = BinomialHeap()
        n = node(key)
        temp.head = n
        self.union(temp)

    def extract_min(self):
        n = self.head
        minkey = n.value
        minnode = n
        
        '''find minimum node in root list'''
        while n.sibling != None:
            nextnode = n.sibling
            nextkey = nextnode.value
            if nextkey < minkey:
                minkey = nextkey
                minnode = nextnode
            n = nextnode
        
        '''reverse minimum node's children'''
        h = BinomialHeap()
        n = minnode.child
        n.parent = None
        
        prev = None
        current = n
        nxt = n.sibling
        current.parent = None
        
        while nxt != None:
            current.sibling = prev
            current.parent = None
            
            prev = current  
            current = nxt 
            nxt = current.sibling 
            
        current.sibling = prev
        current.parent = None
            
        '''set last child as head of temp heap'''    
        h.head = current
        
        '''remove minimum from root list'''
        self.head = minnode.sibling
        self.union(h)
        
        '''return extracted value'''
        return minkey
        
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
        self.extract_min()


    def link(self,y,z):
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1
        
    def merge(self,H2):
        
        if not self.head:
            self.head = H2.head #Joining empty list, no need to continue
            return self.head
            
        a = self.head
        b = H2.head
    
        '''choose head of combined rootlist to be smaller of the two list heads'''
        if b.degree < a.degree:
            self.head = b
        
        if self.head == b:
            '''H2 head is overall head, H1 head is now the second in line'''
            b = a
            
        a = self.head
        
        '''iterate over root list until none remain'''
        while b != None:
            
            if a.sibling == None:
                '''first list only has head, simply append it to second list'''
                a.sibling = b
                return self.head
                
            elif a.sibling.degree < b.degree:
                '''a's sibling is smaller degree than other choice. Make sibling 
                next root to compare to b'''
                a = a.sibling

            else:
                '''b is smaller or the same degree as a. Make b's sibling next 
                comparison, and put b next to a in combined rootlist'''
                c = b.sibling
                b.sibling = a.sibling
                a.sibling = b
                a = a.sibling
                b = c

                
        del H2
        return self.head
        
    def union(self,H2):
        H = self     
        H.head = self.merge(H2)
    
        if H.head == None:
            return H
        
        prev = None
        x = H.head
        after = x.sibling

        
        while after != None:
            if (x.degree != after.degree) or (after.sibling != None and after.sibling.degree == x.degree):
                prev = x
                x = after
            else:
                if x.value <= after.value:

                    x.sibling = after.sibling
                    self.link(after,x)
                else:
                    if prev == None:
                        H.head = after

                    else:
                        prev.sibling = after
                        
                    self.link(x,after)
                    x = after
                                  
            after = x.sibling


        
    def find_minimum(self):
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