# Importing a node class which contains a pointer and value fields
from node import Node

#A Linked list class with one direction pointers
#Containing methods such as insertings, traversing the linked list

class SinglyLinkedList():

    # An field containing the first Node
    headValue = None
    
    
    def __init__(self):
        self.headValue = None
       
    # Inserting methods either at beginning, end or in middle of the list
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
        
        
