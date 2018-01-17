"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

"""

"""
smallest heap
time: N*log(K)
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        heap = []
        res = 0
        
        for i in nums:
            heapq.heappush(heap, -i)
        
        for j in range(k):
            res = -heapq.heappop(heap)
        
        return res