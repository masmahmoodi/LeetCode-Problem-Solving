# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):


        temp = head
        after = None
        prev = None
        while temp:
            after = temp.next
            temp.next = prev
            prev = temp 
            temp = after
        head = prev
        somthing = head
        sum = 0 
        degree = 0
        while somthing:
            sum += (pow(2,degree)) * somthing.val
            degree +=1
            somthing = somthing.next
        return sum



        """
        :type head: ListNode
        :rtype: int
        """
        