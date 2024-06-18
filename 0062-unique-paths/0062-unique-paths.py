from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 and n == 1:
            return 1
        
        q = deque()
        q.append((0,0))
        ans = [[1]*n for _ in range(m)]

        d = [(1, 0), (0,1)]
        while q:
            (x,y) = q.popleft()
            
            if x == m or y == n or ans[x][y] > 1:
                continue 
                
            if x-1 >= 0 and y-1 >= 0:
                ans[x][y] = ans[x-1][y] + ans[x][y-1]
            
            for dx, dy in d:
                nx = dx + x
                ny = dy + y

                q.append((nx,ny))

        return ans[-1][-1]

