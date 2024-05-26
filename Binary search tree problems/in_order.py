# In order traversal (left,root,right)

class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def in_order(self):
        if self.left:
            self.left.pre_order()
              
        print(self.value)
        
        if self.right:
            self.right.pre_order()
                