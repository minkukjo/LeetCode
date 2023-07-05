from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,0))


        result = 0
        while q:
            (i,j,time) = q.popleft()

            result = max(time, result)
            visit.add((i,j))

            for dr,dc in (1,0), (-1,0), (0,1), (0,-1):
                cr,cc = i + dr, j+dc

                if 0 <= cr < len(grid) and 0<= cc < len(grid[0]) and grid[cr][cc] == 1 and (cr,cc) not in visit:
                    grid[cr][cc] = 2
                    q.append((cr,cc,time+1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return result