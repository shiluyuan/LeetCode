"""
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
"""

class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        ref: https://discuss.leetcode.com/topic/72569/java-dfs-solution-with-various-optimizations-sorting-sequential-partition-dp/2
        """
        def backtracking(i, tot):
            if tot == 0:
                return True
            if i == len(num):
                return False
            
            if mask[i] and num[i] <= tot:
                mask[i] = False
                if backtracking(i + 1, tot - num[i]):
                    return True
                mask[i] = True
                
            return backtracking(i + 1, tot)        

        
        if len(nums) < 4 or sum(nums) % 4 != 0:
            return False
        
        num = sorted(nums, reverse=True)
        mask = [True]*len(nums)
        target = sum(nums) / 4
        
        for _ in range(4):
            if not backtracking(0, target):
                return False
            
        return True