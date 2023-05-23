class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,board,word, path):
                    return True
        return False

def dfs(l,r,board, word, path):
    if len(word) == 0:
        return True
    if l < 0 or l >= len(board) or r < 0 or r >= len(board[0]) or word[0] != board[l][r] or (l,r) in path:
        return False
    
    path.add((l,r)) 
    res = dfs(l-1,r,board,word[1:], path) or dfs(l,r-1,board,word[1:], path) or dfs(l+1,r,board,word[1:], path) or dfs(l,r+1,board,word[1:], path)
    path.remove((l,r)) 
    return res
