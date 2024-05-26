# Search for a node

class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def search(self,value):
        
        if self.value is None:
          print("Tree is empty!")
          return
        
        if self.value == value:
            print("Node found!")
            return 
        
        if value < self.value:
            if self.left is None:
                print("Node not found!")
            else:
                self.left.search(value)
                    
        else:
            if self.right is None:
                print("Node not found!")
            else:
                self.right.search(value)
                
                
    
