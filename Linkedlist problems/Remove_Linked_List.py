# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):

        dummy = ListNode(None)
        
        dummy.next = head
        prev = dummy
        temp = head

        while temp:
            if temp.val == val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next

        return dummy.next
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        