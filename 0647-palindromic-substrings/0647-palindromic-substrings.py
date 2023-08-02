class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def expandPalindrome(i, j):

            cnt = 0
            while 0<=i and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                cnt += 1
            return cnt
        
        return sum(expandPalindrome(i, i) + expandPalindrome(i,i+1) for i in range(len(s)))