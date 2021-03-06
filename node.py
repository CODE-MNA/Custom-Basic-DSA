

from pickle import NONE


class Node():
    value = None
    next = None
    def __init__(self,data):
        self.value = data
        self.next =  None
        
    def __str__(self):
        return str(self.value)
    def __eq__(self,other):
        if type(other) is type(self):
            return self.value == other.value
        else:
            return False
        
class TreeNode():
    
        def __init__(self,value):
            self.value = value
            self.right = None
            self.left = None
        def __str__(self):
            return str(self.value)
        def __eq__(self,other):
            if type(other) is type(self):
                return self.value == other.value
            else:
                return False
