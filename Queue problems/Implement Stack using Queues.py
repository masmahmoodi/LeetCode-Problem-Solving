class MyStack(object):

    def __init__(self):
        self.q1 =  []
        self.q2 =  []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        popedElement = self.q1.pop(0)
        temp = self.q1
        self.q1 = self.q2
        self.q2 =temp

        return popedElement

        """
        :rtype: int
        """
        

    def top(self):
        """
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        topElement = self.q1.pop(0)
        self.q2.append(topElement)
        temp = self.q1
        self.q1 = self.q2
        self.q2 =temp

        return topElement
        

    def empty(self):
        """
        :rtype: bool
        """

        return not self.q1 and not self.q2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()