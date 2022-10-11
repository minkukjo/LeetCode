class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        
        def dfs(s, path, answer):
            if not s:
                answer.append(path)
                return

            for i in range(1, len(s)+1):
                if isPalindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]], answer)
        
        def isPalindrome(s):
            return s == s[::-1]
        dfs(s,[],answer)

        return answer