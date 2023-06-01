class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl","6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}

        ans = []
        def dfs(index, cur):

            if len(cur) == len(digits):
                ans.append(cur)
                return
            
            for digit in list(map[digits[index]]):
                dfs(index+1, cur + digit)
        dfs(0,"")
        return ans


