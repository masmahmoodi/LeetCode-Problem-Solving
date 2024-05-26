
# Find min node 
class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
   
    
    def min_node(self):
        if self.value is None:
            print("tree is empty !")
            return 
        
        current = self
        while current.left:
            current = current.left
        
        print(current.value)
