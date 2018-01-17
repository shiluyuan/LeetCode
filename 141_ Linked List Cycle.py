"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
"""
method 1:
To detect if a list is cyclic, we can check whether a node had been visited before. A natural way is to use a hash table.
time: O(n)
space: O(n)
"""
"""
method 2:
fast and slow pointers 
fast 2 steps and slow 1 step, so fast go twice length when catch slow, is there is loop.
2(before_loop + in_loop_before_meet) = before_loop + 2in_loop_before_meet + in_loop_after_loop

we get before_loop = in_loop_after_loop    
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False