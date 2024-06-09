"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def dfs(grid, i,j,range):
            if canCompress(grid, i,j, range):
                value = None
                if grid[i][j] == 1:
                    value = 1
                else:
                    value = 0

                return Node(value, True)
            
            limit = range//2
            result = Node(1, False)
            result.topLeft = dfs(grid,i,j,limit)
            result.topRight = dfs(grid,i,j+limit, limit)
            result.bottomLeft = dfs(grid, i+limit, j, limit)
            result.bottomRight = dfs(grid,i+limit, j+limit, limit)
            return result

        def canCompress(grid, i,j,w):
            for x in range(i, i+w):
                for y in range(j, j+w):
                    if grid[x][y] != grid[i][j]:
                        return False
            return True
        return dfs(grid, 0,0,len(grid))