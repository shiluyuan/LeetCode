"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

"""
Use a dict to store node.

"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        nodeDict = {None:None}
        node = head
        while node:
            nodeDict[node] = RandomListNode(node.label)
            node = node.next
            
        node = head
        while node:
            nodeDict[node].next = nodeDict[node.next]
            nodeDict[node].random = nodeDict[node.random]
            node = node.next
        return nodeDict[head]