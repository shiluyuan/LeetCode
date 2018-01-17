"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def isqueens(depth,j):
            for i in range(depth):
                if board[i] == j or abs(depth - i) == abs(board[i] - j):
                    return False
            return True
        def dfs(depth,row):
            if depth == n:
                ans.append(row);return
            for i in range(n):
                if isqueens(depth,i):
                    board[depth]= i
                    dfs(depth + 1,row + ['.'*i + 'Q' + '.'*(n - i - 1)])
        board = [-1 for i in range(n)]
        ans = []
        dfs(0,[])
        return ans 