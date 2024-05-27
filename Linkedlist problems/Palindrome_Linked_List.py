# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        pre = None    
        
        while slow:
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        
        first = head
        end = pre

        while end:
            if first.val != end.val:
                return False
            
            first =first.next
            end = end.next
        
        return True
        