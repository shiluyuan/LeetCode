"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
"""

import heapq

class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0
        width, height = len(heightMap[0]), len(heightMap)
        sinks, result = [], 0
        visited = [[False]*width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if i == 0 or j == 0 or j == width - 1 or i == height -1:
                    heapq.heappush(sinks, (heightMap[i][j], i, j))
                    visited[i][j] = True
        while sinks:
            sh, si, sj = heapq.heappop(sinks)
            for (vi, vj) in ((si-1, sj), (si, sj+1), (si+1, sj), (si, sj-1)):
                if not (0 <= vi < height and 0 <= vj < width):
                    continue
                if visited[vi][vj]:
                    continue
                water = max(sh - heightMap[vi][vj], 0)
                visited[vi][vj] = True
                heapq.heappush(sinks, (heightMap[vi][vj] + water, vi, vj))
                result += water
        return result