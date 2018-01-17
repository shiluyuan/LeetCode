"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. 
The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. 
In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. 
A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
"""

"""
greedy policy: choose the one that may be the longest
"""

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        inc = dec = 1
        for x in range(1, size):
            if nums[x] > nums[x - 1]:
                inc = dec + 1
            elif nums[x] < nums[x - 1]:
                dec = inc + 1
        return max(inc, dec) if size else 0
"""
Linear Dynamic Programming [Accepted]

Algorithm

Any element in the array could correspond to only one of the three possible states:

up position, it means nums[i] > nums[i-1]nums[i]>nums[i−1]
down position, it means nums[i] < nums[i-1]nums[i]<nums[i−1]
equals to position, nums[i] == nums[i-1]nums[i]==nums[i−1]
The updates are done as:

If nums[i] > nums[i-1]nums[i]>nums[i−1], that means it wiggles up. The element before it must be a down position.
So up[i] = down[i-1] + 1up[i]=down[i−1]+1, down[i]down[i] remains the same as down[i-1]down[i−1]. If nums[i] < nums[i-1]nums[i]<nums[i−1], 
that means it wiggles down. The element before it must be a up position. So down[i] = up[i-1] + 1down[i]=up[i−1]+1, 
up[i]up[i] remains the same as up[i-1]up[i−1]. If nums[i] == nums[i-1]nums[i]==nums[i−1], 
that means it will not change anything becaue it didn't wiggle at all. 
So both down[i]down[i] and up[i]up[i] remain the same as down[i-1]down[i−1] and up[i-1]up[i−1].

At the end, we can find the larger out of up[length-1]up[length−1] and down[length-1]down[length−1] to find the max. 
wiggle subsequence length, where lengthlength refers to the number of elements in the given array.

The process can be illustrated with the following example:
"""