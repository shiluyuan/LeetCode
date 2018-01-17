"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        node = new_head
        
        for i in range(m-1):
            node = node.next
        
        prev = node.next
        curr = prev.next
        
        for i in range(n-m):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        node.next.next = curr
        node.next = prev
        return new_head.next