# Importing a node class which contains a pointer and value fields
from ast import List
from pickle import NONE
from node import Node

#Linked Lists

class SinglyLinkedList():

    
    headValue = None
    
    
    def __init__(self):
        self.headValue = None
       
    # Inserting methods
    def appendList(self,list:list):
        for i in list:
          self.append(Node(i))  
        
        
        
    def append(self, Node):
        if self.headValue is None:
            self.headValue = Node
        else:
            last = self.headValue
            while last.next is not None:
                last = last.next
            last.next = Node
            
    def prepend(self, Node):
        if self.headValue is None:
            self.headValue = Node
        else:
            Node.next = self.headValue
            self.headValue = Node
    def insert(self,index,Node):
        cursor = self.headValue
        for i in range(index):
            cursor = cursor.next
            if(cursor is None):
              raise IndexError("index out of range") 
      
        
    
    # Overriding the to string function so that print method works correctly when 
    # printing the lists
 
    def __str__(self):
        output = ""
        pointer = self.headValue
        output += str(pointer)
        while pointer.next is not None:
            
            pointer = pointer.next
            output += ", "+ str(pointer) 
        
        return output
        
        
    def reverse(self):
        First = self.headValue
        
        Second = self.headValue.next
        
        while Second.next is not None:
            temp = Second.next
            Second.next = First
            First = First.next
            Second = temp
        self.headValue = Second
        
    def recurseReversed(self,cursor : Node, previousNode : Node):
        if (cursor.next == None):
            self.headValue = cursor
            self.headValue.next = previousNode
            return 
        temp = Node(cursor.value)
        temp.next = cursor.next
        
        cursor.next = previousNode
        
        return self.recurseReversed(temp.next,cursor)
    
 