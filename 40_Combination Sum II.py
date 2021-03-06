"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]"""

class Solution:
    def bfs(self, candidates, target, result, valuelist, start):  
        if target == 0 and valuelist not in result:  
            return result.append(valuelist)  
        for index in range(start, len(candidates)):  
            if target < candidates[index]:  
                return  
            self.bfs(candidates, target - candidates[index], result, valuelist + [candidates[index]], index + 1)  
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()  
        result = []  
        self.bfs(candidates, target, result, [], 0)  
        return result  