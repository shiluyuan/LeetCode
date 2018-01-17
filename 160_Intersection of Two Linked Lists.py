"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

"""
method 1:

Use set, store the address of pointers of nodelist A, then go through B to chech
whether the keys of nodelist B is in A.
"""

"""
method 2:
cut in the same length and go through A and B.     

time: O(n)
"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        def get_length(node):
            length = 0
            while(node):
                node = node.next
                length += 1
            return length
        
        lenA = get_length(headA)
        lenB = get_length(headB)
        
        if lenA >= lenB:
            for i in range(lenA-lenB):
                headA = headA.next
        else:
            for i in range(lenB-lenA):
                headB = headB.next
        
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None