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
        
        
class BinomialHeap():
    def __init__(self):
        self.head = None   
            
    def insert(self,key):
        temp = BinomialHeap()
        n = node(key)
        temp.head = n
        self.union(temp)
    
    def extract_min(H):
        n = H.head
        minkey = n.key
        minnode = n
        while n.sibling != None:
            nextnode = n.sibling
            nextkey = nextnode.key
            if nextkey < minkey:
                minkey = nextkey
                minnode = nextnode
            n = nextnode
        
        '''in progress'''
        h = BinomialHeap()
    
    def decrease_key():
        pass
    
    def delete():
        pass
    
    def link(y,z):
        y.parent = z
        y.sibling = z.child
        z.children.append(y)
        z.degree += 1
        
    def merge(self,H2):
        
        if not self.head:
            self.head = H2.head #Joining empty list, no need to continue
            return self.head
            
        a = self.head
        b = H2.head
    
        '''choose head of combined rootlist to be smaller of the two list heads'''
        if a.degree <= b.degree:
            self.head = a
        elif b.degree < a.degree:
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
        H = BinomialHeap()        
        H.head = self.merge(H2)
    
        if H.head == None:
            return H
        
        prev = None
        x = H.head
        nxt = x.sibling
        
        while nxt != None:
            if (x.degree != nxt.degree) or (nxt.sibling != None and nxt.sibling.degree == x.degree):
                prev = x
                x = nxt
                
            elif x.value <= nxt.value:
                x.sibling = nxt.sibling
                link(nxt,x)
                
            elif prev == None:
                H.head = nxt
            else:
                prev.sibling = nxt
                link(x,nxt)
                x = nxt
            
            nxt = x.sibling

def minimum(self,H):
    
    y = None
    
    pass
