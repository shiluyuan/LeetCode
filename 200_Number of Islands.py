"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""
"""
dfs
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m = len(grid); n = len(grid[0])
        count = 0
        
        def helper(i,j,grid):
            if i > m-1 or i < 0 or j > n-1 or j < 0 or grid[i][j] != "1": return 
            
            grid[i][j] = "0"
            helper(i+1,j,grid)
            helper(i-1,j,grid)
            helper(i,j+1,grid)
            helper(i,j-1,grid)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    helper(i,j,grid)
                    
        return count