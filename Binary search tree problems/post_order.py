# Post order traversal (left,right,root)

class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def post_order(self):
        if self.left:
            self.left.pre_order() 
        if self.right:
            self.right.pre_order()
        print(self.value)
        
                