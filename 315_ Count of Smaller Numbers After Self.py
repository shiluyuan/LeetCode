"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
"""
"""
The smaller numbers on the right of a number are exactly those that jump from its right to its left during a stable sort.
"""

class Solution(object):
    def countSmaller(self, nums):
        def sort_list(enum):
            half = int(len(enum) / 2)
            if half:
                left, right = sort_list(enum[:half]), sort_list(enum[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        enum[i+j] = left[i]
                        smaller[left[i][0]] += j
                        i += 1
                    else:
                        enum[i+j] = right[j]
                        j += 1
            return enum
        smaller = [0] * len(nums)
        sort_list(list(enumerate(nums)))
        return smaller
    

########

nums = [5,2,6,1]

def sort_list(enum):
    half = int(len(enum) / 2)
    if half:
        left, right = sort_list(enum[:half]), sort_list(enum[half:])
        m, n = len(left), len(right)
        i = j = 0
        while i < m or j < n:
            if j == n or i < m and left[i][1] <= right[j][1]:
                enum[i+j] = left[i]
                smaller[left[i][0]] += j
                i += 1
            else:
                enum[i+j] = right[j]
                j += 1
    return enum
smaller = [0] * len(nums)
sort_list(list(enumerate(nums)))
print(smaller)

########### Binary Search Tree

class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r


class Solution(object):
    def countSmaller(self, nums):
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = BinaryIndexedTree(len(hashTable)), []
        for i in xrange(len(nums) - 1, -1, -1):
            r.append(tree.sum(hashTable[nums[i]]))
            tree.update(hashTable[nums[i]] + 1, 1)
        return r[::-1]
   
    