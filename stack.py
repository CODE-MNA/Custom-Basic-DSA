class Stack:
    def __init__(self):
        self.data = []
       
        
    def pop(self):
        return self.data.pop()
    
    def push(self, value):
        self.data.append(value)
        
    def pushMultiple(self, values):
        for value in values:
            self.data.append(value)
            
    def peek(self):
        return self.data[-1]
    
    def __len__(self):
        return len(self.data)
    def __str__(self):
        return self.data