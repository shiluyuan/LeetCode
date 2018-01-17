"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
"""
divede and conquer
Time complexity : O(N log k) where \text{k}k is the number of linked lists.
Space complexity : O(1)

We can merge two sorted linked lists in O(1)O(1) space.
"""

class Solution(object):
    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval,2*interval):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists
