"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first=0
        second=0
        flag=False
        
        l=0
        r=len(nums)-1
        
        while l<=r:
            mid=l+(r-l)/2
            
            if nums[mid]==target:
                flag=True
            if nums[mid]<=target:
                l=mid+1
            else:
                r=mid-1
        second=l
            
        l=0
        r=len(nums)-1
        
        while l<=r:
            mid=l+(r-l)/2
            
            if nums[mid]==target:
                flag=True
            if nums[mid]>=target:
                r=mid-1
            else:
                l=mid+1
        first=l
        
        if flag:
            return [first,second-1]
        return [-1,-1]