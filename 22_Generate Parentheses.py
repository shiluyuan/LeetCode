"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
"""
backtracking
"""
class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
    
N = 3

ans = []
def backtrack(S = '', left = 0, right = 0):
    print("s is ",S)
    if len(S) == 2 * N:
        ans.append(S)
        print("s:",S)
        print("ans:", ans)
        #return
    print("left",left, "right", right)
    if left < N:
        print("left < N")
        backtrack(S+'(', left+1, right)
        print("from left",S)
    if right < left:
        print("right < left")
        backtrack(S+')', left, right+1)
        print("from right",S)

backtrack()