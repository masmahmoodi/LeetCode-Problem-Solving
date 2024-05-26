# Pre order traversal (root,left,right)

class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def pre_order(self):
        print(self.value)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
                