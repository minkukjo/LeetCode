class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        lst = []

        def dfs(i, curr):
            if i == len(s):
                lst.append(curr)
                return
        
            for j in range(i,len(s)):
                sol = s[i:j+1]
                if sol == sol[::-1]:
                    dfs(j+1,curr+[sol])
            return
        dfs(0,[])
        return lst
