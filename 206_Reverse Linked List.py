"""
Reverse a singly linked list.
"""
"""
time: O(n)
space: O(1)
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            new_head = temp
        return new_head