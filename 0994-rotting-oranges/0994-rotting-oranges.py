from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        q = deque()

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 2:
                    q.append((i,j, 0))
        
        d = [(0,1), (0,-1), (1,0) ,(-1,0)]

        ans = 0
        while q:
            
            x,y, days = q.popleft()
            ans = max(ans, days)

            for dx, dy in d:
                nx = dx + x
                ny = dy + y

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    q.append((nx,ny,days+1))

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    return -1
        
        return ans



            