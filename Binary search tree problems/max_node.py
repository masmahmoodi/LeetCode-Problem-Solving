# find max node 
class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    
    def max_node(self):
        current = self
        while current.right:
            current = current.right
        print(current.value)