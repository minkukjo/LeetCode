class Solution: 
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left + 1: right -1]
        
        if len(s) < 2 or s == s[::-1]:
            return s

        ans = ""
        for i in range(0,len(s)):
            even = expand(i, i+1)
            odd = expand(i, i+2)
            ans = max(ans,even, odd, key=len)
        return ans