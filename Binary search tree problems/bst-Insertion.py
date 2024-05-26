class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    
    def insert(self,value):
        
        if self.value is None:
            self.value = value
            return
        
        if self.value == value:
            return
        
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                 self.left.insert(value)

        else:
            if self.right is None:
                self.right = BST(value)
            else:
               self.right.insert(value)
                
            
                        
                
                
                

root = BST(10)
array = [20,4,30,4,1,5,6]
for i in len(array):
    root.insert(i)

  