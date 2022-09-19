from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS의 코스트가 크므로 계산이 불필요한 조건을 먼저 고려한다.
        if not word:
            return True
        
        m, n = len(board), len(board[0])
        if len(word) > m * n:
            return False
        
        counter = Counter(word)
        for line in board:
            for c in line:
                if c in counter:
                    counter[c] -= 1
        for v in counter.values():
            if v > 0:
                return False
        
        def DFS(r, c, w):
            if not w:
                return True
            
            if 0 <= r < m and 0 <= c < n and board[r][c] == w[0]:
                board[r][c] = '#'
                for nR, nC in [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]:
                    if DFS(nR, nC, w[1:]):
                        return True
                board[r][c] = w[0]
            return False
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and DFS(r, c, word):
                    return True
        
        return False