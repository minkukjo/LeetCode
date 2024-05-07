from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            q=deque()
            q.append((i,j))
            visit.add((i,j))
            d = [(1,0), (-1,0), (0,1), (0,-1)]

            while q:
                x,y = q.popleft()
                for dx,dy in d:
                    nx = dx+x
                    ny = dy+y

                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx,ny) not in visit and grid[nx][ny] == '1':
                        visit.add((nx,ny))
                        q.append((nx,ny))
        
        visit = set()
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visit:
                    ans += 1
                    bfs(i,j)

        return ans


            



