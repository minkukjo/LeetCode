from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for char in word:
            if not any(char in board[row] for row in range(len(board))):
                return False
            
            
        d = [(1,0), (0,1), (-1,0), (0,-1)]
        def bfs(i,j):
            q = deque()
            q.append((i,j,"",set()))
            
            while q:
                (x,y, s, visited) = q.popleft()
                ans = s + board[x][y]

                if ans == word:
                    return True

                if not word.startswith(ans):
                    continue

                visited = visited | {(x, y)}
                
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx,ny) not in visited:
                        q.append((nx,ny,ans, visited))
            return False        
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if bfs(i,j):
                        return True


        return False
