"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""
"""
use another stack to store the minist value
"""

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        else:
            if self.minStack[-1] >= x:
                self.minStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack:
            if self.minStack[-1] == self.stack[-1]:
                self.minStack.pop()
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]